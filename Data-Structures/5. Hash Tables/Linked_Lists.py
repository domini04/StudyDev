class Node:
  def __init__(self, value):
    self.value = value
    self.next_node = None
    
  def get_value(self):
    return self.value
  
  def get_next_node(self):
    return self.next_node
  
  def set_next_node(self, next_node):
    self.next_node = next_node

class LinkedList:
  def __init__(self, head_node=None):
    self.head_node = head_node
  
  def insert(self, new_node): #Linked List의 head node를 추가하는 메서드
    current_node = self.head_node

    if not current_node:
      self.head_node = new_node

    while(current_node):
      next_node = current_node.get_next_node()
      if not next_node:
        current_node.set_next_node(new_node)
      current_node = next_node

  def __iter__(self): #iterable하게 만들어주는 메서드
    current_node = self.head_node
    while(current_node):  #current node가 None이 아닐 때까지 반복
      yield current_node.get_value()  #current node의 value를 반환
      current_node = current_node.get_next_node() #current node를 다음 node로 지정