class Vertex :
  def __init__(self, value) :
    self.value = value
    self.edges = {} #store the vertices that are connected to this vertex
    
  def get_edges(self): #return a list of all the edges
    return list(self.edges.keys())

  def add_edges(self, vertex, weight : int = 0) :
    print(f'Adding edge from {self.value} to {vertex} with weight {weight}')
    self.edges[vertex] = weight

