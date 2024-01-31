my_book = {
    "title": "The Hunger Games",
    "author": "Suzanne Collins",
    "year": 2008,
    "rating": 4.32,
    "pages": 374,
}

my_book_dictionary = [
    {
    "title": "Harry Potter and the Prisoner of Azkaban",
    "author": "J.K. Rowling",
    "year": 1999,
    "rating": 5,
    "pages": 317,
    },
    {
    "title": "Ender's Game",
    "author": "Orson Scott Card",
    "year": 1985,
    "rating": 4,
    "pages": 324,
    },
    {
    "title": "The Great Gatsby",
    "author": "F. Scott Fitzgerald",
    "year": 1925,
    "rating": 3,
    "pages": 208,
    },
]
# Follow the instructions in this part of the project. Define and flesh out your function below, which should accept a dictionary as an argument when called, and return a string of the info in that book-dictionary in a user-friendly readable format.

# Code below

def book_parser(book_dictionary):
    book_string = f'{my_book["title"]} was written by {my_book["author"]} in {my_book["year"]}. It has {my_book["pages"]} pages, and is rated a {my_book["rating"]} out of 5.' 
    return book_string

# print(book_parser(my_book))

# Once you are finished with that function, create several more functions which return individual pieces of information from the book.

# Code below

# BOOK TITLE FUNCTION

def book_title(book_dictionary):
    book_string = f'The book title is {my_book["title"]}.'
    return book_string

# BOOK AUTHOR FUNCTION

# print(book_title(my_book))

def book_author(book_dictionary):
    book_string = f'The author of {my_book["title"]} is {my_book["author"]}.'
    return book_string

# print(book_author(my_book))

# PUBLICATION YEAR FUNCTION

def publication_year(book_dictionary):
    book_string = f'The year {my_book["title"]} was published is {my_book["year"]}.'
    return book_string

# print(publication_year(my_book))

# BOOK RATING FUNCTION

def book_rating(book_dictionary):
    book_string = f'{my_book["title"]} is rated {my_book["rating"]} out of 5.'
    return book_string

# print(book_rating(my_book))

# BOOK PAGES FUNCTION

def book_pages(book_dictionary):
    book_string = f'{my_book["title"]} has {my_book["pages"]} pages.'
    return book_string

# print(book_pages(my_book))

# Finally, create at least three new functions that might be useful as we expand our home library app. Perhaps thing of a way you could accept additional arguments when the function is called? Also, imagine you have a list filled with dictionaries like above.

# Code below (I'm thinking maybe a function to compile book titles, take the average rating of books, and calculate the number of pages in the library?)

def book_titles(book_dictionary): 
    book_title_list = []
    for books in book_dictionary:
        book_title_list.append(books["title"])
    return book_title_list
    
print(book_titles(my_book_dictionary))
    
def avg_book_rating(dictionary):
    initial_book_rating = []
    for books in dictionary:
        book_rating = initial_book_rating.append(books["rating"])
        rating_sum = sum(initial_book_rating)
        book_list_length = len(initial_book_rating)
        rating_avg = rating_sum/book_list_length
    return rating_avg
    
print(avg_book_rating(my_book_dictionary))
    
def total_book_pages(dictionary):
    pages_list = []
    for books in dictionary:
        iterable_page_list = pages_list.append(books["pages"])
        total_pages = sum(pages_list)
    return total_pages
    
print(total_book_pages(my_book_dictionary))
        