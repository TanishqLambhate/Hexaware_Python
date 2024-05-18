library_list = [
    {
        "title": "Python Programming",
        "author": "Eric Matthes",
        "year": 2019,
        "available": True
    },
    {
        "title": "Automate the Boring Stuff with Python",
        "author": "Al Sweigart",
        "year": 2020,
        "available": True
    },
    {
        "title": "Learning Python I",
        "author": "Mark Lutz",
        "year": 2013,
        "available": False
    },
    {
        "title": "Fluent Python",
        "author": "Luciano Ramalho",
        "year": 2015,
        "available": True
    },
    {
        "title": "Adavance Python",
        "author": "Mark Lutz",
        "year": 2015,
        "available": False
    },
]
book = {"title": "Fluent Python II", "author": "Alex", "year": 2016, "available": True}
# Task 1
# Add Book Function: Write a function add_book(library, new_book)
def add_book(library,new_book):
    # library=[*library,new_book]
    library.append(book)
    
    # print(library)

add_book(library_list,book)
# print(library_list)

 # Task 2
# Search Books by Author Function: Write a function search_by_author(library, author_name)
# def search_book(library,author):
#     author_books=[]
#     for book1 in library:
#         if author==book1.get("author"):
#             author_books.append(book1)
#     return author_books
# print(search_book(library_list,"Mark Lutz"))

#v2 pyhtonic way
def search_book(library,author):
    return [book1 for book1 in library if author==book1.get("author")]
print(search_book(library_list,"Mark Lutz"))

# Task 3
# Check Out Book Function: Write a function check_out_book(library, title) that marks a book as not available if it exists and is available in the library.
# def check_out_book(library, title):
#     found_flag=False
#     for book1 in library:
#         if title==book1.get("title"):
#             if(book1.get("available")==True):
#                 found_flag=True
#                 return(f"{title} is Available for check out")
#             elif(book1.get("available")==False):
#                 found_flag=True
#                 return("unavailable")
#     if found_flag==False:
#         return f"{title} is not preseent in library"

def check_out_book(library, title):
    for book1 in library:
        if title==book1.get("title") and book1.get("available")==True:
            book1["available"]=False
            return(f"{title} is Available for check out")
        elif title==book1.get("title") and book1.get("available")==False:
            return("unavailable")
    return f"{title} is not preseent in library"

# print(check_out_book(library_list, "Fluent Python II"))
# print(check_out_book(library_list, "Adavance Python"))
# print(check_out_book(library_list, "Fluent Pn I"))

movies = [
    {
        "title": "Inception",
        "ratings": [5, 4, 5, 4, 5]
    },
    {
        "title": "Interstellar",
        "ratings": [5, 5, 4, 5, 4]
    },
    {
        "title": "Dunkirk",
        "ratings": [4, 4, 4, 3, 4]
    },
    {
        "title": "The Dark Knight",
        "ratings": [5, 5, 5, 5, 5]
    },
    {
        "title": "Memento",
        "ratings": [4, 5, 4, 5, 4]
    },
]
# Function
# Task 1
# get_movies_avg_rating

# Import package - Inbuilt

from pprint import pprint
from pprint import pprint
#from package import function_name
def get_movies_avg_rating(movies):
    for movie in movies:
        # movie["average_ratings"]=movie.get("average_ratings",0)
        movie["average_ratings"]=sum(movie.get("ratings"))/len(movie.get("ratings"))
    return movies    
    # print (movies)
    
# pprint(get_movies_avg_rating(movies))
# Task 2 - break it into 2 functions
def calc_avg_ratings(movie):
    return sum(movie.get("ratings"))/len(movie.get("ratings"))

def get_movies_avg_rating(movies):
    for movie in movies:
        movie["average_ratings"]=sum(movie.get("ratings"))/len(movie.get("ratings"))
    return movies 
pprint(get_movies_avg_rating(movies))
# Expected Output
output = [
    {"title": "Inception", "ratings": [5, 4, 5, 4, 5], "average_rating": 4.6},
    {"title": "Interstellar", "ratings": [5, 5, 4, 5, 4], "average_rating": 4.2},
    {"title": "Dunkirk", "ratings": [4, 4, 4, 3, 4], "average_rating": 4.1},
    {"title": "The Dark Knight", "ratings": [5, 5, 5, 5, 5], "average_rating": 5},
    {"title": "Memento", "ratings": [4, 5, 4, 5, 4], "average_rating": 4.2},
]

# def own_max(*nums):
#     print(nums, type(nums))
 
 
# own_max(5, 6, 10)
# own_max(5, 6, 10, 7, 80, 60)
# Arbitary Arguments
def own_max(*nums):
    curr_max=nums[0]
    for n in nums:
        if n>curr_max:
            curr_max=n
    return curr_max
 
 
own_max(5, 6, 10)
print(own_max(5, 6, 10, 7, 80, 60))