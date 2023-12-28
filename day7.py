countlines = 0
letters = ['T', 'J', 'Q', 'K', 'A']
handtypes  = {"fiveofakind": [], "fourofakind": [], "fullhouse": [], "threeofakind": [], "twopair": [], "pair": [], "highcard": []}

def toInt(x):
    if x not in letters:
        return int(x)
    if x == 'J':
        return 1
    else:
        curr = letters.index(x) + 10
    return curr

with open('input.txt', 'r') as file:
    for line in file:
        countlines += 1
        thing = line.split(' ')
        high = 1
        repeat= 0
        card = {"2" :[], "1" : []}
        man = []
        for x in thing[0].strip():
            curr = toInt(x)
            if (curr != repeat and curr != 1):
                if thing[0].count(x) > high:
                    card[str(high)].append(toInt(repeat))
                    high = thing[0].count(x)
                    repeat = curr
                elif thing[0].count(x) == high and curr > repeat:
                    card[str(high)].append(toInt(repeat))
                    repeat = curr
                elif toInt(x) not in card['2'] and toInt(x) not in card['1']:
                    card[str(thing[0].count(x))].append(toInt(x))
            man.append(curr)
        high += thing[0].count('J')
        if high >= 5:
            handtypes['fiveofakind'].append([man, thing[1]])
        if high == 4:
            handtypes['fourofakind'].append([man, thing[1]])
        if high == 3:
           if card['2'].__len__() > 0:
                handtypes['fullhouse'].append([man, thing[1]])
           else:
                handtypes['threeofakind'].append([man, thing[1]])
        if high == 2:
            if card['2'].__len__() > 0:
                handtypes['twopair'].append([man, thing[1]])
            else:
                handtypes['pair'].append([man, thing[1]])
        if high == 1:  
            handtypes['highcard'].append([man, thing[1]])


tot = 0
placement = 0
for x in handtypes:
    print(x)
    print(sorted(handtypes[x], reverse=True))
    print('\n')
    for cards,bid in sorted(handtypes[x], reverse=True):
        tot += int(bid) * (countlines - placement)
        # print(bid.replace('\n', '') + " * " + str(countlines - placement))
        placement += 1
        
print(tot)