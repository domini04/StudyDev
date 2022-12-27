import random
import utils
import sorts

bookshelf = utils.load_books('books_small.csv')
  # randomize the order of the bookshelf
# bookshelf.sort(key=lambda x: random.random()) 
print(bookshelf)
# for book in bookshelf:
#   print(book)


#Python 글자 순서 정렬 파악하기
#Checking how python is comparing letters lexicographically
# print(ord('a'))
# print(ord('b'))
# print(ord(' '))
# print(ord('!'))
# print(ord('A'))
  # need to change all cases to something -> utils.load_books

# print("Adentures" > "Revenge best served cold") 

#I. Bubble Sort

#I-1. compare by title
def compare_by_title_ascending(book_a, book_b):
  if book_a['title'] > book_b['title']:
    return True
  else:
    return False

# print("Bubble sort: " + str(sorts.bubble_sort(bookshelf, compare_by_title_ascending)))
# get the average number of swaps for 1000 runs of bubble sort
# swap_count = 0
# for i in range(1000):
#   bookshelf.sort(key=lambda x: random.random())
#   swap_count += sorts.bubble_sort(bookshelf, compare_by_title_ascending)[1]

# print("Bubble sort average number of swaps: " + str(swap_count / 1000))
  #average swap count : 22.319


#I-2. compare by author
def by_author_ascending(book_a, book_b):
  if book_a['author'] > book_b['author']:
    return True
  else:
    return False

  # create a copy of the bookshelf
# bookshelf_copy = bookshelf.copy()
# get the average number of swaps for 1000 runs of bubble sort
# swap_count = 0
# for i in range(1000):
#   bookshelf_copy.sort(key=lambda x: random.random())
#   swap_count += sorts.bubble_sort(bookshelf_copy, by_author_ascending)[1]
# print( "Bubble sort average number of swaps: " + str(swap_count / 1000))
  #average swap count : 22.389

#II. Quick Sort

  #create another copy of the bookshelf
bookshelf_copy2 = bookshelf.copy()
# print(bookshelf_copy2)

#II-1. compare by title
# swap_count = 0
# for i in range(1000):
#   bookshelf_copy2.sort(key=lambda x: random.random())
#   swap_count += sorts.quicksort(bookshelf_copy2, 0, len(bookshelf_copy2) - 1, compare_by_title_ascending)
# print("Quick sort average number of swaps: " + str(swap_count / 1000))
  #average swap count : 24.254

#II-2. compare by the length of the sum of the title and author
def by_title_author_length(book_a, book_b):
  if len(book_a['title'] + book_a['author']) > len(book_b['title'] + book_b['author']):
    return True
  else:
    return False

# swap_count = 0
# for i in range(1000):
#   bookshelf_copy2.sort(key=lambda x: random.random())
#   swap_count += sorts.quicksort(bookshelf_copy2, 0, len(bookshelf_copy2) - 1, by_title_author_length)
# print("Quick sort average number of swaps: " + str(swap_count / 1000))
  #average swap count : 24.13
#python if all elements in re