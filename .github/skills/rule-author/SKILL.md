---
name: rule-author
description: Add or revise Ventura Pro OpenCode engineering rules so they encode repository-specific decisions rather than generic coding advice. Use when a recurring engineering workflow needs a new or updated rule. Do not use when existing rules already cover the task or when only installing Ventura Pro.
---

# Rule author

- Inspect `.opencode/rules/` and the main agent prompt before editing.
- Define the concrete recurring failure or decision the rule should prevent.
- Put the rule in the narrowest existing domain file when possible.
- Keep instructions imperative and operational.
- Remove advice an engineering model already knows without Ventura-specific context.
- Avoid overlap with existing rules and merge competing guidance.
- Add examples only when they clarify a repository convention or decision boundary.
