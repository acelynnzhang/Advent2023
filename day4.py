tot = 0

count = []
for x in range(0, 204):
    count.append(1)

cardnum = 1

with open('input.txt', 'r') as file:
    for line in file:
        dat = line.strip().split(':')
        dataa = dat[1].strip().split('|')
        cards = dataa[0].strip().split(' ')
        nums = dataa[1].strip().split(' ')
        seen = {}
        currcount = 0
        for x in cards:
            if str(x).isdigit():
                seen[x] = 1
        for x in nums:
            if x in seen:
                currcount = currcount + 1
        if currcount != 0:
            for i in range(cardnum,(cardnum + currcount)):
                count[i] += 1 * count[cardnum-1]
        cardnum +=1

for x in count:
    tot += x

print(tot)
