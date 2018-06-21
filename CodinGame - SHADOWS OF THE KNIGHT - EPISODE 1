import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

# w: width of the building.
# h: height of the building.
w, h = [int(i) for i in input().split()]
n = int(input())  # maximum number of turns before game over.
x0, y0 = [int(i) for i in input().split()]
top = 0
bottom =h-1
left = 0
right = w-1
# game loop

while True:
    bomb_dir = input()  # the direction of the bombs from batman's current location (U, UR, R, DR, D, DL, L or UL)  
    if bomb_dir == "U":
        bottom = y0-1

    elif bomb_dir == "UR":
        bottom = y0-1
        left = x0+1
    elif bomb_dir == "R":
        left = x0+1

    elif bomb_dir == "DR":
        top = y0+1
        left = x0+1
    elif bomb_dir == "D":
        top = y0+1

    elif bomb_dir == "DL":
        top = y0+1
        right = x0-1
    elif bomb_dir == "L":
        right = x0-1

    elif bomb_dir == "UL":
        bottom = y0-1
        right = x0 - 1
    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr)
    print("bottom",bottom, file=sys.stderr)
    print("top",top, file=sys.stderr)
    print("left",left, file=sys.stderr)
    print("right",right, file=sys.stderr)
    
    x0 = (left+right)//2
    y0 = (top+bottom)//2
    print(x0,y0)

    # the location of the next window Batman should jump to.
    
