#모든 iteration들은 recursion으로 바꿀 수 있고 반대도 마찬가지.


# I. 다음 factorial recursion을 iterative하게 바꾸어라.

# def factorial(n):
#   #base case : n이 1이면 1을 return
#   if n == 1 :
#     return 1
#   else :
#     return factorial(n-1) *n # *=n이 piecewise solution에 해당.

def factorial(n):
  result = 1
  for i in range(n,1,-1): #n부터 1까지 1씩 감소하면서 반복
    result *= i
  return result

# II. 다음 fibonacci recursion을 iterative하게 바꾸어라.
# def fibonacci(n):
#   if n < 0:
#     ValueError("Input 0 or greater only!")
#   if n <= 1:
#     return n
#   return fibonacci(n - 1) + fibonacci(n - 2)

def fibonacci(n):  # 피보나치 수열 전체가 아니라 n번째 피보나치 수를 구하는 것이다. 1,1,2 ....
  if n < 0:
    ValueError("Input 0 or greater only!")
  
  if n <= 1:
    return n
  
  fib = [0,1] #fib 배열의 마지막 두개의 합이 다음 피보나치 수가 된다.
  while len(fib) != n+1: #n이 0,1이 아닌 경우, fib배열의 길이가 n+1이 될 때까지 반복. 특정 횟수 반복이 아니라, 특정 조건이 만족될 때까지 반복하는 경우 while문을 사용한다.  
    fib.append(fib[-1]+fib[-2]) 

  return fib[n]

# III. n의 각 자릿수를 더하는 함수를 iterative & recursive버전 각각으로 구현.

# iterative solution
def sum_digits(n):
  result = 0
  ndigits = len(str(n)) #n의 자릿수를 구한다.
  for i in range(ndigits): #n의 자릿수만큼 반복
    result += n % 10**(i+1) // 10**i #각 자리수 :  10의 i+1승으로 나눈 나머지를 10의 i승으로 나눈 몫
  return result

# recursive solution
def sum_digits(n):
  # base case:
  if n < 10:
    return n
  # recursive case:
  else:
    return n % 10 + sum_digits(n // 10) # n = 12345라면 5 + sum_digits(1234) -> 5+ 4 + sum_digits(123) -> ... -> 5+4+3+2+1

# IV. 다음 find_min함수를 recursive하게 구현하라.

'''
def find_min(my_list): #list의 최솟값을 찾는 함수
  min = None  #최솟값이 0보다 작을 수 있으므로 None으로 초기화
  for element in my_list:
    if not min or (element < min): #min이 None이거나 element가 min보다 작으면 해당 element를 min으로 설정
      min = element
  return min
'''

def find_min(my_list):

  if len(my_list) == 0:
    return None

  #base case : list의 길이가 1이면() 해당 element를 return
  if len(my_list) == 1:
    return my_list[0]

  
  #recursive case :
  if my_list[0] < my_list[1]: #첫번째 원소가 두번째 원소보다 작으면 두번째 원소를 제거한 리스트에서 다시 최솟값을 찾는다.
    return find_min(my_list[0:1] + my_list[2:])

  else: #첫번째 원소가 두번째 원소보다 크면 첫번째 원소를 제거한 리스트에서 다시 최솟값을 찾는다.
    return find_min(my_list[1:])
  # [1,4,2,-1] -> [1,2,-1] -> [1,-1] -> [-1] -> -1

# V. 해당 단어가 palindrome인지 확인하는 함수를 recursive하게 구현하라.
  # Palindrome : 앞뒤가 똑같은 단어. ex) racecar, madam, level, 이효리

'''
# Linear - O(N)
ver 1.
def is_palindrome(my_string):
  while len(my_string) > 1:
    if my_string[0] != my_string[-1]:
      return False
    my_string = my_string[1:-1]
  return True 

ver2
def is_palindrome(my_string):
  string_length = len(my_string)
  middle_index = string_length // 2
  for index in range(0, middle_index):
    opposite_character_index = string_length - index - 1
    if my_string[index] != my_string[opposite_character_index]:
      return False  
  return True
'''
def is_palindrome(string):
  #base case:
  if len(string) <= 1:
    return True

  #recursive case:
  return string[0] == string[-1] and is_palindrome(string[1:-1]) #앞부분이 piecewise solution, 뒷부분이 recursion. and 연산자로 인해 한쪽이 False면 False를 return한다.
    # abba -> a == a and is_palindrome(bb) -> b == b and is_palindrome(b) -> True
    # abca -> a == a and is_palindrome(bc) -> b == c and is_palindrome(b) -> False
  
# VI. 곱셈을 recursive하게 구현하라.
'''
def multiplication(num_1, num_2):
  result = 0
  for count in range(0, num_2):
    result += num_1
  return result
'''

def multiplication(n1, n2):
  #base case:
  if n2 == 0:
    return 0

  #recursive case:
  return n1 + multiplication(n1, n2-1)
# 위 버전은 음수를 곱할 때 문제가 생긴다. -> n2가 음수일 때 n1을 빼는 방식으로 수정
def multiplication(n1, n2):
  #base case:
  if n2 == 0:
    return 0

  #recursive case:
  if n2 > 0:
    return n1 + multiplication(n1, n2-1)
  else:
    return -n1 + multiplication(n1, n2+1)


# VII. Binary Tree를 한 번씩 방문하는 depth 메소드를 recursive하게 구현하라.

'''  #전략 : root node를 방문하고, left subtree를 방문하고, right subtree를 방문한다. right subtree 방문전에 left subtree의 자식이 있으면 left subtree의 자식을 먼저 방문한다(반복).
def depth(tree):
  result = 0
  # our "queue" will store nodes at each level
  queue = [tree]
  # loop as long as there are nodes to explore
  while queue:
    # count the number of child nodes
    level_count = len(queue)
    for child_count in range(0, level_count):
      # loop through each child
      child = queue.pop(0)
     # add its children if they exist
      if child["left_child"]:
        queue.append(child["left_child"])
      if child["right_child"]:
        queue.append(child["right_child"])
    # count the level
    result += 1
  return result
  '''

def depth(tree):
  #base case:
  if tree == None: #tree가 None이면 0을 return한다.
    return 0

  #recursive case:
  return 1 + max(depth(tree["left_child"]), depth(tree["right_child"])) #left child와 right child 중 더 깊은 depth를 return한다. 
    #각 left & right subtree가 recursive하게 호출되면서 최하위 leaf node까지 내려간다.
    #leaf node에서는 left child와 right child가 None이므로 0을 return한다.
  # {'data': 42, 'left_child': {'data': 34, 'left_child': {'data': 27}}, 'right_child': {'data': 56}} -> 
  # 왼쪽 : 1 + max(depth({'data': 34, 'left_child': {'data': 27}})) -> 1 + max(1 + depth({'data': 27})) -> 1 + max(1 + 0) -> 1 + 1 -> 2
  # 오른쪽 : 1 + max(depth({'data': 56})) -> 1 + max(0) -> 1
    # 2와 1 중 더 큰 2를 return한다. root node를 포함한 depth는 3이다.

# first level
root_of_tree = {"data": 42}
# adding a child - second level
root_of_tree["left_child"] = {"data": 34}
root_of_tree["right_child"] = {"data": 56}
# adding a child to a child - third level
first_child = root_of_tree["left_child"]
first_child["left_child"] = {"data": 27}

print (root_of_tree)