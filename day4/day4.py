count = [1] * 204

cardnum = 1

with open("input.txt") as f:
    lines = f.readlines()

for line in lines:
    dat = line.strip().split(":")
    dataa = dat[1].strip().split("|")
    cards = dataa[0].strip().split(" ")
    nums = dataa[1].strip().split(" ")
    seen = {}
    currcount = 0
    for x in cards:
        if str(x).isdigit():
            seen[x] = 1
    for x in nums:
        if x in seen:
            currcount = currcount + 1
    if currcount != 0:
        for i in range(cardnum, (cardnum + currcount)):
            count[i] += 1 * count[cardnum - 1]
    cardnum += 1

tot = sum(count)

print(tot)
