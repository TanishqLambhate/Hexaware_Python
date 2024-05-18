# Abstract or Interface
# Force other class to implement certain methods
# Autocomplete
from abc import ABC, abstractmethod
 
 
# Abstract class / Interface
class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass
 
    @abstractmethod
    def move(self):
        pass
 
 
class Dog(Animal):
    def make_sound(self):
        print("Woof Woof")
 
    def move(self):
        print("Runnning... 🐕")
 
    def jump(self):
        print("Jumps 🦘")
 
 
maxy = Dog()
maxy.move()

class Bird(Animal):
    def make_sound(self):
        print("Chirp Chirp")
    def move(self):
        print("Flying... 🐕")

Birdie=Bird()
Birdie.move()


# # Encapsulation
# from MyExceptions.director_exception import DirectorNotFoundError
# from Util.DBconn import DBConnection
# from abc import ABC, abstractmethod
 
 
# # @ - decorators
# class IDirectorService(ABC):
#     @abstractmethod
#     def read_directors(self):
#         pass
 
#     @abstractmethod
#     def create_director(self, director):
#         pass
 
#     @abstractmethod
#     def read_director_by_id(self, director_id):
#         pass
 
 
# # Multiple Inheritance - Class
# class DirectorService(IDirectorService, DBConnection):
#     def read_directors(self):
#         try:
#             self.cursor.execute("Select * from Directors")
#             directors = self.cursor.fetchall()  # Get all data
#             for director in directors:
#                 print(director)
#         except Exception as e:
#             print(e)
 
#     def create_director(self, director):
#         try:
#             self.cursor.execute(
#                 "INSERT INTO Directors (Name) VALUES (?)",
#                 (director.name),
#             )
#             self.conn.commit()  # Permanent storing | If no commit then no data
#         except Exception as e:
#             print(e)
 
#     def read_director_by_id(self, director_id):
#         try:
#             self.cursor.execute(
#                 "Select * from Directors Where DirectorId = ?", director_id
#             )
#             directors = self.cursor.fetchall()  # Get all data
#             if len(directors) == 0:
#                 raise DirectorNotFoundError(director_id)
#             else:
#                 print(directors)
#         except Exception as e:
#             print("Ooops Error happened: ", e)
 