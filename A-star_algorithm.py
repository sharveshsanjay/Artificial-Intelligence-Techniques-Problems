import heapq


def manhattan_distance(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def a_star_search(start, goal, graph):
    open_list = []
    heapq.heappush(open_list, (0, start))  # (f, node)

    came_from = {}
    g_score = {node: float('inf') for node in graph}
    g_score[start] = 0

    f_score = {node: float('inf') for node in graph}
    f_score[start] = manhattan_distance(start, goal)

    while open_list:
        current_f, current = heapq.heappop(open_list)

        if current == goal:
            # Reconstruct path
            path = []
            total_cost = g_score[goal]

            while current in came_from:
                path.append(current)
                current = came_from[current]

            path.append(start)
            path.reverse()
            return path, total_cost

        for neighbor, cost in graph[current]:
            tentative_g = g_score[current] + cost
            if tentative_g < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g
                f_score[neighbor] = tentative_g + manhattan_distance(neighbor, goal)
                heapq.heappush(open_list, (f_score[neighbor], neighbor))

    return None, float('inf')


# Sample Input
graph = {
    (0, 0): [((1, 0), 1), ((0, 1), 4)],
    (1, 0): [((0, 0), 1), ((1, 1), 2)],
    (0, 1): [((0, 0), 4), ((1, 1), 3)],
    (1, 1): [((1, 0), 2), ((0, 1), 3), ((2, 1), 1)],
    (2, 1): [((1, 1), 1), ((2, 2), 2)],
    (2, 2): [((2, 1), 2)]
}

start = (0, 0)
goal = (2, 2)

path, cost = a_star_search(start, goal, graph)

print("Optimal Path:", path)
print("Total Cost:", cost)
