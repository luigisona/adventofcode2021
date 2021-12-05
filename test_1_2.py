text_file = open("input.txt", "r")
lines = text_file.readlines()
previous_sum_val = -1
previous_val_minus_1 = -1
previous_val_minus_2 = -1
number_of_increases = 0
sum_val = -1
for l in lines:
    val = int(l)
    if previous_val_minus_1 > 0 and previous_val_minus_2 > 0:
        sum_val = val + previous_val_minus_1 + previous_val_minus_2
        if previous_sum_val > 0:
            if sum_val > previous_sum_val:
                number_of_increases+=1
    previous_sum_val = sum_val
    previous_val_minus_2 = previous_val_minus_1
    previous_val_minus_1 = val

text_file.close()
print(number_of_increases)