# TMS File Interpreter

This is a Python program designed to parse tournament data from .tms files, interpret that data, and display it in various ways.

## How to Format TMS Files

the included data.tms.sample file demonstrates how the format looks in an actual file. As a more general example, the expected format is as follows:
```
[seed]	[last name], [first name]	[cfc ID]	[cfc Rating]	[results for each round]
```
Each piece of data is tab-delimited.

**Seed:** The player's position in the list (ie. the first player will have a seed of 1)

**Name:** Although it says "last name, first name", additional names can also be included if applicable

**Results:** Each result is tab-separated, and follows the following format:
- W, D, or L to denote a win, draw, or loss
- The seed number of the opposing player
- Example:  W10  D2  L5
