class MaxHeap :
  #Rule
  # 1. The parent node is always greater than the child node
  # 2. The 1st index is the root node -> has the largest value
  def __init__(self) : 
    self.heap_list = [None] # the None is for the 0th index
    self.count = 0  

  def parent(self, index) :
    return index // 2

  def left_child(self, index) :
    return index * 2

  def right_child(self, index) :  
    return index * 2 + 1

  def get_larger_child(self, index) : #returns the index of the larger child
    if self.right_child(index) > self.count : #if there is no right child, return the left child if it exists
      if self.left_child(index) > self.count :
        return None
      return self.left_child(index)

    else :
      left_child = self.heap_list[self.left_child(index)]
      right_child = self.heap_list[self.right_child(index)]
      if left_child > right_child :
        return self.left_child(index)
      else :
        return self.right_child(index)

  def insert(self, value) :
    #1. Add the new value to the end of the list
    self.heap_list.append(value)
    self.count += 1
    #2. Heapify the list
    self.heapify_up()

  def heapify_up(self) : #adjusts the heap to maintain the heap property, by sorting the new value up the tree
    #1. Check if the new value is greater than its parent
      #to do so, get the index of the new value
    index = self.count
    # while index > 1 : 
    #   parent_index = index // 2
    #   if self.heap_list[index] > self.heap_list[parent_index] :
    #     #2. If it is, swap the values
    #     self.heap_list[index], self.heap_list[parent_index] = self.heap_list[parent_index], self.heap_list[index]
    #     #3. Repeat the process with the new parent
    #     index = parent_index
    #   else :
    #     break    #위 버전은 무조건 root node까지 가야함. 아래 버전은 더 빠름

    while index > 1 and self.heap_list[index] > self.heap_list[self.parent(index)] :
      self.heap_list[index], self.heap_list[self.parent(index)] = self.heap_list[self.parent(index)], self.heap_list[index]
      index = self.parent(index)

  def delete(self) :
    #1. Swap the first and last value
    self.heap_list[1], self.heap_list[self.count] = self.heap_list[self.count], self.heap_list[1]
    #2. Remove the last value
    max_value = self.heap_list.pop()
    self.count -= 1
    #3. Heapify down
    self.heapify_down()
    return max_value
