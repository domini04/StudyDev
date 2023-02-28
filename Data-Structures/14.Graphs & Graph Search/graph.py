from vertex import Vertex
class Graph :
  def __init__(self, directed=False) :
    self.graph_dict = {}
    self.directed = directed

  def add_vertex(self, vertex: Vertex) :
    self.graph_dict[vertex.value] = vertex

  def add_edge(self, from_vertex: Vertex, to_vertex: Vertex, weight=0) :
    self.graph_dict[from_vertex.value].add_edges(to_vertex.value, weight) #add the edge using the Vertex class method
    if not self.directed : #if undirected, add the reverse edge
      self.graph_dict[to_vertex.value].add_edges(from_vertex.value, weight)

  def find_all_paths(self, start_vertex: Vertex, end_vertex: Vertex) :
    #find all the paths from start_vertex to end_vertex in graph
    print(f'Finding path from {start_vertex.value} to {end_vertex.value}')
    #use DFS to find all the paths
    stack = [(start_vertex.value, [start_vertex.value])] #create a stack to store the nodes to visit. 
    path=[] #create a list to store the path
    seen = set() #create a set to store the nodes that have been visited
      

    while stack :
      (vertex, path) = stack.pop()
      if vertex not in seen : #if the vertex has not been visited, add the vertex to the set of visited vertices
        seen.add(vertex) 

      for next in set(self.graph_dict[vertex].edges) - set(path) :
          #set(self.graph_dict[vertex].edges) : get all the connected vertices of the current vertex
          #set(path) : get all the vertices in the current path
          #set(self.graph_dict[vertex].edges) - set(path) : get all the vertices that are connected to the current vertex but not in the current path
            #ex) if the current vertex has edges to A, B, C, D and the current path is A -> B -> C, then the next vertex to visit is D
        if next == end_vertex.value : #if the next vertex is the end vertex, then we have found a path
          yield path + [next]
        else :  #if not, then add the next vertex to the stack
          stack.append((next, path + [next]))
    #if there is no path, return an empty list
    if not path[-1] == end_vertex.value :
      print('No path found')
      return []
    

  def find_shortest_path(self, start_vertex: Vertex, end_vertex: Vertex) :
    #find the shortest path from start_vertex to end_vertex in graph
    #use find_all_paths to find all the paths
    #return the path with the least weight
    print(f'Finding shortest path from {start_vertex.value} to {end_vertex.value}')
    all_paths = self.find_all_paths(start_vertex, end_vertex)
    lengths = []
    for path in  all_paths:
      weight_sum = 0
      #each path is a list of vertices
      #ex) ['callan', 'peel', 'harwick']
      #find the weight of each edge in the path
      for i in range(len(path) - 1) :
        weight_sum += self.graph_dict[path[i]].edges[path[i+1]]
      #add the weight of the path to the list
      lengths.append(weight_sum)
    #return the path with the least weight
    min_weight = min(lengths)
    min_index = lengths.index(min_weight)
    return list(self.find_all_paths(start_vertex, end_vertex))[min_index], min_weight
    
