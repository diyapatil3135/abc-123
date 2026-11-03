from collections import deque

goal = (1, 2, 3, 4, 5, 6, 7, 8, 0)

moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def get_neighbors(state):
    neighbors = []
    zero = state.index(0)
    x, y = divmod(zero, 3)

    for dx, dy in moves:
        nx, ny = x + dx, y + dy
        if 0 <= nx < 3 and 0 <= ny < 3:
            new_position = nx * 3 + ny
            new_state = list(state)
            new_state[zero], new_state[new_position] = new_state[new_position], new_state[zero]
            neighbors.append(tuple(new_state))
    return neighbors


def bfs(start):
    queue = deque([(start, [])])
    visited = {start}

    while queue:
        state, path = queue.popleft()

        if state == goal:
            return path + [state]

        for neighbor in get_neighbors(state):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, path + [state]))

    return None


start = (1, 2, 3, 4, 5, 6, 7, 0, 8)
solution = bfs(start)

if solution:
    print("Solution found")
    for step in solution:
        print(step)
else:
    print("No solution found")