#define a tree search algorithm using breadth first search
  #Override the traverse method of the TreeNode class

from collections import deque

#1. Search starts with two values : root node and target value
def level_search(root_node, val) :
#2. Create a queue to store the nodes to visit
  path_queue = deque() #self is the root node
  initial_path = [root_node]
  path_queue.append(initial_path)
  while len(path_queue) > 0 :
    path = path_queue.popleft()
    node = path[-1]
    if node.value == val :
      return node
    for child in node.children :
      new_path = list(path)
      new_path.append(child)
      path_queue.append(new_path)



