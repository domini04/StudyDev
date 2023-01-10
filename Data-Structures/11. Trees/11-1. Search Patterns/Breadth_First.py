#define a tree search algorithm using breadth first search
  #Override the traverse method of the TreeNode class

class TreeNode :
  def __init__(self, value) :
    self.value = value
    self.children = []
    self.parent = None

  def add_child(self, child_node) : 
    child_node.parent = self
    self.children.append(child_node)

  def remove_child(self, child_node) :
    self.children = [child for child in self.children if child is not child_node]

  #1. Search starts with two values : root node and target value
  def level_search(self, val) :
  #2. Create a queue to store the nodes to visit
    nodes_to_visit = [self] #self is the root node
    while len(nodes_to_visit) > 0 : 
      current_node = nodes_to_visit.pop(0)
      if current_node.value == val :
        return current_node
      # Add the children of the current node to the queue
      nodes_to_visit += current_node.children
    return None

Seed = TreeNode("Shin")
A = TreeNode("A")
B = TreeNode("B")
Seed.add_child(A)
Seed.add_child(B)
A.add_child(TreeNode("C"))
A.add_child(TreeNode("D"))
B.add_child(TreeNode("E"))
B.add_child(TreeNode("F"))
print(Seed.level_search("F").value)


