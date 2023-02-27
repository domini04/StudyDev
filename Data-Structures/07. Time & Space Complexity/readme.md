# Space Complexity

### 개요

- 해당 알고리즘의 **메모리 효율성**을 나타냄
    - denotes **space growth in relation to the input size**
- **메모리 효율성**
    - 해당 알고리즘의 the ***number of variables declared***에 비례

### Space Complexity vs. Time Complexity

- most functions **do not** have matching space and time complexities

```python
def simple_loop(input_array):
  for i in input_array:
    print(i)

#위 메서드의 TimeComplexity는 O(N)
#하지만 Space Coplexity는 O(1) -> i 외에 따로 변수를 선언하는 것이 없기 때문
```

- A **recursive function** that is passed the same array or object in each call doesn’t add to the space complexity **if the array or object is passed by reference** (which it is in Python).

```python
def double_array(input_array):
  # Returns an array that is the double of the input array
  length = len(input_array)
  doubled_array = [0] * length
  for i in range(length):
    doubled_array[i] = input_array[i] * 2
  return doubled_array
 # doubled_array[i]가 정의되므로 O(N)
 
def find_min(input_array):
  # Returns the smallest element in the array
  minimum = input_array[0]
  for i in input_array:
    if i < minimum:
      minimum = i
  return minimum
# N배로 늘어나는 부분 없으므로 O(1)
```