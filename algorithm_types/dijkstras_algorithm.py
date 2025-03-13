# Shortest Path Algorithm
# Updates the shortest path as it goes

import heapq

def dijkstra_algorithm(graph, start):
    # Priority-Queue (min-heap)
    pq = [(0, start)]

    # Dictionary stores shortest known distance
    shortest_paths = {node: float('inf') for node in graph}
    shortest_paths[start] = 0

    while pq:
        current_distance, current_node = heapq.heappop(pq)

        # Continue if it is not shortest path
        if current_distance > shortest_paths[current_node]:
            continue

        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight

            # If there is a shorter path
            if distance < shortest_paths[neighbor]:
                shortest_paths[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))

    return shortest_paths

graph = {
    'A': {'B': 2, 'C': 5, 'D': 1},
    'B': {'A': 2, 'E': 3, 'F': 1},
    'C': {'A': 5, 'F': 2, 'G': 3},
    'D': {'A': 1, 'H': 4},
    'E': {'B': 3, 'I': 6},
    'F': {'B': 1, 'C': 2, 'J': 4},
    'G': {'C': 3, 'J': 5},
    'H': {'D': 4, 'I': 7},
    'I': {'E': 6, 'H': 7, 'J': 2},
    'J': {'F': 4, 'G': 5, 'I': 2}
}



# Algorithm runs from node "A"
shortest_paths = dijkstra_algorithm(graph, "A")

for node, distance in shortest_paths.items():
    print(f"Shortest path from A to {node}: {distance}")

# Shortest path from A to A: 0
# Shortest path from A to B: 2
# Shortest path from A to C: 5
# Shortest path from A to D: 1
# Shortest path from A to E: 5
# Shortest path from A to F: 3
# Shortest path from A to G: 8
# Shortest path from A to H: 5
# Shortest path from A to I: 9
# Shortest path from A to J: 7