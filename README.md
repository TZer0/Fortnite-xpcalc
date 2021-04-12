# Fortnite-xpcalc
Usage:
```
python xpcalc.py YOURLEVEL [TARGETLEVEL1, TARGETLEVEL2...]
```
If no `TARGETLEVEL`s provided, will use some defaults. `YOURLEVEL` can include a `.` to denote estimated progress through the current level.

Examples:
Calculate xp and matches needed from 112.5 to the default levels.
```
python xpcalc.py 112.5
```


Same, but for level 60 to level 100 and level 120.
```
python xpcalc.py 60 100 120

```
Sample output:
```
$ python xpcalc.py 60 100 120
2021-04-12 23:49:02.885774
There are at least 57 days left of the season
Xp per match estimated to 9000
Bonus: 3762000 xp - daily 3*22 k
Estimated bonus xp: 3762000

>>>> 60 -> 100 (current xp per level: 80000, average per level: 80000)
Levels until 100: 40
Levels per day: 0.70
Xp total: 3200000
Xp per day: 56140.35
Which is roughly 355.56 matches or 6.24 per day
Xp with bonus xp: -562000
Xp with bonus xp per day: -9859.65
Which is roughly -62.44 matches or -1.10 per day

>>>> 60 -> 120 (current xp per level: 80000, average per level: 70666)
Levels until 120: 60
Levels per day: 1.05
Xp total: 4240000
Xp per day: 74385.96
Which is roughly 471.11 matches or 8.27 per day
Xp with bonus xp: 478000
Xp with bonus xp per day: 8385.96
Which is roughly 53.11 matches or 0.93 per day
```
