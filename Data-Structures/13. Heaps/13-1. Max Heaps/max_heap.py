class MaxHeap :
  #Rule
  # 1. The parent node is always greater than the child node
  # 2. The 1st index is the root node -> has the largest value
  def __init__(self) : 
    self.heap_list = [None] # the None is for the 0th index
    self.count = 0

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