# TAXCON’26 Demo Toolkit — Imperal Cloud & Webbee

**Event:** TAXCON’26, AmCham Moldova — 24 September 2026  
**Audience:** accounting firms, auditors, tax consultants, CFOs, finance operations and internal tax teams  
**Purpose:** demonstrate one practical, human-led workflow for tax/audit evidence preparation.  
**Owner:** Vlad Ivanco  
**Last reviewed:** 7 August 2026

> This document is the source of truth for **what we will show**, what must be working in the Imperal panel, and what must remain off-stage until it is ready. It does not claim that a feature is delivered merely because local code exists.

---

## 1. The one promise we demonstrate

**Imperal Cloud with Webbee helps a tax, audit or finance team turn scattered preparation work into a controlled evidence-readiness workflow: case, requirements, evidence register, tasks, reviewable pack and traceable human approval.**

We do **not** demonstrate an AI that decides taxes, interprets tax law, signs or files returns, gives a tax opinion, or replaces an auditor's judgement.

### The audience problem in plain words

A team receives an audit PBC list or a request for explanation. Documents arrive in email, chats and folders. Nobody has one current list of what is required, what is missing, who owns the next action, or which version was approved.

### The outcome they should see

By the end of a 10-minute workflow, the audience can see:

1. one named owner and period for a case;
2. an explicit checklist of required material;
3. a controlled register of evidence references;
4. missing items turned into owned tasks;
5. a pack that cannot be marked ready while requirements are incomplete;
6. a named human approval and a traceable preparation record.

---

## 2. Product toolkit — exactly what is on stage

### A. Required, primary app: Tax & Audit Evidence Readiness Hub

**Role:** the main workspace and the only product that must carry the core live story.

| Capability | Audience value | What we demonstrate | Current code status | Required live proof |
|---|---|---|---|---|
| Case | One controlled folder for one request/audit period | Create `FY2026 audit PBC — DemoCo` with owner, period and purpose | Implemented | App opens in panel; form creates a case visibly |
| Checklist | Nobody guesses what should be collected | Add required documents/controls | Implemented | Checklist can be added and shown for the case |
| Evidence register | Sources are traceable without copying confidential files | Register safe HTTPS demo links plus period/reference metadata | Implemented | Evidence appears against the right case |
| Human review | AI does not silently certify evidence | Mark an item for human review/approval with a named reviewer | Implemented | Approval requires and shows the human name |
| Tasks | Gaps have an owner and deadline | Create task: request missing bank statement | Implemented | Task is visible and status can be updated |
| Evidence pack | Review gets a structured index rather than an inbox search | Build pack only after every required checklist item is approved | Implemented | Incomplete pack is blocked; complete pack builds visibly |
| Human pack approval | Responsibility stays explicit | Approve readiness with name and note | Implemented | Named approval is visible in the case/audit trail |
| Audit trail | Team can answer “who did what and when?” | Show relevant changes/approvals | Partial: core event records exist; dedicated timeline is not confirmed | A visible chronological audit trail or a documented, panel-visible substitute |

**Hard safety boundary:** this app stores references and human review decisions. P0 does not download, OCR, read, interpret or validate linked documents.

### B. Required experience layer: Webbee

**Role:** natural-language coordinator, not an extra dashboard.

**On-stage example:**

> “Create an audit PBC case for DemoCo for FY2026, show what is missing, and create a task for the owner to provide the bank statement.”

**What it proves:** the workflow can be initiated and navigated in ordinary language.

**Fallback:** presenter performs the same steps directly in the Evidence Readiness panel. The demo must remain complete even if chat routing is unavailable.

### C. Optional, only after explicit live verification: one task tracker

**Candidate:** Asana **or** Trello — choose one only.

**Role:** demonstrate that a gap can become a task in a tool the team already uses.

**Not a prerequisite for TAXCON:** Evidence Hub has its own task workflow. Do not make an external task tracker a dependency for the core demo.

**Go/no-go rule:** include it only if a real case task can be created and shown during a rehearsal. Otherwise mention it as a future integration, not as a live feature.

### D. Optional, only after explicit live verification: Mail

**Role:** show an incoming audit request connected to the case, or show a human-approved draft follow-up.

**Not a prerequisite for TAXCON:** correspondence is not in the Evidence Hub P0 workflow yet. Do not present it as a released workflow.

**Go/no-go rule:** no automatic sending, no tax conclusion, and no live dependency on mail delivery. A redacted static example is acceptable only when labelled as a concept/future slice.

### E. Optional, blocked until repaired: Google Drive Connector

**Intended role:** select already-authorised documents from a Drive folder instead of manually registering links.

**Current status:** **blocked.** The available Google Drive account requires reconnect and Drive context access is disabled. This is not safe to put into the primary demo.

**Core demo fallback:** use pre-created HTTPS demo document links and clearly describe P0 as a reference register.

**Entry condition for use on stage:** reconnect succeeds, the authorised account is identifiable, context permission is intentionally enabled, a restricted demo folder can be browsed, and the exact flow is rehearsed end-to-end.

---

## 3. Explicitly out of scope for the TAXCON stage

Do not show these products merely because they are installed:

- Brand Strategy Hub / VBS;
- Content Strategy;
- Article Writer;
- Media Hub / image generation;
- WordPress Hub;
- SEO Audit, Google Search Console or Google Analytics;
- DataForSEO;
- any face/likeness or personal-data-oriented workflow.

They do not prove the tax/audit evidence-preparation story and would make the demo look like a catalogue rather than a solution.

---

## 4. The 10-minute live demo script

### Safe demo data

Use a fictional company only: **DemoCo SRL**. Use invented documents, dates, references, names and public/safe URLs. No customer data, tax identifiers, bank details, actual audit requests or live confidential Drive folders.

### Flow

| Time | Presenter action | What the audience learns | Control to state aloud |
|---:|---|---|---|
| 0:00–0:45 | State the problem: fragmented PBC/request preparation | This is an operations problem, not a “replace the accountant” pitch | “Professional judgement remains with your team.” |
| 0:45–1:30 | Create evidence-readiness case | Every request has a named owner, period and stated purpose | “A case is preparation coordination, not a tax opinion.” |
| 1:30–2:45 | Add checklist requirements | Completeness is explicit | “The human defines what is required.” |
| 2:45–4:00 | Register two received evidence references | Sources can be organised without copying documents | “P0 registers references; it does not read documents.” |
| 4:00–5:00 | Show one required item missing | Gaps are visible before review day | “The system flags missing preparation material; it does not decide legal sufficiency.” |
| 5:00–6:00 | Create/assign follow-up task | Work becomes owned and actionable | “A person owns the request and confirms completion.” |
| 6:00–7:30 | Demonstrate blocked evidence-pack attempt | The system fails closed when requirements remain incomplete | “You cannot label an incomplete pack as ready.” |
| 7:30–8:45 | Complete the fictional checklist and build the index | Review receives a structured pack index | “This is an index for review, not a filing.” |
| 8:45–9:30 | Named human approves readiness with note | Accountability is explicit and traceable | “Approval belongs to the responsible professional.” |
| 9:30–10:00 | Close with call to action | Invite discovery, not a vague AI conversation | “Tell us which workflow causes the most chasing in your team.” |

---

## 5. Demo readiness matrix

A feature has three different statuses. They must never be conflated.

| Status | Meaning | May be said on stage? |
|---|---|---|
| **Implemented locally** | Code and tests exist in the workspace | No — not yet |
| **Built/validated** | Local package validation passed | No — not yet |
| **Live verified** | Deployed, visible in Imperal panel and rehearsed in the exact flow | Yes |

### Current known state — 7 August 2026

| Item | Status | Evidence / next proof |
|---|---|---|
| Evidence Hub P0 code | Implemented locally | README, manifest, handlers and panel exist in `tax-audit-evidence-hub/` |
| Evidence Hub build/validation | Passed locally | `imperal build .`, `imperal validate .` and 3 local tests passed on 7 Aug 2026 |
| Evidence Hub deployment | Passed | Deployed from the public GitHub repository at commit `6d6ffe45`; platform validation passed `20/20`. |
| Evidence Hub installation in user panel | **Pending Marketplace review** | App submission checks passed, but Marketplace does not yet list it for installation. |
| Evidence Hub demo flow in live panel | **Not verified** | Marketplace approval → install → create a fictional case → rehearse steps 1–9 |
| Google Drive intake | **Blocked** | Account needs reconnect; context permission disabled |
| Google Analytics | Not relevant to TAXCON core demo | Exclude |
| Google Search Console | Working but not relevant | Exclude |
| AmCham participation format | Not confirmed | Send outreach and obtain response |

---

## 6. Go/no-go gates

### Gate 1 — product can be shown

All must be true:

- Evidence Hub is deployed and installed in the Imperal panel;
- app opens for the owner account;
- the fictional case flow works visibly from creation to human pack approval;
- an incomplete checklist demonstrably blocks pack creation;
- safety copy is visible or stated in the demo;
- no confidential/live customer data is used.

### Gate 2 — session can rely on live internet

All Gate 1 conditions, plus:

- venue connectivity is tested or an independent connection is available;
- presenter has an authenticated session ready;
- no demo step depends on Google Drive, Mail or a third-party task tracker unless that step has been rehearsed successfully.

### Gate 3 — contingency is ready

- static screenshot deck or screen recording of the exact approved workflow;
- PDF of the 6 slides;
- one-page Evidence Pack Readiness Checklist;
- backup script that does not claim unverified integration features.

If Gate 1 is not met, do not offer a “live product demo.” Present a labelled product concept/case walkthrough only, or choose a showcase format instead.

---

## 7. Discovery questions for leads

Collect answers, with explicit consent, from 8–12 relevant participants:

1. Which workflow causes the most document chasing: audit PBC, month-end close, VAT support, or tax-authority inquiries?
2. Where do documents arrive today?
3. How do you know a package is complete before review?
4. What information must be visible in an audit trail?
5. Which tasks must stay in your current tracker?
6. What must never be accessed or processed by an AI assistant?
7. Who gives the final human approval?
8. What would make this worth piloting in the next 30 days?

These answers decide the first production template. They are not a sales survey pretending to be product research.

---

## 8. Immediate owner checklist

1. Send AmCham outreach and confirm participation format.
2. Deploy and install the Evidence Hub; record deployment/version/link.
3. Run the Gate 1 manual panel test; record pass/fail and screenshots.
4. Create fictional DemoCo data only.
5. Prepare the 10-minute script and static contingency.
6. Choose whether to include **zero** optional integrations (recommended) or one verified task tracker.
7. Run internal rehearsal before committing to a live demo.

---

## Related records

- Event/positioning/outreach: [`../taxcon26-imperal-webbee-go-to-market.md`](../taxcon26-imperal-webbee-go-to-market.md)
- Product preparation and P0/P1 gate: [`PREPARATION.md`](PREPARATION.md)
- Discovery interviews and template-selection rubric: [`DISCOVERY_INTERVIEW_GUIDE.md`](DISCOVERY_INTERVIEW_GUIDE.md)
- Product delivery roadmap: [`TAX_AUDIT_EVIDENCE_DEVELOPMENT_PLAN.md`](TAX_AUDIT_EVIDENCE_DEVELOPMENT_PLAN.md)
- Current P0 usage and safety boundary: [`README.md`](README.md)
