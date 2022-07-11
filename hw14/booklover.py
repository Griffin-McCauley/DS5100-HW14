import numpy as np
import pandas as pd

class BookLover():
    
    def __init__(self, name, email, fav_genre, num_books = 0, book_list = pd.DataFrame({'book_name':[], 'book_rating':[]})):
        self.name = name
        self.email = email
        self.fav_genre = fav_genre
        # ensure that num_books corresponds to the number of entries in book_list
        self.num_books = int(len(book_list))
        self.book_list = book_list
        
    def add_book(self, book_name, rating):
        if book_name in list(self.book_list['book_name']):
            print('You have already logged this book!')
        else:
            new_book = pd.DataFrame({'book_name': [book_name], 'book_rating': [int(rating)]})

            self.book_list = pd.concat([self.book_list, new_book], ignore_index=True)
            
            self.num_books = int(len(self.book_list))

    def has_read(self, book_name):
        return book_name in list(self.book_list['book_name'])
    
    def num_books_read(self):
        return self.num_books
    
    def fav_books(self):
        return self.book_list[self.book_list['book_rating'] > 3]