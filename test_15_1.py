import copy

text_file = open("input_14.txt", "r")
#text_file = open("input_14_test.txt", "r")
input_lines = text_file.readlines()

#polimer template
pt = input_lines[0].strip()

# read input rules
chars = []
rules = []
# init letter count
cnt_let = {}

for j in range(0, len(pt) - 1):
    if pt[j] not in cnt_let:
        cnt_let[pt[j]] = 0

pair_count = {}
for l in input_lines[2:]:
    rule = l.strip().split()
    rules.append((rule[0],rule[2]))
    pair_count[rule[0]] = 0
    if rule[0][0] not in chars:
        chars.append(rule[0][0])
    if rule[0][1] not in chars:
        chars.append(rule[0][1])
    if rule[2] not in chars:
        chars.append(rule[2])
    if rule[0][0] not in cnt_let:
        cnt_let[rule[0][0]] = 0
    if rule[0][1] not in cnt_let:
        cnt_let[rule[0][1]] = 0
    if rule[2] not in cnt_let:
        cnt_let[rule[2]] = 0

print(cnt_let)

steps = 40
current_len = len(pt)

# init pair counters from initial template
for j in range(0, len(pt) - 1):
    pair = pt[j] + pt[j + 1]
    pair_count[pair] += 1

updated_pair_count = {}
for i in range(0,steps):
    # for each pair counter > 0
    # create the two new pairs and count them
    # decrease of one the counter of the pair

    print("PC",pair_count)
    updated_pair_count = copy.deepcopy(pair_count)
    for pair in pair_count:
        pc = pair_count[pair]
        if pc > 0:
            for r in rules:
                if r[0] == pair:
                    new_c = r[1]
                    print("NEWC", new_c)
                    f_pair = pair[0] + new_c
                    s_pair = new_c + pair[1]
                    print("FPAIR", f_pair)
                    print("SPAIR", s_pair)
                    updated_pair_count[f_pair] += pc
                    updated_pair_count[s_pair] += pc
                    updated_pair_count[pair] -= pc

    for let in cnt_let:
        cnt_let[let] = 0
    for pair in updated_pair_count:
        let = pair[1]
        print(let,pair)
        cnt = updated_pair_count[pair]
        cnt_let[let] += cnt
    print(cnt_let)
    print("UPC",updated_pair_count)
    pair_count = copy.deepcopy(updated_pair_count)

cnt_let[pt[0]] += 1
print(cnt_let)

counters  = [cnt_let[let] for let in cnt_let]
print(counters)
print(min(counters))
print(max(counters))
print(max(counters) - min(counters))
text_file.close()


