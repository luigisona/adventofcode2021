import numpy

#text_file = open("input_16_test.txt", "r")
text_file = open("input_16.txt", "r")
input_lines = text_file.readlines()

hex_to_bin = {
'0':'0000',
'1':'0001',
'2':'0010',
'3':'0011',
'4':'0100',
'5':'0101',
'6':'0110',
'7':'0111',
'8':'1000',
'9':'1001',
'A':'1010',
'B':'1011',
'C':'1100',
'D':'1101',
'E':'1110',
'F':'1111'
}

def do_op(op, nums):
    result = 0
    if op == 0:
        result = numpy.sum(nums)
    elif op == 1:
        result =  numpy.prod(nums)
    elif op == 2:
        result = min(nums)
    elif op == 3:
        result = max(nums)
    elif op == 5:
        if nums[0] > nums[1]:
            result = 1
        else:
            result = 0
    elif op == 6:
        if nums[0] < nums[1]:
            result = 1
        else:
            result = 0
    elif op == 7:
        if nums[0] == nums[1]:
            result = 1
        else:
            result = 0
    return result

# function returns the number of consumed bits
def process_packets(bits):
    global sum
    pos = 0
    cbits = 0  # consumed bits
    version = int(bits[pos:pos + 3], 2)
    sum += version
    type = int(bits[pos + 3:pos + 6], 2)
    cbits += 6
    pos = pos + 6
    nums = []
    if type == 4:
        # literal
        binliteral = ''
        firstbit = bits[pos]
        idx = 0
        n = 0
        while firstbit == '1':
            binliteral += bits[pos + 5 * idx:pos + 5 + 5 * idx]
            digit = int(bits[pos + 5 * idx + 1:pos + 5 + 5 * idx], 2)
            n = n*16 + digit
            firstbit = bits[pos + 5 + 5 * idx]
            idx += 1
            cbits+= 5
            # add last digit
        binliteral += bits[pos + 5 * idx:pos + 5 + 5 * idx]
        digit = int(bits[pos + 5 * idx + 1:pos + 5 + 5 * idx],2)
        n = n*16 + digit
        cbits += 5
        pos += 5 + 5*idx
        return (cbits,n)
    else:
        # operator
        # process the packet and call nested process_packets
        # on n packets if operator contains bit I = 1
        # or need to separate
        op = type
        l_type = int(bits[pos])
        cbits += 1
        pos += 1
        if (l_type == 0):
            bitl = int(bits[pos:pos + 15], 2)
            cbits += 15
            pos += 15
            cb = 0
            group_end = pos+bitl
            while cb < bitl:
                # process one packet
                c,n = process_packets(bits[pos:group_end])  # num of bits
                nums.append(n)
                # sum packet length
                cb += c
                pos += c
                cbits+= c
        else:  # l_type = 1
            pl = int(bits[pos:pos + 11], 2)
            cbits += 11
            pos += 11
            np = pl
            while np > 0:
                c,n = process_packets(bits[pos:])  # num of packets
                nums.append(n)
                pos+= c
                cbits += c
                np -= 1
        n = do_op(op,nums)
        return cbits, n

bitstrings = []
for line in input_lines:
    hexstr = line.strip()
    bitstr = ''
    for hexc in hexstr:
        bitstr += hex_to_bin[hexc]
    completed = False
    sum = 0
    # bitstr can contain one or more packets
    # the tuple contains the binary string plus the number of packets or the number of bits
    # if t[1] == 1 it is the number of packets
    # if t[1] == 0 it is the number of bits
    c,n = process_packets(bitstr)

    print("VERSIONSUM=",sum)
    print("RES=",n)

text_file.close()


