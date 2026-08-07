"""Extension declaration for Tax & Audit Evidence Readiness Hub."""
from imperal_sdk import Extension, ChatExtension

ext = Extension(
    "tax-audit-evidence-hub",
    version="0.1.0",
    display_name="Tax & Audit Evidence Readiness Hub",
    description=(
        "Human-led evidence readiness for tax and audit preparation: cases, "
        "checklists, evidence, tasks, pack indexes and approvals. Never makes "
        "tax decisions or files returns."
    ),
    icon="icon.svg",
    actions_explicit=True,
    capabilities=["tax_audit_evidence:read", "tax_audit_evidence:write"],
)

chat = ChatExtension(
    ext,
    tool_name="tax-audit-evidence-hub",
    description=(
        "Coordinates human-led tax and audit evidence preparation; never "
        "provides tax advice or makes tax decisions."
    ),
)
