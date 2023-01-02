# I. Basic Tree
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

  def traverse(self) :
    nodes_to_visit = [self]
    while len(nodes_to_visit) > 0 :
      current_node = nodes_to_visit.pop()
      print(current_node.value)
      nodes_to_visit += current_node.children


# II. Binary Tree
# class TreeNode :
#     def __init__(self, val):
#         print("TreeNode.__init__({0})".format(val))
#         self.val = val
#         self.left = None
#         self.right = None

#     def add_child (self, child_node):
#         print("TreeNode.add_child({0})".format(child_node.val))
#         #자신보다 작으면 왼쪽, 크면 오른쪽에 추가
#         #만약 자식이 있으면 자식에게 위임
#         if child_node.val < self.val: 
#             if self.left: # if left node exists
#                 self.left.add_child(child_node)
#             else:
#                 self.left = child_node
#         else:
#             if self.right:
#                 self.right.add_child(child_node)
#             else:
#                 self.right = child_node
# Seed = TreeNode("Shin")