#get the nth last node of the linked list
def nth_last_node(linked_list, n):
  current = None
  tail_seeker = linked_list.head_node
  count = 1 
  while tail_seeker: #tail_seeker가 None일 때까지 LL을 순회
    tail_seeker = tail_seeker.get_next_node()
    count += 1
    if count >= n + 1: # tail_seeker와 current의 거리가 n일 때 부터 current를 이동시킨다(동일한 속도로 이동)
      if current is None:
        current = linked_list.head_node
      else:
        current = current.get_next_node()
  return current #tail_seeker이 LL의 끝에 다다라 멈췄을 때, current는 뒤에서 n번째 노드를 가리킨다

#Return the right-weighted middle for even-length linked lists
#For example, in a linked list of 4 elements it should return the element at the third position
from LinkedList import LinkedList

# Complete this function:
def find_middle(linked_list):
    #방법 1.
    #첫 번째 pointer로 LL의 길이를 구한다
    #두 번째 pointer로 LL의 중간이 되는 위치값을 구한다

    #방법 2.
    # pointer1은 한 칸씩 이동, pointer2는 두 칸씩 이동
    # pointer2가 LL의 끝에 다다르면 pointer1은 LL의 중간이 되는 위치를 가리킨다
    pointer_head = self.head_node
    pointer_tail = self.head_node
    while pointer_head:
        pointer_head = pointer_head.get_next_node()
        if pointer_head:
            pointer_head = pointer_head.get_next_node()
            pointer_tail = pointer_tail.get_next_node()
    return pointer_tail
    #방법 3. -> 방법 2와 원리는 동일
#   count = 0
#   fast = linked_list.head_node
#   slow = linked_list.head_node
#   while fast:
#     fast = fast.get_next_node()
#     if count % 2 != 0:
#       slow = slow.get_next_node()
#     count += 1
#   return slow

def generate_test_linked_list(length):
  linked_list = LinkedList()
  for i in range(length, 0, -1):
    linked_list.insert_beginning(i)
  return linked_list

# Use this to test your code:
test_list = generate_test_linked_list(7)
print(test_list.stringify_list())
middle_node = find_middle(test_list)
print(middle_node.value)