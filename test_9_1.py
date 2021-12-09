import sys

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
print(rows)
print(columns)
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

sum_of_minimum_heights = 0

# find minimums in the input matrix and sum up
for i in range(1,rows+1):
    for j in range(1,columns+1):
        p = matrix[i][j]
        if p < matrix[i+1][j] and p < matrix[i-1][j] and p < matrix[i][j+1] and p < matrix[i][j-1]:
            # is a minumum
            sum_of_minimum_heights += p + 1

print(sum_of_minimum_heights)

text_file.close()


