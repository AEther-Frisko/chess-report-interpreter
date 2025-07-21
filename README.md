# Chess File Interpreter

This is a Python program designed to parse tournament data from .tms and .ctr files, interpret that data, and display it in various ways.

## How to Format TMS Files

the included data.tms.sample file demonstrates how the format looks in an actual file. As a more general example, the expected format is as follows:
```
[seed]	[player name]	[cfc ID]	[cfc Rating]	[results for each round]
```
Each piece of data is tab-delimited.

**Seed:** The player's position in the list (ie. the first player will have a seed of 1)

**Results:** Each result is tab-separated, and follows the following format:
- W, D, or L to denote a win, draw, or loss (or 1, =, or 0 in Round Robin format)
- The seed number of the opposing player (this is not included in the Round Robin format)
- Example:  W10  D2  L5 (or 1   =   0)

## How to Format CTR Files
the included data.ctr.sample file demonstrates how the format looks in an actual file. As a more general example, the expected format is as follows:
```
"event","province","reference number","pairings","end date","no. of players","no. of rounds","type","organizer id","arbiter id"
"player id"
"round result","opponent seed"
...
"player score"
```
Each piece of data is enclosed in quotations and is comma-delimited.

**Province:** In the shortened format (ie. "ON" for Ontario).

**Reference Number:** This one is completely optional.

**Pairings:** The pairing type ("S" for Swiss, "R" for Round Robin).

**End Date:** The end date of the tournament, in YYYY/MM/DD format (ie. "2025/06/21").

**Type:** The format/type of the tournament ("A" for quick/active, "R" for regular).

**Round Result:** The result of the round ("W" for a win, "D" for a draw, "L for a loss").
- In Round Robin format the opponent seed is not included, and the round result is different ("1" for a win, "=" for a draw, "0" for a loss)
- Example:  "W","10" (or "1")