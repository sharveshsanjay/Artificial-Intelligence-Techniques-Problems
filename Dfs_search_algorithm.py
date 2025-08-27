# Graph for DFS using stack (recursive simulation)
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['G'],
    'F': [],
    'G': []
}

visited_dfs = set()
stack = []


def dfs_stack_recursive():
    if not stack:
        return

    current = stack[-1]
    unvisited_found = False

    for neighbor in graph[current]:
        if neighbor not in visited_dfs:
            visited_dfs.add(neighbor)
            print(neighbor, end=' ')
            stack.append(neighbor)
            unvisited_found = True
            break

    if not unvisited_found:
        stack.pop()

    dfs_stack_recursive()


# Run DFS traversal
start_node_dfs = 'A'
visited_dfs.add(start_node_dfs)
stack.append(start_node_dfs)

print("\nDFS Traversal Output:")
print(start_node_dfs, end=' ')
dfs_stack_recursive()


# ---------------------------
# DFS in a forest grid
def dfs_forest(grid, x, y, visited, path):
    rows, cols = len(grid), len(grid[0])

    # Boundary and obstacle check
    if (
        x < 0 or y < 0 or x >= rows or y >= cols
        or grid[x][y] == 'X' or visited[x][y]
    ):
        return False

    path.append((x, y))
    visited[x][y] = True

    if grid[x][y] == 'H':  # Found hotspot
        return True

    # Move in 4 directions
    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        if dfs_forest(grid, x + dx, y + dy, visited, path):
            return True

    # Backtrack if dead end
    path.pop()
    return False


# Forest grid
forest = [
    ['S', 'O', 'X', 'O'],
    ['X', 'O', 'X', 'O'],
    ['O', 'O', 'O', 'H'],
    ['X', 'X', 'O', 'X']
]

rows, cols = len(forest), len(forest[0])
visited = [[False for _ in range(cols)] for _ in range(rows)]
path = []

# Find start point 'S'
for i in range(rows):
    for j in range(cols):
        if forest[i][j] == 'S':
            start_x, start_y = i, j

# Run DFS on forest
found = dfs_forest(forest, start_x, start_y, visited, path)

if found:
    print("\nPath to hotspot:", path)
else:
    print("\nNo hotspot found.")
