---
name: agent-contract-review
description: Review the Ventura Pro agent prompt for conflicting autonomy safety tool and engineering instructions. Use when changing `.opencode/agent/ventura-pro.md` or adding a rule that affects agent behavior. Do not use when only applying the agent to a target coding task.
---

# Agent contract review

- Read the full agent prompt and all rule files affected by the change.
- Check mission domain autonomy tool assumptions and escalation behavior for conflicts.
- Keep security and human-approval boundaries stronger than convenience instructions.
- Remove duplicated guidance that can produce competing priorities.
- Ensure rule references point to files that exist in `.opencode/rules/`.
- Keep vendor or technology expertise claims as guidance rather than certification.
- Summarize any intentional behavior change before finishing.
