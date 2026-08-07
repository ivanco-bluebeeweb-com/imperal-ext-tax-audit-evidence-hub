# Tax & Audit Evidence Readiness Hub — Preparation

**Preparation status:** initial preparation recorded; discovery still required before P1 expansion  
**Product owner:** Vlad Ivanco  
**Last reviewed:** 7 August 2026  
**Related event:** TAXCON’26 — 24 September 2026  
**Standard:** [`../APP_PREPARATION_STANDARD.md`](../APP_PREPARATION_STANDARD.md)  
**Related delivery plan:** [`TAX_AUDIT_EVIDENCE_DEVELOPMENT_PLAN.md`](TAX_AUDIT_EVIDENCE_DEVELOPMENT_PLAN.md)  
**Related demo plan:** [`TAXCON26_DEMO_TOOLKIT.md`](TAXCON26_DEMO_TOOLKIT.md)

> This preparation note governs the product before and during implementation. Unknowns are marked as hypotheses or discovery questions; they are not presented as customer facts.

---

## 1. Passport

**What it is:** a human-led workspace for preparing tax, finance and audit evidence. It turns scattered preparation into a controlled case:

```text
case → checklist → evidence register → human review → tasks → evidence-pack index → named human approval
```

**Why now:** TAXCON’26 is a focused opportunity to validate whether accounting firms, auditors, tax consultants, CFOs and finance operations need an operational evidence-readiness tool—not an AI that makes tax decisions.

**Business purpose:** test one practical product wedge with a relevant professional audience, then use real discovery evidence to decide what to build next.

---

## 2. Problem statement

### Observed operating problem

When an audit, close or tax-information request starts, a team often gathers documents through email, chats and several storage folders. The team may lack one current list of requirements, a named owner for every gap, a clear review state and a traceable answer to “who approved this package?”.

### Problem statement

> When an audit manager, accounting firm coordinator, tax consultant or finance lead receives an audit PBC list, close requirement or request for explanation, they coordinate documents and follow-ups across disconnected places. This makes completeness, ownership, version/review state and deadline risk hard to see, creating repeated chasing and an unreliable preparation process.

### Current alternatives

- email and chat threads;
- spreadsheets/checklists maintained manually;
- shared folders with inconsistent naming;
- task trackers disconnected from evidence;
- personal knowledge of a senior accountant, manager or reviewer.

### What this app is not solving

It is not solving legal interpretation, tax calculation, tax advisory, audit assurance or filing. Those remain professional activities performed and approved by accountable humans.

---

## 3. Audience, roles and access

| Role | Job to be done | Expected permissions/responsibility |
|---|---|---|
| Case owner / audit manager | Coordinate preparation and remove blockers | Create/manage case, requirements and tasks; see readiness |
| Contributor / accountant | Provide or register requested material and close assigned work | Register evidence references; update assigned tasks; cannot self-approve restricted decisions unless permitted |
| Reviewer / auditor | Check whether listed requirements and evidence are ready for the stated preparation purpose | Review evidence/checklist; record review rationale |
| Approver / partner / responsible professional | Decide whether the assembled package is ready to proceed | Named human approval; accountable for the approval |
| CFO / finance operations lead | See readiness, deadlines and owners without chasing people | Read status/blockers; approval only if assigned that role |

### Access principles

- data is tenant-local and must never cross tenants;
- every future role/permission must be enforced server-side, not only hidden in UI;
- named approval must remain attributable to a real accountable human;
- no external recipient receives data or a pack automatically.

**Known gap:** P0 has named people but not yet a verified multi-person role/permission model. This is P1 work, not a claim of P0 completeness.

---

## 4. User journeys and human decision points

### Primary P0 journey: audit PBC preparation

```text
Audit PBC/request arrives
→ case owner creates a case with organisation, period, purpose and owner
→ human creates/edit checklist requirements
→ contributor registers safe references to received material
→ reviewer marks evidence/checklist ready or asks for follow-up
→ owner creates tasks for gaps
→ system blocks pack construction while requirements remain incomplete
→ reviewer builds evidence-pack index
→ named responsible human approves readiness with a note
```

### Happy-path result

The team can answer in under two minutes: what is the case, what is missing, who owns the next action, and who approved the readiness of the pack.

### Missing/error paths

| Situation | Required product behaviour | Human decision |
|---|---|---|
| Required item has not arrived | Show it as missing; allow task creation | Owner decides who will provide it and by when |
| Evidence reference is unclear/wrong period | Keep it unapproved and request review | Reviewer decides relevance and correction |
| Checklist incomplete | Prevent evidence-pack construction | Reviewer/owner resolves gaps; system never waives them silently |
| Evidence exists but has no human approval | Prevent it from satisfying readiness | Named reviewer decides approval/rejection |
| User wants a professional conclusion | Do not provide one | Qualified professional makes the judgement outside/alongside the tool |

### Mandatory human decision points

1. What evidence/checklist requirements apply to a case.
2. Whether a referenced item is appropriate for the stated preparation purpose.
3. Whether a gap is resolved.
4. Whether a pack is ready to approve.
5. Any tax, accounting, audit, legal or filing conclusion.

---

## 5. Value and success metrics

### Expected value

| Role | Value if the product works |
|---|---|
| Case owner | One current view of readiness and owners instead of chasing across tools |
| Contributor | Clear, bounded requests instead of vague reminders |
| Reviewer | Pack index and visible review state instead of reconstructing history |
| CFO / partner | Early visibility of blockers and explicit accountability |

### P0 success criteria

For fictional or consented pilot data, a non-developer can complete the P0 flow in the Imperal panel without engineering intervention and can answer the four readiness questions in under two minutes.

### Candidate pilot measures — validate in discovery

- time from request to review-ready pack;
- number of follow-up chases per case;
- percentage of open items with a named owner;
- percentage of packs with named approval;
- number of late-discovered missing requirements;
- willingness of a firm to run a 30-day pilot.

### Failure signals

- users do not recognise the workflow as a real recurring pain;
- users cannot understand next actions without a walkthrough;
- teams need a different first template/use case;
- the panel cannot complete the core journey reliably.

---

## 6. Scope, non-scope and safety boundary

### P0 includes

- human-owned cases;
- editable human-defined checklist;
- evidence metadata and HTTPS references;
- human review status and named approvers;
- human-owned tasks;
- fail-closed evidence-pack index;
- named pack approval with note;
- a panel entry point for the core flow.

### Explicitly excluded from P0

- tax-law interpretation or calculation;
- tax opinions, audit opinions or legal-sufficiency claims;
- filing, signing or submission;
- automatic approval;
- document downloading, OCR, source-content analysis or blanket Drive scanning;
- email intake/outbound correspondence workflow;
- external task-tracker dependency;
- client/auditor export or sharing;
- broad dashboarding unrelated to evidence readiness.

### Product language rule

The app may say **“missing”, “awaiting review”, “approved for pack”** or **“blocked by incomplete requirement.”** It must not say **“tax compliant”, “legally sufficient”, “correct tax treatment”** or equivalent professional conclusions.

---

## 7. Data, privacy and integration map

### Minimum P0 data

- case name, organisation/client name, period, stated request type and owner;
- checklist item title/status/reviewer/approval note;
- evidence title, HTTPS reference, optional period/reference metadata, source owner and review state;
- task title, owner, due/status data;
- pack metadata and named approval record.

### Data handling decisions

- P0 stores metadata and links; it does not copy or inspect document contents.
- Demo uses fictional **DemoCo SRL** data and safe public/test URLs only.
- Customer documents, identifiers, bank data and actual tax requests do not enter rehearsals without an explicitly designed and approved future data policy.

### Integration map

| Integration | Intended use | P0 need | Status on 7 Aug 2026 | Decision |
|---|---|---:|---|---|
| Imperal panel | Primary user workflow | Required | Live unverified for Evidence Hub | Deployment/install gate |
| Webbee | Natural-language coordination | Helpful, not required for core completion | Live behaviour for this flow unverified | Panel fallback always required |
| Google Drive | Select authorised source documents | Not required | Blocked: reconnect required; context disabled | Exclude from core demo/P0 |
| Mail | Link incoming requests / draft follow-up | Not required | Not verified for this workflow | Future controlled slice |
| Asana or Trello | Optional task handoff | Not required | Not selected or rehearsed | Future optional integration |

### Privacy and retention open decisions

Before controlled document intake or export, define retention, deletion, permitted storage locations, access revocation, recipient scope, provider policy and incident handling. These are prerequisites, not polish.

---

## 8. P0 definition and acceptance criteria

### P0 promise

A user can prepare a complete, reviewable evidence-pack index for a fictional audit PBC case without the system making any tax/audit decision.

### P0 acceptance test

1. Evidence Hub is deployed and installed in Imperal panel.
2. User creates `FY2026 audit PBC — DemoCo`.
3. User adds at least three requirements.
4. User registers safe HTTPS evidence references.
5. Incomplete requirements visibly block pack construction.
6. Named human reviews/approves the required items.
7. User creates and closes one collection task.
8. User builds the pack index.
9. Named human approves the pack with a note.
10. The resulting case visibly shows status, blockers/ready state and traceable approval.

### P0 non-negotiables

- no confidential production data;
- no silent bypass of missing checklist items;
- no anonymous approval;
- no claim of professional conclusion;
- no dependency on Drive, Mail or external task tracker.

### Current status

**Implemented locally; live unverified.** The next work is deploy/install and manual P0 verification, not new features.

---

## 9. Imperal panel UX map

### Required user-facing states

| State | What the panel must communicate | Next action |
|---|---|---|
| Empty | No cases exist; explain purpose and safety boundary | Create a case |
| Case created / collecting | Case owner, period, requirements and open gaps | Add requirement/evidence or create task |
| Awaiting review | Evidence registered but not approved | Reviewer checks it |
| Blocked | Requirement missing or unapproved; pack cannot be built | Resolve named blocker |
| Ready for pack | All stated requirements and eligible evidence are ready | Build reviewable pack index |
| Awaiting final approval | Pack built but no named approval | Responsible human approves or returns it |
| Approved | Pack approved with attributable name/note | Read-only review or controlled future handoff |

### Known P0 UI facts and gap

The local panel is known to include a create-case form and case list. Case-detail workflow, action wiring, status visibility and approval trace must be manually verified in the live panel. If this is missing or unclear, **case-detail workspace is the first corrective slice**; it is not optional cosmetic work.

---

## 10. Safety, approvals and audit trail

### Authority model

| Action | Webbee/system may do | Human required |
|---|---|---|
| Organise case and status | Yes | No professional conclusion implied |
| Surface missing/awaiting-review state | Yes | Human resolves significance |
| Suggest or create operational task | Yes, within authorised workflow | Owner remains accountable |
| Mark evidence approved for pack | No autonomous approval | Named reviewer/approver |
| Approve pack | No | Named accountable human and note |
| Tax/accounting/audit conclusion | No | Qualified responsible professional |
| Send/share externally | No autonomous action | Explicit future human confirmation |

### Audit trail requirements

For each future audit event, record at minimum: timestamp, event type, actor, object/case, prior/new state where relevant and short human note. Events must be tenant-isolated and should not be editable as ordinary case content.

**Known gap:** a visible chronological audit-trail screen is conditional P0.2 work if Gate B reveals existing records are not sufficient or legible.

---

## 11. Discovery and validation plan

### Before P1 expansion

Conduct 8–12 short interviews with the target audience. Ask:

1. Which workflow causes the most document chasing: audit PBC, month-end close, VAT support or authority inquiry?
2. Where do documents arrive now?
3. How do teams decide a package is complete?
4. Which items must appear in a trace/audit record?
5. Who is allowed to approve readiness?
6. What must never be accessible to an AI assistant?
7. What current tools must remain in place?
8. What would make a 30-day pilot worthwhile?

### Evidence standard

Collect concrete examples and language, with consent and without retaining confidential documents unnecessarily. A sales conversation does not count as discovery unless it produces answers to the above decisions.

### Live validation sequence

1. Deploy/install the app.
2. Run the fictional P0 case in panel.
3. Capture screenshots/recording and exact failures.
4. Ask one non-developer to repeat the flow.
5. Correct only observed flow blockers.
6. Rehearse the TAXCON script.
7. At TAXCON, collect interview evidence before choosing P1 template.

---

## 12. Implementation plan and delivery statuses

### Mandatory first delivery gate

| Slice | Why | Visible result | Status |
|---|---|---|---|
| Deploy/install + P0 manual verification | Local code is not a customer product | Evidence Hub opens in panel and DemoCo journey completes | **Next required work** |

### Conditional correction slices after live proof

| Slice | Trigger | Visible result | Status |
|---|---|---|---|
| Case-detail workspace | User cannot complete/understand actions after opening a case | One case shows checklist, evidence, tasks, blockers and next action | Conditional |
| Visible audit trail | Reviewer cannot answer who changed what/when | Read-only chronology visible per case | Conditional |

### Later roadmap — do not start before P0 is live verified

| Priority | Slice | Entry condition |
|---|---|---|
| P1 | One human-editable workflow template | 8–12 interviews choose one workflow by frequency/pain/pilot demand |
| P1 | Roles and server-enforced approvals | Pilot team role map exists |
| P1 | Controlled pack handoff/export | Retention, recipient scope and human confirmation rules agreed |
| P2 | Controlled document intake | Privacy, permissions, source access and retention policy defined; no automatic content use |
| P2 | Human-review discrepancy flags | Source policy and reviewer workflow defined |
| P3 | Correspondence workflow | Explicit draft/review/send authority model agreed |
| P3 | Optional external task integrations | Core tasks are live verified and a customer needs a specific integration |

### Delivery status rule

Only **`live verified`** means the feature may be described as available to customers or shown as live on stage. See the full delivery-status definitions in the master standard.

---

## 13. Decision log

| Date | Decision | Why |
|---|---|---|
| 7 Aug 2026 | Start with evidence readiness, not tax advice | Clear operational pain; lower-risk human-led boundary |
| 7 Aug 2026 | Use Audit PBC demo framing | Familiar workflow across auditors, accounting firms and CFOs; still needs discovery validation as first production template |
| 7 Aug 2026 | Exclude Google Drive from core demo | Connector requires reconnect and context access is disabled |
| 7 Aug 2026 | Treat deploy/install/live proof as the next work | Local implementation is not visible product delivery |
| 7 Aug 2026 | Require `PREPARATION.md` for every new app | Prevents coding before a clear problem, scope, UX, data and proof plan exist |

---

## 14. Preparation-completeness matrix and transition gate

### Stage 1 status — preparation

| Preparation area | Status on 7 Aug 2026 | Evidence / decision | What closes it |
|---|---|---|---|
| Product passport and business purpose | Ready | Sections 1–2; TAXCON’26 creates a focused validation opportunity | Keep current if event/pilot scope changes |
| Problem statement and current alternatives | Ready as a hypothesis | Section 2; grounded in the documented operating pattern, not yet interview-confirmed | Confirm or revise through discovery |
| Audience, roles and access principles | Ready for P0; role model incomplete for P1 | Section 3; multi-person server-enforced permissions remain P1 | Validate real team roles in interviews/pilot |
| Primary user journey and human decision points | Ready for P0 | Section 4; Audit PBC is the demo framing | Confirm that Audit PBC is the first real template, or replace it |
| Value, metrics and failure signals | Ready as a measurement plan | Section 5 | Set baseline/target with a consented pilot |
| Scope, non-scope and safety boundary | Ready and binding | Section 6 and 10 | Any change requires an explicit recorded product decision |
| Minimum data, privacy and integration map | Ready for P0 | Section 7; metadata/links only and no document reading | Approve retention/access design before intake or export |
| P0 definition and acceptance criteria | Ready | Section 8; fictional DemoCo manual flow | Pass the live panel test |
| Panel UX map | Designed; live unverified | Section 9; only create/list is known locally | Verify all action/detail states in Imperal panel |
| Approval/audit-trail model | Ready for P0 boundary; P1 details open | Section 10 | Validate required events and authority model with pilot users |
| Discovery plan | Ready to execute | Section 11; 8–12 interviews and decision questions defined | Record interviews and make a template decision |
| Delivery roadmap and statuses | Ready | Section 12; P0–P3 plus status rules | Update after each verified delivery event |

### Gate from preparation to embodiment

The application may move from **Stage 1: preparation** to **Stage 2: embodiment** only when the following are true:

- this `PREPARATION.md` has every required section marked `Ready`, `Ready as a hypothesis`, or an explicit `Blocked` decision;
- the P0 scenario, safety boundary, data minimum, user-visible panel flow and success test are written and internally coherent;
- unknowns are labelled as hypotheses rather than converted into invented facts;
- implementation work is limited to the documented P0 until a change decision is recorded;
- for expansion beyond P0, discovery evidence selects the next workflow/template.

### Current gate decision

**P0 embodiment is authorised only to prove the already-defined fictional DemoCo flow in the Imperal panel.**

**P1 embodiment is not authorised yet.** It remains blocked on 8–12 discovery interviews and a documented decision selecting the first real workflow template. The likely candidate is Audit PBC, but it is a hypothesis—not a completed customer finding.

---

## 15. Live verification log

| Date | Environment | Flow tested | Result | Evidence / blocker | Next action |
|---|---|---|---|---|---|
| 7 Aug 2026 | Local workspace | P0 build, validation and tests | Passed | `imperal build .` succeeded; `imperal validate .` reported no issues; `../.venv/bin/python -m pytest -q` reported 4 passed after the read-action regression test was added | Register app, then deploy |
| 7 Aug 2026 | Imperal Developer Catalog | First deploy attempt | Blocked before deployment | Deployment returned `App not found`: the app had not yet been registered in the developer catalog. | Create/publish a source repository and register the app, then retry deploy |
| 7 Aug 2026 | GitHub + Imperal Developer Catalog | Repository and app registration | Complete | GitHub repository created and pushed at `ivanco-bluebeeweb-com/imperal-ext-tax-audit-evidence-hub`; Developer Catalog registration for `tax-audit-evidence-hub` succeeded. | Retry deploy |
| 7 Aug 2026 | Imperal deployment service | Deploy from registered GitHub repository | Blocked before clone | Git clone failed because GitHub requested a username for the then-private HTTPS repository. | Publish repository after a secret review, then retry deploy |
| 7 Aug 2026 | GitHub | Source visibility | Complete | Tracked files were scanned for common credential patterns; no matches found. Repository visibility changed to public and verified. | Retry deploy |
| 7 Aug 2026 | Imperal deployment service | Deploy from public GitHub repository | Passed | Deployment completed at commit `6d6ffe45`; validation `20/20`; manifest, panel, icon and one catalog tool synced. | Install when Marketplace review is approved |
| 7 Aug 2026 | Imperal Marketplace | Submit application for review | Pending review | All submission checks passed: HTTPS Git URL, display name, description and successful deployment. Marketplace does not yet list the app for installation. | Wait for Marketplace approval, then install |
| 7 Aug 2026 | Imperal Marketplace | Recheck availability after deployed-action proof | Still pending review | Marketplace search has no exact match for the Evidence Hub; the app remains unavailable for installation. | Wait for Marketplace approval, then install |
| 7 Aug 2026 | Deployed Evidence Hub actions | Full fictional DemoCo P0 journey through actions | Passed — API proof | Created case, checklist item, fictional HTTPS reference and task; incomplete pack and anonymous approvals failed closed; named reviewer approved evidence and checklist; read-only one-item pack was built; named human approval was recorded. No document was read and no tax/audit conclusion was made. | Install and repeat the intended flow visibly in Imperal panel |
| 7 Aug 2026 | Owner Chrome + Imperal panel | Full fictional DemoCo P0 journey through UI | Passed — UI proof | In Chrome, created the DemoCo checklist requirement, registered one fictional HTTPS evidence link, created and completed a task, recorded named fictional human reviews, built the read-only index and recorded a named fictional pack approval. The selected case reached `approved`; RU/RO/EN switcher also changed visible UI copy. The incomplete checklist was first sent to pack build and did not produce a pack; it became buildable only after named approvals. No document was opened/read and no tax/audit conclusion was made. | Run non-developer usability dry run, then discovery interviews before P1 |
