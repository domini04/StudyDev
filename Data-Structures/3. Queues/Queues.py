class Node:
  def __init__(self, value, next_node=None):
    self.value = value
    self.next_node = next_node
    
  def set_next_node(self, next_node):
    self.next_node = next_node
    
  def get_next_node(self):
    return self.next_node
  
  def get_value(self):
    return self.value
# create Queue class with enqueue, dequeue, and peek methods
class Queue:
  def __init__(self, max_size=None):
    self.head = None
    self.tail = None
    self.max_size = max_size
    self.size = 0
  
  def peek(self): # head의 값을 반환
    if self.get_size() > 0:
      return self.head.get_value()
    else:
      print("Nothing to see here!")

  def get_size(self): # 현재 큐의 크기를 반환
    return self.size
  
  def has_space(self):  # 큐에 공간이 있는지 확인 : enqueue에서 사용
    if self.max_size : # max_size가 None이 아니라면 공간이 있을 경우에만 True를 반환
      if self.max_size >  self.size:
        return True
      else:
        return False

    if self.max_size == None: # max_size가 없다면 언제나 충분한 공간이 있음
      return True
  
  def is_empty(self): # 큐가 비어있는지 확인 : dequeue에서 사용
    if self.size == 0:
      return True
    else:
      return False

  def enqueue(self, value): # 큐에 노드를 추가하는 메소드. 가장 마지막에 추가된 노드를 tail로 지정
    if self.has_space(): # 먼저 큐에 공간이 있는지 확인
      item_to_add = Node(value)
      print("Adding " + str(item_to_add.get_value()) + " to the queue!")
      if self.is_empty(): # 큐가 비어있다면 head와 tail을 새로운 노드로 지정
        self.head = item_to_add
        self.tail = item_to_add
      else: # 큐가 비어있지 않다면 현재 tail과 연겨랳주고, tail의 다음 노드를 새로운 노드로 지정
        self.tail.set_next_node(item_to_add)
        self.tail = item_to_add
      self.size += 1
    else :  # 큐에 공간이 없다면
      print("Sorry, no more room!")
  
  def dequeue(self):  # 큐에서 노드를 제거하는 메소드. 가장 먼저 추가된 노드(head)를 제거
    if self.get_size() > 0: # 큐에 노드가 있다면
      item_to_remove = self.head 
      print("Removing " + str(item_to_remove.get_value()) + " from the queue!")
      if self.get_size() == 1:
        self.head = None
        self.tail = None
      else :
        self.head = self.head.get_next_node() 
      self.size -= 1
      return item_to_remove.get_value()
    else :
      print("This queue is totally empty!")