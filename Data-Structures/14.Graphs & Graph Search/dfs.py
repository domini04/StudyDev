#graph will be given as a dictionary of vertices
#ex) {'A': ['B', 'C'], 'B': ['A', 'C'], 'C': ['A', 'B', 'D'], 'D': ['C']}


def depth_first_search(graph, current_vertex, target_value, visited = None):
  #if visited is None, set visited to an empty set, and add the current vertex to the set
  if visited is None:
    visited = set()
  visited.add(current_vertex)

  #if the current vertex is the target value, return True
  if current_vertex == target_value:
    return visited
  
  #recursively call depth_first_search on each neighbor of the current vertex
  for neighbor in graph[current_vertex]:
    if neighbor not in visited:
      path = depth_first_search(graph, neighbor, target_value, visited)
      if path:
        return path
  #if there is no path, return False
  return False

# print(depth_first_search({'A': ['B', 'C'], 'B': ['A', 'C'], 'C': ['A', 'B', 'D'], 'D': ['C']}, 'A', 'D'))
    
    