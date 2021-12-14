
text_file = open("input_14.txt", "r")
#text_file = open("input_14_test.txt", "r")
input_lines = text_file.readlines()

#polimer template
pt = input_lines[0].strip()

# read input rules
chars = []
rules = []
for l in input_lines[2:]:
    rule = l.strip().split()
    rules.append((rule[0],rule[2]))
    if rule[0][0] not in chars:
        chars.append(rule[0][0])
    if rule[0][1] not in chars:
        chars.append(rule[0][1])
    if rule[2] not in chars:
        chars.append(rule[2])


steps = 10
current_len = len(pt)

for i in range(0,steps):
    print(current_len)
    new_pt = pt[0]
    for j in range(0,current_len-1):
        pair = pt[j]+pt[j+1]
        for r in rules:
            if r[0] == pair:
                new_pt += r[1]+pair[1]
    current_len = len(new_pt)
    pt = new_pt

print(len(pt))

nums = [(char,sum(c == char for c in pt)) for char in chars]
print (nums)
maxcnt = max([n[1] for n in nums])
mincnt = min([n[1] for n in nums])

print (maxcnt)
print (mincnt)
print(maxcnt-mincnt)
text_file.close()


