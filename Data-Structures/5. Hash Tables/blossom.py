# implement a hash map to relate the names of flowers to their meanings :
  # - use separate chaining to handle collisions
  # - use linked lists for each of the separate chains

from Linked_Lists import Node, LinkedList


# Our HashMap class
class HashMap:
  def __init__(self, size):
    self.array_size = size
    self.array = [LinkedList() for i in range(size)]  # HashMap의 underlying structure를 LinkedList로 구현. 입력된 size만큼의 LinkedList를 array에 저장
  
  def hash(self, key):
    hash_code = sum(key.encode())
    return hash_code

  def compress(self, hash_code):
    return hash_code % self.array_size
  
  def assign(self, key, value):
    array_index = self.compress(self.hash(key))
    payload = Node([key, value])
    list_at_array = self.array[array_index]
    for i in list_at_array: #list_at_array의 모든 node를 순회하며 key가 같은 node가 있는지 확인
      if i[0] == key: #key가 같은 node가 있는 경우 value를 변경
        i[1] = value
        return
    list_at_array.insert(payload) # insert() : Linked List의 head node를 추가하는 메서드. 같은 key를 가진 node가 없는 경우 추가

  def retrieve(self, key):
    array_index = self.compress(self.hash(key))
    list_at_index = self.array[array_index]
    for i in list_at_index: #list_at_index의 모든 node를 순회하며 key가 같은 node가 있는지 확인
      if i[0] == key: #key가 같은 node가 있는 경우 value를 반환
        return i[1]
    return None #key가 같은 node가 없는 경우 None을 반환

# Test your hash map with the driver code below
from blossom_lib import flower_definitions 

blossom = HashMap(len(flower_definitions))  #flower_definitions의 길이만큼의 크기를 가진 HashMap 생성

for flower in flower_definitions: #flower_definitions의 모든 item을 순회하며 HashMap에 추가
  blossom.assign(flower[0], flower[1])

print(blossom.retrieve('daisy')) #daisy의 value를 출력
print(blossom.retrieve('begonia')) #begonia의 value를 출력
print(blossom.retrieve('sunflower')) #sunflower의 value를 출력


