
from max_heap import MaxHeap

def heapsort(array) :
  sorted_array = []
  heap = MaxHeap()
  #1. Build a max heap from the array
  for value in array :
    heap.insert(value)
  #2. Extract the max value from the heap and append it to the sorted array
  while heap.count > 0 :
    sorted_array.append(heap.extract())
  return sorted_array
  

my_list = [99, 22, 61, 10, 21, 13, 23]
sorted_list = heapsort(my_list)
print(sorted_list)