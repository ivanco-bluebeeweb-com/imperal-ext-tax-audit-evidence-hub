"""Panel-first workspace for Tax & Audit Evidence Readiness Hub.

The UI is intentionally a guide for the human workflow; all safety gates are
implemented by the handlers and remain authoritative.
"""
from __future__ import annotations

from imperal_sdk import ui
from app import ext


def _case_row(record: dict) -> ui.ListItem:
    status = record.get("status", "open")
    color = {"open": "gray", "ready_for_review": "yellow", "approved": "green", "closed": "gray"}.get(status, "gray")
    subtitle = " · ".join(x for x in [record.get("organization_name", ""), record.get("period", ""), record.get("request_type", "")] if x)
    return ui.ListItem(
        id=record.get("id", ""),
        title=record.get("case_name", "Untitled case"),
        subtitle=subtitle,
        icon="📁",
        badge=ui.Badge(status.replace("_", " "), color=color),
    )


def _create_case_form() -> ui.UINode:
    return ui.Card(
        title="Start an evidence-readiness case",
        subtitle="Human-led preparation — not tax advice or filing",
        content=ui.Form(
            action="create_case",
            submit_label="Create case",
            children=[
                ui.Input(param_name="case_name", placeholder="FY2026 audit PBC — Acme"),
                ui.Input(param_name="organization_name", placeholder="Organisation / client"),
                ui.Input(param_name="period", placeholder="FY2026 or 2026-09"),
                ui.Input(param_name="request_type", placeholder="Audit PBC, tax inquiry, month-end close…"),
                ui.Input(param_name="owner", placeholder="Human case owner"),
            ],
        ),
    )


@ext.panel(
    "evidence_cases",
    slot="left",
    title="Evidence Readiness",
    icon="📂",
    default_width=360,
    min_width=300,
    max_width=520,
)
async def evidence_cases_panel(ctx, **kwargs) -> object:
    page = await ctx.store.query("evidence_cases", order_by="-created_at", limit=100)
    records = [doc.data | {"id": doc.id} for doc in page.data]
    items = [_case_row(record) for record in records]
    workflow = ui.Card(
        title="Human control points",
        subtitle="The system coordinates; specialists decide.",
        content=ui.Stack(direction="v", gap=1, children=[
            ui.Text("1. Define the checklist", variant="caption"),
            ui.Text("2. Register evidence links and assign gaps", variant="caption"),
            ui.Text("3. A named human reviews evidence and checklist items", variant="caption"),
            ui.Text("4. Build the pack only when every required item is approved", variant="caption"),
            ui.Text("5. A named human approves readiness — never a tax decision", variant="caption"),
        ]),
    )
    cases = ui.Section(
        title=f"Cases ({len(items)})",
        children=[ui.List(items=items) if items else ui.Text("No cases yet. Start with one real preparation workflow.", variant="caption")],
    )
    return ui.Stack(direction="v", gap=3, children=[_create_case_form(), ui.Divider(), workflow, ui.Divider(), cases])
