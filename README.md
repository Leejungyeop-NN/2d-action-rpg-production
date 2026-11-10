# 2D Action RPG Production

**A Korean-first agent skill and skills-only Codex plugin for sprite-based 2D action RPG and belt-scroll production.** It helps an agent plan and review dialogue, motion, skill effects, party/inventory interfaces, research, and handoff. It is not an all-genre game-making solution.

**Release status:** early public release, 0.1.0. GitHub/marketplace distribution and official directory approval are separate. This repository does not claim OpenAI endorsement or official directory approval.

## Fit and limits

|Fit|Scope|
|---|---|
|Best fit|Sprite-based 2D action RPGs / belt-scroll; Korean dialogue; party and inventory workflows; motion timing; weapon/element/hit FX; 2D scene staging|
|Adapt before use|2D metroidvania, top-down RPG and narrative games; apply only relevant modules|
|Outside validated scope|3D rigging/rendering, VR, network/multiplayer architecture, competitive balancing, engine-specific implementation, other-language prose quality|

The references are primarily **Korean**. The English overview is not a claim of multilingual editorial validation. There is no engine adapter, MCP server, executable hook, hosted service, paid asset or generation account in the plugin. An agent needs its own permitted tools to inspect a game, view video, research references or generate assets. Production quality and commercial results are not guaranteed.

See [scope](skills/game-production-handbook/references/scope.md), [validation](VALIDATION.md), and [한국어 안내](docs/README.ko.md).

## Install as a Codex plugin

Add this GitHub-backed marketplace:

```sh
codex plugin marketplace add Leejungyeop-NN/2d-action-rpg-production --ref v0.1.0
codex plugin add 2d-action-rpg-production@lee-game-production
```

Plugin commands and local marketplace surfaces vary by Codex version. Inspect `codex plugin --help` if a command is unavailable. Start a fresh session after installation. The plugin provides the `game-production-handbook` skill; invoke it by name or point your agent at its SKILL.md. Example:

> Use the game-production-handbook skill to review this belt-scroll party equipment workflow. Keep the changes limited to the stated task and report untested parts.

## Use as a standalone skill

Copy the entire `skills/game-production-handbook/` directory into a skills location supported by your agent, or supply [SKILL.md](skills/game-production-handbook/SKILL.md) as instructions. Referenced files must travel with it. This does not promise automatic compatibility with every agent host.

## What is included

One entrypoint routes to focused references for design/economy, Korean narrative/dialogue, image prompts, sprite motion, skill effects, game UI/UX, world/cinematics, research/handoff, and scope. Only relevant references should be read for a task. Small fixes should not trigger a full redesign.

The reusable guidance was adapted from production experience in a private project. **That project's title, canon, scripts, source code, assets, saves and local paths are not included or licensed here.** MIT applies to the files published in this repository, not to any external game IP.

## Validate and package

```sh
python3 tools/validate.py
python3 tools/package.py
```

These use the Python standard library and do not invoke models, download assets or run a game. Build ZIPs are written to ignored `dist/`. [Validation](VALIDATION.md) distinguishes structural checks, behavioral dry runs and tests that have not been performed.

## Official public directory

A marketplace install is not an official directory listing. The release ZIP can be submitted as a skills-only plugin using the [OpenAI submission process](https://developers.openai.com/plugins/deploy/submission). Publisher verification, automated scans and review apply. Current submission status is tracked in [SUBMISSION.md](SUBMISSION.md).

## License and contributions

[MIT](LICENSE), Jung Yeop Lee. Contributions should use generic fixtures and contain no confidential project data, credentials or unlicensed game assets. Report issues through this repository's issue tracker. See [privacy](PRIVACY.md) and [security](SECURITY.md).
