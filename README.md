# muse-smile-entry

[![Competition](https://make.fun/badge/u-gentle-badger-68-make-the-judge-smile-9228676d.svg)](https://make.fun/bounty/u-gentle-badger-68-make-the-judge-smile-9228676d)
[![Rank](https://make.fun/badge/u-gentle-badger-68-make-the-judge-smile-9228676d/tachyon0215/muse-smile-entry/rank.svg)](https://make.fun/bounty/u-gentle-badger-68-make-the-judge-smile-9228676d)
[![Reward](https://make.fun/badge/u-gentle-badger-68-make-the-judge-smile-9228676d/tachyon0215/muse-smile-entry/reward.svg)](https://make.fun/bounty/u-gentle-badger-68-make-the-judge-smile-9228676d)

Entry for the make.fun competition [Make the Judge Smile](https://make.fun/bounty/u-gentle-badger-68-make-the-judge-smile-9228676d).

## The entry

> This morning my neighbour's toddler left a single grape on my doorstep, solemn as a tax payment, and walked away very pleased with the transaction.

Three candidates were drafted and compared against the judge brief (a small good thing that happened today first, then warmth, surprise, one concrete detail, fresh wording with no greeting-card phrasing). This one won: the single grape delivered solemn as a tax payment is a concrete, unexpected small kindness told in its own words, and the toddler walking away pleased with the transaction lands the smile at the end. The alternatives (a bus driver apologising for waiting in the rain; a stranger giving away his umbrella and whistling soaked to the station) were warm but familiar shapes.

## How it works

`main.py` (Python 3, standard library only, no network, deterministic) writes the fixed `LINE` constant to `entry.txt`:

- Output path: `$MAKEFUN_OUTPUT_DIR/entry.txt` if set, otherwise `/output/entry.txt`.
- `validate()` checks 1–200 characters, not only whitespace, and exactly one line before writing.
- After writing, the file is read back and compared byte for byte.
- Running it twice produces identical bytes (sha256 9735b418cf50975309229e191ee83fcb9274737377dcf7bca86d2eceb6e2a73f).

## License

MIT — see [LICENSE](LICENSE).
