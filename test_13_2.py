import sys
import numpy

text_file = open("input_13.txt", "r")
#text_file = open("input_13_test.txt", "r")
input_lines = text_file.readlines()


max_x = 0
max_y = 0
points=[]
# read initial sheet
for l in input_lines:
    #print(l.strip())
    if len(l.strip()) == 0:
    # exit from the loop when there is the empty line in the input
        break
    x = int(l.strip().split(',')[0])
    y = int(l.strip().split(',')[1])
    if x > max_x:
        max_x = x
    if y > max_y:
        max_y = y
    points.append((x,y))


print(max_x,max_y)

# now we now size of the sheet
sheet = []
for j in range(0,max_y+1):
    row = [0 for x in range(0,max_x+1)]
    sheet.append(row)
for p in points:
    sheet[p[1]][p[0]] = 1
print ("Count=",len(points))

size_x = max_x+1
size_y = max_y+1
print(size_x, size_y)

# we have the entire sheet
# read comments
cmds = []
found_blank = False
icount = 0


for l in input_lines:

    if len(l.strip()) == 0:
        found_blank = True
        continue
    if not found_blank:
        continue
    cmds.append(l.strip().split()[2])

print(cmds)

# now apply commnda
for cmd in cmds:
    # fold the sheet
    along = cmd.split('=')[0]
    pos = int(cmd.split('=')[1])
    print(f"fold along {along} at {pos}")

    if along == 'y':
        for j in range(0,size_y -pos):
            for i in range(0,size_x-1):
                c = sheet[j+pos][i]
                sheet[pos-j][i] |=  c
        # set size to half
        size_y = pos
    if along == 'x':
        for i in range(0, size_x  -pos):
            for j in range(0,size_y-1):
                c = sheet[j][i+pos]
                sheet[j][pos-i] |= c
        # set size to half
        size_x = pos

    print(size_x, size_y)
    #for i in range(0, size_y):
        #print(sheet[i])
    count = 0
    for j in range(0, size_y ):
        l = []
        for i in range(0,size_x):
            l.append(sheet[j][i])
        for i in range(0, size_x ):
            if sheet[j][i] == 1:
                count+=1
    print("Count=",count)
    if count < 300:
        print(size_x, size_y)
        for i in range(0, size_y):
            print(sheet[i])




text_file.close()


