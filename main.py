"""Tax & Audit Evidence Readiness Hub — human-led preparation, never tax advice."""
from __future__ import annotations
from datetime import datetime, timezone
from imperal_sdk import ActionResult

from app import chat, ext
from schemas import *

def now(): return datetime.now(timezone.utc).isoformat()
def entity(cls, doc): return cls(**(doc.data | {"id": doc.id, "title": doc.data.get("case_name") or doc.data.get("label") or doc.data.get("title_text", "")}))
async def get(ctx, collection, id, message):
    doc = await ctx.store.get(collection, id)
    if not doc: raise ValueError(message)
    return doc
async def rows(ctx, collection, case_id, limit=200):
    page = await ctx.store.query(collection, limit=limit)
    return [d for d in page.data if d.data.get("case_id") == case_id]

@ext.on_install
async def on_install(ctx):
    """Initialize no data; cases are created explicitly by a human."""
    return True

@ext.health_check
async def health_check(ctx):
    await ctx.store.query("evidence_cases", limit=1); return True

@chat.function("create_case", description="Create a human-owned tax/audit preparation case. This does not create a tax opinion or filing.", action_type="write", data_model=EvidenceCase, effects=["case.create"], event="tax-audit-evidence-hub.create_case")
async def create_case(ctx, params: CreateCaseParams) -> ActionResult:
    """Handle create case within the human-led evidence workflow."""
    data = params.model_dump() | {"status":"open", "created_at":now(), "updated_at":now()}
    doc = await ctx.store.create("evidence_cases", data)
    return ActionResult.success(entity(EvidenceCase, doc), summary="Evidence readiness case created.")

@chat.function("list_cases", description="List evidence readiness cases.", action_type="read", data_model=EvidenceCaseList)
async def list_cases(ctx, params: ListCasesParams) -> ActionResult:
    """Handle list cases within the human-led evidence workflow."""
    page=await ctx.store.query("evidence_cases", order_by="-created_at", limit=params.limit)
    docs=[d for d in page.data if not params.status or d.data.get("status")==params.status]
    return ActionResult.success(EvidenceCaseList(items=[entity(EvidenceCase,d) for d in docs], total=len(docs)))

@chat.function("add_checklist_item", description="Add a human-authored document/control requirement to a case.", action_type="write", data_model=ChecklistItem, effects=["checklist_item.create"], event="tax-audit-evidence-hub.add_checklist_item")
async def add_checklist_item(ctx, params: AddChecklistItemParams) -> ActionResult:
    """Handle add checklist item within the human-led evidence workflow."""
    await get(ctx,"evidence_cases",params.case_id,"Case not found.")
    doc=await ctx.store.create("checklist_items",params.model_dump()|{"status":"missing","review_note":"","approved_by":""})
    return ActionResult.success(entity(ChecklistItem,doc),summary="Checklist item added.")

@chat.function("update_checklist_item", description="Update a checklist status. Only a named human may mark it approved_for_pack.", action_type="write", data_model=ChecklistItem, effects=["checklist_item.update"], event="tax-audit-evidence-hub.update_checklist_item")
async def update_checklist_item(ctx, params: UpdateChecklistItemParams) -> ActionResult:
    """Handle update checklist item within the human-led evidence workflow."""
    if params.status not in ITEM_STATUSES: return ActionResult.error("Invalid checklist status.", retryable=False)
    if params.status=="approved_for_pack" and not params.approved_by.strip(): return ActionResult.error("approved_by is required to approve an item for the pack.", retryable=False)
    if params.status=="rejected" and not params.review_note.strip(): return ActionResult.error("review_note is required when rejecting an item.", retryable=False)
    doc=await get(ctx,"checklist_items",params.checklist_item_id,"Checklist item not found.")
    await ctx.store.update("checklist_items",doc.id,params.model_dump())
    return ActionResult.success(entity(ChecklistItem,await get(ctx,"checklist_items",doc.id,"Checklist item not found.")),summary="Checklist item updated.")

@chat.function("register_evidence", description="Register an existing HTTPS evidence source. This app does not fetch, interpret or validate the document.", action_type="write", data_model=EvidenceItem, effects=["evidence.register"], event="tax-audit-evidence-hub.register_evidence")
async def register_evidence(ctx, params: RegisterEvidenceParams) -> ActionResult:
    """Handle register evidence within the human-led evidence workflow."""
    await get(ctx,"evidence_cases",params.case_id,"Case not found.")
    if not params.source_url.startswith("https://"): return ActionResult.error("source_url must be an HTTPS URL to an existing document or approved storage location.",retryable=False)
    if params.checklist_item_id:
        item=await get(ctx,"checklist_items",params.checklist_item_id,"Checklist item not found.")
        if item.data.get("case_id")!=params.case_id: return ActionResult.error("Checklist item belongs to a different case.",retryable=False)
    doc=await ctx.store.create("evidence_items",params.model_dump()|{"status":"received","review_note":"","approved_by":""})
    return ActionResult.success(entity(EvidenceItem,doc),summary="Evidence registered for human review.")

@chat.function("review_evidence", description="Record a human evidence review. Only a named human may mark evidence approved_for_pack.", action_type="write", data_model=EvidenceItem, effects=["evidence.review"], event="tax-audit-evidence-hub.review_evidence")
async def review_evidence(ctx, params: ReviewEvidenceParams) -> ActionResult:
    """Handle review evidence within the human-led evidence workflow."""
    if params.status not in ("received","needs_review","rejected","approved_for_pack"): return ActionResult.error("Invalid evidence status.",retryable=False)
    if params.status=="approved_for_pack" and not params.approved_by.strip(): return ActionResult.error("approved_by is required to approve evidence for the pack.",retryable=False)
    if params.status=="rejected" and not params.review_note.strip(): return ActionResult.error("review_note is required when rejecting evidence.",retryable=False)
    doc=await get(ctx,"evidence_items",params.evidence_item_id,"Evidence item not found.")
    await ctx.store.update("evidence_items",doc.id,params.model_dump())
    return ActionResult.success(entity(EvidenceItem,await get(ctx,"evidence_items",doc.id,"Evidence item not found.")),summary="Evidence review recorded.")

@chat.function("create_task", description="Create a human-owned preparation task for a case.", action_type="write", data_model=CaseTask, effects=["case_task.create"], event="tax-audit-evidence-hub.create_task")
async def create_task(ctx, params: CreateTaskParams) -> ActionResult:
    """Handle create task within the human-led evidence workflow."""
    await get(ctx,"evidence_cases",params.case_id,"Case not found.")
    if params.evidence_item_id:
        evidence=await get(ctx,"evidence_items",params.evidence_item_id,"Evidence item not found.")
        if evidence.data.get("case_id")!=params.case_id:return ActionResult.error("Evidence item belongs to a different case.",retryable=False)
    doc=await ctx.store.create("case_tasks",params.model_dump()|{"status":"open"})
    return ActionResult.success(entity(CaseTask,doc),summary="Preparation task created.")

@chat.function("update_task", description="Update a human-owned preparation task status.", action_type="write", data_model=CaseTask, effects=["case_task.update"], event="tax-audit-evidence-hub.update_task")
async def update_task(ctx, params: UpdateTaskParams) -> ActionResult:
    """Handle update task within the human-led evidence workflow."""
    if params.status not in TASK_STATUSES:return ActionResult.error("Invalid task status.",retryable=False)
    doc=await get(ctx,"case_tasks",params.task_id,"Task not found."); await ctx.store.update("case_tasks",doc.id,{"status":params.status})
    return ActionResult.success(entity(CaseTask,await get(ctx,"case_tasks",doc.id,"Task not found.")),summary="Task updated.")

@chat.function("list_checklist_items", description="List case checklist items and their review status.", action_type="read", data_model=ChecklistItemList)
async def list_checklist_items(ctx, params: ListCaseItemsParams) -> ActionResult:
    """Handle list checklist items within the human-led evidence workflow."""
    await get(ctx,"evidence_cases",params.case_id,"Case not found."); docs=[d for d in await rows(ctx,"checklist_items",params.case_id,params.limit) if not params.status or d.data.get("status")==params.status]
    return ActionResult.success(ChecklistItemList(items=[entity(ChecklistItem,d) for d in docs],total=len(docs)))

@chat.function("list_evidence", description="List registered evidence sources and human review status for one case.", action_type="read", data_model=EvidenceItemList)
async def list_evidence(ctx, params: ListCaseItemsParams) -> ActionResult:
    """Handle list evidence within the human-led evidence workflow."""
    await get(ctx,"evidence_cases",params.case_id,"Case not found."); docs=[d for d in await rows(ctx,"evidence_items",params.case_id,params.limit) if not params.status or d.data.get("status")==params.status]
    return ActionResult.success(EvidenceItemList(items=[entity(EvidenceItem,d) for d in docs],total=len(docs)))

@chat.function("list_tasks", description="List human-owned preparation tasks for one case.", action_type="read", data_model=CaseTaskList)
async def list_tasks(ctx, params: ListCaseItemsParams) -> ActionResult:
    """Handle list tasks within the human-led evidence workflow."""
    await get(ctx,"evidence_cases",params.case_id,"Case not found."); docs=[d for d in await rows(ctx,"case_tasks",params.case_id,params.limit) if not params.status or d.data.get("status")==params.status]
    return ActionResult.success(CaseTaskList(items=[entity(CaseTask,d) for d in docs],total=len(docs)))

@chat.function("build_evidence_pack", description="Build a read-only index of evidence already approved by a named human. It is not a tax opinion or filing.", action_type="write", data_model=EvidencePack, effects=["evidence_pack.build"], event="tax-audit-evidence-hub.build_evidence_pack")
async def build_evidence_pack(ctx, params: BuildEvidencePackParams) -> ActionResult:
    """Handle build evidence pack within the human-led evidence workflow."""
    case=await get(ctx,"evidence_cases",params.case_id,"Case not found.")
    checklist=await rows(ctx,"checklist_items",params.case_id)
    incomplete=[d.data.get("label", "Checklist item") for d in checklist if d.data.get("status") != "approved_for_pack"]
    if incomplete:
        return ActionResult.error(
            "Evidence pack cannot be built while required checklist items remain incomplete: " + ", ".join(incomplete),
            retryable=False,
        )
    approved=[d for d in await rows(ctx,"evidence_items",params.case_id) if d.data.get("status")=="approved_for_pack"]
    if not approved:return ActionResult.error("No human-approved evidence is available for this pack.",retryable=False)
    lines=[f"# Evidence Pack Index — {case.data.get('case_name','')}","",f"Period: {case.data.get('period','')}",f"Purpose: {case.data.get('request_type','')}","","## Human-approved evidence"]
    for n,d in enumerate(approved,1):
        x=d.data; lines.append(f"{n}. {x.get('title_text','')} — {x.get('source_url','')} (period: {x.get('period','')}; reference: {x.get('reference','')}; approved by: {x.get('approved_by','')})")
    doc=await ctx.store.create("evidence_packs",{"case_id":params.case_id,"status":"draft","approved_by":"","approved_at":"","item_count":len(approved),"index_markdown":"\n".join(lines)})
    await ctx.store.update("evidence_cases",case.id,{"status":"ready_for_review","updated_at":now()})
    return ActionResult.success(entity(EvidencePack,doc),summary="Read-only evidence pack index built for human approval.")

@chat.function("approve_evidence_pack", description="A named human approves the latest evidence-pack index for its stated preparation purpose. Not a tax opinion or filing approval.", action_type="write", data_model=EvidencePack, effects=["evidence_pack.approve"], event="tax-audit-evidence-hub.approve_evidence_pack")
async def approve_evidence_pack(ctx, params: ApproveEvidencePackParams) -> ActionResult:
    """Handle approve evidence pack within the human-led evidence workflow."""
    case=await get(ctx,"evidence_cases",params.case_id,"Case not found.")
    if not params.approved_by.strip() or not params.approval_note.strip():return ActionResult.error("approved_by and approval_note are required for human pack approval.",retryable=False)
    packs=await rows(ctx,"evidence_packs",params.case_id)
    if not packs:return ActionResult.error("Build an evidence pack before approving it.",retryable=False)
    latest=packs[-1]; stamp=now(); await ctx.store.update("evidence_packs",latest.id,{"status":"approved","approved_by":params.approved_by,"approved_at":stamp,"approval_note":params.approval_note}); await ctx.store.update("evidence_cases",case.id,{"status":"approved","updated_at":stamp})
    return ActionResult.success(entity(EvidencePack,await get(ctx,"evidence_packs",latest.id,"Evidence pack not found.")),summary="Human approval recorded. This does not constitute a tax decision or filing.")


# Import after all handlers so the panel uses the same extension instance.
import panels  # noqa: E402,F401
