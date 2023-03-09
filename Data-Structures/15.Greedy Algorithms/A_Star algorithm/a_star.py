from math import inf
from heapq import heappop, heappush
from manhattan_graph import manhattan_graph, thirty_sixth_and_sixth, grand_central_station
from heuristic import m_heuristic


# A* algorithm
def a_star(graph, start, target):
    print("A* algorithm")
    count = 0 #a count to keep track of the number of iterations
    paths_and_distances = {vertex: [inf, [start.name]] for vertex in graph}

    paths_and_distances[start][0] = 0
    vertices_to_visit = [(0, start)]

    while vertices_to_visit and paths_and_distances[target][0] == inf: #paths_and_distances[target][0] == inf means that the target has not been reached yet. If the target has been reached, the while loop will stop
        current_distance, current_vertex = heappop(vertices_to_visit)
        for neighbor, weight in graph[current_vertex]:
            #total distance = current distance + weight of the edge + heuristic distance
            new_distance = current_distance + weight + m_heuristic(neighbor, target) #update the total distance to the neighbor
            new_path =  paths_and_distances[current_vertex][1] + [neighbor.name] #update the path to the neighbor
            if new_distance < paths_and_distances[neighbor][0]: #if the new distance is less than the current distance, update the distance and the path
                paths_and_distances[neighbor][0] = new_distance
                paths_and_distances[neighbor][1] = new_path
                heappush(vertices_to_visit, (new_distance, neighbor))
        count += 1
    print("Number of iterations: " + str(count))
    return paths_and_distances[target][1]

print(a_star(manhattan_graph, thirty_sixth_and_sixth, grand_central_station))
