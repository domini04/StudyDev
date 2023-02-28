from graph_search import bfs, dfs
from vc_metro import vc_metro
from vc_landmarks import vc_landmarks
from landmark_choices import landmark_choices

# Vancouver’s public metro system has asked you to help create a program to help commuters get from one landmark to another. 
# You’ll be building out “SkyRoute,” a routing tool that uses breadth-first search, depth-first search, and Python dictionaries to accomplish this feat. 
# For the purposes of this project, you can assume that it takes the same amount of time to get from each station to each of its connected neighboring stations.

landmark_string = ""
for letter, landmark in landmark_choices.items():
  landmark_string += "{0} - {1}\n".format(letter, landmark)
# print(landmark_string)

def greet():
  print("Hi there and welcome to SkyRoute!")
  print("We'll help you find the shortest route between the following Vancouver landmarks:\n" + landmark_string)

def skyroute():
  greet()
  new_route()
  goodbye()

def set_start_and_end(start_point, end_point): 
  if start_point:
    start_point = landmark_choices[start_point]
  else:
    start_point = get_start()
  if end_point:
    end_point = landmark_choices[end_point]
  else:
    end_point = get_end()
  return start_point, end_point

def get_start():
  start_point_letter = input("Where are you coming from? Type in the corresponding letter: ")
  if start_point_letter in landmark_choices:
    start_point = landmark_choices[start_point_letter]
  else:
    print("Sorry, that's not a landmark we have data on. Let's try this again...")
    return get_start()
  return start_point

def get_end():
  end_point_letter = input("Ok, where are you headed? Type in the corresponding letter: ")
  if end_point_letter in landmark_choices:
    end_point = landmark_choices[end_point_letter]
  else:
    print("Sorry, that's not a landmark we have data on. Let's try this again...")
    return get_end()
  return end_point

def new_route(start_point = None, end_point = None):
  start_point, end_point = set_start_and_end(start_point, end_point)
  shortest_route = get_route(start_point, end_point)
  if shortest_route:
    shortest_route_string = '\n'.join(shortest_route)
    print("The shortest metro route from {0} to {1} is:\n{2}".format(start_point, end_point, shortest_route_string))
  else:
    print("Unfortunately, there is currently no path between {0} and {1} due to maintenance.".format(start_point, end_point))
  again = input("Would you like to see another route? Enter y/n: ")
  if again == "y":
    show_landmarks()
    new_route(start_point, end_point)

def get_route(start_point, end_point):
  start_stations = vc_landmarks[start_point]
  end_stations = vc_landmarks[end_point]
  routes = []
  for start_station in start_stations:
    for end_station in end_stations:
      if end_station in start_stations:  # If the end station is in the list of connected stations for the start station,
        route = [start_station, end_station] # then the route is just the start and end stations
        routes.append(route)
      else:  # Otherwise, we'll need to use BFS to find the shortest path between the start and end stations
        route = bfs(vc_metro, start_station, end_station)
        if route:
          routes.append(route)
  shortest_route = min(routes, key=len)  # key=len means that we're sorting by the length of each route
  return shortest_route

def show_landmarks():
  see_landmarks = input("Would you like to see the list of landmarks again? Enter y/n: ")
  if see_landmarks == "y":
    print(landmark_string)

def goodbye():
  print("Thanks for using SkyRoute!")


skyroute()
