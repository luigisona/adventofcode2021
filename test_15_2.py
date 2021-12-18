import sys
import time

text_file = open("input_15.txt", "r")
#text_file = open("input_15_test.txt", "r")
input_lines = text_file.readlines()

# fill with input data
cost = []

for line in input_lines:
    row = [int(x) for x in list(line.strip())]
    cost.append(row)

size_y = len(cost)
size_x = len(cost[0])

start_point = (0,0)
end_point =(size_x-1,size_y-1)


# find best path from start_point to end_point


def minCost(cost, m, n):
    if (n < 0 or m < 0):
        return sys.maxsize
    elif (m == 0 and n == 0):
        return cost[m][n]
    else:
        return cost[m][n] + min(minCost(cost, m - 1, n),minCost(cost, m, n - 1))


def minCost2(cost, m, n):
    # Instead of following line, we can use int tc[m+1][n+1] or
    # dynamically allocate memoery to save space. The following
    # line is used to keep te program simple and make it working
    # on all compilers.
    tc = [[0 for x in range(size_x)] for x in range(size_y)]

    tc[0][0] = cost[0][0]

    # Initialize first column of total cost(tc) array
    for i in range(1, m + 1):
        tc[i][0] = tc[i - 1][0] + cost[i][0]

    # Initialize first row of tc array
    for j in range(1, n + 1):
        tc[0][j] = tc[0][j - 1] + cost[0][j]

    # Construct rest of the tc array
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            tc[i][j] = min(tc[i][j - 1], tc[i - 1][j]) + cost[i][j]

    return tc[m][n]




#mincost = minCost(cost, size_x-1, size_y-1)
mincost = minCost2(cost, size_x-1, size_y-1)
mincost = mincost - cost[0][0]
print("Costominimo=",mincost)


# This code is contributed by
# Smitha Dinesh Semwal


text_file.close()


