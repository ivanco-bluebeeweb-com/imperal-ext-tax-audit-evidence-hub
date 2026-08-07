"""Panel-first workspace for Tax & Audit Evidence Readiness Hub.

The UI guides a human-led workflow. Handlers remain authoritative for every
approval, HTTPS check and evidence-pack safety gate.
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
        "open_case": "Open case", "back": "Back to cases", "case_details": "Case details",
        "checklist": "Checklist", "add_requirement": "Add requirement", "requirement": "Required document or control", "requirement_help": "Why it is needed / how a human must check it", "responsible": "Responsible person", "due_date": "Due date (YYYY-MM-DD)",
        "evidence": "Evidence register", "register_evidence": "Register evidence link", "evidence_title": "Evidence title", "https_link": "HTTPS link to an existing document or storage location", "source_type": "Source type", "reference": "Reference / document number", "evidence_owner": "Evidence owner", "link_to_requirement": "Link to checklist item (optional)",
        "tasks": "Preparation tasks", "create_task": "Create task", "task_title": "Concrete human-owned task", "assignee": "Assignee", "link_to_evidence": "Link to evidence (optional)",
        "review": "Human review", "review_checklist": "Review checklist item", "review_evidence": "Review evidence", "select_item": "Select item", "select_evidence": "Select evidence", "status": "Status", "review_note": "Human review note", "named_reviewer": "Named human reviewer", "save_review": "Save human review",
        "pack": "Evidence pack", "build_pack": "Build read-only evidence-pack index", "approve_pack": "Record named human pack approval", "approver": "Named human approver", "approval_note": "Approval note — not a tax opinion", "approve": "Approve evidence pack",
        "nothing": "Nothing registered yet.", "steps": ["1. Define the checklist", "2. Register evidence links and assign gaps", "3. A named human reviews evidence and checklist items", "4. Build the pack only when every required item is approved", "5. A named human approves readiness — never a tax decision"],
    },
    "ru": {
        "language": "Язык", "start": "Создать кейс готовности доказательств",
        "safety": "Подготовку ведёт человек — это не налоговая консультация и не подача отчётности", "create": "Создать кейс",
        "case": "Аудиторский PBC за 2026 год — DemoCo", "organisation": "Организация / клиент",
        "period": "2026 финансовый год или 2026-09", "request": "Аудиторский PBC, налоговый запрос, закрытие месяца…",
        "owner": "Ответственный за кейс", "control": "Точки человеческого контроля",
        "control_subtitle": "Система координирует; решение принимают специалисты.", "cases": "Кейсы",
        "empty": "Кейсов пока нет. Начните с одного реального процесса подготовки.", "untitled": "Кейс без названия",
        "open_case": "Открыть кейс", "back": "К списку кейсов", "case_details": "Детали кейса",
        "checklist": "Checklist", "add_requirement": "Добавить требование", "requirement": "Обязательный документ или контроль", "requirement_help": "Зачем это нужно / как должен проверить человек", "responsible": "Ответственный", "due_date": "Срок (ГГГГ-ММ-ДД)",
        "evidence": "Реестр доказательств", "register_evidence": "Зарегистрировать ссылку на доказательство", "evidence_title": "Название доказательства", "https_link": "HTTPS-ссылка на существующий документ или хранилище", "source_type": "Тип источника", "reference": "Номер документа / ссылка", "evidence_owner": "Владелец доказательства", "link_to_requirement": "Связать с пунктом checklist (необязательно)",
        "tasks": "Задачи подготовки", "create_task": "Создать задачу", "task_title": "Конкретная задача человека", "assignee": "Исполнитель", "link_to_evidence": "Связать с доказательством (необязательно)",
        "review": "Проверка человеком", "review_checklist": "Проверить пункт checklist", "review_evidence": "Проверить доказательство", "select_item": "Выберите пункт", "select_evidence": "Выберите доказательство", "status": "Статус", "review_note": "Заметка человека при проверке", "named_reviewer": "Имя проверяющего", "save_review": "Сохранить проверку",
        "pack": "Пакет доказательств", "build_pack": "Собрать read-only индекс пакета", "approve_pack": "Записать именное подтверждение пакета", "approver": "Имя утверждающего", "approval_note": "Заметка о подтверждении — не налоговое заключение", "approve": "Подтвердить пакет доказательств",
        "nothing": "Пока ничего не зарегистрировано.", "steps": ["1. Определите checklist", "2. Зарегистрируйте ссылки на доказательства и назначьте задачи", "3. Именованный человек проверяет доказательства и checklist", "4. Соберите пакет только после подтверждения всех обязательных пунктов", "5. Именованный человек подтверждает готовность — это не налоговое решение"],
    },
    "ro": {
        "language": "Limbă", "start": "Creează un caz de pregătire a dovezilor",
        "safety": "Pregătire condusă de oameni — nu este consultanță fiscală și nu este depunere", "create": "Creează cazul",
        "case": "PBC pentru audit FY2026 — DemoCo", "organisation": "Organizație / client",
        "period": "Anul financiar 2026 sau 2026-09", "request": "PBC pentru audit, solicitare fiscală, închidere lunară…",
        "owner": "Responsabilul cazului", "control": "Puncte de control uman",
        "control_subtitle": "Sistemul coordonează; specialiștii decid.", "cases": "Cazuri",
        "empty": "Nu există cazuri încă. Începe cu un flux real de pregătire.", "untitled": "Caz fără titlu",
        "open_case": "Deschide cazul", "back": "Înapoi la cazuri", "case_details": "Detaliile cazului",
        "checklist": "Listă de verificare", "add_requirement": "Adaugă cerință", "requirement": "Document sau control obligatoriu", "requirement_help": "De ce este necesar / cum trebuie verificat de o persoană", "responsible": "Responsabil", "due_date": "Termen (AAAA-LL-ZZ)",
        "evidence": "Registrul dovezilor", "register_evidence": "Înregistrează linkul dovezii", "evidence_title": "Titlul dovezii", "https_link": "Link HTTPS către un document sau spațiu de stocare existent", "source_type": "Tipul sursei", "reference": "Referință / număr document", "evidence_owner": "Proprietarul dovezii", "link_to_requirement": "Leagă de elementul din listă (opțional)",
        "tasks": "Sarcini de pregătire", "create_task": "Creează sarcină", "task_title": "Sarcină concretă deținută de o persoană", "assignee": "Persoană responsabilă", "link_to_evidence": "Leagă de dovadă (opțional)",
        "review": "Revizuire umană", "review_checklist": "Revizuiește elementul din listă", "review_evidence": "Revizuiește dovada", "select_item": "Selectează elementul", "select_evidence": "Selectează dovada", "status": "Status", "review_note": "Notă de revizuire umană", "named_reviewer": "Numele persoanei care revizuiește", "save_review": "Salvează revizuirea",
        "pack": "Dosar de dovezi", "build_pack": "Creează indexul read-only al dosarului", "approve_pack": "Înregistrează aprobarea umană nominală", "approver": "Numele aprobatorului", "approval_note": "Notă de aprobare — nu este opinie fiscală", "approve": "Aprobă dosarul de dovezi",
        "nothing": "Încă nu este nimic înregistrat.", "steps": ["1. Definește lista de verificare", "2. Înregistrează linkurile către dovezi și atribuie lipsurile", "3. O persoană identificată verifică dovezile și lista", "4. Creează dosarul numai după aprobarea tuturor elementelor obligatorii", "5. O persoană identificată confirmă pregătirea — nu este o decizie fiscală"],
    },
}


def _copy(language: str) -> dict:
    return COPY.get(language, COPY["en"])


def _language_switcher(language: str, case_id: str = "") -> ui.UINode:
    target = "__panel__evidence_case_detail" if case_id else "__panel__evidence_cases"
    return ui.Card(
        title=_copy(language)["language"],
        content=ui.Stack(direction="h", gap=1, children=[
            ui.Button("RU", variant="primary" if language == "ru" else "secondary", on_click=ui.Call(target, language="ru", case_id=case_id)),
            ui.Button("RO", variant="primary" if language == "ro" else "secondary", on_click=ui.Call(target, language="ro", case_id=case_id)),
            ui.Button("EN", variant="primary" if language == "en" else "secondary", on_click=ui.Call(target, language="en", case_id=case_id)),
        ]),
    )


def _case_row(record: dict, copy: dict, language: str) -> ui.ListItem:
    status = record.get("status", "open")
    color = {"open": "gray", "ready_for_review": "yellow", "approved": "green", "closed": "gray"}.get(status, "gray")
    subtitle = " · ".join(x for x in [record.get("organization_name", ""), record.get("period", ""), record.get("request_type", "")] if x)
    return ui.ListItem(
        id=record.get("id", ""), title=record.get("case_name", copy["untitled"]), subtitle=subtitle,
        icon="📁", badge=ui.Badge(status.replace("_", " "), color=color),
        on_click=ui.Call("__panel__evidence_case_detail", case_id=record.get("id", ""), language=language),
    )


def _create_case_form(copy: dict) -> ui.UINode:
    return ui.Card(title=copy["start"], subtitle=copy["safety"], content=ui.Form(
        action="create_case", submit_label=copy["create"], children=[
            ui.Input(param_name="case_name", placeholder=copy["case"]),
            ui.Input(param_name="organization_name", placeholder=copy["organisation"]),
            ui.Input(param_name="period", placeholder=copy["period"]),
            ui.Input(param_name="request_type", placeholder=copy["request"]),
            ui.Input(param_name="owner", placeholder=copy["owner"]),
        ],
    ))


def _options(records: list, label_key: str, placeholder: str) -> list[dict]:
    return [{"value": "", "label": placeholder}] + [
        {"value": record["id"], "label": record.get(label_key, record["id"])} for record in records
    ]


def _record_list(records: list, title_key: str, copy: dict) -> ui.UINode:
    if not records:
        return ui.Text(copy["nothing"], variant="caption")
    return ui.Stack(direction="v", gap=1, children=[
        ui.Text(f"{record.get(title_key, '')} — {record.get('status', '')}", variant="caption") for record in records
    ])


@ext.panel("evidence_cases", slot="left", title="Evidence Readiness", icon="📂", default_width=360, min_width=300, max_width=520)
async def evidence_cases_panel(ctx, language: str = "en", **kwargs) -> object:
    """List cases and open a detail workspace for a selected case."""
    language = language if language in COPY else "en"
    copy = _copy(language)
    page = await ctx.store.query("evidence_cases", order_by="-created_at", limit=100)
    records = [doc.data | {"id": doc.id} for doc in page.data]
    items = [_case_row(record, copy, language) for record in records]
    workflow = ui.Card(title=copy["control"], subtitle=copy["control_subtitle"], content=ui.Stack(
        direction="v", gap=1, children=[ui.Text(step, variant="caption") for step in copy["steps"]],
    ))
    cases = ui.Section(title=f"{copy['cases']} ({len(items)})", children=[
        ui.List(items=items) if items else ui.Text(copy["empty"], variant="caption")
    ])
    return ui.Stack(direction="v", gap=3, children=[_language_switcher(language), _create_case_form(copy), ui.Divider(), workflow, ui.Divider(), cases])


@ext.panel("evidence_case_detail", slot="center", title="Evidence case", icon="📋", center_overlay=True)
async def evidence_case_detail_panel(ctx, case_id: str = "", language: str = "en", **kwargs) -> object:
    """Human-led P0 workspace for one evidence-readiness case."""
    language = language if language in COPY else "en"
    copy = _copy(language)
    if not case_id:
        return ui.Empty(message=copy["empty"], icon="📋")
    case_doc = await ctx.store.get("evidence_cases", case_id)
    if not case_doc:
        return ui.Empty(message=copy["empty"], icon="📋")
    case = case_doc.data | {"id": case_doc.id}
    checklist_page = await ctx.store.query("checklist_items", limit=200)
    evidence_page = await ctx.store.query("evidence_items", limit=200)
    tasks_page = await ctx.store.query("case_tasks", limit=200)
    packs_page = await ctx.store.query("evidence_packs", limit=200)
    checklist = [doc.data | {"id": doc.id} for doc in checklist_page.data if doc.data.get("case_id") == case_id]
    evidence = [doc.data | {"id": doc.id} for doc in evidence_page.data if doc.data.get("case_id") == case_id]
    tasks = [doc.data | {"id": doc.id} for doc in tasks_page.data if doc.data.get("case_id") == case_id]
    packs = [doc.data | {"id": doc.id} for doc in packs_page.data if doc.data.get("case_id") == case_id]
    checklist_options = _options(checklist, "label", copy["select_item"])
    evidence_options = _options(evidence, "title_text", copy["select_evidence"])
    item_statuses = [{"value": value, "label": value.replace("_", " ")} for value in ("received", "needs_review", "rejected", "approved_for_pack")]
    task_statuses = [{"value": value, "label": value.replace("_", " ")} for value in ("open", "in_progress", "blocked", "done")]

    header = ui.Card(title=case.get("case_name", copy["untitled"]), subtitle=" · ".join(filter(None, [case.get("organization_name", ""), case.get("period", ""), case.get("request_type", "")])), content=ui.Stack(direction="h", gap=2, children=[
        ui.Badge(case.get("status", "open").replace("_", " "), color="green" if case.get("status") == "approved" else "yellow" if case.get("status") == "ready_for_review" else "gray"),
        ui.Button(copy["back"], variant="secondary", on_click=ui.Call("__panel__evidence_cases", language=language)),
    ]))
    checklist_card = ui.Card(title=copy["checklist"], content=ui.Stack(direction="v", gap=2, children=[
        _record_list(checklist, "label", copy),
        ui.Form(action="add_checklist_item", submit_label=copy["add_requirement"], defaults={"case_id": case_id}, children=[
            ui.Input(param_name="label", placeholder=copy["requirement"]),
            ui.Input(param_name="description", placeholder=copy["requirement_help"]),
            ui.Input(param_name="owner", placeholder=copy["responsible"]),
            ui.Input(param_name="due_date", placeholder=copy["due_date"]),
        ]),
    ]))
    evidence_card = ui.Card(title=copy["evidence"], content=ui.Stack(direction="v", gap=2, children=[
        _record_list(evidence, "title_text", copy),
        ui.Form(action="register_evidence", submit_label=copy["register_evidence"], defaults={"case_id": case_id}, children=[
            ui.Input(param_name="title_text", placeholder=copy["evidence_title"]),
            ui.Input(param_name="source_url", placeholder=copy["https_link"]),
            ui.Select(param_name="source_type", options=[{"value": "document", "label": "document"}, {"value": "email", "label": "email"}, {"value": "link", "label": "link"}, {"value": "other", "label": "other"}]),
            ui.Select(param_name="checklist_item_id", options=checklist_options),
            ui.Input(param_name="period", placeholder=copy["period"]),
            ui.Input(param_name="reference", placeholder=copy["reference"]),
            ui.Input(param_name="owner", placeholder=copy["evidence_owner"]),
        ]),
    ]))
    tasks_card = ui.Card(title=copy["tasks"], content=ui.Stack(direction="v", gap=2, children=[
        _record_list(tasks, "title_text", copy),
        ui.Form(action="create_task", submit_label=copy["create_task"], defaults={"case_id": case_id}, children=[
            ui.Input(param_name="title_text", placeholder=copy["task_title"]),
            ui.Input(param_name="assignee", placeholder=copy["assignee"]),
            ui.Input(param_name="due_date", placeholder=copy["due_date"]),
            ui.Select(param_name="evidence_item_id", options=evidence_options),
        ]),
    ]))
    review_card = ui.Card(title=copy["review"], subtitle=copy["safety"], content=ui.Stack(direction="v", gap=2, children=[
        ui.Form(action="update_checklist_item", submit_label=copy["review_checklist"], children=[
            ui.Select(param_name="checklist_item_id", options=checklist_options), ui.Select(param_name="status", options=item_statuses),
            ui.Input(param_name="review_note", placeholder=copy["review_note"]), ui.Input(param_name="approved_by", placeholder=copy["named_reviewer"]),
        ]),
        ui.Form(action="review_evidence", submit_label=copy["review_evidence"], children=[
            ui.Select(param_name="evidence_item_id", options=evidence_options), ui.Select(param_name="status", options=item_statuses),
            ui.Input(param_name="review_note", placeholder=copy["review_note"]), ui.Input(param_name="approved_by", placeholder=copy["named_reviewer"]),
        ]),
        ui.Form(action="update_task", submit_label=copy["tasks"], children=[
            ui.Select(param_name="task_id", options=_options(tasks, "title_text", copy["select_item"])), ui.Select(param_name="status", options=task_statuses),
        ]),
    ]))
    pack_card = ui.Card(title=copy["pack"], subtitle=copy["safety"], content=ui.Stack(direction="v", gap=2, children=[
        _record_list(packs, "status", copy),
        ui.Button(copy["build_pack"], variant="primary", on_click=ui.Call("build_evidence_pack", case_id=case_id)),
        ui.Form(action="approve_evidence_pack", submit_label=copy["approve"], defaults={"case_id": case_id}, children=[
            ui.Input(param_name="approved_by", placeholder=copy["approver"]), ui.Input(param_name="approval_note", placeholder=copy["approval_note"]),
        ]),
    ]))
    return ui.Stack(direction="v", gap=3, children=[_language_switcher(language, case_id), header, ui.Grid(columns=2, gap=3, children=[checklist_card, evidence_card, tasks_card, review_card, pack_card])])
