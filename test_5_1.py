
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
    if not (x1 == x2 or y1 == y2):
        continue
    else:
        # it is a horizontal or vertical
        print(line)
        # increment values in the counter matrix
        if (x1 == x2):
            # increment y
            if y2 > y1:
                r = range(y1,y2+1)
            else:
                r = range(y2,y1+1)
            print(r)
            for col in r:
                counters_matrix[x1][col] += 1
        elif (y1 == y2):
            # increment x
            if x2 > x1:
                r = range(x1,x2+1)
            else:
                r = range(x2,x1+1)
            print(r)
            for row in r:
                counters_matrix[row][y1] += 1

# now find in how many cells at least tow lines overlaps
howmany = 0
total = 0
for row in range(0,size):
    for col in range(0,size):
        total = total + counters_matrix[row][col]
        if counters_matrix[row][col] >= 2:
            howmany += 1

print(howmany)
text_file.close()


