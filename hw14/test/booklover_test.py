import numpy as np
import pandas as pd
import unittest
from ../booklover import BookLover

class BookLoverTestSuite(unittest.TestCase):
    
    def test_1_add_book(self): 
        # add a book and test if it is in `book_list`.
        bibliophile = BookLover('Griffin','kzj5qw@virginia.edu','Science Fiction')
        bibliophile.add_book('Jurassic Park', 3)
        
        self.assertTrue('Jurassic Park' in list(bibliophile.book_list['book_name']))

    def test_2_add_book(self):
        # add the same book twice. Test if it's in `book_list` only once.
        bibliophile = BookLover('Griffin','kzj5qw@virginia.edu','Science Fiction')
        bibliophile.add_book('The Andromeda Strain', 3)
        bibliophile.add_book('The Andromeda Strain', 3)
        
        self.assertEqual(len(bibliophile.book_list[bibliophile.book_list['book_name'] == 'The Andromeda Strain']), 1)
            
    def test_3_has_read(self): 
        # pass a book in the list and test if the answer is `True`.
        bibliophile = BookLover('Griffin','kzj5qw@virginia.edu','Science Fiction', book_list = pd.DataFrame({'book_name':['Prey'], 'book_rating':[3]}))
        
        self.assertTrue(bibliophile.has_read('Prey'))
        
    def test_4_has_read(self): 
        # pass a book NOT in the list and use `assert False` to test the answer is `True`
        bibliophile = BookLover('Griffin','kzj5qw@virginia.edu','Science Fiction', book_list = pd.DataFrame({'book_name':['Congo'], 'book_rating':[3]}))
        
        self.assertFalse(bibliophile.has_read('Sphere'))
        
    def test_5_num_books_read(self): 
        # add some books to the list, and test num_books matches expected.
        bibliophile = BookLover('Griffin','kzj5qw@virginia.edu','Science Fiction', book_list = pd.DataFrame({'book_name':['Jurassic Park','The Andromeda Strain'], 'book_rating':[3,3]}))
        bibliophile.add_book('Prey', 3)
        bibliophile.add_book('Congo', 3)
        bibliophile.add_book('Sphere', 3)
        
        self.assertEqual(bibliophile.num_books_read(), 5)

    def test_6_fav_books(self):
        # add some books with ratings to the list, making sure some of them have rating > 3. 
        # Your test should check that the returned books have rating  > 3
        bibliophile = BookLover('Griffin','kzj5qw@virginia.edu','Science Fiction', book_list = pd.DataFrame({'book_name':['Jurassic Park','The Andromeda Strain'], 'book_rating':[3,3]}))
        bibliophile.add_book('Prey', 3)
        bibliophile.add_book('Congo', 3)
        bibliophile.add_book('Sphere', 3)
        bibliophile.add_book('State of Fear', 4)
        bibliophile.add_book('Next', 4)
        bibliophile.add_book('Micro', 5)
        bibliophile.add_book('The Terminal Man', 4)
        
        ratings = bibliophile.fav_books()['book_rating']
        self.assertTrue(all(rating > 3 for rating in ratings))
                
if __name__ == '__main__':
    unittest.main(verbosity=3)