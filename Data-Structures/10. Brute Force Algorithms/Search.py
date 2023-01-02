# I. Basic Linear Search
  # def linear_search(search_list, target_value) :
  #   for i,j in enumerate(search_list):
  #     if j == target_value:
  #       return i
  #   return "{} Not found".format(target_value)

def linear_search(search_list, target_value):
  for idx in range(len(search_list)):
    if search_list[idx] == target_value:
      return idx
  raise ValueError("{0} not in list".format(target_value))

number_list = [ 10, 14, 19, 26, 27, 31, 33, 35, 42, 44]
target_number = 33

try :
  print(linear_search(number_list, target_number))
except ValueError as e:
  print(e)


target_number = 100
try :
  print(linear_search(number_list, target_number))
except ValueError as e:
  print(e)


# II. Finding Duplicate Values

 #pseudo code
# For each element in the searchList
  # if element equal target value then
    # Add its index to a list of occurrences
# if the list of occurrences is empty
  # raise ValueError
# otherwise
  # return the list occurrences

def linear_search_all(search_list, target_value):
  occurrences = []
  for idx in range(len(search_list)):
    if search_list[idx] == target_value:
      occurrences.append(idx)
  if not occurrences:
    raise ValueError("{0} not in list".format(target_value))
  return occurrences


tour_locations = [ "New York City", "Los Angeles", "Bangkok", "Istanbul", "London", "New York City", "Toronto"]
target_city = "New York City"

try :
  print(linear_search_all(tour_locations, target_city))
except ValueError as e:
  print(e)

# III. Finding the Maximum Value

  # pseudo code
  # Create a variable called max_value_index    
# Set max_value_index to the index of the first element of the search list
     # For each element in the search list
          # if element is greater than the element at max_value_index
               # Set max_value_index equal to the index of the element
# return max_value_index

def linear_search_max(search_list):
  max_value_index = 0
  for idx in range(1, len(search_list)):
    if search_list[idx] > search_list[max_value_index]:
      max_value_index = idx
  return max_value_index

test_scores = [88, 93, 75, 100, 80, 67, 71, 92, 90, 83]
print(linear_search_max(test_scores))

