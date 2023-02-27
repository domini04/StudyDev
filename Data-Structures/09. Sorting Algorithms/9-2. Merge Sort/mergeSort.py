#정리  
# 1. divide and conquer에서 list를 divide하는 부분을 재귀적으로 호출하여 single item list로 만든다. -> 이 부분을 변수 선언으로 처리.
# 2. single item list들을 merge한다. -> 이 부분을 return statement로 처리.
def merge(l, r): #나뉘어진 배열을 merge하면서 정렬한다.
  result = []
  while len(l) > 0 and len(r) > 0:
    if l[0] < r[0]:
      result.append(l.pop(0))
    else:
      result.append(r.pop(0))
  #l, r중 하나가 비어있는 경우 남은 것을 result에 추가한다.
  if l:
    result += l
  if r:
    result += r
  return result


def merge_sort(items): #배열을 나누고 다시 merge하면서 정렬
  if len(items) == 1:
    return items

  middle_index = len(items) // 2
  left_split = items[:middle_index]
  right_split = items[middle_index:]


  #재귀적으로 merge_sort를 호출하여 left_split, right_split을 single item list로 만든다.
    #Key Point : recursive call을 반드시 return으로 처리할 필요 없다! 경우에 따라 변수 선언으로 처리할 수 있다.
  left_sorted = merge_sort(left_split) #계속해서 left, right로 나눠지면서 최종적으로 single item list들의 집합이 된다.
  right_sorted = merge_sort(right_split)
    #left_sorted, right_sorted는 single item list들의 집합이다.

  #나뉘어진 single item list들을 merge한다.
  return merge(left_sorted, right_sorted)


# testing
unordered_list1 = [356, 746, 264, 569, 949, 895, 125, 455]
unordered_list2 = [787, 677, 391, 318, 543, 717, 180, 113, 795, 19, 202, 534, 201, 370, 276, 975, 403, 624, 770, 595, 571, 268, 373]
unordered_list3 = [860, 380, 151, 585, 743, 542, 147, 820, 439, 865, 924, 387]
print(merge_sort(unordered_list1))
print(merge_sort(merge(unordered_list1, unordered_list2))) 
print(merge_sort(unordered_list1 + unordered_list2 + unordered_list3))