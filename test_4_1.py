
text_file = open("input_4.txt", "r")

testdraws = [7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1]
testboards = [
[[22,13,17,11,0],
 [8,2,23,4,24],
[21,9,14,16,7],
 [6,10,3,18,5],
 [1,12,20,15,19]],

[[3,15,0,2,22],
 [9,18,13,17,5],
[19,8,7,25,23],
[20,11,10,24,4],
[14,21,16,12,6]],

[[14,21,17,24,4],
[10,16,15,9,19],
[18,8,23,26,20],
[22,11,13,6,5],
 [2,0,12,3,7]]
    ]

cols = 5
rows = 5

input_lines = text_file.readlines()
non_empty_lines = [line for line in input_lines if line.strip() != ""]

draws = non_empty_lines[0].split(',')
print (draws)
num_of_boards = int(len(non_empty_lines[1:])/5)
print(num_of_boards)
zero_matrices = []
boards = []
cols = 5
rows = 5
for mx in range(0,num_of_boards):
  zero_matrix = [([0]*cols) for i in range(rows)]
  zero_matrices.append(zero_matrix)

print(zero_matrices[0])
print(zero_matrices[2])
print(zero_matrices[0][0])
print(zero_matrices[2][0])

for bd in range(0,num_of_boards):
    board = []
    for i in range(0,5):
        strrow = list(map(str, non_empty_lines[5*bd+1+i].split()))
        introw = [int(x) for x in strrow]
        board.append(introw)
    boards.append(board)


print(boards[0])
print(boards[2])

winning_board = -1
winning_row = -1
winning_col = -1

for draw in draws:
    print(draw)
    for i in range(0,num_of_boards):
        for j in range(0,5):
            for k in range(0,5):
                if int(draw) == boards[i][j][k]:
                    print(zero_matrices[i][j][k])
                    zero_matrices[i][j][k] = 1
                    print(zero_matrices[i][j][k])
    # check if there is a bingo
    for i in range(0,num_of_boards):
        for j in range(0,5):
            row = zero_matrices[i][j]
            if sum(row) == 5:
                winning_row = j
                winning_board = i
        for j in range(0,5):
            col = [row[j] for row in zero_matrices[i]]
            if sum(col) == 5:
                winning_col = j
                winning_board = i
    if winning_board > 0:
        break

# calculate result:
# Start by finding the sum of all unmarked numbers on that board;
# in this case, the sum is 188.
# Then, multiply that sum by the number that was just called when the board won, 24,
# to get the final score, 188 * 24 = 4512.
print(zero_matrices[winning_board])
print(boards[winning_board])

print(winning_board)
print(winning_col)
print(winning_row)
print(draw)

unmarked_sum = 0
for j in range(0, 5):
    for k in range(0, 5):
        if zero_matrices[winning_board][j][k] == 0:
            unmarked_sum += boards[winning_board][j][k]

print(unmarked_sum)
print(int(draw)*unmarked_sum)

text_file.close()


