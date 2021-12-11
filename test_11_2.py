import sys
import numpy

# python stack: use a list
# To push an item in the stack, use the list function append list.append(item)
# To pop an item in the stack, use the list function pop list.pop()
# To get the top most item in the stack, write list[-1]

#text_file = open("input_11_test.txt", "r")
text_file = open("input_11.txt", "r")
input_lines = text_file.readlines()


oct_matrix = []
for i,line in enumerate(input_lines):
    octs = [int(x) for x in list(line.strip())]
    oct_matrix.append(octs)

size = i+1

flashed_in_step = []
for i in range (0,size):
    flashed_in_step.append([False for j in range(0,size)])

steps = 1000
flash_count = 0

def flash(i,j, rec_count):
    global flash_count
    global flashed_in_step
    global oct_matrix

    flash_count += 1
    flashed_in_step[i][j] = True


    for k in range(-1,2):
        for z in range(-1,2):
            l = i+k
            m = j+z
            if l >= 0 and l < size and m >= 0 and m < size and flashed_in_step[l][m] == False:
                # increase adjacent
                if not (k == 0 and z == 0):
                    oct_matrix[l][m] += 1
                    if oct_matrix[l][m] > 9 and flashed_in_step[l][m] == False:
                        flash(l, m, rec_count)

first_sync_flash_step = 0
for s in range(0,steps):
    flash_count = 0
    # phase 1 increase
    for i in range(0,10):
        for j in range(0,10):
            oct_matrix[i][j] += 1

    # phase 2 flashes
    rec_count = 0
    for i in range(0,10):
        for j in range(0,10):
            flashed_in_step[i][j] = False
    for i in range(0,10):
        for j in range(0,10):
            if oct_matrix[i][j] > 9 and flashed_in_step[i][j] == False:
                flash(i,j, rec_count)

    # phase 3 reset to 0 flashed
    for i in range(0,10):
        for j in range(0,10):
            if flashed_in_step[i][j]:
                oct_matrix[i][j] = 0

    sync = True

    if (flash_count == 100):
        print("STEP:",s+1)
        break



print(first_sync_flash_step)
text_file.close()


