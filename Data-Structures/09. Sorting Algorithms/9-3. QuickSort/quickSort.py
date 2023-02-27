# Pointer 개념을 이용한 QuickSort 구현
from random import randrange, shuffle
def quicksort(li, start, end):
  #base case : list가 더 이상 나뉘어질 수 없을 때
  if start >= end:
    return

  #randrange를 이용해 pivot을 설정
  pivot_idx = randrange(start, end+1)
  pivot = li[pivot_idx]
  #pivot을 맨 뒤로 보냄
  li[pivot_idx], li[end] = li[end], li[pivot_idx]
  #pivot을 기준으로 작은 값들을 왼쪽으로, 큰 값들을 오른쪽으로 보냄
  for i in range(start, end):
    if li[i] < pivot:
      li[i], li[start] = li[start], li[i]
      start += 1
  #pivot을 중간으로 보냄
  li[start], li[end] = li[end], li[start]
  #pivot을 기준으로 왼쪽과 오른쪽을 다시 정렬
  quicksort(li, 0, start-1)
  quicksort(li, start+1, end)
#testing
unsorted_list = [3,7,12,24,36,42]
shuffle(unsorted_list)
print(unsorted_list)
quicksort(unsorted_list, 0, len(unsorted_list) - 1)
print(unsorted_list)


  #Python의 기능을 최대한 활용해 QuickSort 구현
def QuickSort(arr):
  if len(arr) <= 1:
    return arr
  #pivot을 정하는 방법 :  1. 첫번째 원소 2. 마지막 원소 3. 중간 값 4. 랜덤 원소
    #여기서는 첫 번째 원소를 pivot으로 정함
  pivot = arr[0]
  tail = arr[1:]
  left_side = [x for x in tail if x <= pivot] #pivot보다 작은 값들을 모음
  right_side = [x for x in tail if x > pivot] #pivot보다 큰 값들을 모음

  return QuickSort(left_side) + [pivot] + QuickSort(right_side) 
    #이렇게 하면 재귀적으로 QuickSort가 호출되면서 최소 단위까지 분할됨. 분할 되는 과정에서 정렬이 이루어짐




  
