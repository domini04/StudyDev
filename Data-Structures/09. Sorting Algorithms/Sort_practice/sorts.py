import random

def bubble_sort(arr, comp_func):
  
  swaps = 0
  sorted = False
  while not sorted:
    sorted = True
    for idx in range(len(arr) - 1):
      if comp_func(arr[idx], arr[idx + 1]):
        sorted = False
        arr[idx], arr[idx + 1] = arr[idx + 1], arr[idx]
        swaps += 1
  print("Bubble sort: There were {0} swaps".format(swaps))
  return arr, swaps

# def quicksort(list, start, end, comp_func):
#   if start >= end:
#     return
#   pivot_idx = random.randrange(start, end + 1)
#   pivot_element = list[pivot_idx]
#   list[end], list[pivot_idx] = list[pivot_idx], list[end]
#   less_than_pointer = start
#   for i in range(start, end):
#     if comp_func(list[i], pivot_element):
#       list[i], list[less_than_pointer] = list[less_than_pointer], list[i]
#       less_than_pointer += 1
#   list[end], list[less_than_pointer] = list[less_than_pointer], list[end]
#   quicksort(list, start, less_than_pointer - 1, comp_func)
#   quicksort(list, less_than_pointer + 1, end, comp_func)

#quicksort version keeping count of swaps
def quicksort(list, start, end, comp_func):
  if start >= end:
    return 0
  pivot_idx = random.randrange(start, end + 1)
  pivot_element = list[pivot_idx]
  list[end], list[pivot_idx] = list[pivot_idx], list[end]
  less_than_pointer = start
  for i in range(start, end):
    if comp_func(list[i], pivot_element):
      list[i], list[less_than_pointer] = list[less_than_pointer], list[i]
      less_than_pointer += 1
  list[end], list[less_than_pointer] = list[less_than_pointer], list[end]
  swaps = end - start
  swaps += quicksort(list, start, less_than_pointer - 1, comp_func)
  swaps += quicksort(list, less_than_pointer + 1, end, comp_func)
  return swaps