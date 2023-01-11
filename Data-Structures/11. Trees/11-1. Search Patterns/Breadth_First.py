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
    path = path_queue.popleft() #get the first path in the queue
    node = path[-1] #get the last node in the path and check if it is the target
    if node.value == val :
      return node
    #if not, add the children of the node(path) to the queue
    for child in node.children : 
      new_path = list(path) 
      new_path.append(child)
      path_queue.append(new_path)
    #ex) if the path is [A, B, C] and C has two children, D and E, then the queue will have [A, B, C, D] and [A, B, C, E]
  return None



