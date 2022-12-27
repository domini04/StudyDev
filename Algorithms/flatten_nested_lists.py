example = [[1,2,3], [4,[5,6]],7,[8,[9]]]

def clean_list(li):
  cleaned = []
  # 주어진 list 안의 모든 원소들이 int라면 :
  if all(isinstance(i,int) for i in li):
    return li #해당 list를 반환
  
  #그렇지 않다면, list안의 list는 +=로 평탄화 실행
  for i in li:
    if isinstance(i,list):
      cleaned += i
    # nested list가 아닌 int들은 append
    else: cleaned.append(i)
  return clean_list(cleaned)
clean_list(example)


## 다른 사람이 작성한 버전 (내가 한거 아님)

# def unpack(arr):
#     if isinstance(arr, int):
#         return [arr]
#     goodList = 1
#     for elem in arr:
#         if not isinstance(elem, int):
#             goodList = 0
#             break
#     if goodList == 1:
#         return arr
#     return unpack(arr[0]) + unpack(arr[1:])

# example = [[1,2,3], [4,[5,6]],7,[8,[9]]]
# unpack(example)