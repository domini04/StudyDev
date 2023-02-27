nums = [5, 2, 9, 1, 5, 6]

def swap(arr, index_1, index_2):
  temp = arr[index_1]
  arr[index_1] = arr[index_2]
  arr[index_2] = temp


def bubble_sort(arr):
  for i in range(len(arr)): #n번 반복을 위한 for문
    for j in range(len(arr)-1):  #실제 정렬을 위한 for문
      if arr[j] > arr[j+1]:
        swap(arr, j, j+1)

#Bubble Sort Optimization 
# 매 outer loop마다 가장 큰 수가 맨 뒤로 가기 때문에 그 다음 outer loop에서는 맨 뒤에 있는 수는 정렬할 필요가 없다.
# 마지막으로 swap이 일어난 index를 기억하여 그 이후로는 정렬을 하지 않는다.

def bubble_sort_optimized(arr):
  for i in range(len(arr)):
    swapped = False
    for j in range(len(arr)-1):
      if arr[j] > arr[j+1]:
        swap(arr, j, j+1)
        swapped = True
    if not swapped:
      break