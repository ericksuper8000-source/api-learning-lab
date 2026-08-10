# ADR-0005 — English Public Documentation

**Status:** Accepted
**Date:** 2026-08-04
**Context:** Phase 0 — Planning (documentation strategy)

---

## Decision

All **public** project documentation (README, AGENTS.md, `docs/`) is written in **English**.
Internal planning notes and the daily-session instructions remain in **Spanish**.

## Context & Problem

The repository is a professional portfolio aimed at DevOps/Backend Junior positions. The
technical industry works in English: job posts, documentation, error messages, and
interviews frequently require it. Public docs in English maximize the reach and
credibility of the portfolio.

## Alternatives Considered

- **Spanish public docs** — more comfortable for daily use, but limits the portfolio's
  audience and looks less standard in an international context.
- **English public docs (chosen)** — professional standard; Spanish remains for internal
  planning (e.g., `INSTRUCCIONES SESION DIARIA - IA.txt`).
- **Bilingual everything** — rejected: doubles maintenance for little added value.

## Why This Option

The *evidence* (README, ADRs, stage reports) is what an interviewer reads, so it must be
in the language of the industry. The *workflow* (session instructions for the AI) is what
the student reads every day, so it stays in the most comfortable language. The mentor may
explain in Spanish during sessions.

## Consequences

- README and `docs/` are written in English.
- `INSTRUCCIONES SESION DIARIA - IA.txt` and the original planning drafts stay in Spanish.
- Session-log entries are written in English (they are public evidence), but the mentor
  may explain in Spanish during the session.

## If It Disappeared

The portfolio would lose international reach and the "industry standard" impression an
interviewer expects from a backend/DevOps candidate.
