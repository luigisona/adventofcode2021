
#text_file = open("input_7_test.txt", "r")
text_file = open("input_7.txt", "r")
input_lines = text_file.readlines()

# best position is the minimum of the sum of distances of crabs from any position
fuel = 0

# init list of crab positions
crabs_positions = [int(x) for x in input_lines[0].split(",")]
print(crabs_positions)
num_of_crabs = len(crabs_positions)
print(num_of_crabs)
# sorted crab positions
sorted_positions = sorted(crabs_positions)
print(sorted_positions)

# calculate the median of the positions
median_position = int(len(crabs_positions)/2)
best_position = sorted_positions[median_position]
sum_of_crab_moves = 0

for crab_position in crabs_positions:
    fuel += abs(crab_position - best_position)

print(best_position)
print(fuel)

text_file.close()


