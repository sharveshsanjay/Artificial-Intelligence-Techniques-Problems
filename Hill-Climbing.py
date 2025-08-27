import random

# Sample 2D grid (5x6)
warehouse = [
    ['S', 'O', 'O', 'X', 'O', 'O'],
    ['X', 'X', 'O', 'X', 'O', 'X'],
    ['O', 'O', 'O', 'O', 'O', 'O'],
    ['O', 'X', 'X', 'X', 'X', 'O'],
    ['O', 'O', 'O', 'O', 'G', 'O']
]


# Find start/goal positions
def find_position(grid, char):
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == char:
                return (i, j)


start = find_position(warehouse, 'S')
goal = find_position(warehouse, 'G')


# Manhattan distance heuristic
def heuristic(pos, goal):
    return abs(pos[0] - goal[0]) + abs(pos[1] - goal[1])


# Valid neighbors (up, down, left, right)
def get_neighbors(grid, position):
    x, y = position
    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    neighbors = []

    for dx, dy in moves:
        nx, ny = x + dx, y + dy
        if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]):
            if grid[nx][ny] in ['O', 'G']:  # walkable
                neighbors.append((nx, ny))

    return neighbors


# Hill Climbing Algorithm
def hill_climbing(grid, start, goal):
    current = start
    path = [current]

    while current != goal:
        neighbors = get_neighbors(grid, current)

        if not neighbors:
            print("Stuck at local maximum. No path to goal.")
            return path

        next_move = min(neighbors, key=lambda n: heuristic(n, goal))

        if heuristic(next_move, goal) >= heuristic(current, goal):
            print("Reached local maximum. Cannot improve further.")
            return path

        current = next_move
        path.append(current)

    return path


# Run the algorithm
path = hill_climbing(warehouse, start, goal)

# Print path
print("\nPath found:")
for step in path:
    print(step)
