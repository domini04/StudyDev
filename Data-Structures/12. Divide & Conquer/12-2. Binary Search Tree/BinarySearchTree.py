class BinarySearchTree :

  def __init__(self, value, depth = 1) :
    self.value = value
    self.depth = depth
    #left and right represent subtrees
    self.left = None
    self.right = None

  def insert(self, value) : #inserts a new node in the tree
    #같은 값 허용
    #value가 self.value보다 작으면 왼쪽에, 크면 오른쪽에 삽입. 자식이 있는 경우 자식의 자식으로 삽입
    if value < self.value : 
      if self.left is None :
        self.left = BinarySearchTree(value, self.depth + 1)
      else :
        self.left.insert(value)
    #value가 self.value보다 크거나 같으면 오른쪽에 삽입. 자식이 있는 경우 자식의 자식으로 삽입
    else :
      if self.right is None :
        self.right = BinarySearchTree(value, self.depth + 1)
      else :
        self.right.insert(value)
    
  def search(self, value) : #searches for a node in the tree
    #if current node matches the value, return current node
    if self.value == value :
      return self
    #if value is less than current node, search left subtree
    elif (value < self.value) and (self.left is not None) :
        return self.left.search(value)
    # if value is greater than current node, search right subtree
    elif (value > self.value) and (self.right is not None) :
        return self.right.search(value)
    #if value is not found, return None
    else :
      return None
  
  def depth_first_traversal(self):
    #use the in-order traversal method
      #left -> root -> right

    #1. if left subtree exists, traverse left subtree
    if self.left is not None :
      self.left.depth_first_traversal()
    #2. if left subtree does not exist, print root node
    print(self.value)
    #3. After printing root node, traverse right subtree
    if self.right is not None :
      self.right.depth_first_traversal()


tree = BinarySearchTree(48)
tree.insert(24)
tree.insert(55)
tree.insert(26)
tree.insert(38)
tree.insert(56)
tree.insert(74)

print(tree.search(26).depth) #3
print(tree.search(38).depth) #4

tree.depth_first_traversal()