import random
from random import randrange
from Graph import Graph
from Vertex import Vertex

def print_graph(graph):
  for vertex in graph.graph_dict:
    print("")
    print(vertex + " connected to")
    vertex_neighbors = graph.graph_dict[vertex].edges
    if len(vertex_neighbors) == 0:
      print("No edges!")
    for adjacent_vertex in vertex_neighbors:
      print("=> " + adjacent_vertex)

def build_tsp_graph(directed):
  g = Graph(directed)
  vertices = []
  for val in ['a', 'b', 'c', 'd']:
    vertex = Vertex(val)
    vertices.append(vertex)
    g.add_vertex(vertex)

  g.add_edge(vertices[0], vertices[1], 3)
  g.add_edge(vertices[0], vertices[2], 4)
  g.add_edge(vertices[0], vertices[3], 5)
  g.add_edge(vertices[1], vertices[0], 3)
  g.add_edge(vertices[1], vertices[2], 2)
  g.add_edge(vertices[1], vertices[3], 6)
  g.add_edge(vertices[2], vertices[0], 4)
  g.add_edge(vertices[2], vertices[1], 2)
  g.add_edge(vertices[2], vertices[3], 1)
  g.add_edge(vertices[3], vertices[0], 5)
  g.add_edge(vertices[3], vertices[1], 6)
  g.add_edge(vertices[3], vertices[2], 1)
  return g

def check_visited_all(visited):
  for vertex in visited:
    if not visited[vertex]: # if any vertex is False, meaning it is unvisited
      return False
  return True


def traveling_salesperson(graph):
  vertices_status = {x: False for x in graph.graph_dict}
  current_vertex = random.choice(list(graph.graph_dict.keys()))
  vertices_status[current_vertex] = True
  while not check_visited_all(vertices_status):
    cv_edges = graph.graph_dict[current_vertex].get_edges()
    cv_weights = [graph.graph_dict[current_vertex].edges[x] for x in cv_edges]
    next_vertex_found = False
    next_vertex = ""
    while not next_vertex_found:
      if cv_weights == []:
        break
      min_weight = min(cv_weights)
      min_weight_index = cv_weights.index(min_weight)
      next_vertex = cv_edges[min_weight_index]
      if not vertices_status[next_vertex]: # if the next vertex is unvisited, mark it as visited and move to it
        next_vertex_found = True
      else: # if the next vertex is visited, remove it from the list of edges and weights
        cv_edges.pop(min_weight_index)
        cv_weights.pop(min_weight_index)
    if next_vertex_found:
      print("Moving from " + current_vertex + " to " + next_vertex)
      current_vertex = next_vertex
      vertices_status[current_vertex] = True
    else:
      print("No more unvisited vertices")
      break
  print("All vertices visited")

g = build_tsp_graph(False)
print_graph(g)
print('-------------------------------')
traveling_salesperson(g)


