# Tax & Audit Evidence Readiness Hub

A human-led operating layer for preparing tax, finance and audit evidence.

It turns a scattered preparation process into a reviewable case:

`case → checklist → evidence register → human review → tasks → evidence-pack index → human approval`

## What it solves

For accounting firms, audit teams, tax consultants, CFOs and finance operations:

- keep one named owner and period for a preparation case;
- make required documents and controls explicit;
- register links to existing evidence without copying or silently reading it;
- route gaps and follow-up work into human-owned tasks;
- distinguish received evidence from evidence explicitly approved for a pack;
- create an immutable-in-practice pack index for review;
- require a named human to approve the readiness of that pack.

## Safety boundary — deliberately non-negotiable

This extension **does not**:

- interpret tax law;
- calculate tax liability or make tax decisions;
- issue tax advice or a tax opinion;
- validate whether a document is legally sufficient;
- perform audit procedures or replace professional judgement;
- sign or submit a filing;
- fetch, download, OCR or otherwise inspect linked documents.

A human defines the checklist, reviews the evidence, resolves discrepancies,
and approves the evidence pack for its stated preparation purpose.

## P0 workflow

1. `create_case`
2. `add_checklist_item` for each required document/control
3. `register_evidence` with an existing **HTTPS** storage/document URL
4. `review_evidence` → `approved_for_pack` requires `approved_by`
5. `update_checklist_item` → `approved_for_pack` requires `approved_by`
6. `create_task` / `update_task` for collection and review work
7. `build_evidence_pack`
8. `approve_evidence_pack` with named human and approval note

`build_evidence_pack` fails closed when either:
- no human-approved evidence is available; or
- any checklist item remains incomplete.

## Current P0 tools

| Area | Tools |
|---|---|
| Case | `create_case`, `list_cases` |
| Requirements | `add_checklist_item`, `update_checklist_item`, `list_checklist_items` |
| Evidence | `register_evidence`, `review_evidence`, `list_evidence` |
| Work coordination | `create_task`, `update_task`, `list_tasks` |
| Pack | `build_evidence_pack`, `approve_evidence_pack` |

## Evidence standard

An evidence record is metadata and a reference to an existing source:

- title;
- HTTPS URL;
- optional period and document/reference number, both requiring human review;
- source owner;
- review status, note and named approver.

No document content is analysed or relied on by the extension at P0.

## Test and validate

```bash
../.venv/bin/python -m pytest -q
../.venv/bin/imperal build .
../.venv/bin/imperal validate .
```

## Product preparation and delivery records

- [`PREPARATION.md`](PREPARATION.md) — required product preparation: problem, users, scope, data, UX, safety and validation plan.
- [`TAX_AUDIT_EVIDENCE_DEVELOPMENT_PLAN.md`](TAX_AUDIT_EVIDENCE_DEVELOPMENT_PLAN.md) — detailed delivery roadmap and truthful status.
- [`TAXCON26_DEMO_TOOLKIT.md`](TAXCON26_DEMO_TOOLKIT.md) — TAXCON-specific demo scope, gates and contingency.
- [`DISCOVERY_INTERVIEW_GUIDE.md`](DISCOVERY_INTERVIEW_GUIDE.md) — interview script and evidence-based decision rubric for the first reusable workflow template.

## Next product slices — only after user interviews

1. case templates by workflow (audit PBC, month-end close, tax authority query);
2. controlled document intake/storage with retention and access policy;
3. source-aware extraction and discrepancy flags, always routed to human review;
4. approval/audit chain and team roles;
5. handoff/export to a client, auditor or tax adviser.
