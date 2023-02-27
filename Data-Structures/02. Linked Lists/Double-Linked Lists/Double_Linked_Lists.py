class Node:
  def __init__(self, value, next_node=None, prev_node=None):
    self.value = value
    self.next_node = next_node
    self.prev_node = prev_node
    
  def set_next_node(self, next_node):
    self.next_node = next_node
    
  def get_next_node(self):
    return self.next_node

  def set_prev_node(self, prev_node):
    self.prev_node = prev_node
    
  def get_prev_node(self):
    return self.prev_node
  
  def get_value(self):
    return self.value
    

class DoublyLinkedList:
  def __init__(self):
    self.head_node = None
    self.tail_node = None
  
  def add_to_head(self, new_value):
    new_head = Node(new_value)
    current_head = self.head_node

    if current_head != None:
      current_head.set_prev_node(new_head)
      new_head.set_next_node(current_head)

    self.head_node = new_head

    if self.tail_node == None:
      self.tail_node = new_head

  def add_to_tail(self, new_value):
    new_tail = Node(new_value)
    current_tail = self.tail_node

    if current_tail != None:
      current_tail.set_next_node(new_tail)
      new_tail.set_prev_node(current_tail)

    self.tail_node = new_tail

    if self.head_node == None:
      self.head_node = new_tail

  def remove_head(self):
    removed_head = self.head_node

    if removed_head == None:
      return None

    self.head_node = removed_head.get_next_node()

    if self.head_node != None:
      self.head_node.set_prev_node(None)

    if removed_head == self.tail_node:
      self.remove_tail()

    return removed_head.get_value()

  def remove_tail(self):
    removed_tail = self.tail_node
    if removed_tail == None:
      return None

    else:
      self.tail_node = removed_tail.get_prev_node() 
      if self.tail_node != None:
        self.tail_node.set_next_node(None)

    if removed_tail == self.head_node:  # 삭제한 tail이 head와 같다면 -> 이제 head가 없다는 뜻
      self.remove_head()
    return removed_tail.get_value()

  def remove_by_value(self, value_to_remove): # value를 기준으로 삭제
    #Iterate through the list to find the matching node
    node_to_remove = None
    current_node = self.head_node
    while current_node != None: # current_node가 None이 아닐 때까지 반복  
      if current_node.get_value() == value_to_remove: # current_node iterate하면서 value_to_remove와 같은 값이 나오면 loop 탈출
        node_to_remove = current_node
        break
      current_node = current_node.get_next_node()
    if node_to_remove == None:   #If there is no matching element in the list: Return None
      return None
    if node_to_remove == self.head_node:  #If the matching element is the head node: Call remove_head()
      self.remove_head()
    elif node_to_remove == self.tail_node:  #If the matching element is the tail node: Call remove_tail()
      self.remove_tail()
    else: #If there is a matching element in the list & head/tail이 아닌 경우: Remove it
      next_node = node_to_remove.get_next_node()
      prev_node = node_to_remove.get_prev_node()
      next_node.set_prev_node(prev_node)
      prev_node.set_next_node(next_node)
    return node_to_remove

  def stringify_list(self): # Linked List의 값들을 문자열로 반환하는 메서드
    string_list = ""
    current_node = self.head_node
    while current_node != None:
      if current_node.get_value() != None:
        string_list += str(current_node.get_value()) + "\t" "->\t"
      current_node = current_node.get_next_node()
    return string_list

# Create your subway line here:
subway = DoublyLinkedList()
subway.add_to_head("Times Square")
subway.add_to_head("Grand Central")
subway.add_to_head("Central Park")

# print(subway.stringify_list())
subway.add_to_tail("Penn Station")
subway.add_to_tail("Wall Street")
subway.add_to_tail("Brooklyn Bridge")
# print(subway.stringify_list())
subway.remove_head()
subway.remove_tail()
# print(subway.stringify_list())
subway.remove_by_value("Times Square")
print(subway.stringify_list())