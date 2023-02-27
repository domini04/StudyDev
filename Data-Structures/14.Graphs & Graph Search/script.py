from vertex import Vertex
from graph import Graph

railway = Graph()

callan = Vertex('callan')
peel = Vertex('peel')
ulfstead = Vertex('ulfstead')
harwick = Vertex('harwick')

railway.add_vertex(callan)
railway.add_vertex(peel)
railway.add_vertex(harwick)
railway.add_vertex(ulfstead)

railway.add_edge(peel, harwick)
railway.add_edge(harwick, callan)
railway.add_edge(callan, peel)

print()

# print(callan.edges)
# print(harwick.edges)
# print(peel.edges)

for path in railway.find_all_paths(callan, harwick) :
  print(path)

print()

#case where there is no path
for path in railway.find_all_paths(callan, ulfstead) :
  print(path)


print()

print(railway.find_shortest_path(callan, harwick))