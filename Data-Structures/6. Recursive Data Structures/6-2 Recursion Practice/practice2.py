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



  