---
name: opencode-install
description: Install Ventura Pro agent and rule files into a target OpenCode project using the repository layout and configuration contract. Use when a user wants Ventura Pro activated in another project. Do not use when editing Ventura Pro rules themselves or when the target does not use OpenCode.
---

# OpenCode install

- Confirm the target project uses OpenCode before copying files.
- Copy `.opencode/agent/ventura-pro.md` into the target `.opencode/agent/` directory.
- Copy only the required files from `.opencode/rules/` or the complete supported rule set when requested.
- Preserve existing target rules and inspect name collisions before overwriting anything.
- Set `default_agent` to `ventura-pro` only when the user wants it as the default.
- Validate the target configuration syntax and confirm OpenCode can discover the agent.
