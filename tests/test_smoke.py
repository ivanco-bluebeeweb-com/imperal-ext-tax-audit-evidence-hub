import sys
from pathlib import Path
import pytest
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from imperal_sdk.testing import MockContext
import main as m
import panels
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

def test_case_row_opens_case_detail_in_the_selected_language():
    row = panels._case_row({"id": "case-123", "case_name": "DemoCo", "status": "open"}, panels.COPY["ru"], "ru")
    assert row.props["on_click"].params["function"] == "__panel__evidence_case_detail"
    assert row.props["on_click"].params["params"] == {"case_id": "case-123", "language": "ru"}


def test_language_switcher_has_ru_ro_en_panel_actions():
    for language in ("ru", "ro", "en"):
        switcher = panels._language_switcher(language)
        buttons = switcher.props["content"].props["children"]
        assert [button.props["label"] for button in buttons] == ["RU", "RO", "EN"]
        assert buttons[0].props["on_click"].params["params"] == {"language": "ru", "case_id": ""}
        assert buttons[1].props["on_click"].params["params"] == {"language": "ro", "case_id": ""}
        assert buttons[2].props["on_click"].params["params"] == {"language": "en", "case_id": ""}
        assert [button.props["variant"] for button in buttons].count("primary") == 1

@pytest.mark.asyncio
async def test_empty_case_list_returns_a_successful_read_response():
    result = await m.list_cases(MockContext(), ListCasesParams(limit=20))
    assert result.status == "success"
    assert result.data.total == 0
    assert result.summary == "Evidence readiness cases listed."

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


def test_status_label_translates_internal_codes_for_every_language():
    for language in ("en", "ru", "ro"):
        copy = panels.COPY[language]
        assert panels._status_label("approved_for_pack", copy) != "approved_for_pack"
        assert panels._status_label("needs_review", copy) != "needs_review"
        # Unknown/custom statuses still render readably instead of raising.
        assert panels._status_label("some_future_status", copy) == "some future status"


def test_next_step_message_guides_a_first_time_user_through_the_workflow():
    copy = panels.COPY["en"]
    case = {"status": "open"}
    assert panels._next_step_message(copy, case, [], [], []) == copy["next_missing_checklist"]

    checklist = [{"status": "open"}, {"status": "approved_for_pack"}]
    assert panels._next_step_message(copy, case, checklist, [], []) == copy["next_checklist_incomplete"].format(approved=1, total=2)

    checklist_done = [{"status": "approved_for_pack"}]
    assert panels._next_step_message(copy, case, checklist_done, [], []) == copy["next_need_evidence"]

    evidence_done = [{"status": "approved_for_pack"}]
    assert panels._next_step_message(copy, case, checklist_done, evidence_done, []) == copy["next_ready_to_build"]
    assert panels._next_step_message(copy, case, checklist_done, evidence_done, [{"status": "draft"}]) == copy["next_ready_to_approve"]

    approved_case = {"status": "approved"}
    assert panels._next_step_message(copy, approved_case, checklist_done, evidence_done, [{"status": "draft"}]) == copy["next_done"]


def test_pack_summary_reports_readable_counts_and_blockers():
    copy = panels.COPY["en"]
    checklist = [{"status": "approved_for_pack"}, {"status": "open"}]
    evidence = [{"status": "approved_for_pack"}]
    tasks = [{"status": "done"}, {"status": "open"}]
    summary = panels._pack_summary(copy, checklist, evidence, tasks)
    assert "1/2 checklist items accepted" in summary
    assert "1/1 evidence approved" in summary
    assert "1/2 tasks done" in summary
    assert copy["pack_summary_blockers"].format(blockers=1) in summary

    all_clear = panels._pack_summary(copy, [{"status": "approved_for_pack"}], [{"status": "approved_for_pack"}], [])
    assert copy["pack_summary_clear"] in all_clear

