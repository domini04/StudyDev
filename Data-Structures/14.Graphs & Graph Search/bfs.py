def breadth_first_search(graph, start_vertex, target_value):
  visited = set()
  path = [start_vertex]
  vertex_and_path = [start_vertex, path] #this is a list of the current vertex and the path to get to it
  queue = [vertex_and_path] #this is a queue of lists of the current vertex and the path to get to it.

  #while queue is not empty
  while queue:
    #check the current vertex_and_path and mark it as visited
    current, path = queue.pop(0)
    visited.add(current)

    #if the current vertex is the target value, return the path
    if current == target_value:
      return path
    #add the neighbors of the current vertex to the queue
    for neighbor in graph[current]:
      if neighbor not in visited:
        queue.append([neighbor, path + [neighbor]])
  #if there is no path, return False
  return False


# print(breadth_first_search({'A': ['B', 'C'], 'B': ['A', 'C'], 'C': ['A', 'B', 'D'], 'D': ['C']}, 'A', 'D'))