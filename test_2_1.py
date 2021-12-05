text_file = open("input2.txt", "r")
lines = text_file.readlines()
horizontal = 0
depth = 0

# Commands
# forward
# down
# up

for l in lines:
    cmd = l.split()
    print(cmd[0], cmd[1])
    if cmd[0] == "forward":
        horizontal += int(cmd[1])
    elif cmd[0] == "down":
        depth += int(cmd[1])
    elif cmd[0] == "up":
        depth -= int(cmd[1])


text_file.close()
print(horizontal*depth)