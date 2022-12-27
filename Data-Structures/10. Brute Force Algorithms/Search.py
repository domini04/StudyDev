def linear_search(search_list, target_value) :
  for i,j in enumerate(search_list):
    if j == target_value:
      return i
  return "{} Not found".format(target_value)