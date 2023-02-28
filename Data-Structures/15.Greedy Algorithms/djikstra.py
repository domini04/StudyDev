#Djikstra's Algorithm
#Djikstra's Algorithm is a greedy algorithm that finds the shortest path between two nodes in a graph.
#It utilizes a heap to keep track of the closest unvisited node to the starting node.

#1. Create a dictionary of distances from the starting node to all other nodes in the graph.
#2. Create a heap of all the nodes in the graph.
#3. set the distance of the starting node to 0.
#4. set the distance of all other nodes to infinity.
#5. pop the closest node from the heap.
  #a. if the node is the end node, return the distance of the end node.
  #b. if the node is not the end node, update the distance of all of its neighbors.
    #i. if new_distance < old_distance, update the distance of the neighbor.
    #ii. push the neighbor onto the heap.
#6. repeat steps 5 until the heap is empty.

from heapq import heappush, heappop
from math import inf

# ex) graph = graph = { 'A' : [('B', 10), ('C', 3)], 'B' : [('C', 1), ('D', 2)], 'C' : [('B', 4), ('D', 8), ('E', 2)], 'D' : [('E', 7)], 'E' : [('D', 9)]


def dijkstra(graph, start, end):
  #distances :  a dictionary of distances from the start node to all other nodes in the graph
  distances = {node: inf for node in graph}
  distances[start] = 0
  # print(distances)
  heap = []
  heappush(heap, [distances[start], start]) #push the starting node onto the heap
  while heap:
    current_distance, current_node = heappop(heap) 
    # print(current_distance, current_node)
    if current_node == end:
      return current_distance
    for neighbor, weight in graph[current_node]:
      new_distance = current_distance + weight
      if new_distance < distances[neighbor]:
        distances[neighbor] = new_distance
        heappush(heap, [new_distance, neighbor])
  return distances

graph = { 'A' : [('B', 10), ('C', 3)], 'B' : [('C', 1), ('D', 2)], 'C' : [('B', 4), ('D', 8), ('E', 2)], 'D' : [('E', 7)], 'E' : [('D', 9)]}
print(dijkstra(graph, 'A', 'E'))
