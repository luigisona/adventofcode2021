
text_file = open("input_6.txt", "r")
#text_file = open("input_6.txt", "r")
input_lines = text_file.readlines()

#days = 18
days = 256

result = 0

# init list of fishes
fishes = [int(x) for x in input_lines[0].split(",")]

for days in range(0,days):
    # decrement time to generate for each fish and create new fish for each counter equals to 0 that is reset to 6
    newfishes = 0
    for i, fish in enumerate(fishes):
        if fish == 0:
            fishes[i] = 6
            newfishes += 1
        else:
            fishes[i] -=1
    for i in range(0,newfishes):
        fishes.append(8)

num = len(fishes)
print(fishes)
print(num)



text_file.close()


