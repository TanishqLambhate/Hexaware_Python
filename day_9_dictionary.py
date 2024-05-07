books = [
    {
        "title": "Infinite Jest",
        "rating": 4.5,
        "genre": "Fiction"
    },
    {
        "title": "The Catcher in the Rye",
        "rating": 3.9,
        "genre": "Fiction"
    },
    {
        "title": "Sapiens",
        "rating": 4.9,
        "genre": "History"
    },
    {
        "title": "A Brief History of Time",
        "rating": 4.8,
        "genre": "Science"
    },
    {
        "title": "Clean Code",
        "rating": 4.7,
        "genre": "Technology"
    },
]
top_rated_books=[]
book=0
for book in  books:
    if(book['rating'])>=4.7:
        top_rated_books.append(book['title'])

print(top_rated_books)

#task2 list comprehension - pythonic way
top_rated_books=[book['title'] for book in  books if(book['rating'])>=4.7]
print(top_rated_books)

# person={"name":"Tanishq","age":22}
# for key in person:
#     print(key,person[key])

# for k,v in person.items():
#     print(k,v)

person = {
    "name": "Lionel Messi",
    "age": 36,
    "address": {
        "city": "rosario",
        "country": "Argentina",
    },
    # "stats": {"goals": 300, "assists": 500},
    "sport": "football",
}
print(person["address"]["city"])# Access nested dictionary

#print(person["stats"])#KeyError: 'stats'

#Safer way: Access vlaue
print(person.get("stats") )#None
print(person.get("name") )
#none->Bottom B=value

# print(person["stats"]["goals"]) # KeyError: 'stats'
# print(person.get("stats").get("goals")) #'NoneType' object has no attribute 'get'
# Default  value -person.get(key,default value)


print(person.get("height", 174))
# print(person.get("stats",("goals":15) ).get("goals",15))
# Default value - person.get(key, default value)
print(person.get("stats", {}).get("goals"))  # None
print(person.get("stats", {"goals": 0}).get("goals"))  # None