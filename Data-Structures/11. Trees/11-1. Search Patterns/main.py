from Breadth_First import level_search
from Depth_First import depth_search
from collections import deque

class TreeNode :
  def __init__(self, value) :
    self.value = value
    self.children = []
    self.parent = None

  #override the str method so that it returns the path 
  def __str__(self) :
    stack = deque()
    stack.append([self, 0]) #self is the root node. 0 is the level
    level_str = "\n"
    while len(stack) > 0 :
      node, level = stack.pop()
      #add the current node to the string
      if level > 0 :
        level_str += "\t" * level + "|__" + node.value + "\n"
      else :
        level_str += node.value + "\n"
      #add its children to the stack
      for child in node.children :
        stack.append([child, level + 1])
    return level_str

  def add_child(self, child_node) : 
    child_node.parent = self
    self.children.append(child_node)

  def remove_child(self, child_node) :
    self.children = [child for child in self.children if child is not child_node]
  
  def breadthFirst_search(self, val) :
    return level_search(self, val)

  def depthFirst_search(self, val) :
    path = depth_search(self, val)
    #print each value in the path
    for node in path :
      print(node.value)
      print("->")

sample_root_node = TreeNode("Home")
docs = TreeNode("Documents")
photos = TreeNode("Photos")
sample_root_node.children = [docs, photos]
my_wish = TreeNode("WishList.txt")
my_todo = TreeNode("TodoList.txt")
my_cat = TreeNode("Fluffy.jpg")
my_dog = TreeNode("Spot.jpg")
docs.children = [my_wish, my_todo]
photos.children = [my_cat, my_dog]

print(sample_root_node)
print(sample_root_node.breadthFirst_search("Photos"))
print(sample_root_node.depthFirst_search("Fluffy.jpg"))

# Seed = TreeNode("Shin")
# A = TreeNode("A")
# B = TreeNode("B")
# Seed.add_child(A)
# Seed.add_child(B) 
# A.add_child(TreeNode("C"))
# A.add_child(TreeNode("D"))
# B.add_child(TreeNode("E"))
# B.add_child(TreeNode("F"))
# print(Seed.breadthFirst_search("F"))


# print(Seed.depthFirst_search("E"))
