# Binary Tree : Trees that have at most two children per node

'''#Binary Tree 예시
bst_tree_node = {"data": 42}
bst_tree_node["left_child"] = {"data": 36}
bst_tree_node["right_child"] = {"data": 73}
'''

#Define a function that takes a sorted value list and returns a binary search tree
#sorted value list를 binary search tree로 변환하는 함수를 정의하라.
#ex) [1,2,3,4,5,6,7] -> binary search tree

#base case : the input list is empty -> return None
#Recursive step: The input list must be divided into two halves ->
'''
1.Find the middle index of the list
2.Store the value located at the middle index
3.Make a tree node with a "data" key set to the value
4.Assign tree node’s "left child" to a recursive call using the left half of the list
5.Assign tree node’s "right child" to a recursive call using the right half of the list
6.Return the tree node
'''
def build_bst(sorted_list):
  if len(sorted_list) == 0: #base case : the input list is empty -> return None
    return None

  else:
    middle_index = len(sorted_list) // 2 #중간 index를 찾는다.
    middle_value = sorted_list[middle_index] #중간 index의 값을 찾는다.
    tree_node = {"data": middle_value}  #중간 index의 값을 가지는 tree node를 만든다.
    tree_node["left_child"] = build_bst(sorted_list[:middle_index]) #바로 왼쪽에 있는 값을 갖고 recursion -> 리스트가 점점 작아지면서 base case에 도달한다.
    tree_node["right_child"] = build_bst(sorted_list[middle_index+1:])
    return tree_node


def power_set(li):
  if len(li) == 0: #base case
    return [[]]
  else:
    power_set_without_first = power_set(li[1:]) #recursive step 
    #power_set(['a','b','c']) -> power_set(['b','c']) -> power_set(['c']) -> power_set([]) 순서대로 call stack에 들어간다.
    power_set_with_first = [[li[0]] + subset for subset in power_set_without_first] #호출되는 대로 ['c'] -> ['b','c'] -> ['a','b','c'] 순서대로 return 된다.
    return power_set_without_first + power_set_with_first

print(power_set(['a', 'b', 'c'])) 