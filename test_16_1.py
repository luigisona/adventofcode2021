import math

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

# function returns the number of consumed bits
def process_packets(bits):
    global sum
    print(bits)
    pos = 0
    cbits = 0  # consumed bits
    print("LEN",len(bits))
    version = int(bits[pos:pos + 3], 2)
    print("VERSION", version)
    sum += version
    type = int(bits[pos + 3:pos + 6], 2)
    print("TYPE", type)
    cbits += 6
    pos = pos + 6
    if type == 4:
        print("LIT")
        # literal
        binliteral = ''
        firstbit = bits[pos]
        idx = 0
        while firstbit == '1':
            binliteral += bits[pos + 5 * idx:pos + 5 + 5 * idx]
            firstbit = bits[pos + 5 + 5 * idx]
            idx += 1
            cbits+= 5
            # add last digit
        binliteral += bits[pos + 5 * idx:pos + 5 + 5 * idx]
        cbits += 5
        pos += 5 + 5*idx
        print(binliteral)
    else:
        # operator
        # process the packet and call nested process_packets
        # on n packets if operator contains bit I = 1
        # or need to separate
        l_type = int(bits[pos])
        cbits += 1
        pos += 1
        if (l_type == 0):
            print("OPER-0")
            bitl = int(bits[pos:pos + 15], 2)
            cbits += 15
            pos += 15
            cb = 0
            group_end = pos+bitl
            while cb < bitl:
                # process one packet
                c = process_packets(bits[pos:group_end])  # num of bits
                # sum packet length
                cb += c
                pos += c
                cbits+= c
        else:  # l_type = 1
            print("OPER-1")
            pl = int(bits[pos:pos + 11], 2)
            cbits += 11
            print("PL",pl)
            pos += 11
            np = pl
            while np > 0:
                c = process_packets(bits[pos:])  # num of packets
                pos+= c
                cbits += c
                np -= 1
    print("RETURNCBITS",cbits)
    return cbits

bitstrings = []
for line in input_lines:
    hexstr = line.strip()
    bitstr = ''
    for hexc in hexstr:
        bitstr += hex_to_bin[hexc]
    print(hexstr)
    completed = False
    sum = 0
    # bitstr can contain one or more packets
    # the tuple contains the binary string plus the number of packets or the number of bits
    # if t[1] == 1 it is the number of packets
    # if t[1] == 0 it is the number of bits
    process_packets(bitstr)

    print(sum)

text_file.close()


