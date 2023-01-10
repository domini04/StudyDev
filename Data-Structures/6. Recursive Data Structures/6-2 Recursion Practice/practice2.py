#1. Move item to end of the list using recursion
def move_to_end(li, st):
  result = []
  #base case : if list is empty, return empty list
  if len(li) == 0:
    return result
  #recursive case 
    #option 1 : if the first item is not the item to move, append it to the result list 
    # and call the function again with the rest of the list
  if li[0] != st:
    result.append(li[0])
    result += move_to_end(li[1:], st)

    #option 2 : if the first item is the item to move, call the function again with the rest of the list
    # and append the item to the result list
  else:
    result += move_to_end(li[1:], st)
    result.append(li[0])
  return result


#2. Delete i-th item from linked list using recursion

class ListNode:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next_node = next_node

def delete_at_index(head, i):
  #edge case : if the index is negative, return the current node
  if i < 0:
    return head
  #base case : 
  # option 1 : if the current node is None, return None
  if head == None:
    return None
  # option 2 : if the index is 0, return the next node
  if i == 0:
    return head.next_node

  #recursive case : call the function again with the next node and the index - 1
  head.next_node = delete_at_index(head.next_node, i-1)
  return head
  
  

  