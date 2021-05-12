import sys
import datetime
daysLeft =  (datetime.date(2021, 6, 8) - datetime.date.today()).days
matchXp = 9000
print(datetime.datetime.now())

print("There are at least %d days left of the season" % (daysLeft))
print("Xp per match estimated to %d" % (matchXp))

table = {}

with open("table.txt", "r") as f:
	for l in f:
		sl = l.split(", ")
		table[int(sl[0])] =  int(sl[1])

global modifiers
modifiers = 0
def addBonusXp(amount, desc):
	global modifiers
	print("Bonus: %d xp - %s" % (amount, desc))
	modifiers += amount

addBonusXp(daysLeft * 66000, "daily 3*22 k")
for i in range(int(daysLeft/7)):
    addBonusXp(35000 + 4 * 24500 + 24000*7, "Weekly legendary/epic in " + str(i + 1) + " week")
print("Estimated bonus xp: %d" % (modifiers))
print()

def getXp(level):
	if level in table:
		return table[level]
	else:
		return 80000
	

def roughMatches(xp):
	matches = xp/9000
	print("Which is roughly %.2f matches or %.2f per day" % (matches, matches/daysLeft))

def xpCalc(startString, end):
	s = 0
	startS = startString.split(".")
	start = int(startS[0])
	forAvgS = 0
	if start >= end:
		print("%d has already been achieved" % (end))
		print()
		return
	for i in range(start, end):
		forAvgS += getXp(i)
	if len(startS) == 2:
		firstLevelPartial = float("0."+startS[1])
	else:
		firstLevelPartial = 0
	sWithModifiers = 0
	print(">>>> %s -> %d (current xp per level: %d, average per level: %d)" % (startString, end, getXp(start), forAvgS/(end-start)))
	print("Levels until %d: %d"  % (end, end-start))
	print("Levels per day: %.2f" % ((end-start) / daysLeft))
	if firstLevelPartial != 0:
		partXp = (1 - firstLevelPartial) * getXp(start)
		print("Xp left until level up: %d" % (partXp))
		s += partXp
		start += 1
	for i in range(start, end):
		s += getXp(i)
	print("Xp total: %d" % (s))
	print("Xp per day: %.2f" % (s/daysLeft))
	roughMatches(s)
	sWithModifiers = s - modifiers
	print("Xp with bonus xp: %d" % (sWithModifiers))
	print("Xp with bonus xp per day: %.2f"  % (sWithModifiers/daysLeft))
	roughMatches(sWithModifiers)
	print()

start = sys.argv[1]
if len(sys.argv) == 2:
	xpCalc(start, 225)
else:
	for v in sys.argv[2:]:
		xpCalc(start, int(v))
