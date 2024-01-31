### Step 1 - Store data in a .txt

## This step's instructions explains how to use the open() function, to write and read info from a .txt file. Follow the instructions to create and call a function to add a book, based off of the previous dictionaries for our library, to the .txt file properly formatted with commas as separators.

# Code here

# with open("library.txt", "a") as f:
#     f.write(f"{title}, {author}, {year}, {rating}, {pages}\n")

### Step 2 - Read data from a .txt

## Now take your previously create function which prints info about all the books in your library, but gets the info from a list, and make it work by reading the information in your home library's .txt document. This will take some new logic, but you can do it.

# Code here

# with open("library.txt", "r") as f:
#     file = f.readlines()
    
#     for line in file:
#         line = line.split(", ")
        
#         book_dictionary = {
#             "title": title,
#             "author": author,
#             "year": int(year),
#             "rating": int(rating),
#             "pages": int(pages),
#         }

### Step 3 - if __name__ == "__main__":

## Wrap your main menu function call in an "if __name__ == '__main__':" statement to ensure it doesn't accidentally run if this file is imported as a module elsewhere.

# Code this at the bottom of the script

### Step 4 - Expand and refactor

## Now follow the instructions in this final step. Expand your project. Clean up the code. Make your application functional. Great job getting your first Python application finished!


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

    with open("library.txt", "a") as f:
        f.write(f"{title}, {author}, {year}, {rating}, {pages}\n")
        
        book_dictionary = {
            "title": title,
            "author": author,
            "year": int(year),
            "rating": float(rating),
            "pages": int(pages),
        }

    return book_dictionary

def read_the_dictionary(dictionary): 
    with open("library.txt", "r") as f:
        file = f.readlines()
    
    for line in file:
        title, author, year, rating, pages = line.split(", ")
        
        book_dictionary = {
            "title": title,
            "author": author,
            "year": int(year),
            "rating": float(rating),
            "pages": int(pages),
        }
    return book_dictionary

def avg_book_rating(dictionary):
    with open("library.txt", "r") as f:
        file = f.readlines()
        
        initial_book_rating = []
        
    for line in file:
        title, author, year, rating, pages = line.split(", ")
        
        book_dictionary = {"rating": float(rating)}
        
        rating_list = initial_book_rating.append(book_dictionary.get("rating"))
        rating_sum = sum(initial_book_rating)
        rating_length = len(initial_book_rating)
        rating_avg = rating_sum/rating_length
        
    return rating_avg
        
def main_menu(dictionary):
    
    active = True
    
    while active:
        options = input("""
            Choose 1 to add a book
            Choose 2 to view your most recent book entry
            Choose 3 to view the average rating of all your books
            Choose 4 to exit
            Type Here: """)
        if options == "1":
            create_new_book()
        elif options == "2":
            print(read_the_dictionary(dictionary))
        elif options == "3":
            print(avg_book_rating(dictionary))
        elif options == "4":
            print("\nGoodbye")
            active = False
        else:
            print("\nPlease choose a number on the list\n")
            
if __name__ == "__main__":
    main_menu("library.txt") 
