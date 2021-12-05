text_file = open("input.txt", "r")
lines = text_file.readlines()
previous_val = -1
number_of_increases = 0
for l in lines:
    val = int(l)
    if val > previous_val and previous_val > 0:
        number_of_increases += 1
    previous_val = val
text_file.close()
print(number_of_increases)