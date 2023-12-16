
file = open("input.txt", 'r')
lines = file.readlines()
line_count =len(lines)


def inrange(x, y):
    # print(x, y)
    # print(x >= 0 and x < line_count and y >= 0 and y < len(lines[0].strip()))
    return x >= 0 and x < line_count and y >= 0 and y < len(lines[0].strip())
    

def issym(x):
    return not x.isdigit() and x != "."
# Create a grid to keep track of locations

tot = 0
for i in range(line_count):
    takethis = False
    currint = ""
    for j in range(len(lines[0].strip())):
        if lines[i][j].isdigit():
            currint += lines[i][j]
            if inrange(j+1, i) and issym(lines[i][j + 1]):
                takethis = True
            if inrange(j-1, i) and issym(lines[i][j - 1]):
                takethis = True
            if inrange(j, i +1)and issym(lines[i + 1][j]):
                takethis = True
            if inrange(j, i-1) and issym(lines[i - 1][j]):
                takethis = True
            if inrange(j+1, i+1)  and issym(lines[i + 1][j + 1]):
                takethis = True
            if inrange(j-1, i-1)and issym(lines[i - 1][j - 1]):
                takethis = True
            if inrange(j+1, i-1) and issym(lines[i - 1][j + 1]):
                takethis = True
            if inrange(j-1, i+1) and issym(lines[i + 1][j - 1]) :
                takethis = True
        else:
            if takethis:
                print(currint)
                tot += int(currint)
            takethis = False
            currint = ""
    if takethis:
        print(currint)
        tot += int(currint)
print(tot)
                