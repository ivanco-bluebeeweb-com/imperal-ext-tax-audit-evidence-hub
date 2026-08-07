"""Contracts for a human-led tax/audit evidence readiness workflow.

This app deliberately coordinates preparation work; it never makes tax
judgements, provides tax advice, files returns, or replaces audit judgement.
"""
from __future__ import annotations
from pydantic import BaseModel, Field
from imperal_sdk import sdl

CASE_STATUSES = ("open", "ready_for_review", "approved", "closed")
ITEM_STATUSES = ("missing", "received", "needs_review", "rejected", "approved_for_pack")
TASK_STATUSES = ("open", "in_progress", "blocked", "done")

class EvidenceCase(sdl.Entity):
    case_name: str = ""
    organization_name: str = ""
    period: str = ""
    request_type: str = ""
    owner: str = ""
    status: str = "open"
    created_at: str = ""
    updated_at: str = ""

class EvidenceCaseList(sdl.EntityList[EvidenceCase]):
    pass

class ChecklistItem(sdl.Entity):
    case_id: str = ""
    label: str = ""
    description: str = ""
    owner: str = ""
    due_date: str = ""
    status: str = "missing"
    review_note: str = ""
    approved_by: str = ""

class ChecklistItemList(sdl.EntityList[ChecklistItem]):
    pass

class EvidenceItem(sdl.Entity):
    case_id: str = ""
    checklist_item_id: str = ""
    title_text: str = ""
    source_url: str = ""
    source_type: str = ""
    period: str = ""
    reference: str = ""
    owner: str = ""
    status: str = "received"
    review_note: str = ""
    approved_by: str = ""

class EvidenceItemList(sdl.EntityList[EvidenceItem]):
    pass

class CaseTask(sdl.Entity):
    case_id: str = ""
    title_text: str = ""
    assignee: str = ""
    due_date: str = ""
    status: str = "open"
    evidence_item_id: str = ""

class CaseTaskList(sdl.EntityList[CaseTask]):
    pass

class EvidencePack(sdl.Entity):
    case_id: str = ""
    status: str = "draft"
    approved_by: str = ""
    approved_at: str = ""
    item_count: int = 0
    index_markdown: str = ""

class CreateCaseParams(BaseModel):
    case_name: str = Field(description="Human-readable case name, e.g. 'FY2025 audit PBC — Acme'")
    organization_name: str = Field(description="Company/client for this case")
    period: str = Field(description="Human-defined reporting or audit period, e.g. 'FY2025' or '2026-01'")
    request_type: str = Field(description="Purpose, e.g. audit PBC, tax inquiry, month-end close")
    owner: str = Field(description="Person accountable for coordinating the preparation")

class ListCasesParams(BaseModel):
    status: str = Field("", description="Optional: open|ready_for_review|approved|closed")
    limit: int = Field(50, ge=1, le=100, description="Maximum cases to return")

class AddChecklistItemParams(BaseModel):
    case_id: str = Field(description="Case id from list_cases")
    label: str = Field(description="Human-authored required document/control item")
    description: str = Field("", description="Why the item is needed or how it must be checked")
    owner: str = Field("", description="Person responsible for providing/reviewing it")
    due_date: str = Field("", description="Optional human-set due date, YYYY-MM-DD")

class UpdateChecklistItemParams(BaseModel):
    checklist_item_id: str = Field(description="Checklist item id")
    status: str = Field(description="missing|received|needs_review|rejected|approved_for_pack")
    review_note: str = Field("", description="Human review note; required for rejection")
    approved_by: str = Field("", description="Human approver; required for approved_for_pack")

class RegisterEvidenceParams(BaseModel):
    case_id: str = Field(description="Case id from list_cases")
    title_text: str = Field(description="Human-readable document/evidence title")
    source_url: str = Field(description="HTTPS link to a document or its approved storage location")
    source_type: str = Field("document", description="document|email|link|other")
    checklist_item_id: str = Field("", description="Optional checklist item this evidence supports")
    period: str = Field("", description="Period asserted by the submitting user; requires human review")
    reference: str = Field("", description="Reference, invoice number, registry number, etc.; requires human review")
    owner: str = Field("", description="Person who supplied or owns the evidence")

class ReviewEvidenceParams(BaseModel):
    evidence_item_id: str = Field(description="Evidence item id")
    status: str = Field(description="received|needs_review|rejected|approved_for_pack")
    review_note: str = Field("", description="Human review note; required for rejection")
    approved_by: str = Field("", description="Human approver; required for approved_for_pack")

class CreateTaskParams(BaseModel):
    case_id: str = Field(description="Case id")
    title_text: str = Field(description="Concrete human-owned preparation task")
    assignee: str = Field("", description="Person responsible")
    due_date: str = Field("", description="Optional human-set due date, YYYY-MM-DD")
    evidence_item_id: str = Field("", description="Optional evidence item this task relates to")

class UpdateTaskParams(BaseModel):
    task_id: str = Field(description="Task id")
    status: str = Field(description="open|in_progress|blocked|done")

class ListCaseItemsParams(BaseModel):
    case_id: str = Field(description="Case id")
    status: str = Field("", description="Optional status filter")
    limit: int = Field(100, ge=1, le=200, description="Maximum items to return")

class BuildEvidencePackParams(BaseModel):
    case_id: str = Field(description="Case id")

class ApproveEvidencePackParams(BaseModel):
    case_id: str = Field(description="Case id")
    approved_by: str = Field(description="Named human who confirms the pack is ready for its stated purpose")
    approval_note: str = Field(description="Human approval note; this is not a tax opinion")
