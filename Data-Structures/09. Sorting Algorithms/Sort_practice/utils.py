import csv
import os
import sys
# This code loads the current book
# shelf data from the csv file
def load_books(filename):
  bookshelf = []
  with open(os.path.join(sys.path[0], filename)) as file:
      shelf = csv.DictReader(file)
      for book in shelf:
          #change all cases to lower
          book['author'] = book['author'].lower()
          book['title'] = book['title'].lower()
          
          bookshelf.append(book)
  return bookshelf