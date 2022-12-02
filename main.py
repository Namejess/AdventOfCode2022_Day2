if __name__ == '__main__':

    with open('input') as f:
        listInput = [i.replace(" ", "") for i in f.read().strip().split("\n")]

# LOOSE = 0
# WIN = 6
# DRAW = 3
# A & X = 1
# B & Y = 2
# C & Z = 3
#

winMap = {
    "AX": 4,
    "AY": 8,
    "AZ": 3,
    "BX": 1,
    "BY": 5,
    "BZ": 9,
    "CX": 7,
    "CY": 2,
    "CZ": 6
}

score = 0
for tour in listInput:
    score += winMap[tour]

# PART TWO
#
# X = LOOSE = 0
# Y = DRAW = 3
# Z = WIN = 6
# A & X = 1
# B & Y = 2
# C & Z = 3

fullMap = {
    "AX": 3,
    "AY": 4,
    "AZ": 8,
    "BX": 1,
    "BY": 5,
    "BZ": 9,
    "CX": 2,
    "CY": 6,
    "CZ": 7
}

score2 = 0
for tour2 in listInput:
    score2 += fullMap[tour2]

print(score2)
