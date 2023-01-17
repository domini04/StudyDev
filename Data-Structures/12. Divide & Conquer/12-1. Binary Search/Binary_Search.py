#I.
#assume the array is sorted -> use sorting algorithm to sort the array

def Binary_Search(arr, target):
  #1. Check the middle value of the target
    #2. If the middle value is the target, return the index
  mid = len(arr) // 2
  if arr[mid] == target:
    return mid
  #3. If the middle value is greater than the target, search the left half
  elif arr[mid] > target:
    return Binary_Search(arr[:mid], target)
  #4. If the middle value is less than the target, search the right half
  elif arr[mid] < target:
    return Binary_Search(arr[mid+1:], target)
  #5. If the target is not in the array, return -1
  else:
    return -1


sorted_values = [13, 14, 15, 16, 17]
print(Binary_Search(sorted_values, 14))

#II. Version that uses pointer to keep track of the index
  # By using pointers instead of copying the list, we can reduce the space complexity

  #Changes 
    #1. Instead of passing in the array, pass in the left and right pointer
    #2. Instead of returning the index, return the left pointer
    #3. Instead of returning -1, return None

def Binary_Search2(arr, left_pointer, right_pointer, target):
  #1. Check the middle value of the target
    #2. If the middle value is the target, return the index
  mid = (left_pointer + right_pointer) // 2
  if arr[mid] == target:
    return mid
  #3. If the middle value is greater than the target, search the left half
  elif arr[mid] > target:
    return Binary_Search2(arr, left_pointer, mid, target)
  #4. If the middle value is less than the target, search the right half
  elif arr[mid] < target:
    return Binary_Search2(arr, mid+1, right_pointer, target)
  #5. If the target is not in the array, return -1
  else:
    return None

#III. Iterative version
def Binary_Search3(arr, target):
  left_pointer = 0
  right_pointer = len(arr) - 1
  while left_pointer <= right_pointer:
    mid = (left_pointer + right_pointer) // 2
    if arr[mid] == target:
      return mid
    elif arr[mid] > target:
      right_pointer = mid - 1
    elif arr[mid] < target:
      left_pointer = mid + 1
  return None