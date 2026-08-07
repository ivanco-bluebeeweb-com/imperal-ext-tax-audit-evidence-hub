import sys
from pathlib import Path
import pytest
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from imperal_sdk.testing import MockContext
import main as m
from schemas import *

@pytest.mark.asyncio
async def test_human_led_evidence_pack_happy_path():
    ctx=MockContext()
    case=await m.create_case(ctx,CreateCaseParams(case_name="FY2025 audit PBC",organization_name="Acme",period="FY2025",request_type="audit PBC",owner="Elena"))
    item=await m.add_checklist_item(ctx,AddChecklistItemParams(case_id=case.data.id,label="Bank confirmations",owner="Elena"))
    evidence=await m.register_evidence(ctx,RegisterEvidenceParams(case_id=case.data.id,checklist_item_id=item.data.id,title_text="Bank confirmation",source_url="https://drive.example/bank.pdf",period="FY2025",reference="BC-1",owner="Elena"))
    denied=await m.build_evidence_pack(ctx,BuildEvidencePackParams(case_id=case.data.id)); assert denied.status != "success"
    reviewed=await m.review_evidence(ctx,ReviewEvidenceParams(evidence_item_id=evidence.data.id,status="approved_for_pack",approved_by="Senior Auditor")); assert reviewed.status=="success"
    still_incomplete=await m.build_evidence_pack(ctx,BuildEvidencePackParams(case_id=case.data.id)); assert still_incomplete.status != "success"
    checklist_review=await m.update_checklist_item(ctx,UpdateChecklistItemParams(checklist_item_id=item.data.id,status="approved_for_pack",approved_by="Senior Auditor")); assert checklist_review.status=="success"
    task=await m.create_task(ctx,CreateTaskParams(case_id=case.data.id,title_text="Confirm bank balance",assignee="Elena",evidence_item_id=evidence.data.id)); assert task.status=="success"
    pack=await m.build_evidence_pack(ctx,BuildEvidencePackParams(case_id=case.data.id)); assert pack.status=="success" and "Bank confirmation" in pack.data.index_markdown
    approved=await m.approve_evidence_pack(ctx,ApproveEvidencePackParams(case_id=case.data.id,approved_by="Senior Auditor",approval_note="Ready for audit review.")); assert approved.status=="success" and approved.data.status=="approved"

@pytest.mark.asyncio
async def test_evidence_requires_https_and_human_approval_identity():
    ctx=MockContext(); case=await m.create_case(ctx,CreateCaseParams(case_name="Close",organization_name="Acme",period="2026-01",request_type="close",owner="Elena"))
    insecure=await m.register_evidence(ctx,RegisterEvidenceParams(case_id=case.data.id,title_text="Invoice",source_url="http://bad.example/a.pdf")); assert insecure.status != "success"
    evidence=await m.register_evidence(ctx,RegisterEvidenceParams(case_id=case.data.id,title_text="Invoice",source_url="https://drive.example/a.pdf"))
    approval=await m.review_evidence(ctx,ReviewEvidenceParams(evidence_item_id=evidence.data.id,status="approved_for_pack")); assert approval.status != "success"

@pytest.mark.asyncio
async def test_case_boundaries_prevent_cross_case_evidence_link():
    ctx=MockContext(); a=await m.create_case(ctx,CreateCaseParams(case_name="A",organization_name="Acme",period="2026",request_type="audit",owner="E")); b=await m.create_case(ctx,CreateCaseParams(case_name="B",organization_name="Beta",period="2026",request_type="audit",owner="E"))
    item=await m.add_checklist_item(ctx,AddChecklistItemParams(case_id=a.data.id,label="Ledger"))
    result=await m.register_evidence(ctx,RegisterEvidenceParams(case_id=b.data.id,checklist_item_id=item.data.id,title_text="Ledger",source_url="https://drive.example/ledger.pdf")); assert result.status != "success"
