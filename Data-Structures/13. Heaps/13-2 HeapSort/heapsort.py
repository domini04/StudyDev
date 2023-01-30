from max_heap import MaxHeap

class MaxHeap :
  def extract(self) : #extracts the max value from the heap, and returns it. Then it adjusts the heap to maintain the heap property
    if self.count == 0 :
      return None
    #1. Get the max value
    max_value = self.heap_list[1]
    #2. Swap the max value with the last value
    self.heap_list[1], self.heap_list[self.count] = self.heap_list[self.count], self.heap_list[1]
    #3. Remove the last value
    self.heap_list.pop()
    self.count -= 1
    #4. Heapify the list
    self.heapify_down()
    return max_value

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
  