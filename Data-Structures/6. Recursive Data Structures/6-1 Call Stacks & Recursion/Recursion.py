#1. Define a function that takes an integer as an input and returns the sum of all numbers from the input down to 1

'''## iterative version
def sum_to_one(n):
  result = 0
  for num in range(n, 0, -1):
    result += num
  return result
'''

# Using recursion
def sum_to_one(n):
  #base case : n이 1이면 1을 return
  if n == 1:
    return 1
  #recursive case : n이 1이 아니면 n + sum_to_one(n-1)을 return
  else : 
    return sum_to_one(n-1) + n # +=n이 piecewise solution에 해당.


#2. Define a function that returns the factorial of a given number
  # If the input is less than 2, return 1.

def factorial(n):
  #base case : n이 1이면 1을 return
  if n == 1 :
    return 1
  else :
    return factorial(n-1) *n # *=n이 piecewise solution에 해당.

#3. Analyze the Big O of the previous function
  # O(n) : n이 1이 될 때까지 n-1을 반복하므로 n번의 연산이 필요하다.

#4. write a function that removes nested lists within a list but keeps the values contained
  # ex) [1,2,[3,4]] -> [1,2,3,4]

#base case : list에 nested list가 없으면 list를 return
#recursive step : list에 nested list가 있으면 nested list를 제거하고 list를 return

def flatten(li):
  result = []
  for item in li:
    if type(item) == list:
      print("nested list found : ", item)
      result += flatten(item) #recursive step : 자기 자신을 계속해서 호출하여 nested list를 제거. +=item이 piecewise solution에 해당.
    else:
      result.append(item) #base case : nested list가 없으면 item을 result에 추가
  return result

planets = ['mercury', 'venus', ['earth'], 'mars', [['jupiter', 'saturn']], 'uranus', ['neptune', 'pluto']]
print(flatten(planets))