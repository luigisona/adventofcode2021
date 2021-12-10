import sys
import numpy

# python stack: use a list
# To push an item in the stack, use the list function append list.append(item)
# To pop an item in the stack, use the list function pop list.pop()
# To get the top most item in the stack, write list[-1]

#text_file = open("input_10_test.txt", "r")
text_file = open("input_10.txt", "r")
input_lines = text_file.readlines()
result = 0

penalties = {
                ')':3,
                ']':57,
                '}':1197,
                '>':25137
            }
closing = {
    '(': ')',
    '[': ']',
    '{': '}',
    '<': '>'
}
penalty_sum = 0
for line in input_lines:
    stak = []
    cmds = list(line.strip())
    print(cmds)
    penalty = 0
    for cmd in cmds:
        if cmd in ['[','(','{','<']:
            stak.append(cmd)
        if cmd in [']',')','}','>']:
            prec = stak.pop()
            if cmd == closing[prec]:
                pass
            else:
                penalty = penalties[cmd]
                penalty_sum += penalty
                break
    if len(stak) == 0:
        line_complete = True
    else:
        line_complete = False


print(penalty_sum)


text_file.close()


