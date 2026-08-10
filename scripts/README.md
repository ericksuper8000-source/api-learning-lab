# Scripts

## Purpose

This folder holds every script created during the stages: `requests` client scripts,
SQL setup scripts, quality-tool invocations, and any small automation produced while
learning to build and test the API.

## Conventions

- One folder per stage when a stage produces several scripts: `stage-01/`, `stage-03/`, …
- Every script is **reproducible**: it documents what it does and why it exists
  (the "why" in a short header or in the stage report).
- Scripts never contain secrets. Database credentials live in environment variables,
  `.env` files (never committed), or CI variables.
- A script is committed with the stage that created it, as part of the same meaningful
  commit.

> Scripts are written **after** the manual process is understood (see "Understand before
> automating" in `docs/project-specification.md`).
