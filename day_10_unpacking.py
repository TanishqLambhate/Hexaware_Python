# Unpacking / Destructuring
# a=10
# b=10
# c=10

# Multiple variable assignment
a = b = c = 10
print(a, b, c)

# unpacking
# poojitha,shivam,samar=("Black","Choco","Butterscotch")
poojitha, shivam, samar = "Black", "Choco", "Butterscotch"  # Tuple without brackets
print(poojitha)
print(shivam)
print(samar)

movies = ["MI", "JJK", "Avengers"]
mathesh, nandini, devesh = movies
print(mathesh, nandini, devesh)

# t1,t2,t3=[100,200,300,400]
# print(t1,t2,t3) #ValueError: too many values to unpack (expected 3)

t1, t2, t3, _ = [100, 200, 300, 400]
print(t1, t2, t3)

# *-> unpacking operator
t1, t2, *t3 = [100, 200, 300, 400, 60, 30]
print(t1, t2, t3)  # 100 200 [300, 400, 60, 30]
t1, t2, *t3 = (100, 200, 300, 400, 60, 30)
print(t1, t2, t3)  # 100 200 [300, 400, 60, 30]

# Task 1
coordinates = [(5, 4), (1, 1), (6, 10), (9, 10)]
# for i in coordinates:
#     # print(i)
#     for j in i:
#         print(int(j**2+(j+1)**2)**0.5)
#         j=j+2
distance=[]
for cord in coordinates:
    x=cord[0]
    y=cord[1]
    d=(x**2+y**2)**0.5
    distance.append(d)
print(distance)

# Task 1.2 - for loop + unpacking

# distance=[]
# for cord in coordinates:
#     x,y=cord
#     d=(x**2+y**2)**0.5
#     distance.append(d)
# print(distance)

# distance=[]
# for x,y in coordinates:
#     d=(x**2+y**2)**0.5
#     distance.append(d)
# print(distance)

# Task 1.3 - unpacking + list comprehension
distance = [round((x**2 + y**2) ** 0.5, 2) for x, y in coordinates]
print(distance)

marks1 = [70, 80, 60]
# marks2=[*marks1] # copy -1. slice 2. .copy()
marks2 = [*marks1, 75, 68]
print(marks2)

# merging multiple list
t1 = [80, 90]
t2 = [50, 60]
t3 = [*t1, *t2]
print(t3)
# t3=[80,90,50,60]
# Unpacking -> ** Dict
movie = {"name": "John wick", "year": 2014}
# Copy
mv1 = {**movie, "actor": "keanu Reeves"}
mv2 = {**movie, "actor": "keanu Reeves", "year": 2015}
mv3 = {
    "actor": "keanu Reeves",
    "year": 2015,
    **movie,
}
print(mv1)
print(mv2)
print(mv3)
print(movie)
