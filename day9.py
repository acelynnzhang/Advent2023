
tot = 0

with open('input.txt', 'r') as file:
    for line in file:
        curr = line.split(' ')
        layers= []
        layers.append([int(i) for i in curr])
        
        currlayer = 0
        diff = False
        while not diff:
            curr = []
            countzeros = 0
            for i in range(len(layers[currlayer]) -1):
                if layers[currlayer][i+1] - layers[currlayer][i] == 0:
                    countzeros += 1
                curr.append(layers[currlayer][i+1] - layers[currlayer][i])
            layers.append(curr)
            if(countzeros == len(layers[currlayer]) -1):
                diff = True
            currlayer += 1
            
        #print(layers)
        for x in range(len(layers)-1, 0, -1):
            layers[x-1][0] -= layers[x][0]
            #print(str(layers[x-1][len(layers[x-1])-1]) + " += " + str(layers[x][len(layers[x])-1]))
        #print(layers)
        tot += layers[0][0]

print(tot)