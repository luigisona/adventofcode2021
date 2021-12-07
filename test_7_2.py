import sys

#text_file = open("input_7_test.txt", "r")
text_file = open("input_7.txt", "r")
input_lines = text_file.readlines()

#even n+1 * int(n/2)
#odd  = n+1 * int(n/2) + int(n/2)+1

# best position is the minimum of the sum of distances of crabs from any position
fuel = 0

def required_fuel(ref_position, crab_position):
    fuel = 0
    d = abs(crab_position - ref_position)
    if (d % 2) == 0:  # even
        fuel = (d + 1) * int(d/2)
    else: # odd
        fuel = (d + 1) * int(d/2) + int(d/2) + 1
    return fuel

# init list of crab positions
crabs_positions = [int(x) for x in input_lines[0].split(",")]
num_of_crabs = len(crabs_positions)
max_position = max(crabs_positions)
best_fuel = sys.maxsize
best_position = 0
for position in range(0,max_position+1):
    # calculate the sum of necessary fuels
    fuel = 0
    for crab_position in crabs_positions:
        fuel = fuel + required_fuel(position, crab_position)
    if fuel < best_fuel:
        best_fuel = fuel
        best_position = position

print(best_position)
print(best_fuel)

text_file.close()


