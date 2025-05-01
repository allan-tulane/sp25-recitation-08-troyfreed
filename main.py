from collections import deque
from heapq import heappush, heappop 


def shortest_shortest_path(graph, source):
    """
    Efficiently computes the shortest paths from source to all other nodes,
    tracking both weight and number of edges.
    """
    heap = [(0, 0, source)]  # (total_weight, num_edges, current_node)
    visited = {}

    while heap:
        weight, edges, node = heapq.heappop(heap)
        print(f"heap: {heap}")
        print(f"weight: {weight}, node: {node}, edges: {edges}")
        print(f"vistited: {visited}")
        print("_____")
        if node in visited:
            prev_weight, prev_edges = visited[node]
            if weight > prev_weight or (weight == prev_weight and edges >= prev_edges):
                continue

        visited[node] = (weight, edges)

        for neighbor, w in graph.get(node, []):
            if neighbor not in visited or weight + w < visited[neighbor][0] or \
               (weight + w == visited[neighbor][0] and edges + 1 < visited[neighbor][1]):
                heapq.heappush(heap, (weight + w, edges + 1, neighbor))

    return print(visited)

    

    
    
def bfs_path(graph, source):
    """
    Returns:
      a dict where each key is a vertex and the value is the parent of 
      that vertex in the shortest path tree.
    """
    parents = {}
    visited = {source}
    queue = deque([source])

    while queue:
        u = queue.popleft()
        for v in graph[u]:
            if v not in visited:
                visited.add(v)
                parents[v] = u
                queue.append(v)
    return parents
    pass

def get_sample_graph():
     return {'s': {'a', 'b'},
            'a': {'b'},
            'b': {'c'},
            'c': {'a', 'd'},
            'd': {}
            }


    
def get_path(parents, destination):
    """
    Returns:
      The shortest path from the source node to this destination node 
      (excluding the destination node itself). See test_get_path for an example.
    """
    path_rev = []
    cur = destination
    # follow parent‐pointers back to the source
    while cur in parents:
        p = parents[cur]
        path_rev.append(p)
        cur = p
    # reverse to get source parent_of_destination
    path = list(reversed(path_rev))
    # concatenate
    return ''.join(path)
    pass

