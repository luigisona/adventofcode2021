
text_file = open("input_4.txt", "r")

cols = 5
rows = 5

input_lines = text_file.readlines()
non_empty_lines = [line for line in input_lines if line.strip() != ""]

draws = non_empty_lines[0].split(',')
num_of_boards = int(len(non_empty_lines[1:])/5)
#print(num_of_boards)
zero_matrices = []
boards = []

for mx in range(0,num_of_boards):
  zero_matrix = [([0]*cols) for i in range(rows)]
  zero_matrices.append(zero_matrix)


for bd in range(0,num_of_boards):
    board = []
    for i in range(0,5):
        strrow = list(map(str, non_empty_lines[5*bd+1+i].split()))
        introw = [int(x) for x in strrow]
        board.append(introw)
    boards.append(board)


last_winning_board = -1
winning_row = -1
winning_col = -1
winning_boards = []

for draw in draws:
    #print(draw)
    for i in range(0,num_of_boards):
        for j in range(0,5):
            for k in range(0,5):
                if int(draw) == boards[i][j][k]:
                    zero_matrices[i][j][k] = 1
    # check if there is a bingo
    for i in range(0,num_of_boards):
        if i in winning_boards:
            continue
        for j in range(0,5):
            row = zero_matrices[i][j]
            if sum(row) == 5:
                winning_row = j
                #print(f"{i} won")
                winning_boards.append(i)
                #print(f"winning boards are {len(winning_boards)}")
                if len(winning_boards) == num_of_boards:
                    last_winning_board = i
                    #print(f"Set last winning to {last_winning_board}")
        for j in range(0,5):
            col = [row[j] for row in zero_matrices[i]]
            if sum(col) == 5:
                winning_col = j
                if i not in winning_boards:
                    #print(f"{i} won")
                    winning_boards.append(i)
                    #print(f"winning boards are {len(winning_boards)}")
                    if len(winning_boards) == num_of_boards:
                        last_winning_board = i
                        #print(f"Set last winning to {last_winning_board}")
    if last_winning_board >= 0:
        # last winning board have been found
        break

# calculate result:
# Start by finding the sum of all unmarked numbers on that board;
# in this case, the sum is 188.
# Then, multiply that sum by the number that was just called when the board won, 24,
# to get the final score, 188 * 24 = 4512.

unmarked_sum = 0
for j in range(0, 5):
    for k in range(0, 5):
        if zero_matrices[last_winning_board][j][k] == 0:
            unmarked_sum += boards[last_winning_board][j][k]

print(int(draw)*unmarked_sum)

text_file.close()


