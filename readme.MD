# Dota 2 Rune Remainder
## Scope

The purpose of this program is rather simple, given the addition of many different runes with patch 7.33, it might be helpful to have a reminder of the different spawning times.

## How it works

Given your steamID, the program search for your current match, starts a timer and reminds you to pick up that rune you almost surely forgot about.


### Practically

The application is always checking for a match, every 30s or so checks if the user is in a match. 

- if in a match: retrieve the time of the match and start a counter.
- else: sleep. 
