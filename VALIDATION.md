# Validation and limits

## Structural checks

Run `python3 tools/validate.py` to inspect manifest identity, metadata limits, icon shape, skill frontmatter, local references, marketplace paths and public package contents. Run `python3 tools/package.py` to create and re-read the submission ZIP with CRC and per-file SHA-256 checks. These checks do not run a game or a model.

## Initial behavioral evidence

A previous independent agent exercised four isolated, text-only requests: separating 12fps sprite playback from 60fps screen rendering; a narrow long-name equipment dropdown correction; first-meeting dialogue continuity; and excluding a non-game SaaS task. Relevant references were selected without loading the private project profile. The reviewed answers kept scope and did not assume pixel-art filtering was universally correct.

This is a small dry-run sample, not proof of all-genre suitability, visual quality, automatic skill routing, engine integration, multilingual prose or commercial outcomes. Further public-candidate evaluation and actual plugin installation are recorded only after they run.

## Public-candidate independent review (2026-11-11)

An independent agent read this candidate and answered three further text-only tasks: declining all-in-one 3D/VR/network production claims; specifying a sword/fire hit effect without changing gameplay; and reviewing first-meeting narrative continuity without inventing past relationships. Scope/claims were judged consistent. The reviewer found missing documents/tools in the first ZIP; packaging was corrected to include the audited public tree and validate the actual extracted archive. This review did not view video, run an engine or establish marketplace installation success.

## Actual local Codex install (2026-11-11)

The candidate was registered with `codex plugin marketplace add` and installed with `codex plugin add`. `codex plugin list` reported version 0.1.0 installed and enabled. All packaged skill files matched the installed cache byte-for-byte. This establishes local discovery/installation in the tested client, not official directory approval, fresh-session model routing, visual playback or engine integration.
