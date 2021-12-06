
text_file = open("input_6.txt", "r")
#text_file = open("input_6_test.txt", "r")
input_lines = text_file.readlines()

#days = 80
days = 256

result = 0

# init list of counters to keep the number of fishes with same age
countfish = [0 for i in range(0,9)]
for x in input_lines[0].split(","):
    xi = int(x)
    countfish[xi] += 1

print(countfish)


for days in range(0,days):
    # decrement time to generate for each fish and create new fish for each counter equals to 0 that is reset to 6
    newfishes = countfish[0]
    print(newfishes)
    for i in range(0,8):
        countfish[i] = countfish[i+1]
    countfish[8] = newfishes
    countfish[6] += newfishes

numfishes = sum(countfish)
print(countfish)
print(numfishes)




text_file.close()


