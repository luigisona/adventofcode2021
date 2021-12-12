import sys
import numpy

# Your goal is to find the number of distinct paths that start at start,
# end at end, and don't visit small caves more than once.
# There are two types of caves:
# big caves (written in uppercase, like A)
# and small caves (written in lowercase, like b).
# It would be a waste of time to visit any small cave more than once,
# but big caves are large enough that it might be worth visiting them multiple times.
# So, all paths you find should visit small caves at most once, and can visit big caves any number of times.

#text_file = open("input_12_test_1.txt", "r")
#text_file = open("input_12_test_2.txt", "r")
#text_file = open("input_12_test_3.txt", "r")
text_file = open("input_12.txt", "r")
input_lines = text_file.readlines()

# example
# start-A
# start-b
# A-c
# A-b
# b-d
# A-end
# b-end

# read connections and create the adjacency table
adjs = {}
cave_size = {}
for adj in input_lines:
     caves = list(adj.strip().split('-'))
     if caves[0] not in adjs and not caves[0] == 'end' and not caves[1] == 'start':
         adjs[caves[0]] = [caves[1]]
     elif not caves[1] == 'start' and not caves[0] == 'end':
         print(adj)
         adjs[caves[0]].append(caves[1])
     if caves[1] not in adjs and not caves[0] == 'start' and not caves[1] == 'end':
         adjs[caves[1]] = [caves[0]]
     elif not caves[1] == 'end' and not caves[0] == 'start':
         adjs[caves[1]].append(caves[0])
     if caves[0].isupper():
         cave_size[caves[0]] = "BIG"
     else:
         cave_size[caves[0]] = "LOW"
     if caves[1].isupper():
         cave_size[caves[1]] = "BIG"
     else:
         cave_size[caves[1]] = "LOW"

print(adjs)

def noduplowcave(r):
    s = sorted(r)
    nodup = True
    for i in range(0,len(r)-1):
        if s[i+1] == s[i] and s[i].islower():
            nodup = False
    return nodup



complete_routes = []
extendable_routes = [['start']]
while len(extendable_routes) > 0:
     routes_to_analyze = extendable_routes[:]
     extendable_routes = []
     for route in routes_to_analyze:
         # get the last element of the route
         routetail = route[-1]
         for cave in adjs[routetail]:
             r = route[:]
             if (cave) == 'end':
                 r.append(cave)
                 complete_routes.append(r)
                 # route is complete
             else:
                 if cave not in r or cave_size[cave] == 'BIG' or noduplowcave(r):
                     r.append(cave)
                     extendable_routes.append(r)

print(len(complete_routes))


# find traversal paths from start to end


text_file.close()


