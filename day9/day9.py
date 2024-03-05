tot = 0

with open("input.txt", "r") as f:
    lines = f.readlines()

for line in lines:
    curr = line.split(" ")
    layers = []
    layers.append([int(i) for i in curr])

    currlayer = 0
    diff = False
    while not diff:
        curr = []
        countzeros = 0
        for i in range(len(layers[currlayer]) - 1):
            if layers[currlayer][i + 1] - layers[currlayer][i] == 0:
                countzeros += 1
            curr.append(layers[currlayer][i + 1] - layers[currlayer][i])
        layers.append(curr)
        if countzeros == len(layers[currlayer]) - 1:
            diff = True
        currlayer += 1

    for x in range(len(layers) - 1, 0, -1):
        layers[x - 1][0] -= layers[x][0]
    tot += layers[0][0]

print(tot)
