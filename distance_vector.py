import heapq

# Define the network graph
network = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}

# Dijkstra's Algorithm
def dijkstra(start, graph):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))
    
    return distances

# Simulate for each router
for router in network:
    print(f"Shortest paths from Router {router}:")
    shortest_paths = dijkstra(router, network)
    for destination, cost in shortest_paths.items():
        print(f"  To {destination}: {cost} units")
    print()
