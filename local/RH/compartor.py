list = [["India", 91, 1148],
    ["China", 86, 1321],
    ["New Zealand", 64, 5],
    ["France", 33, 65],
    ["Mexico", 52, 110]]

# Define our sorting functions.
def byAlpha(countryA, countryB):
    if countryA[0] < countryB[0]:
        return -1
    elif countryA[0] > countryB[0]:
        return 1
    else:
        return 0

def byCode(countryA, countryB):
    return countryA[1] - countryB[1]

def byPop(countryA, countryB):
    return countryA[2] - countryB[2]

list.sort(key = byAlpha)
print (list)
list.sort(byCode)
print (list)
list.sort(byPop)
print (list)