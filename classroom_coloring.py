import networkx as nx
import matplotlib.pyplot as plt

# Define the graph (Classroom seating as adjacency list)
graph = {
    'A': ['B', 'D'],
    'B': ['A', 'C', 'E'],
    'C': ['B', 'F'],
    'D': ['A', 'E', 'G'],
    'E': ['B', 'D', 'F', 'H'],
    'F': ['C', 'E', 'I'],
    'G': ['D', 'H'],
    'H': ['E', 'G', 'I'],
    'I': ['F', 'H']
}

# Available color palette (extendable if needed)
color_palette = ['red', 'green', 'blue', 'yellow', 'orange', 'purple', 'cyan', 'brown']

# Greedy coloring algorithm
def greedy_coloring(graph):
    color_assignment = {}
    for node in graph:
        # Collect used colors from adjacent nodes
        used_colors = {color_assignment.get(neigh) for neigh in graph[node] if neigh in color_assignment}
        # Assign the lowest unused color
        for color in color_palette:
            if color not in used_colors:
                color_assignment[node] = color
                break
    return color_assignment

# Apply the greedy coloring
coloring_result = greedy_coloring(graph)

# Create a graph using NetworkX
G = nx.Graph()
for node, neighbors in graph.items():
    for neighbor in neighbors:
        G.add_edge(node, neighbor)

# Prepare node colors from coloring result
node_colors = [coloring_result[node] for node in G.nodes()]

# Set positions manually to mimic a 3x3 classroom seating grid
positions = {
    'A': (0, 2),
    'B': (1, 2),
    'C': (2, 2),
    'D': (0, 1),
    'E': (1, 1),
    'F': (2, 1),
    'G': (0, 0),
    'H': (1, 0),
    'I': (2, 0)
}

# Plotting the graph
plt.figure(figsize=(8, 6))
nx.draw(G, pos=positions, with_labels=True, node_color=node_colors,
        node_size=1200, font_size=14, font_weight='bold')
plt.title("Classroom Seating Plan - Greedy Coloring", fontsize=16)
plt.axis('off')
plt.show()

# Print the color assignment
print("Seat : Assigned Color")
for seat, color in coloring_result.items():
    print(f"{seat} : {color}")
