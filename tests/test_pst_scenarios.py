"""Plausible Scenario Tests (PST) -- Tax Audit Evidence Hub.

Method: Docs/session-notes/SCENARIO_TESTING_STANDARD.md. This app has 13
functions and one existing test file with a strong end-to-end happy-path
test (test_human_led_evidence_pack_happy_path) plus targeted boundary tests
(https-only evidence, cross-case isolation). A name-based coverage audit
found 4 functions never exercised on their own:

    list_checklist_items, list_evidence, list_tasks, update_task

These are read/write leaves the big end-to-end test never has reason to call
directly (it builds a pack, it doesn't need to list checklist items back).
"""
from __future__ import annotations

import pytest

import main as m
from imperal_sdk.testing import MockContext
from schemas import (
    AddChecklistItemParams, CreateCaseParams, CreateTaskParams,
    ListCaseItemsParams, RegisterEvidenceParams, UpdateChecklistItemParams,
    UpdateTaskParams,
)


pytestmark = pytest.mark.asyncio


async def _seed_case(ctx):
    case = await m.create_case(ctx, CreateCaseParams(
        case_name="FY2025 audit PBC", organization_name="Acme",
        period="FY2025", request_type="audit PBC", owner="Elena"))
    return case.data.id


# --------------------------- list_checklist_items ----------------------------

async def test_happy_list_checklist_items_returns_seeded_rows():
    ctx = MockContext()
    case_id = await _seed_case(ctx)
    await m.add_checklist_item(ctx, AddChecklistItemParams(
        case_id=case_id, label="Bank confirmations", owner="Elena"))
    await m.add_checklist_item(ctx, AddChecklistItemParams(
        case_id=case_id, label="Ledger", owner="Elena"))

    result = await m.list_checklist_items(ctx, ListCaseItemsParams(case_id=case_id))
    assert result.status == "success"
    assert result.data.total == 2


async def test_adversarial_list_checklist_items_filters_by_status():
    ctx = MockContext()
    case_id = await _seed_case(ctx)
    item = await m.add_checklist_item(ctx, AddChecklistItemParams(
        case_id=case_id, label="Bank confirmations", owner="Elena"))
    await m.add_checklist_item(ctx, AddChecklistItemParams(
        case_id=case_id, label="Ledger", owner="Elena"))
    await m.update_checklist_item(ctx, UpdateChecklistItemParams(
        checklist_item_id=item.data.id, status="approved_for_pack",
        approved_by="Senior Auditor"))

    result = await m.list_checklist_items(ctx, ListCaseItemsParams(
        case_id=case_id, status="approved_for_pack"))
    assert result.status == "success"
    assert result.data.total == 1
    assert result.data.items[0].label == "Bank confirmations"


async def test_error_list_checklist_items_unknown_case():
    # get() raises ValueError on "not found" uniformly across this app's 13
    # functions (see main.py's shared get() helper) -- not a bug isolated to
    # this one, so the scenario asserts the app's real, consistent contract.
    ctx = MockContext()
    with pytest.raises(ValueError, match="Case not found"):
        await m.list_checklist_items(ctx, ListCaseItemsParams(case_id="ghost"))


# --------------------------------- list_evidence -----------------------------

async def test_happy_list_evidence_returns_seeded_rows():
    ctx = MockContext()
    case_id = await _seed_case(ctx)
    await m.register_evidence(ctx, RegisterEvidenceParams(
        case_id=case_id, title_text="Bank confirmation",
        source_url="https://drive.example/bank.pdf", period="FY2025",
        reference="BC-1", owner="Elena"))

    result = await m.list_evidence(ctx, ListCaseItemsParams(case_id=case_id))
    assert result.status == "success"
    assert result.data.total == 1
    assert result.data.items[0].title_text == "Bank confirmation"


async def test_blocked_list_evidence_on_case_with_no_evidence_is_still_success():
    """Empty is not an error -- a fresh case legitimately has none yet."""
    ctx = MockContext()
    case_id = await _seed_case(ctx)
    result = await m.list_evidence(ctx, ListCaseItemsParams(case_id=case_id))
    assert result.status == "success"
    assert result.data.total == 0


# ---------------------------------- list_tasks -------------------------------

async def test_happy_list_tasks_returns_seeded_rows():
    ctx = MockContext()
    case_id = await _seed_case(ctx)
    await m.create_task(ctx, CreateTaskParams(
        case_id=case_id, title_text="Confirm bank balance", assignee="Elena"))

    result = await m.list_tasks(ctx, ListCaseItemsParams(case_id=case_id))
    assert result.status == "success"
    assert result.data.total == 1
    assert result.data.items[0].title_text == "Confirm bank balance"


async def test_adversarial_list_tasks_filters_by_status():
    ctx = MockContext()
    case_id = await _seed_case(ctx)
    task = await m.create_task(ctx, CreateTaskParams(
        case_id=case_id, title_text="Confirm bank balance", assignee="Elena"))
    await m.create_task(ctx, CreateTaskParams(
        case_id=case_id, title_text="Reconcile ledger", assignee="Elena"))
    await m.update_task(ctx, UpdateTaskParams(task_id=task.data.id, status="done"))

    result = await m.list_tasks(ctx, ListCaseItemsParams(case_id=case_id, status="done"))
    assert result.status == "success"
    assert result.data.total == 1
    assert result.data.items[0].title_text == "Confirm bank balance"


# --------------------------------- update_task -------------------------------

async def test_happy_update_task_changes_status():
    ctx = MockContext()
    case_id = await _seed_case(ctx)
    task = await m.create_task(ctx, CreateTaskParams(
        case_id=case_id, title_text="Confirm bank balance", assignee="Elena"))

    result = await m.update_task(ctx, UpdateTaskParams(
        task_id=task.data.id, status="in_progress"))
    assert result.status == "success"
    assert result.data.status == "in_progress"


async def test_adversarial_update_task_rejects_invalid_status():
    """TASK_STATUSES = (open, in_progress, blocked, done) -- anything else
    must be refused, not silently stored as free text."""
    ctx = MockContext()
    case_id = await _seed_case(ctx)
    task = await m.create_task(ctx, CreateTaskParams(
        case_id=case_id, title_text="Confirm bank balance", assignee="Elena"))

    result = await m.update_task(ctx, UpdateTaskParams(
        task_id=task.data.id, status="cancelled"))
    assert result.status == "error"


async def test_error_update_task_unknown_task():
    # Same app-wide get() contract as list_checklist_items above.
    ctx = MockContext()
    with pytest.raises(ValueError, match="Task not found"):
        await m.update_task(ctx, UpdateTaskParams(
            task_id="ghost-task", status="done"))


# ── Part D2 (SCENARIO_TESTING_STANDARD.md): idempotency / double-invocation ─

async def test_d2_double_approve_evidence_pack_is_naturally_idempotent():
    """approve_evidence_pack has no prior-status guard -- it just overwrites
    the pack's approved_by/approved_at/approval_note fields again. A second
    approval call (e.g. a retried request) must succeed cleanly with the
    same semantics, not crash or silently double anything."""
    import schemas as s

    ctx = MockContext()
    case_id = await _seed_case(ctx)
    item = await m.register_evidence(ctx, RegisterEvidenceParams(
        case_id=case_id, title_text="Bank statement Q1",
        source_url="https://example.com/statement.pdf", period="Q1"))
    await m.review_evidence(ctx, s.ReviewEvidenceParams(
        evidence_item_id=item.data.id, status="approved_for_pack",
        approved_by="Elena"))
    await m.build_evidence_pack(ctx, s.BuildEvidencePackParams(case_id=case_id))

    first = await m.approve_evidence_pack(ctx, s.ApproveEvidencePackParams(
        case_id=case_id, approved_by="Elena", approval_note="Looks complete."))
    assert first.status == "success", first.error

    second = await m.approve_evidence_pack(ctx, s.ApproveEvidencePackParams(
        case_id=case_id, approved_by="Elena", approval_note="Looks complete."))
    assert second.status == "success", second.error
    assert second.data.status == "approved"


# ── Part D3 (SCENARIO_TESTING_STANDARD.md): security / SSRF surface -------

async def test_d3_register_evidence_never_fetches_source_url():
    """register_evidence's own description states it explicitly: 'This app
    does not fetch, interpret or validate the document.' source_url is
    purely stored data (an HTTPS pointer a human already trusts), never
    dereferenced by this app -- confirmed here by grepping main.py for any
    fetch call anywhere near source_url, so a future change threading it
    into an outbound request trips this test."""
    import inspect
    src = inspect.getsource(m)
    register_src = src[src.index("async def register_evidence"):
                        src.index("async def review_evidence")]
    for banned in ("ctx.http", "httpx.", "requests.", "urlopen"):
        assert banned not in register_src, (
            f"register_evidence must never fetch source_url ({banned} found)")
