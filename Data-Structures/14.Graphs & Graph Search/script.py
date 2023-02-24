from vertex import Vertex
from graph import Graph

railway = Graph()

callan = Vertex('callan')
peel = Vertex('peel')
harwick = Vertex('harwick')

railway.add_vertex(callan)
railway.add_vertex(peel)
railway.add_vertex(harwick)


railway.add_edge(callan, peel, 1)
railway.add_edge(harwick, callan, 7)
railway.add_edge(peel, harwick, 8)

# print(callan.edges)
# print(harwick.edges)
# print(peel.edges)

for path in railway.find_all_paths(callan, harwick) :
  print(path)


print(railway.find_shortest_path(callan, harwick))