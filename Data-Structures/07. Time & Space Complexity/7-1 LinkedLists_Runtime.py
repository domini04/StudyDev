#Analyze the runtime of data structures

from etc.linkedlist import LinkedList

#I. Finding the Maximum Value in a Linked List
def find_max(linked_list):
  print("--------------------------")
  print("Finding the maximum value of:\n{0}".format(linked_list.stringify_list()))
  max_value = linked_list.get_head_node().get_value()
  current_node = linked_list.get_head_node()
  while current_node:
    if current_node.get_value() > max_value:
      max_value = current_node.get_value()
    current_node = current_node.get_next_node()
  return max_value

  
  

#Test Cases
ll = LinkedList(6)
ll.insert_beginning(32)
ll.insert_beginning(-12)
ll.insert_beginning(48)
ll.insert_beginning(2)
ll.insert_beginning(1)
print("The maximum value in this linked list is {0}\n".format(find_max(ll)))

ll_2 = LinkedList(60)
ll_2.insert_beginning(12)
ll_2.insert_beginning(22)
ll_2.insert_beginning(-10)
print("The maximum value in this linked list is {0}\n".format(find_max(ll_2)))

ll_3 = LinkedList("A")
ll_3.insert_beginning("X")
ll_3.insert_beginning("V")
ll_3.insert_beginning("L")
ll_3.insert_beginning("D")
ll_3.insert_beginning("Q")
print("The maximum value in this linked list is {0}\n".format(find_max(ll_3)))

#Runtime
runtime = "N"
print("The runtime of find_max is O({0})".format(runtime))

# II. Sorting a Linked List in Ascending Order
  # Strategy
#1. Instantiate a new linked list
#2. Find the maximum value of our inputted linked list
#3. Insert the maximum to the beginning of the new linked list
#4. Remove the maximum value from the inputted linked list
#5. Repeat steps 2-4 until the head node of the inputted linked list points to None
#6. Return the new linked list


def sort_linked_list(linked_list):
  print("\n---------------------------")
  print("The original linked list is:\n{0}".format(linked_list.stringify_list()))
  new_linked_list = LinkedList()
  while linked_list.get_head_node(): #input LL에 노드가 존재할 때 까지 max value node를 뜯어다가 new LL에 붙인다.
    max_value = find_max(linked_list)
    new_linked_list.insert_beginning(max_value)
    linked_list.remove_node(max_value)

  return new_linked_list
  #Test Cases
ll = LinkedList("Z")
ll.insert_beginning("C")
ll.insert_beginning("Q")
ll.insert_beginning("A")
print("The sorted linked list is:\n{0}".format(sort_linked_list(ll).stringify_list()))

ll_2 = LinkedList(1)
ll_2.insert_beginning(4)
ll_2.insert_beginning(18)
ll_2.insert_beginning(2)
ll_2.insert_beginning(3)
ll_2.insert_beginning(7)
print("The sorted linked list is:\n{0}".format(sort_linked_list(ll_2).stringify_list()))

ll_3 = LinkedList(-11)
ll_3.insert_beginning(44)
ll_3.insert_beginning(118)
ll_3.insert_beginning(1000)
ll_3.insert_beginning(23)
ll_3.insert_beginning(-92)
print("The sorted linked list is:\n{0}".format(sort_linked_list(ll_3).stringify_list()))

#Runtime
runtime = "N^2"
print("The runtime of sort_linked_list is O({0})\n\n".format(runtime))