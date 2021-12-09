import sys
import numpy

#text_file = open("input_9_test.txt", "r")
text_file = open("input_9.txt", "r")
input_lines = text_file.readlines()

#2199943210
#3987894921
#9856789892
#8767896789
#9899965678

# get the size
rows = len(input_lines)
for line in input_lines:
    columns =(len(list(line.strip())))
    break
#init with maxint
matrix = []
for i in range(0,rows+2):
    row = [sys.maxsize for j in range(0,columns+2)]
    matrix.append(row)

# fill with input data
i = 1
for line in input_lines:
    row = list(line.strip())
    for j in range(1,columns+1):
        matrix[i][j] = int(row[j-1])
    i += 1

# find minimum and sum up

def extend_basin(min,basin):
    adjs = []
    val = min[0]
    i = min[1]
    j = min[2]
    for move in [(0,1),(1,0),(0,-1),(-1,0)]:
        aval = matrix[i+move[0]][j+move[1]]
        if aval > val and aval < 9 and (aval,i+move[0],j+move[1]) not in basin:
            adjs.append((matrix[i+move[0]][j+move[1]],i+move[0],j+move[1]))
    if len(adjs) > 0:
        basin.extend(adjs)
        for adj in adjs:
            extend_basin(adj,basin)
    return

sum_of_minimum_heights = 0
minimums = []
# find minimums in the input matrix and sum up
for i in range(1,rows+1):
    for j in range(1,columns+1):
        p = matrix[i][j]
        if p < matrix[i+1][j] and p < matrix[i-1][j] and p < matrix[i][j+1] and p < matrix[i][j-1]:
            # is a minumum
            sum_of_minimum_heights += p + 1
            minimums.append((p, i ,j))

# initialize basins, to contain the minimum itself
basins = {}
for min in minimums:
    basins[min] = [min]
# calculate basins of minimums
print (basins)
for min in minimums:
    # examine adjacent and add to the basin if > p and < 9
    extend_basin(min,basins[min])

for min in minimums:
    basins_sizes = []

basins_sizes = sorted([len(basins[min]) for min in minimums])
# get the highest 3
last = basins_sizes[-3:]
print(numpy.prod(last))


text_file.close()


