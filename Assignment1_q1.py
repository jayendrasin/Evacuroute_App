# Building Evacuation System using Graphs
# BFS Algorithm for Shortest Safe Path

from collections import deque

# -------------------------------
# Building Graph (Adjacency List)
# -------------------------------

building = {
    "Room 101": ["Hallway A"],
    "Room 102": ["Hallway A"],
    "Room 103": ["Hallway B"],
    "Hallway A": ["Room 101", "Room 102", "Corridor"],
    "Hallway B": ["Room 103", "Corridor"],
    "Corridor": ["Hallway A", "Hallway B", "Staircase"],
    "Staircase": ["Corridor", "Exit A"],
    "Exit A": ["Staircase"]
}

# Exit nodes
exits = ["Exit A"]

# -------------------------------
# BFS Function
# -------------------------------

def bfs_safe_path(graph, start, blocked_nodes, exits):

    queue = deque([(start, [start])])
    visited = set()

    while queue:
        current, path = queue.popleft()

        if current in visited:
            continue

        visited.add(current)

        # If exit found
        if current in exits:
            return path

        # Visit neighbors
        for neighbor in graph[current]:
            if neighbor not in visited and neighbor not in blocked_nodes:
                queue.append((neighbor, path + [neighbor]))

    return None


# -------------------------------
# User Input
# -------------------------------

current_location = input("Enter Current Location: ")
fire_location = input("Enter Fire/Blocked Location: ")

blocked_nodes = [fire_location]

# -------------------------------
# Find Safe Route
# -------------------------------

safe_path = bfs_safe_path(
    building,
    current_location,
    blocked_nodes,
    exits
)

# -------------------------------
# Output
# -------------------------------

print("\n===== EVACUATION REPORT =====")

print("Current Location :", current_location)
print("Blocked/Fire Node :", fire_location)

if safe_path:
    print("\nSafe Route:")
    print(" -> ".join(safe_path))

    print("\nTotal Distance :", len(safe_path) - 1, "steps")

else:
    print("\nNo Safe Path Available!")


# -------------------------------
# OPTIONAL GRAPH VISUALIZATION
# -------------------------------

import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()

# Add edges
for node in building:
    for neighbor in building[node]:
        G.add_edge(node, neighbor)

# Node colors
node_colors = []

for node in G.nodes():
    if node == fire_location:
        node_colors.append("red")
    elif node in exits:
        node_colors.append("green")
    elif safe_path and node in safe_path:
        node_colors.append("skyblue")
    else:
        node_colors.append("lightgray")

# Draw graph
plt.figure(figsize=(10, 7))

pos = nx.spring_layout(G, seed=42)

nx.draw(
    G,
    pos,
    with_labels=True,
    node_color=node_colors,
    node_size=2500,
    font_size=9,
    font_weight="bold"
)

plt.title("Building Evacuation Graph")
plt.show()