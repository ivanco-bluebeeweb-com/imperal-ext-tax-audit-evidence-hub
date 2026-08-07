# Tax & Audit Evidence Readiness Hub — Master Development Plan

**Product purpose:** a human-led operating layer for tax, finance and audit evidence preparation.  
**Primary use case:** turn a scattered request, audit PBC list or close-preparation process into a controlled case with explicit requirements, evidence references, owned tasks, a reviewable pack and named human approval.  
**Product owner:** Vlad Ivanco  
**Last reviewed:** 7 August 2026  
**Related event:** TAXCON’26, 24 September 2026  
**Companion demo plan:** [`TAXCON26_DEMO_TOOLKIT.md`](TAXCON26_DEMO_TOOLKIT.md)  
**Preparation record:** [`PREPARATION.md`](PREPARATION.md)  
**Discovery guide:** [`DISCOVERY_INTERVIEW_GUIDE.md`](DISCOVERY_INTERVIEW_GUIDE.md)

> **Delivery rule:** local code, tests, a commit or a manifest are not “delivered product” by themselves. A slice becomes delivered only after it is deployed, installed and manually verified in the Imperal panel with a visible user flow. Until then it is marked **implemented, live unverified**.

---

## 1. Non-negotiable product boundary

### The product does

- organise case preparation;
- make requirements and collection gaps explicit;
- register references to source material;
- coordinate human-owned tasks;
- surface operational completeness and process status;
- assemble a reviewable evidence-pack index;
- record named human review and approval;
- preserve a traceable preparation history.

### The product never does without a separately approved future scope

- interpret tax law or decide tax treatment;
- calculate tax liability;
- provide a tax opinion or assurance conclusion;
- determine that evidence is legally sufficient;
- perform audit procedures or replace audit judgement;
- sign, submit or amend declarations/filings;
- silently download, inspect, OCR or export confidential documents;
- approve a package without a named human.

**Plain-language rule:** Webbee manages the workbench; the licensed or responsible professional makes the professional decision.

---

## 2. Product model and success measure

### Core flow

```text
request / audit / close event
  → case
  → human-defined checklist
  → evidence references
  → human review + tasks for gaps
  → evidence-pack index
  → named human pack approval
  → optional human-approved handoff/export
```

### Initial users

| User | Job to be done | What good looks like |
|---|---|---|
| Audit manager | Get a complete PBC package without chasing multiple people blindly | One current checklist, owner per gap, reviewable pack |
| Accounting firm manager | Coordinate a client's evidence preparation | Client/document status visible without losing accountability |
| Tax consultant | Prepare a controlled response package | Every draft source and missing item is visible to a human |
| CFO / finance operations lead | See readiness and blockers before a deadline | Simple status: what is ready, blocked and owned |
| Reviewer / partner | Approve only a complete, reviewed package | Pack has provenance and named preparer/reviewer trail |

### P0 measurable outcome

For a fictional or consented pilot case, a user can complete the core workflow in the panel without engineering help and can answer these four questions in under two minutes:

1. What is this case and what period does it cover?
2. What is still missing or unreviewed?
3. Who owns the next action?
4. Who approved the pack, and on what date?

---

## 3. Current inventory — what has actually been done

### P0 implementation: present in the local extension

| Item | What exists | Evidence | Delivery status |
|---|---|---|---|
| Extension scaffold | App manifest, SDK setup, icon, package files | `imperal.json`, `pyproject.toml`, `main.py`, `app.py` | Implemented, live unverified |
| Cases | Create/list a human-owned case with organisation, period, request type and owner | `create_case`, `list_cases` | Implemented, live unverified |
| Requirements checklist | Add/update/list required documents or controls | `add_checklist_item`, `update_checklist_item`, `list_checklist_items` | Implemented, live unverified |
| Evidence register | Register HTTPS references, period/reference metadata and review status | `register_evidence`, `review_evidence`, `list_evidence` | Implemented, live unverified |
| Work coordination | Create/update/list human-owned tasks | `create_task`, `update_task`, `list_tasks` | Implemented, live unverified |
| Pack construction | Build evidence pack only when checklist is complete and approved evidence exists | `build_evidence_pack` | Implemented, live unverified |
| Human pack approval | Named approval with note | `approve_evidence_pack` | Implemented, live unverified |
| Basic panel | Evidence Readiness panel: create-case form, case list and human-control explanation | `panels.py` | Implemented, live unverified |
| Safety tests | Regression tests for safety contracts and panel registration | `tests/test_smoke.py` | Local tests passed in prior run; live unverified |

### Facts that must not be overstated

- The local app was created and validated in the workspace; it was **not found in the installed-app list** during the latest check.
- Therefore it is not yet proven deployable, installed or visible in the user’s Imperal panel.
- The panel currently visibly covers case creation and case listing. Detailed case workspace interactions, pack review screens and a chronological audit-trail screen must be verified in live; do not claim them as a polished UI until verified.
- Google Drive is currently `reconnect_required` and has context access disabled. It is not usable as a demo source.
- Google Analytics is not usable; it is not relevant to this product flow.
- Google Search Console is working but is unrelated to the TAXCON workflow.

### Existing documents

- Event positioning/outreach: `../taxcon26-imperal-webbee-go-to-market.md`
- P0 product usage and safety: `README.md`
- Event demo inventory and gates: `TAXCON26_DEMO_TOOLKIT.md`

---

## 4. Mandatory delivery gates — before new feature work

### Gate A — deploy and install

**Goal:** establish that the app is actually available to the user, not just present in the workspace.

**Work:**
1. Run build and validation against the exact extension version.
2. Deploy the extension through the approved Imperal developer flow.
3. Install it for the authenticated user.
4. Record deployed version, deploy timestamp and panel entry point in this document.

**Done when:** the app appears in the Imperal panel and opens without an error.

**If blocked:** log the exact observed blocker in the Imperal issues record; do not start P1 functionality as a substitute.

### Gate B — P0 live end-to-end proof

**Goal:** prove the entire safe P0 workflow in the panel with fictional data.

**Test data:** `FY2026 audit PBC — DemoCo`; never customer or personal data.

**Steps:**
1. Create a case.
2. Add at least three checklist requirements.
3. Register safe demo HTTPS evidence references.
4. Show that an incomplete checklist blocks pack construction.
5. Review/approve each required evidence and checklist item with a named human.
6. Create and close one collection task.
7. Build the pack.
8. Approve the pack with a named human and note.
9. Show the resulting status and traceable record.

**Done when:** every step is visible, understandable and works in the panel without developer intervention; screenshots or a recording are saved for demo contingency.

### Gate C — usability correction

**Goal:** make the P0 workflow understandable to a non-technical tax/audit user.

**Work:** observe one internal non-developer dry run and capture every point where the person does not know what to do next.

**Done when:** the user can complete the case without a verbal walkthrough beyond the first sentence.

Only after Gates A–C are passed may we call P0 “ready for TAXCON demo.”

---

## 5. Release plan in priority order

## P0 — Evidence readiness core

### P0.0: deployment and live proof

**Why first:** a non-visible app cannot be a product or event demo.

**Observed release blocker — 7 August 2026:** local build, validation and the three local tests passed. The first cloud deployment attempt stopped before deployment because `tax-audit-evidence-hub` is not registered in the Imperal Developer Catalog. Registration requires a real HTTPS Git URL, but the local project currently has no Git repository or remote. Required release sequence: publish source repository → register the app with its real HTTPS Git URL → deploy → install → complete the DemoCo panel proof.

**Scope:** Gates A–C above; no extra features.

**Visible result:** a user opens Evidence Readiness in the panel and completes the fictional DemoCo case.

**Acceptance criteria:** all Gate B steps pass; build/validate/tests pass; user-facing copy keeps the safety boundary clear.

**Status:** next required work.

---

### P0.1: case-detail workspace, only if Gate B reveals missing UI

**Problem:** the present panel exposes case creation/listing, but users need a clear next step after clicking a case.

**Scope:**
- case detail with checklist, evidence, tasks and readiness summary;
- visible blocker list: missing / awaiting review / approved;
- primary next action based on case state;
- no document reading or automatic classification.

**Visible result:** a user can open one case and understand “what is missing, who owns it and whether the pack can be built.”

**Acceptance criteria:** status is derived from authoritative server state; incomplete requirements cannot appear as ready; all actions retain named human approval gates.

**Not in scope:** Drive, email, document extraction, tax advice, AI decisioning.

**Status:** conditional — build only if the live proof exposes this gap.

---

### P0.2: visible audit trail, only if current records are not legible

**Problem:** a vague claim of audit trail is not enough for auditors/CFOs.

**Scope:** a chronological, read-only case activity view: event type, actor/name, time, linked object and short note.

**Visible result:** reviewer answers “who changed what and when?” without searching across records.

**Acceptance criteria:** append-only event records; no actor spoofing; approval events show named approver; entries are tenant isolated.

**Status:** conditional — build only after exact live UI gap is observed.

---

## P1 — make the core usable repeatedly

### P1.1: workflow templates

**Problem:** an empty case is still too much blank-page work.

**Scope:** human-editable templates that prefill checklist and task structure. Start with only **one** template chosen from discovery evidence:
- Audit PBC;
- month-end close;
- tax-authority inquiry response.

**Visible result:** “Create from Audit PBC template” produces a reviewable starting checklist; the user can edit it before use.

**Acceptance criteria:** templates are never legal/tax conclusions; every requirement remains editable by a human; template version appears in the case record.

**Dependency:** Gates A–C passed plus 8–12 discovery interviews.

**Decision rule:** build the template for the workflow with the strongest combination of frequency, pain and willingness to pilot—not the one that sounds best on stage.

---

### P1.2: roles and approvals

**Problem:** “named person” alone is not enough in a multi-person firm.

**Scope:** case roles (owner, contributor, reviewer, approver), permission boundaries and approval delegation rules.

**Visible result:** people see actions relevant to their role; only permitted reviewers/approvers can advance a case.

**Acceptance criteria:** no cross-tenant data; server-enforced permission checks; approvals remain attributable; role changes are recorded.

**Dependency:** real pilot-team role map.

---

### P1.3: controlled handoff/export

**Problem:** a pack is useful only if a reviewer can receive it safely.

**Scope:** create a read-only pack index/export containing case metadata, checklist status, evidence references and approval record.

**Visible result:** user can prepare a review package index for an auditor, adviser or client without auto-sharing source documents.

**Acceptance criteria:** explicit human confirmation before sharing/export; recipient scope stated; no secret URLs or source content leaked; export logs event.

**Dependency:** roles/permissions and agreed retention policy.

---

## P2 — controlled sources and operational intelligence

### P2.1: document intake from one approved source

**Problem:** manual evidence registration is safe but creates repetitive work.

**Scope:** connect one source only after consent and policy design—likely Google Drive or Mail. Present suggested registration, not silent ingestion.

**Visible result:** user selects a permitted folder/message, sees proposed evidence metadata, and confirms linking it to the case.

**Acceptance criteria:** explicit account and context permission; source scope visible; no background reading beyond authorised scope; retention/deletion policy documented; every link is user-confirmed.

**Dependency:** Google connector is working and the access/privacy design is approved.

**Current blocker:** Google Drive needs reconnecting and context access is disabled. Not demo scope until fixed and live tested.

---

### P2.2: source-aware extraction and discrepancy flags

**Problem:** teams need help spotting operational mismatches, not unsupported legal conclusions.

**Scope:** extract only explicitly permitted operational fields (date/period, reference number, counterparty) and raise review flags.

**Visible result:** “This evidence may fall outside the case period—review it,” with source reference and an owner.

**Acceptance criteria:** confidence and source provenance shown; uncertain extraction defaults to review; system says “flag” rather than “violation”; no autonomous resolution or tax conclusion.

**Dependency:** P2.1, document retention policy, review UX and representative consented test corpus.

---

### P2.3: correspondence workspace

**Problem:** incoming requests and drafts become detached from the evidence pack.

**Scope:** register an inquiry, link it to a case, assemble a draft based on human-selected approved evidence and route to human approval.

**Visible result:** a reviewer can see request → selected evidence → draft → named approval; sending remains explicit and human controlled.

**Acceptance criteria:** draft clearly labelled; citations/provenance to evidence references; no tax opinion generated as fact; no auto-send; full version/audit history.

**Dependency:** P1.2/P1.3 and a working Mail integration with a tested permission model.

---

## P3 — only after successful pilots

Potential directions, not commitments:

- multi-entity portfolio dashboard;
- deadline reminders/automations with explicit owner and opt-in;
- client-facing request portal;
- template library governance;
- analytics for cycle time, blocker types and reviewer workload;
- selected integrations with task trackers.

A P3 item needs a documented pilot result and an explicit product decision. Do not implement it merely because it is technically possible.

---

## 6. Demo timeline and decision points

This is a working sequence from 7 August to TAXCON’26, not a claim that participation is already confirmed.

| Window | Product work | Event work | Exit criterion |
|---|---|---|---|
| 7–10 Aug | Gate A: deploy/install or record blocker | Send AmCham outreach | Real app availability known; participation contact initiated |
| 10–14 Aug | Gate B: DemoCo end-to-end panel proof | Confirm possible format, deadline and audience | Pass/fail evidence recorded; no hidden demo risk |
| 14–21 Aug | Fix only P0 UI gaps discovered in Gate B/C | Submit abstract/speaker materials if requested | 10-minute workflow works in panel or contingency format selected |
| 21–28 Aug | Gate C usability dry run; record contingency | Confirm participation | Demo story frozen; no P1 feature chase |
| 28 Aug–11 Sep | Rehearsal, screenshots/video backup, handout | Slides and logistics | Rehearsed, truthful demo kit |
| 11–24 Sep | Bug fixes only; no scope expansion | Final logistics and event | Stable presentation-ready build |
| 25–29 Sep | Capture feedback and opt-in discovery notes | Follow-up | Evidence for choosing first P1 template |

---

## 7. How we decide what to build next

Before any P1/P2 item, record:

1. **Observed user problem:** quote or workflow fact, not a hunch.
2. **User/role:** who has the problem.
3. **Current workaround:** spreadsheet, inbox, shared drive, task board, etc.
4. **Risk boundary:** what must stay human-controlled.
5. **Smallest vertical slice:** one visible flow.
6. **Panel location:** where a user will see it.
7. **Success and blocked states:** what is shown in each.
8. **Test plan:** unit/regression plus manual panel proof.
9. **Exit decision:** ship, revise or stop.

This record belongs in the relevant issue/roadmap entry before implementation begins.

---

## 8. Known blockers and explicit exclusions

| Item | State | Product decision |
|---|---|---|
| Evidence Hub panel availability | Local code exists; installed live app not confirmed | Gate A is the immediate priority |
| Google Drive | Reconnect required; context access off | Exclude from demo and P1 until repaired/tested |
| Google Analytics | No usable account | Irrelevant to this product; do not spend Tax/Audit roadmap time here |
| Google Search Console | Working | Irrelevant to this product; do not include in demo |
| VBS / Content / SEO / Media / WordPress | Separate product line | Do not put into TAXCON scenario; do not use as proxy progress for Evidence Hub |
| Real client documents | High confidentiality/risk | No live customer data on stage; use fictional DemoCo data only |

---

## 9. Change log

| Date | Change | Status |
|---|---|---|
| 7 Aug 2026 | Initial master plan written; P0 implementation inventory, live delivery gates, roadmap P0–P3 and TAXCON timeline recorded | Current |

