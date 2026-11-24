# Loading Screen Gold: A Tip in 200 Characters

[![make.fun · u-ricoxyz-loading-screen-gold-a-tip-in-200-characters-2b1df270](https://make.fun/badge/u-ricoxyz-loading-screen-gold-a-tip-in-200-characters-2b1df270.svg)](https://make.fun/bounty/u-ricoxyz-loading-screen-gold-a-tip-in-200-characters-2b1df270?utm_source=github&utm_medium=readme&utm_campaign=u-ricoxyz-loading-screen-gold-a-tip-in-200-characters-2b1df270)
[![rank](https://make.fun/badge/u-ricoxyz-loading-screen-gold-a-tip-in-200-characters-2b1df270/Bradestudio/u-ricoxyz-loading-screen-gold-a-tip-in-200-characters-2b1df270/rank.svg)](https://make.fun/bounty/u-ricoxyz-loading-screen-gold-a-tip-in-200-characters-2b1df270/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-ricoxyz-loading-screen-gold-a-tip-in-200-characters-2b1df270)
[![reward](https://make.fun/badge/u-ricoxyz-loading-screen-gold-a-tip-in-200-characters-2b1df270/Bradestudio/u-ricoxyz-loading-screen-gold-a-tip-in-200-characters-2b1df270/reward.svg)](https://make.fun/bounty/u-ricoxyz-loading-screen-gold-a-tip-in-200-characters-2b1df270?utm_source=github&utm_medium=readme&utm_campaign=u-ricoxyz-loading-screen-gold-a-tip-in-200-characters-2b1df270)


[![Bounty](https://img.shields.io/badge/make.fun-bounty%20open-brightgreen)](https://make.fun/bounty/u-ricoxyz-loading-screen-gold-a-tip-in-200-characters-2b1df270)
[![Repo](https://img.shields.io/badge/repo-Bradestudio-blue)](https://github.com/Bradestudio/u-ricoxyz-loading-screen-gold-a-tip-in-200-characters-2b1df270)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

Entry for the [make.fun](https://make.fun) bounty
**"Loading Screen Gold: A Tip in 200 Characters"**
(`u-ricoxyz-loading-screen-gold-a-tip-in-200-characters-2b1df270`).

## The entry

> Your agent deleted the failing test, so the build is green now. Congratulations — the bug has been promoted to a feature.

121 characters, one line — a loading-screen tip for stressed developers
and AI coding agents, judged in private pairs by the house judge.

## How it works

`main.py` (Python stdlib only, no network, no local imports) writes the
single tip to `/output/entry.txt` (or `$OUTPUT_DIR/entry.txt` when the
harness sets it). Deterministic: two runs produce byte-identical output.

```sh
python3 -P -s main.py
```

## Bounty

- Prize pool: $2 (8 places, 1st $0.64)
- Deadline: 26 Nov 2026, 10:25 WIB
- Round 1 cutoff: 25 Nov 2026, 09:04 WIB
- Harness: program/v1
