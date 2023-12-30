
start = []
grid = []
linecount = 0

with open("test.txt", "r") as f:
    lines = f.readlines()
    seen = [[0] * len(lines[0])] * len(lines)
    for line in lines:
        currline = []
        for x in range(len(line)):
            currline.append(line[x])
            if line[x] == 'S':
               start.append(linecount)
               start.append(x)
        linecount +=1
        grid.append(currline)
print(start) 
print("start")       
dirr = [1,0]
currloc = []
currloc.append(start[0])
currloc.append(start[1])
steps  = 0 

while currloc != start or steps == 0:
  #print(currloc)
  # print("+")
  # print(dirr)
  seen[currloc[0]][currloc[1]] = 1
  letter = grid[currloc[0] + dirr[0]][currloc[1] + dirr[1]]
  currloc[0] += dirr[0]
  currloc[1] += dirr[1]
  # print("at letter " + letter)
  # print("after adding")
  # print(currloc)
  if letter == 'L': 
    if dirr[0] != 0:
      dirr[1] = 1
      dirr[0] = 0
    else:
      dirr[1] = 0
      dirr[0] = -1
  if letter == 'J':
    if dirr[0] != 0:
      dirr[1] = -1
      dirr[0] = 0
    else:
      dirr[1] = 0
      dirr[0] = -1
  if letter == '7':
    if dirr[0] != 0:
      dirr[1] = -1
      dirr[0] = 0
    else:
      dirr[1] = 0
      dirr[0] = 1
  if letter == 'F':
    if dirr[0] != 0:
      dirr[1] = 1
      dirr[0] = 0
    else:
      dirr[1] = 0
      dirr[0] = 1
  if letter == '.':
    print("fuck")
    break
  steps +=1
wall = sorted(walls, reverse=True)
print(wall)
count = 0
otherwall = []
interval = []
mapp = {}
con = True
while len(wall) > 1:
  if wall[0][0] == wall[1][0]:
    # while len(wall) > 1 and wall[0][1] == wall[1][1] +1:
    #   wall.pop(0)
    if len(wall) > 1 and wall[0][1] - wall[1][1] -1 > 0:
      count += wall[0][1] - wall[1][1] -1
      print(wall[:2])
    wall.pop(0)
    wall.pop(0)
  else: 
    wall.pop(0)

print(count)
# .....
# .S-7.
# .|.|.
# .L-J.
# .....


#  (1,1)
#  (2,1)
#  (3,1)
#  (3,2)
#  (3,3)
#  (2,3)
#  (1,3)
#  (1,2)
#  (1,1)

 

