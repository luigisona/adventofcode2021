import sys
import numpy

# python stack: use a list
# To push an item in the stack, use the list function append list.append(item)
# To pop an item in the stack, use the list function pop list.pop()
# To get the top most item in the stack, write list[-1]

#text_file = open("input_10_test.txt", "r")
text_file = open("input_10.txt", "r")
input_lines = text_file.readlines()

closing = {
    '(': ')',
    '[': ']',
    '{': '}',
    '<': '>'
}

u_penalties = {
                '(':1,
                '[':2,
                '{':3,
                '<':4
            }

uncomplete_penalties = []
for line in input_lines:
    line_errored = False
    uncomplete_penalty = 0
    stak = []
    cmds = list(line.strip())
    penalty = 0
    for cmd in cmds:
        if cmd in ['[','(','{','<']:
            stak.append(cmd)
        if cmd in [']',')','}','>']:
            prec = stak.pop()
            if cmd == closing[prec]:
                pass
            else:
                line_errored = True
                break
    if len(stak) != 0 and not line_errored:
        print(stak)
        for opencmd in reversed(stak):
            uncomplete_penalty = uncomplete_penalty * 5 + u_penalties[opencmd]
        uncomplete_penalties.append(uncomplete_penalty)
sorted_uncomplete_penalties = sorted(uncomplete_penalties)
mid = int(len(sorted_uncomplete_penalties)/2)
print(sorted_uncomplete_penalties)
middle = sorted_uncomplete_penalties[mid]


print(middle)


text_file.close()


