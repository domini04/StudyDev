#Define a Tree Search algorithm using Depth First Search
  #Use Recursive method
from collections import deque

#1. Search starts with two values : root node and target value
def depth_search(root_node, val) :
#2. Create a stack to store the nodes to visit
  stack = deque()
#3. Add the root node to the stack
  stack.append(root_node)
  while len(stack) > 0 :
    node = stack.pop()
    if node.value == val :
      return node
    else :
      for child in node.children :
        stack.append(child)
  return None
    

