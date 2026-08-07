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
        "statuses": {"open": "Open", "ready_for_review": "Ready for review", "approved": "Approved", "closed": "Closed", "missing": "Not received", "received": "Received", "needs_review": "Awaiting review", "rejected": "Rejected", "approved_for_pack": "Accepted into pack", "in_progress": "In progress", "blocked": "Blocked", "done": "Done"},
        "next_step": "Next step",
        "next_missing_checklist": "Add your first required document or control to the checklist.",
        "next_checklist_incomplete": "Checklist accepted into pack: {approved} of {total}. Keep reviewing the rest before building the pack.",
        "next_need_evidence": "Register at least one evidence link and get it reviewed by a named human.",
        "next_ready_to_build": "All required checklist items are accepted. You can build the read-only evidence pack.",
        "next_ready_to_approve": "The evidence pack has been built. A named human can approve it now.",
        "next_done": "This case's evidence pack has been approved. No further action required.",
        "required_mark": "Required", "optional_mark": "Optional",
        "pack_summary_line": "{checklist_approved}/{checklist_total} checklist items accepted · {evidence_approved}/{evidence_total} evidence approved · {tasks_done}/{tasks_total} tasks done",
        "pack_summary_blockers": "{blockers} item(s) still block the pack.",
        "pack_summary_clear": "No blockers — ready to build.",
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
        "statuses": {"open": "Открыт", "ready_for_review": "Готов к проверке", "approved": "Подтверждён", "closed": "Закрыт", "missing": "Не получено", "received": "Получено", "needs_review": "Ожидает проверки", "rejected": "Отклонено", "approved_for_pack": "Принято в пакет", "in_progress": "В работе", "blocked": "Заблокировано", "done": "Готово"},
        "next_step": "Следующий шаг",
        "next_missing_checklist": "Добавьте первый обязательный документ или контроль в checklist.",
        "next_checklist_incomplete": "Принято в пакет: {approved} из {total} пунктов checklist. Проверьте оставшиеся, прежде чем собирать пакет.",
        "next_need_evidence": "Зарегистрируйте хотя бы одну ссылку на доказательство и получите проверку именованного человека.",
        "next_ready_to_build": "Все обязательные пункты checklist приняты. Можно собрать read-only индекс пакета.",
        "next_ready_to_approve": "Индекс пакета собран. Именованный человек может подтвердить его сейчас.",
        "next_done": "Пакет доказательств по этому кейсу подтверждён. Дальнейших действий не требуется.",
        "required_mark": "Обязательно", "optional_mark": "Необязательно",
        "pack_summary_line": "{checklist_approved}/{checklist_total} пунктов checklist принято · {evidence_approved}/{evidence_total} доказательств проверено · {tasks_done}/{tasks_total} задач завершено",
        "pack_summary_blockers": "блокирует сборку пакета: {blockers}.",
        "pack_summary_clear": "Блокеров нет — можно собирать.",
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
        "statuses": {"open": "Deschis", "ready_for_review": "Pregătit pentru revizuire", "approved": "Aprobat", "closed": "Închis", "missing": "Nu a fost primit", "received": "Primit", "needs_review": "Așteaptă revizuire", "rejected": "Respins", "approved_for_pack": "Acceptat în dosar", "in_progress": "În lucru", "blocked": "Blocat", "done": "Finalizat"},
        "next_step": "Următorul pas",
        "next_missing_checklist": "Adaugă primul document sau control obligatoriu în lista de verificare.",
        "next_checklist_incomplete": "Acceptate în dosar: {approved} din {total} elemente. Revizuiește restul înainte de a crea dosarul.",
        "next_need_evidence": "Înregistrează cel puțin un link de dovadă și obține revizuirea unei persoane identificate.",
        "next_ready_to_build": "Toate elementele obligatorii sunt acceptate. Poți crea indexul read-only al dosarului.",
        "next_ready_to_approve": "Indexul dosarului a fost creat. O persoană identificată îl poate aproba acum.",
        "next_done": "Dosarul de dovezi al acestui caz a fost aprobat. Nu este necesară nicio altă acțiune.",
        "required_mark": "Obligatoriu", "optional_mark": "Opțional",
        "pack_summary_line": "{checklist_approved}/{checklist_total} elemente acceptate · {evidence_approved}/{evidence_total} dovezi aprobate · {tasks_done}/{tasks_total} sarcini finalizate",
        "pack_summary_blockers": "{blockers} element(e) blochează încă dosarul.",
        "pack_summary_clear": "Fără blocaje — poate fi creat.",
    },
}


def _copy(language: str) -> dict:
    return COPY.get(language, COPY["en"])


def _status_label(status: str, copy: dict) -> str:
    return copy.get("statuses", {}).get(status, status.replace("_", " "))


def _status_options(copy: dict, *values: str) -> list[dict]:
    return [{"value": value, "label": _status_label(value, copy)} for value in values]


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
        icon="📁", badge=ui.Badge(_status_label(status, copy), color=color),
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
        ui.Text(f"{record.get(title_key, '')} — {_status_label(record.get('status', ''), copy)}", variant="caption") for record in records
    ])


def _pack_summary(copy: dict, checklist: list, evidence: list, tasks: list) -> str:
    """Human-readable readiness counts before a named human approves the pack."""
    checklist_total, checklist_approved = len(checklist), sum(1 for i in checklist if i.get("status") == "approved_for_pack")
    evidence_total, evidence_approved = len(evidence), sum(1 for i in evidence if i.get("status") == "approved_for_pack")
    tasks_total, tasks_done = len(tasks), sum(1 for i in tasks if i.get("status") == "done")
    line = copy["pack_summary_line"].format(
        checklist_approved=checklist_approved, checklist_total=checklist_total,
        evidence_approved=evidence_approved, evidence_total=evidence_total,
        tasks_done=tasks_done, tasks_total=tasks_total,
    )
    blockers = (checklist_total - checklist_approved) + (0 if evidence_approved > 0 else 1 if evidence_total == 0 else evidence_total - evidence_approved)
    tail = copy["pack_summary_clear"] if blockers <= 0 else copy["pack_summary_blockers"].format(blockers=blockers)
    return f"{line}\n{tail}"


def _next_step_message(copy: dict, case: dict, checklist: list, evidence: list, packs: list) -> str:
    """Tell a first-time human what to do next, derived from stored state only."""
    if case.get("status") == "approved":
        return copy["next_done"]
    if not checklist:
        return copy["next_missing_checklist"]
    approved_checklist = sum(1 for item in checklist if item.get("status") == "approved_for_pack")
    total_checklist = len(checklist)
    if approved_checklist < total_checklist:
        return copy["next_checklist_incomplete"].format(approved=approved_checklist, total=total_checklist)
    if not any(item.get("status") == "approved_for_pack" for item in evidence):
        return copy["next_need_evidence"]
    if not packs:
        return copy["next_ready_to_build"]
    return copy["next_ready_to_approve"]


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
    item_statuses = _status_options(copy, "received", "needs_review", "rejected", "approved_for_pack")
    task_statuses = _status_options(copy, "open", "in_progress", "blocked", "done")

    next_step_card = ui.Card(title=copy["next_step"], content=ui.Text(_next_step_message(copy, case, checklist, evidence, packs), variant="body"))
    header = ui.Card(title=case.get("case_name", copy["untitled"]), subtitle=" · ".join(filter(None, [case.get("organization_name", ""), case.get("period", ""), case.get("request_type", "")])), content=ui.Stack(direction="h", gap=2, children=[
        ui.Badge(_status_label(case.get("status", "open"), copy), color="green" if case.get("status") == "approved" else "yellow" if case.get("status") == "ready_for_review" else "gray"),
        ui.Button(copy["back"], variant="secondary", on_click=ui.Call("__panel__evidence_cases", language=language)),
    ]))
    checklist_card = ui.Card(title=copy["checklist"], content=ui.Stack(direction="v", gap=2, children=[
        _record_list(checklist, "label", copy),
        ui.Text(f"{copy['required_mark']}: {copy['requirement']}. {copy['optional_mark']}: {copy['requirement_help']}, {copy['responsible']}, {copy['due_date']}.", variant="caption"),
        ui.Form(action="add_checklist_item", submit_label=copy["add_requirement"], defaults={"case_id": case_id}, children=[
            ui.Input(param_name="label", placeholder=copy["requirement"]),
            ui.Input(param_name="description", placeholder=copy["requirement_help"]),
            ui.Input(param_name="owner", placeholder=copy["responsible"]),
            ui.Input(param_name="due_date", placeholder=copy["due_date"]),
        ]),
    ]))
    evidence_card = ui.Card(title=copy["evidence"], content=ui.Stack(direction="v", gap=2, children=[
        _record_list(evidence, "title_text", copy),
        ui.Text(f"{copy['required_mark']}: {copy['evidence_title']}, {copy['https_link']}. {copy['optional_mark']}: {copy['source_type']}, {copy['link_to_requirement']}, {copy['period']}, {copy['reference']}, {copy['evidence_owner']}.", variant="caption"),
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
        ui.Text(f"{copy['required_mark']}: {copy['task_title']}. {copy['optional_mark']}: {copy['assignee']}, {copy['due_date']}, {copy['link_to_evidence']}.", variant="caption"),
        ui.Form(action="create_task", submit_label=copy["create_task"], defaults={"case_id": case_id}, children=[
            ui.Input(param_name="title_text", placeholder=copy["task_title"]),
            ui.Input(param_name="assignee", placeholder=copy["assignee"]),
            ui.Input(param_name="due_date", placeholder=copy["due_date"]),
            ui.Select(param_name="evidence_item_id", options=evidence_options),
        ]),
    ]))
    review_card = ui.Card(title=copy["review"], subtitle=copy["safety"], content=ui.Stack(direction="v", gap=2, children=[
        ui.Text(f"{copy['required_mark']}: {copy['select_item']}, {copy['status']}, {copy['named_reviewer']}.", variant="caption"),
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
        ui.Text(_pack_summary(copy, checklist, evidence, tasks), variant="caption"),
        _record_list(packs, "status", copy),
        ui.Text(f"{copy['required_mark']}: {copy['approver']}, {copy['approval_note']}.", variant="caption"),
        ui.Button(copy["build_pack"], variant="primary", on_click=ui.Call("build_evidence_pack", case_id=case_id)),
        ui.Form(action="approve_evidence_pack", submit_label=copy["approve"], defaults={"case_id": case_id}, children=[
            ui.Input(param_name="approved_by", placeholder=copy["approver"]), ui.Input(param_name="approval_note", placeholder=copy["approval_note"]),
        ]),
    ]))
    return ui.Stack(direction="v", gap=3, children=[_language_switcher(language, case_id), header, next_step_card, ui.Grid(columns=2, gap=3, children=[checklist_card, evidence_card, tasks_card, review_card, pack_card])])
