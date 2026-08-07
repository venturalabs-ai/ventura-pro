---
name: target-project-validation
description: Validate a Ventura Pro installation against the target project's actual stack commands tests and constraints. Use after installing or materially changing Ventura Pro in another repository. Do not use when no target OpenCode project is available for validation.
---

# Target project validation

- Inspect the target repository stack test commands CI and architecture before evaluating the agent.
- Confirm OpenCode discovers `ventura-pro` and the intended rule files.
- Run one representative task from each rule domain actually enabled in the target.
- Verify generated changes follow target tests formatting and repository instructions.
- Record conflicts between Ventura Pro guidance and target-local conventions.
- Prefer target-local constraints when they are explicit and valid.
- Do not declare the installation validated until the target project's normal checks pass.
