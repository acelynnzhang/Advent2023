letters = ["T", "J", "Q", "K", "A"]
handtypes = {
    "fiveofakind": [],
    "fourofakind": [],
    "fullhouse": [],
    "threeofakind": [],
    "twopair": [],
    "pair": [],
    "highcard": [],
}


def to_int(x):
    if x not in letters:
        return int(x)
    if x == "J":
        return 1
    else:
        curr = letters.index(x) + 10
    return curr


with open("input.txt") as f:
    lines = f.readlines()

for line in lines:
    thing = line.split(" ")
    high = 1
    repeat = 0
    card = {"2": [], "1": []}
    man = []
    for x in thing[0].strip():
        curr = to_int(x)
        if curr != repeat and curr != 1:
            if thing[0].count(x) > high:
                card[str(high)].append(to_int(repeat))
                high = thing[0].count(x)
                repeat = curr
            elif thing[0].count(x) == high and curr > repeat:
                card[str(high)].append(to_int(repeat))
                repeat = curr
            elif to_int(x) not in card["2"] and to_int(x) not in card["1"]:
                card[str(thing[0].count(x))].append(to_int(x))
        man.append(curr)
    high += thing[0].count("J")
    if high >= 5:
        handtypes["fiveofakind"].append([man, thing[1]])
    if high == 4:
        handtypes["fourofakind"].append([man, thing[1]])
    if high == 3:
        if len(card["2"]) > 0:
            handtypes["fullhouse"].append([man, thing[1]])
        else:
            handtypes["threeofakind"].append([man, thing[1]])
    if high == 2:
        if len(card["2"]) > 0:
            handtypes["twopair"].append([man, thing[1]])
        else:
            handtypes["pair"].append([man, thing[1]])
    if high == 1:
        handtypes["highcard"].append([man, thing[1]])


tot = 0
placement = 0
for x in handtypes:
    for cards, bid in sorted(handtypes[x], reverse=True):
        tot += int(bid) * (len(lines) - placement)
        placement += 1

print(tot)
