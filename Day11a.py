import re


split_lines = """..#............................#....................................................................................#..........#........#...
..........#.........................................#.......................................................................................
...................#..........................................................................#.............................................
.....................................................................................#.............................................#........
.......#.......#.............#..........#......#...................#.....#..................................................................
................................................................................#..................#..............#.........................
....................................#.......................................................................................................
...........#...................................................................................#......................................#.....
.......................................................................................................................#.........#..........
.....................#.................................................#...................#.................#..............#...............
....#...........................................#...............#...........................................................................
.........................#.......................................................................#..........................................
...................................#......................#.......................................................#.......................#.
..................#...........................................................#.......................#.................#...........#.......
..........#........................................................#..........................................#.............................
.............................................#.........#.....#..............................................................................
.......................#.....................................................................#..............................#..........#....
.............................#.......................................................#...........................#..........................
..#...........#.......................#.....................................#...............................................................
...........................................................#.............................................#..................................
......#..........................................................#......#........................................................#..........
................................#.........#...........#....................................#........#...................#..................#
...........................#..................................................#..............................#..............................
..............................................#.................................................#...........................................
.#.................................................................................................................#........................
.......................................................................#....................................................................
...............#.............................................................................................................#..........#...
.................................#.............................#............................................#...............................
.....#.................#...................#................................................................................................
....................................................#...................................................#............#......................
...........#.....#...................................................................#............................................#.........
..............................................#...........................................................................#.................
...#.........................#.....................................................................#........................................
.........................................................#...................................#........................................#.....
.........#....................................................#........#................#.....................#.............................
........................#..........................................................................................#........................
..............#...................................#............................#.............................................#.....#........
.................................#................................................................#.........................................
..................#........................#...............#................................#.............#.............................#...
..........#........................................................#............................................................#...........
..#.....................................................................................#.............................#.....................
..........................#..........#..................................#......................................#...........#................
................................................................#...........................................................................
................#................................#..........................#...............................................................
...........................................#..................................................#.....#.......#...............................
..........#............................................#.....................................................................#..............
.......................#....................................#...........................................................#..............#....
.....#.........................#........#..............................................#.................#........................#.........
.................#....................................................#............................................#........................
....................................#...............#................................................#......................................
.........................#........................................#................#.......#...................#............................
....................................................................................................................................#.......
...........#...................................#...........................#......................#.........................#..............#
..................................#......#..................................................................................................
......#....................#.........................#..................................................#...................................
......................#...................................#......#.....#.................................................#..................
..............#..............................................................................#.................#.....................#......
............................................................................................................................................
#.............................#................#....................................................................#....................#..
............................................................................................................................................
........#...........................................#.......................................................................................
...................................................................#..........#..................#..........................................
.....................#............#........#.............................................#............#................#....................
................#............................................................................................................#..............
...............................................................................................................#...................#........
........................#......#..........................#.....#......#................................................................#...
................................................#..........................................#.............#..................................
......................................#..............................................................................#......................
..#.................................................................#.........#.............................................................
..........#.....#...............................................................................................#...........#...............
.................................#....................................................................#..............................#......
.....................................................#........................................#........................#....................
..........................................#..................#............#.................................................................
......................#...............................................................#..................#.........#............#...........
......#........................................................................#............................................................
...................................#...................................#..................................................#.................
...................................................#.........................................#.................#............................
...........................#...................................#.....................................................................#......
........................................#...................................................................................................
................#......................................#........................#.........#.....#...........................................
...........#......................#.....................................................................#...................................
....#....................#...................#...................#................................................#...........#...........#.
............................................................................................................................................
............................................................................................................................................
.....................................#....................................#.................................................................
.......................#..................#........#............................#................#.............#............................
...............#...............................................#......................#..............................................#......
............................................................................................................................................
.................................#...........#.....................#....................................................#...................
............................................................................................................................................
..#........#..........#...............#..................................................................#..........#......................#
............................................................#............................#..................................................
.................................................................#..........#.................................#.................#...........
.............................#......................#.......................................................................................
....#..................................................................................................................................#....
...................#...............#..................................................#....................#................................
.........................................................#......................................#...................#..............#........
.....................................................................#...................................................#..................
........................#...................................................................#..................#............................
...#.....#...............................#....................#.............................................................................
................#...............#...........................................................................................................
.....................#........................................................#.....................................................#.......
..............................................#.......#................#...............................................#...................#
.........................................................................................#...............#...................#..............
.#...........................#.......#......................................................................................................
.............................................................................................................#........................#.....
.................................#..........................................................................................................
...........#........................................................................................#.............................#.........
................#...............................................#............................#...................#..........................
...#............................................................................#...........................................................
....................................................#.......#.......#......#...........................................................#....
.........................#..................................................................................................................
....................#...............#.........................................................................................#.............
.........................................................#....................#......................#......................................
....#........................#...............#........................#...............#.....................................................
..........#......#....................................................................................................................#.....
..............................................................................................#...................#.........................
.......................................................#...................................................#.................#..............
..........................#....................#............................................................................................
........................................#......................#.........#...............#.......#......................#.........#.....#...
...............................#....................................#.......................................................................
........#...........#.............................#.........................................................................................
...#...........#...................................................................#..................#............#........................
...........................#..............................#...................................#.............................................
...................................#.............................#..........................................#...............................
..............................................#........................#........#..........................................#................
.......................................................................................#.............................#..............#.......
.........................................#..................................................................................................
.....#............#......................................#.....#............................#...............................................
............................#...............................................................................................................
.......................#.........#........................................#..............................#...............................#..
..#...........#.......................................#.........................#...........................................................
.......................................#.........................#..........................................................................
............................................................#...............................................................................
.......#......................#........................................#................................................#..............#....
..............................................................................................................#.............................
...............................................#.....................................................#......................................
......................#..................................................................#......#.................................#.......#.
..#.......#................#......#..................................#.......#.....................................#........................
................#...............................................#..................#....................#..................#................"""

# split_lines = """...#......
# .......#..
# #.........
# ..........
# ......#...
# .#........
# .........#
# ..........
# .......#..
# #...#....."""
split_lines = split_lines.split("\n")


set_index = set()
count = "1"
iter = 0
global_list = []
for line in range(len(split_lines)):
    x = 0
    local_list = []
    while x is not None:
        temp = split_lines[line]
        x = re.search("#", temp)
        
        if x is None:
            break
        #print(x.start(), len(temp), len(split_lines[line]))
        set_index.add(x.start())
        local_list.append(x.start())
        split_lines[line] = re.sub("#", count,temp,1)
    global_list.append(local_list)

l = list(set_index)
l.sort()
#print(l)
ll = [i for i in range(len(split_lines[0]))]
#print(ll)
set_all = set(ll)
final = list(set_all.difference(set_index))
final.sort()
print(final)

# count = "#"
# for line in range(len(split_lines)):
#     x = 0
#     local_list = []
#     while x is not None:
#         temp = split_lines[line]
#         x = re.search("1", temp)
        
#         if x is None:
#             break
#         #print(x.start(), len(temp), len(split_lines[line]))
#         #set_index.add(x.start())
#         local_list.append(x.start())
#         split_lines[line] = re.sub("1", count, temp, 1)
#         #count += 1
#     global_list.append(local_list)
#     #count = 0
# print((global_list))
# global_list = [
#     [2,10,20],[15,20,60],[],[35,80,100]
# ]

def sum_col(i, j):
    total_col = 0
    r = range(*sorted((i,j)))
    for k in final:
        if k in r:
            total_col += 1
    return total_col

answer = []
counter = 0
row = 0
extra_row = 0
while global_list != []:
    #while global_list[0] != []:
    while len(global_list) > 0 and len(global_list[0]) > 0:
        temp = global_list[0].pop(0)
        if global_list[0] == []:
            global_list.pop(0)
            extra_row += 1

        for j in global_list:
            
            for k in j:
                col = sum_col(temp, k)
                answer.append(abs(temp - k) + counter + row*(1) + col*(1) + extra_row)
            if j == []:
                row +=1
            #answer.append(abs(temp - k + counter) for k in j)
            counter += 1
        counter = 0
        row = 0
        col = 0
        extra_row = 0
    #global_list.pop(0)
    if len(global_list) > 0 and global_list[0] == []:
        global_list.pop(0)
    # if global_list == []:
    #     break
print(answer)
print(sum(answer))
print(global_list)


