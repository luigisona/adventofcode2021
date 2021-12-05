def get_segment_points(x1,y1,x2,y2):
    howmany = (x2-x1+1) if x1<x2 else x1-x2+1
    res = []
    for i in range(0,howmany):
        x = x1+i if x1<x2 else x1-i
        y = y1+i if y1<y2 else y1-i
        res.append((x,y))
    return res



text_file = open("input_5.txt", "r")
input_lines = text_file.readlines()



# Example
# 0,9 -> 5,9
size = 1000
counters_matrix = [([0]*size) for i in range(size)]

# parse lines and consider only those that represent an horizontal or vertival line
for line in input_lines:
    tokens = line.split()
    firstpair = tokens[0]
    secondpair = tokens[2]
    x1 = int(firstpair.split(',')[0])
    y1 = int(firstpair.split(',')[1])
    x2 = int(secondpair.split(',')[0])
    y2 = int(secondpair.split(',')[1])

    # it is a horizontal or vertical
    # increment values in the counter matrix
    if (x1 == x2):
            # increment y
            if y2 > y1:
                r = range(y1,y2+1)
            else:
                r = range(y2,y1+1)
            for col in r:
                counters_matrix[x1][col] += 1
    elif (y1 == y2):
            # increment x
            if x2 > x1:
                r = range(x1,x2+1)
            else:
                r = range(x2,x1+1)
            for row in r:
                counters_matrix[row][y1] += 1
    else: # diagonal
        points = get_segment_points(x1,y1,x2,y2)
        print(line)
        for p in points:
            counters_matrix[p[0]][p[1]] += 1
# now find in how many cells at least tow lines overlaps
howmany = 0
total = 0
for row in range(0,size):
    for col in range(0,size):
        if counters_matrix[row][col] >= 2:
            howmany += 1

print(counters_matrix)
print(howmany)
text_file.close()


