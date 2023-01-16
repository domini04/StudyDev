#Define a Tree Search algorithm using Depth First Search
  #Use Recursive method
from collections import deque


#1. Search starts with two values : root node and target value
def depth_search(root_node, val, path = []) :
#2. Create a stack to store the nodes to visit
  stack = deque()
  path = path + [root_node] #

  #base case
  if root_node.value == val :
    return path

  #recursive case
  for child in root_node.children :
    new_path = depth_search(child, val, path)
    if new_path : #if the new path is not None, meaning that the target value is found
      return new_path
  return None
    

