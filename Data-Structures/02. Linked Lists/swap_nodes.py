from 'Linked_Lists.py' import Node
from 'Linked_Lists.py' import LinkedList


def swap_nodes(input_list, val1, val2):  # 데이터 노드를 swap하는 메서드. val1, val2로 바꿀 노드를 검색
  print(f'Swapping {val1} with {val2}')

  #init
  node1_prev = None
  node2_prev = None
  node1 = input_list.head_node
  node2 = input_list.head_node 

  #바꿀 노드를 검색
  if val1 == val2: #val1과 val2가 같은 경우 굳이 바꿀 필요 없음
    print("Elements are the same - no swap needed")
    return

  while node1 is not None: #바꿀 node1을 찾아 순환. 현재 노드가 None이 되면 자동으로 멈춤
    if node1.get_value() == val1: #바꿀 노드를 찾은 경우 break
      break
    node1_prev = node1
    node1 = node1.get_next_node() #바꿀 노드를 찾지 못한 경우 다음 노드로 넘어감

  while node2 is not None:
    if node2.get_value() == val2: #바꿀 노드를 찾은 경우 break
      break
    node2_prev = node2 
    node2 = node2.get_next_node() #바꿀 노드를 찾지 못한 경우 다음 노드로 넘어감

  if (node1 is None or node2 is None): #val1, val2에 해당하는 노드가 없는 경우 출력. return
    print("Swap not possible - one or more element is not in the list")
    return

  #검색한 노드를 swap
  if node1_prev is None:
    input_list.head_node = node2 #node1이 head node인 경우 node2를 head node로 설정
  else:
    node1_prev.set_next_node(node2)

  if node2_prev is None:
    input_list.head_node = node1 #node2가 head node인 경우 node1을 head node로 설정
  else:
    node2_prev.set_next_node(node1)

  temp = node1.get_next_node()
  node1.set_next_node(node2.get_next_node())
  node2.set_next_node(temp) #node1과 node2를 swap


ll = LinkedList.LinkedList()
for i in range(10):
  ll.insert_beginning(i)

print(ll.stringify_list())
swap_nodes(ll, 9, 5)
print(ll.stringify_list())