# with open("test.txt", "r") as f:
#         lines = ''.join(f.readlines()).split('\n')
#         lines.reverse()
#         sp = [list(x) for x in lines]
#         print(sp)
#         for i in range(len(sp) -1):
#                 for j in range(len(sp[i])):
#                         if sp[i][j] == 'O' and sp[i+1][j] == '.':
#                                 sp[i+1][j] = 'O'
#                                 sp[i][j] = '.'
#                                 i = -1
                                
#         summ = 0
#         for x in range(len(sp)):
#                 for y in sp[x]:
#                         if y == 'O':
#                                 summ += x + 1

# print(sp)
# print(summ)

with open("test.txt", "r") as f:
    lines = f.read().split('\n')
    sp = [list(x) for x in lines]
    for col in range(len(sp[0])):
        rocks = 0
        start = 0
        for row in range(len(sp)):
                if sp[row][col] == 'O':
                        rocks +=1
                        sp[row][col] = '.'
                if sp[row][col] == '#':
                        if start == -1:
                                start = row + 1
                        else:
                                while rocks > 0:
                                       sp[start][col] = 'O'
                                       rocks -= 1
                                       start +=1
                                start = -1

        summ = 0
        for x in range(len(sp)):
                for y in sp[x]:
                        if y == 'O':
                                summ += (len(sp) - x)

print(sp)
print(summ)