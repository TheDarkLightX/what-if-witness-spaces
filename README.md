# What-If Witness Spaces

Artifact-backed preprint and replication bundle for:

**What-If Witness Spaces: A Neuro-Symbolic Disaster Loop for Fail-Closed Software Hardening**

Author: Dana Edwards, Independent Researcher
ORCID: <https://orcid.org/0009-0001-1177-4752>

## Status

This repository is the focused publication bundle for the paper.

DOI: 10.5281/zenodo.19763921

Publication posture: this paper introduces a bounded, artifact-backed assurance
technique. It does not claim global safety. It reports a replayable case study
over the MPRD artifact set. The ZenoDEX section is an illustrative extension
unless a full ZenoDEX archive is provided. The result is checker-relative and
witness-language-relative.

Read the current preprint:

- [paper/NEURO_SYMBOLIC_DISASTER_LOOP.pdf](paper/NEURO_SYMBOLIC_DISASTER_LOOP.pdf)
- [paper/NEURO_SYMBOLIC_DISASTER_LOOP.md](paper/NEURO_SYMBOLIC_DISASTER_LOOP.md)

## Artifact Check

Verify the archived MPRD case-study receipt:

```bash
python3 scripts/verify_receipt.py
```

Expected result:

```json
{
  "ok": true
}
```

The receipt verifies:

- stable receipt hash:
  `sha256:b83ee1178c4bea460b9c7e3c67d5ccf1d7ac330e017746236fcfc7274c459561`
- materialized hypotheses: `16003`
- reachable disaster witnesses: `0`
- gate: `OPEN_FOR_BOUNDED_RESEARCH`

## Paper Files

The publication-ready PDF and Markdown source are included directly in
`paper/`. The generated TeX build file is intentionally not part of the public
archive.

## Scope

This repository contains the publishable paper bundle and a compact archived
receipt check. The larger MPRD codebase contains the original case-study checker
and hardening work:

- <https://github.com/TheDarkLightX/MPRD>

The ZenoDEX discussion in the paper is an illustrative second application unless
a separate ZenoDEX archive is provided:

- <https://github.com/TheDarkLightX/ZenoDEX>

## License

Paper, figures, written documentation, and narrative text are licensed under
CC BY 4.0. See [LICENSE-paper.md](LICENSE-paper.md).

Code, scripts, and machine-readable artifact checkers are licensed under
Apache-2.0. See [LICENSE](LICENSE).
