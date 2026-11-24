# Notes — Pickup Lines for Machines (v1)

- Bounty: Pickup Lines for Machines (`u-gentle-badger-68-pickup-lines-for-machines-131631a1`), $5 prize, top 3 ($2/$2/$1), free entry.
- Entries close 24 Nov 2026 12:50 WIB (05:50 UTC). Blind rounds: R1 07:29 WIB, R2 10:09 WIB, final 12:50 WIB.
- Entry line: `You make my gradients descend.` — 30 characters.
- Program: `main.py` (pure stdlib), writes the line to `/output/entry.txt`, chmod 0644.
- Status: built, tested, pushed to GitHub. NOT submitted — awaiting Joni's 'Setuju'.
- Live score/rank: blind rounds — no live score until a round publishes; check GET /api/competitions/<slug>/rounds after R1 (07:29 WIB).

## Update 24 Nov ~10:25 WIB — resumed on Joni's "Lanjutkan semua"
- Kit init run fresh: anchor f58f5e0 (drand round 34228951, freshness.json alone) + LICENSE 5e61599 (SPDX MIT present).
- NOTE: kit copy is level 39, make.fun is at level 40 — re-download a fresh kit from https://make.fun/c/<slug>/kit before bundle/check/submit.
- Genuine revision (thinking_revised): single-line validation in main.py + test_single_line → tests 5/5.
- Entry commit 0886120b41b38729e5fb1fafe88b7f2f0ad258a4, pushed, ls-remote verified. About set (homepage + makefun/ai-agents/bounties, verified via API).
- Ready for Joni's 'Setuju'. NOT submitted.

## Submitted — 24 Nov 2026 ~11:08 WIB (on Joni's "Setuju 1 dan 2")
- Bundle: ~/workspace/tools/makefun/bundles/u-gentle-badger-68-pickup-lines-for-machines-131631a1.tar.gz, sha256 53511428ea3172e848ce793c2fc1349bd27b68d15ba194e81dd530f1fd6b1433 (257,909 B). Fresh level-40 kit (…-kit-fresh/). Sessions: v1 builder 4c8d4f8b + Batch B coordinator c00bfd80; usage ~/.makefun/muse-usage-pickup-lines.jsonl (2 rows).
- Kit check on 0886120b41b38729e5fb1fafe88b7f2f0ad258a4: ok=true, failed=[] (thinking_own_work 130/130; thinking_fresh skip-note only — v1 session never shows the anchor line, not a rejection).
- Submission: 01a20bba-7625-7408-bb46-f67b0537e00d, status submitting. Blind, 3 rounds — counts from round 3 of 3 (final), cutoff 24 Nov 12:50 WIB (close). Claim code ONLY in ~/.config/makefun/u-gentle-badger-68-pickup-lines-for-machines-131631a1-submission.json (0600).
- Repo branding verified before submit: About homepage = bounty page, topics ai-agents/bounties/makefun; README shows the 3 live make.fun badges.
