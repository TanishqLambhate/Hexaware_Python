distance=[]
for cord in coordinates:
    x,y=cord
    d=(x**2+y**2)**0.5
    distance.append(d)
print(distance)

distance=[]
for x,y in coordinates:
    d=(x**2+y**2)**0.5
    distance.append(d)
print(distance)