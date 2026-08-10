# My AI Engineering Path
<!-- Managed by the ai-engineering-from-scratch learning skills.
     Repo: https://github.com/rohitg00/ai-engineering-from-scratch -->

## Mission
Career change — moving into AI/ML as a new career direction. By the end of the course, the goal is to be able to build a RAG (Retrieval-Augmented Generation) product.

## Placement
- Date: 2026-07-26
- Score: 6/10 (Math & Stats 2/2, Classical ML 2/2, Deep Learning 0/2, NLP & Transformers 2/2, Applied AI 0/2) — recommended entry Phase 7, but the learner chose to start at Phase 0 instead
- Entry point: Phase 0 — Setup & Tooling
- Pace: ~2 hours/week

## Path
| Phase | Name | Status | Est. hours |
|-------|------|--------|------------|
| 0 | Setup & Tooling | Done | 14 |
| 1 | Math Foundations | Do | 23 |
| 2 | ML Fundamentals | Do | 21 |
| 3 | Deep Learning Core | Do | 15 |
| 4 | Computer Vision | Do | 27 |
| 5 | NLP — Foundations to Advanced | Do | 30 |
| 6 | Speech & Audio | Do | 18 |
| 7 | Transformers Deep Dive | Do | 14 |
| 8 | Generative AI | Do | 14 |
| 9 | Reinforcement Learning | Do | 13 |
| 10 | LLMs from Scratch | Do | 26 |
| 11 | LLM Engineering | Do | 17 |
| 12 | Multimodal AI | Do | 65 |
| 13 | Tools & Protocols | Do | 24.5 |
| 14 | Agent Engineering | Do | 42 |
| 15 | Autonomous Systems | Do | 20 |
| 16 | Multi-Agent & Swarms | Do | 28 |
| 17 | Infrastructure & Production | Do | 32 |
| 18 | Ethics, Safety & Alignment | Do | 31 |
| 19 | Capstone Projects | Do | 620 |

## Progress log
| Date | Lesson | Quiz | Note |
|------|--------|------|------|
| 2026-07-27 | Phase 0, Lessons 01-06 (Dev Environment, Git & Collaboration, GPU Setup & Cloud, APIs & Keys, Jupyter Notebooks, Python Environments) | — | Completed before this file existed; imported from session memory. Next up: Lesson 07, Docker for AI. |
| 2026-08-03 | Phase 0, Lesson 07 (Docker for AI) | 1/3 | Had already built the Dockerfile/Dockerfile.runtime/app.py hands-on (committed 2026-07-31) before this session, including the runtime-vs-devel size comparison. Missed why volume mounts matter (thought they were about GPU sharing) and what the NVIDIA Container Toolkit does (thought it installs CUDA drivers in-container). Got the devel-vs-runtime image size reasoning and Compose networking-by-service-name right.
| 2026-08-04 | Phase 0, Lesson 08 (Editor Setup) | 3/3 | Already on VS Code via WSL. Hit two real install snags worked through live: a typo installing Ruff (charliemarsh vs charliermarsh), and Remote-SSH refusing to install inside WSL (UI extension vs workspace extension — needs to go in the Windows-side VS Code, not the WSL remote host). Configured Black as default formatter with Ruff wired in via codeActionsOnSave instead of competing as a formatter. Warm-up on volume mounts and Compose networking: 2/2, confirms volume-mounts item below is resolved.
| 2026-08-04 | Phase 0, Lesson 09 (Data Management) | 3/3 | Ran everything hands-on: load/cache IMDB, streamed Wikipedia (hit a stale dataset config in the lesson doc, 20220301.en → 20231101.en, plus a benign interpreter-shutdown crash after early break on a streaming loop), format conversion (Parquet smallest as predicted), nested 70/10/20 splits (got the counts right immediately), model snapshot download (878MB for a small model — snapshot_download grabs every format variant by default). Correctly reasoned through why a blanket `*.json` .gitignore rule would be risky given 338 tracked quiz.json files in this repo, then scoped .gitignore properly themselves.
| 2026-08-07 | Phase 0, Lesson 10 (Terminal & Shell) | 3/3 | Ran piping/redirects hands-on (fake training log, correctly reasoned through bash-only-does-integer-math and $NF as last-field). tmux: Ctrl+B conflicted with VS Code's own "toggle sidebar" shortcut, worked around by using a native Windows Terminal WSL tab instead — built the real 3-pane layout, detached, confirmed alive via `tmux ls`, reattached, killed cleanly. Aliases: hit a genuine oh-my-zsh git-plugin collision (its own `gpu` alias meant "git push upstream", shadowing the new one in an already-loaded shell) plus a typo in the nvidia-smi query fields (period vs comma) — both diagnosed and fixed live. SSH/remote-GPU steps deferred to Phase 3 by mutual agreement, no remote box available yet. Missed one warm-up question next session on 2>&1 redirects (thought file descriptor numbers meant run count).
| 2026-08-08 | Phase 0, Lesson 11 (Linux for AI) | 3/3 | Heavy overlap with Lesson 10 (tmux, grep, du/df) skipped/compressed by agreement; focused hands-on on new material. chmod +x on data_utils.py hit a second real gotcha beyond the lesson doc — no shebang line, so `./script.py` tried to run as a shell script and failed on `import`; resolved by running via `python3 script.py` instead, which is also just the normal way to run Python scripts in practice. Installed dos2unix via apt. Correctly predicted HF cache size (~1GB, actual 1.1GB) from memory of prior lessons' downloads.
| 2026-08-08 | Phase 0, Lesson 12 (Debugging & Profiling) | 3/3 | Found a real gap in the lesson's own debug_print helper live: has_nan=False can sit right next to mean=nan in the same line (inf + -inf = nan on aggregate, but no literal NaN element), fixed by adding an isinf check. First two attempts at an interactive pdb breakpoint() session died on an EOF/BdbQuit — terminal relay here appears to only capture one command's output as a unit, not true multi-turn stdin — worked around with VS Code's GUI debugger, then pdb worked cleanly on a third terminal attempt (p loss.item() -> nan, p loss*2 -> tensor(nan), c -> resumed). Ran the full debug_tools.py ship-it script on the real GPU; correctly computed 100M x 4 bytes = 400MB for the CUDA memory demo. torch 2.6.0+cu124 confirmed working with CUDA on the GTX 1650 via WSL passthrough. **Phase 0 complete.**
| 2026-08-09 | Phase 0 full review (all 12 lessons, `/check-understanding` unavailable — that skill isn't installed in this repo, only course-guide/learn/start-learning are, so ran a manual 12-question spot check instead, one per lesson) | 10/12 | Missed the four-layer environment stack ordering (Lesson 1: System Foundation must come before package managers/runtimes/AI libraries) and, for a second time, the NVIDIA Container Toolkit's actual role (Lesson 7). Everything else — git workflow, GPU benchmarking/synchronize(), API key headers, notebook execution-order pitfalls, CUDA/driver version mismatches, Remote SSH, DVC, SSH port forwarding, chmod, NaN debugging — solid on the first pass.

| 2026-08-10 | Phase 1, Lesson 01 (Linear Algebra Intuition) | 3/3 | First lesson of Phase 1, spanned two sessions (paused mid-lesson at matrix-vector multiplication, resumed at lunch). Found and fixed two real bugs in the lesson's own is_linearly_independent code: wrong indentation caused an early return before rank could ever increment past 0 (always returned False), plus a `pivot is none` lowercase-typo masked by the first bug. Mixed up dot product with FOIL-style full distribution once, corrected cleanly. Confused "shape" terminology with geometric shape once; flagged (twice now, across sessions) that comprehension-question phrasing was telegraphing answers via either/or framing — worth phrasing predictions more neutrally going forward. Solid on projection, rank, linear independence, and PyTorch autodiff by the end.

## Review queue
- Phase 0, Lesson 07 (Docker for AI): NVIDIA Container Toolkit (exposes host GPU via `--gpus`, doesn't install drivers in-container) — missed twice now (2026-08-03, 2026-08-09), needs deliberate review not just passive warm-up
- Phase 0, Lesson 01 (Dev Environment): four-layer environment stack install order (System Foundation → Package Managers → Language Runtimes → AI/ML Libraries, bottom-up)
