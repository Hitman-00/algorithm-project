# **Implementation of Counting Sort Algorithm**

def counting_sort(arr):
    # Find the maximum value in the array
    max_val = max(arr)
    min_val = min(arr)
    range_of_elements = max_val - min_val + 1

    # Initialize the count array
    count = [0] * range_of_elements

    # Store the count of each element
    for num in arr:
        count[num - min_val] += 1

    # Update the count array to store cumulative counts
    for i in range(1, len(count)):
        count[i] += count[i - 1]

    # Output array to store the sorted elements
    output = [0] * len(arr)
    for num in reversed(arr):
        output[count[num - min_val] - 1] = num
        count[num - min_val] -= 1

    return output

# Example usage for Counting Sort:
arr = [4, 2, 2, 8, 3, 3, 1]
print("Sorted Array (Counting Sort):", counting_sort(arr))

# **Implementation of Prim's Algorithm**
import heapq

def prim_mst(graph):
    # Number of vertices in the graph
    n = len(graph)

    # Array to keep track of visited nodes
    visited = [False] * n

    # Priority queue for selecting the edge with minimum weight
    pq = []

    # Start from vertex 0
    heapq.heappush(pq, (0, 0))  # (weight, vertex)

    # Total weight of the MST
    mst_weight = 0

    # MST edges
    mst_edges = []

    while pq:
        weight, u = heapq.heappop(pq)

        if visited[u]:
            continue

        # Mark the vertex as visited
        visited[u] = True

        # Add the weight to the MST
        mst_weight += weight

        # Add the edge to the MST edges (optional, for visualization)
        if weight != 0:
            mst_edges.append((u, weight))

        # Explore the neighbors of the current vertex
        for v, w in graph[u]:
            if not visited[v]:
                heapq.heappush(pq, (w, v))

    return mst_weight, mst_edges

# Example graph as adjacency list
example_graph = [
    [(1, 2), (3, 6)],        # Node 0: (Node 1, Weight 2), (Node 3, Weight 6)
    [(0, 2), (2, 3), (3, 8)], # Node 1: (Node 0, Weight 2), ...
    [(1, 3), (3, 7)],        # Node 2: ...
    [(0, 6), (1, 8), (2, 7)] # Node 3: ...
]

mst_weight, mst_edges = prim_mst(example_graph)
print("MST Weight:", mst_weight)
print("MST Edges:", mst_edges)
