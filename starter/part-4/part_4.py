### Step 1 - Input function

## Create five input statements to gather user's book they want to input to the system. After that be sure to turn it into a function.

# Code here

# def create_new_book():
#    title = input("What is the title of the book you would like to add? - ")
#    author = input("Who is the author of the book you would like to add? - ")
#    year = input("What year was this book published? - ")
#    rating = input("What rating out of 5 would you give this book? - ")
#    pages = input("What is the page count of the book? - ")

### Step 2 - Type conversion

## Now convert the proper data-types front strings to either floats or ints depending on what it is. Feel free to comment out your old function so you don't get an error, or copy/paste and give it a new name.

# Code here

# def create_new_book():
#     title = input("What is the title of the book you would like to add? - ")
#     author = input("Who is the author of the book you would like to add? - ")
#     year = int(input("What year was this book published? - "))
#     rating = float(input("What rating out of 5 would you give this book? - "))
#     pages = int(input("What is the page count of the book? - "))

#     book_dictionary = {
#         "title": title,
#         "author": author,
#         "year": year,
#         "rating": rating,
#         "pages": pages,
#     }

#     return book_dictionary

### Step 3 - Error handling

## Now take your previous function, and handle potential errors should the user type an answer that doesn't convert data-type properly.

# Code here

# try:
#     year = int(input("What year was this book published? - "))
# except:
#     year = int(input("Please type a number for the year? - "))
    
# try:
#     rating = float(input("What rating out of 5 would you give this book? - "))
# except:
#     rating = float(input("Please use a number between 0 and 5? - "))
    
# try:
#     pages = int(input("What is the page count of the book? - "))
# except:
#     pages = int(input("Please enter a whole number of pages? - "))

### Step 4 - if/elif/else

## Now create a main menu function that gives the user options. Handle their choices with if/elif/else statements.

# Code here

# def main_menu(dictionary_function):
#     options = input("Choose 1 to add a book. Choose 2 to view your current book list. Choose 3 to exit. ")
#     if options == "1":
#         dictionary_function.append(create_new_book())
#     elif options == "2":
#         print(my_book_dictionary)
#     elif options == "3":
#         print("\nGoodbye")
#         active = False
#     else:
#         print("\nPlease choose an option\n")
    

### Step 5 - while loops

## Now add a while loop to your main menu to keep it alive, and continually asking for input until the user chooses to exit the program. Call the main menu to ensure it functions properly.

# Code here

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

def create_new_book():
    title = input("What is the title of the book you would like to add? - ")
    author = input("Who is the author of the book you would like to add? - ")
    try:
        year = int(input("What year was this book published? - "))
    except:
        year = int(input("Please type a number for the year? - "))
    try:
        rating = float(input("What rating out of 5 would you give this book? - "))
    except:
        rating = float(input("Please use a number between 0 and 5? - "))
    try:
        pages = int(input("What is the page count of the book? - "))
    except:
        pages = int(input("Please enter a whole number of pages? - "))

    book_dictionary = {
        "title": title,
        "author": author,
        "year": year,
        "rating": rating,
        "pages": pages,
    }

    return book_dictionary

def book_titles(dictionary): 
    book_title_list = []
    for books in dictionary:
        book_title_list.append(books["title"])
    return book_title_list

def avg_book_rating(dictionary):
    initial_book_rating = []
    for books in dictionary:
        book_rating = initial_book_rating.append(books["rating"])
        rating_sum = sum(initial_book_rating)
        book_list_length = len(initial_book_rating)
        rating_avg = rating_sum/book_list_length
    return rating_avg
    
def main_menu(dictionary_function):
    
    active = True
    
    while active:
        options = input("Choose 1 to add a book - \nChoose 2 to view a list of your book titles - \nChoose 3 to view the average rating of all your books - \nChoose 4 to exit - ")
        if options == "1":
            dictionary_function.append(create_new_book())
        elif options == "2":
            print(book_titles(my_book_dictionary))
        elif options == "3":
            print(avg_book_rating(my_book_dictionary))
        elif options == "4":
            print("\nGoodbye")
            active = False
        else:
            print("\nPlease choose a number on the list\n")

main_menu(my_book_dictionary)