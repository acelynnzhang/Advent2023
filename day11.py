with open("test.txt", "r") as f:
    lines = f.readlines()
    actual = []
    for col in range(len(lines)):
      if lines[col].count('.') == len(lines[col].replace('\n', '')):
        actual.append(list(lines[col].replace('\n', '')))
        actual.append(list(lines[col].replace('\n', '')))
      else:
        actual.append(list(lines[col].replace('\n', '')))
    x = len(actual[0])
    col = 0
    gal = 0
    address = []
    while col < x:
      count = len(actual)
      for row in range(len(actual)):
        if actual[row][col]== '.':
          #print( str(row) + " and " +str(col))
          count -= 1
        if count == 0:
          for roww in actual:
            roww.insert(col, '.')
          x += 1
          col +=1
        if actual[row][col]== '#':
          actual[row][col]= gal
          gal += 1
          address.append([row, col])
      col += 1
    
    print(actual)
summ = 0

address.sort()
man = len(address)
while man > 0:
  row = address[0][0]
  col = address[0][1]
  address.pop(0)
  print(str(row) + " " + str(col))
  dyn = [[9999] * (len(actual[0]))] * len(actual)
  dyn[row][col] = 0
  print(dyn)
  for x in range(row, len(actual)):
    for y in range(col,len(actual[0])):
      if x-1 >= 0:
        dyn[x][y] = min(dyn[x][y], dyn[x-1][y] + 1)
      if y -1 >= 0:
        dyn[x][y] = min(dyn[x][y], dyn[x][y-1]+1)
      if str(actual[x][y]).isdigit():
        summ += dyn[x][y]
  print(dyn)
  break
  man-=1

#print(summ)