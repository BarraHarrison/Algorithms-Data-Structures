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


