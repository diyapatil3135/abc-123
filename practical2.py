environment = [
    [0,0,1,0],
    [1,0,1,0],
    [0,0,0,0],
    [0,1,0,0]
]

start = [0,0]
goal = [3,3]
internal_state = {}

while start != goal:
    x,y = start
    internal_state[(x,y)] = "visited"

    moves = [
        [0,1,"right"],
        [1,0,"down"],
        [0,-1,"left"],
        [-1,0,"up"]
    ]
    moved = False
    for dx, dy, action in moves:
        nx, ny = x+dx, y+dy
        if (0 <= nx < 4 and 0 <= ny < 4 and environment[nx][ny] == 0 and (nx,ny) not in internal_state):
            print("Moved")
            moved = True
            start = [nx,ny]
            break
    if not moved:
        print("No safe path found")
        break

if start == goal:
    print("Goal is reached")

print("Internal state: ",internal_state)
