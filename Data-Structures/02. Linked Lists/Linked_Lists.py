# We'll be using our Node class
class Node:
  def __init__(self, value, next_node=None):
    self.value = value
    self.next_node = next_node
    
  def get_value(self):
    return self.value
  
  def get_next_node(self):
    return self.next_node
  
  def set_next_node(self, next_node):
    self.next_node = next_node

# Our LinkedList class
class LinkedList:
  def __init__(self, value=None):
    self.head_node = Node(value)
  
  #make LinkedList class iterable
  def __iter__(self): #iterable하게 만들어주는 메서드
    current_node = self.head_node
    while(current_node):  #current node가 None이 아닐 때까지 반복
      yield current_node.get_value()  #current node의 value를 반환
      current_node = current_node.get_next_node() #current node를 다음 node로 지정

  def get_head_node(self):
    return self.head_node
  
# Add your insert_beginning and stringify_list methods below:
  def insert_beginning(self, new_value): #Linked List에 head node를 추가하는 메서드
    new_node = Node(new_value)
    new_node.set_next_node(self.head_node)
    self.head_node = new_node
  
  def stringify_list(self): #Linked List의 모든 node를 출력하는 메서드
    path = ""
    current_node = self.get_head_node()
    while True:
        if current_node.get_next_node() == None:
            path += str(current_node.get_value()) + "\n"
            break
        else:
            path += str(current_node.get_value()) + "\n"
            current_node = current_node.get_next_node()
    return path    
  
  def remove_node(self, val_to_remove):
    current_node = self.get_head_node()
    if current_node.get_value() == val_to_remove: #head node를 삭제하는 경우 
      self.head_node = current_node.get_next_node()
    else: #head node를 제외한 node를 삭제하는 경우
      while current_node: #current_node가 None이 아닐 때까지 반복
        next_node = current_node.get_next_node() #current node의 다음 node를 next node로 지정
        if next_node.get_value() == val_to_remove: #next node의 value가 삭제하려는 value와 같은 경우는
          current_node.set_next_node(next_node.get_next_node()) #current node의 next node를 next node의 next node로 지정
          break
      #next node가 삭제할 노드가 아닌 경우 다음 노드로 넘어가며 삭제할 노드를 찾는다
          
# Test your code by uncommenting the statements below - did your list print to the terminal?
ll = LinkedList(5)
ll.insert_beginning(70)
ll.insert_beginning(5675)
ll.insert_beginning(90)
print(ll.stringify_list())
