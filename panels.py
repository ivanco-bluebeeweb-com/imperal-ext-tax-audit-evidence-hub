"""Panel-first workspace for Tax & Audit Evidence Readiness Hub.

The UI is intentionally a guide for the human workflow; all safety gates are
implemented by the handlers and remain authoritative.
"""
from __future__ import annotations

from imperal_sdk import ui
from app import ext


COPY = {
    "en": {
        "language": "Language", "start": "Start an evidence-readiness case",
        "safety": "Human-led preparation — not tax advice or filing", "create": "Create case",
        "case": "FY2026 audit PBC — Acme", "organisation": "Organisation / client",
        "period": "FY2026 or 2026-09", "request": "Audit PBC, tax inquiry, month-end close…",
        "owner": "Human case owner", "control": "Human control points",
        "control_subtitle": "The system coordinates; specialists decide.", "cases": "Cases",
        "empty": "No cases yet. Start with one real preparation workflow.", "untitled": "Untitled case",
        "steps": ["1. Define the checklist", "2. Register evidence links and assign gaps", "3. A named human reviews evidence and checklist items", "4. Build the pack only when every required item is approved", "5. A named human approves readiness — never a tax decision"],
    },
    "ru": {
        "language": "Язык", "start": "Создать кейс готовности доказательств",
        "safety": "Подготовку ведёт человек — это не налоговая консультация и не подача отчётности", "create": "Создать кейс",
        "case": "Аудиторский PBC за 2026 год — DemoCo", "organisation": "Организация / клиент",
        "period": "2026 финансовый год или 2026-09", "request": "Аудиторский PBC, налоговый запрос, закрытие месяца…",
        "owner": "Ответственный за кейс", "control": "Точки человеческого контроля",
        "control_subtitle": "Система координирует; решение принимают специалисты.", "cases": "Кейсы",
        "empty": "Кейсов пока нет. Начните с одного реального процесса подготовки.", "untitled": "Кейс без названия",
        "steps": ["1. Определите checklist", "2. Зарегистрируйте ссылки на доказательства и назначьте задачи", "3. Именованный человек проверяет доказательства и checklist", "4. Соберите пакет только после подтверждения всех обязательных пунктов", "5. Именованный человек подтверждает готовность — это не налоговое решение"],
    },
    "ro": {
        "language": "Limbă", "start": "Creează un caz de pregătire a dovezilor",
        "safety": "Pregătire condusă de oameni — nu este consultanță fiscală și nu este depunere", "create": "Creează cazul",
        "case": "PBC pentru audit FY2026 — DemoCo", "organisation": "Organizație / client",
        "period": "Anul financiar 2026 sau 2026-09", "request": "PBC pentru audit, solicitare fiscală, închidere lunară…",
        "owner": "Responsabilul cazului", "control": "Puncte de control uman",
        "control_subtitle": "Sistemul coordonează; specialiștii decid.", "cases": "Cazuri",
        "empty": "Nu există cazuri încă. Începe cu un flux real de pregătire.", "untitled": "Caz fără titlu",
        "steps": ["1. Definește lista de verificare", "2. Înregistrează linkurile către dovezi și atribuie lipsurile", "3. O persoană identificată verifică dovezile și lista", "4. Creează dosarul numai după aprobarea tuturor elementelor obligatorii", "5. O persoană identificată confirmă pregătirea — nu este o decizie fiscală"],
    },
}


def _copy(language: str) -> dict:
    return COPY.get(language, COPY["en"])


def _language_switcher(language: str) -> ui.UINode:
    return ui.Card(
        title=_copy(language)["language"],
        content=ui.Stack(direction="h", gap=1, children=[
            ui.Button("RU", variant="primary" if language == "ru" else "secondary", on_click=ui.Call("__panel__evidence_cases", language="ru")),
            ui.Button("RO", variant="primary" if language == "ro" else "secondary", on_click=ui.Call("__panel__evidence_cases", language="ro")),
            ui.Button("EN", variant="primary" if language == "en" else "secondary", on_click=ui.Call("__panel__evidence_cases", language="en")),
        ]),
    )


def _case_row(record: dict, copy: dict) -> ui.ListItem:
    status = record.get("status", "open")
    color = {"open": "gray", "ready_for_review": "yellow", "approved": "green", "closed": "gray"}.get(status, "gray")
    subtitle = " · ".join(x for x in [record.get("organization_name", ""), record.get("period", ""), record.get("request_type", "")] if x)
    return ui.ListItem(id=record.get("id", ""), title=record.get("case_name", copy["untitled"]), subtitle=subtitle, icon="📁", badge=ui.Badge(status.replace("_", " "), color=color))


def _create_case_form(copy: dict) -> ui.UINode:
    return ui.Card(
        title=copy["start"], subtitle=copy["safety"],
        content=ui.Form(action="create_case", submit_label=copy["create"], children=[
            ui.Input(param_name="case_name", placeholder=copy["case"]),
            ui.Input(param_name="organization_name", placeholder=copy["organisation"]),
            ui.Input(param_name="period", placeholder=copy["period"]),
            ui.Input(param_name="request_type", placeholder=copy["request"]),
            ui.Input(param_name="owner", placeholder=copy["owner"]),
        ]),
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
async def evidence_cases_panel(ctx, language: str = "en", **kwargs) -> object:
    """Render the workspace in the selected UI language (RU, RO or EN)."""
    language = language if language in COPY else "en"
    copy = _copy(language)
    page = await ctx.store.query("evidence_cases", order_by="-created_at", limit=100)
    records = [doc.data | {"id": doc.id} for doc in page.data]
    items = [_case_row(record, copy) for record in records]
    workflow = ui.Card(
        title=copy["control"], subtitle=copy["control_subtitle"],
        content=ui.Stack(direction="v", gap=1, children=[ui.Text(step, variant="caption") for step in copy["steps"]]),
    )
    cases = ui.Section(
        title=f"{copy['cases']} ({len(items)})",
        children=[ui.List(items=items) if items else ui.Text(copy["empty"], variant="caption")],
    )
    return ui.Stack(direction="v", gap=3, children=[_language_switcher(language), _create_case_form(copy), ui.Divider(), workflow, ui.Divider(), cases])
