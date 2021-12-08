import sys

#text_file = open("input_8_test.txt", "r")
text_file = open("input_8.txt", "r")
input_lines = text_file.readlines()
# example of input list
# cgdf eagcbf fc adefg eacdb fbedga geafcd efc dacfe fdgaecb | dcefbag dgcf fc daefc

num_of_1_4_7_8 = 0
for line in input_lines:
    four_digits_codes = line.split('|')[1].split()
    print (four_digits_codes)
    for digit_code in four_digits_codes:
        if len(digit_code) in [2,3,4,7]:
            num_of_1_4_7_8 += 1

print(num_of_1_4_7_8)

text_file.close()


