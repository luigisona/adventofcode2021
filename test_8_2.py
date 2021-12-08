import sys

#text_file = open("input_8_test.txt", "r")
text_file = open("input_8.txt", "r")
input_lines = text_file.readlines()
# example of input list
# cgdf eagcbf fc adefg eacdb fbedga geafcd efc dacfe fdgaecb | dcefbag dgcf fc daefc
# common segments with 1,4,7,9
common_seg_dict = {
                0: {1:2, 4:3, 7:3, 8:6},   # 2336
                2: {1:1, 4:2, 7:2, 8:5},   # 1225
                3: {1:2, 4:3, 7:3, 8:5},   # 2335
                5: {1:1, 4:3, 7:2, 8:5},   # 1325
                6: {1:1, 4:3, 7:2, 8:6},   # 1326
                9: {1:2, 4:4, 7:3, 8:6},   # 2436
}
def howmanycommon(fromcode, code1, code2):
    z = set(code1).intersection(set(code2))
    return len(z)

def calculate_code_mapping(wires):
    # find 1
    map = ['' for i in range(0,10)]
    for code in wires:
        if len(code) == 2:
            map[1] = sorted(list(code))
        elif len(code) == 3:
            map[7] = sorted(list(code))
        elif len(code) == 4:
            map[4] = sorted(list(code))
        elif len(code) == 7:
            map[8] = sorted(list(code))

    for code in wires:
        for digit in common_seg_dict:
            match = 0
            for fromcode in common_seg_dict[digit]:
                common = howmanycommon(fromcode, map[fromcode], code)
                if common == common_seg_dict[digit][fromcode]:
                    match+=1
            if match == 4:
                map[digit] = code
                break
    sorted_code_map = ['' for i in range(0,10)]
    for digit in range(0,10):
        sorted_code_map[digit] = ''.join(sorted(list(map[digit])))
    print (sorted_code_map)

    return sorted_code_map

def decode(digit,mapping):
    index = mapping.index(digit)
    return str(index)

sum_of_4digits_numbers = 0
for line in input_lines:
    # calculate segments mapping
    wires = line.split('|')[0].split()
    mapping = calculate_code_mapping(wires)
    digits = line.split('|')[1].split()
    # translate digits
    four_digit_number = str('')
    for i in range(0,4):
        four_digit_number = four_digit_number + decode(''.join(sorted(list(digits[i]))), mapping)
    print (four_digit_number)
    sum_of_4digits_numbers += int(four_digit_number)


print(sum_of_4digits_numbers)

text_file.close()


