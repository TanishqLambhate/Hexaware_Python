#list of lists
marks=[98,75,40,80,90,45,80,60]
print (marks)
marks.append(75)
sci=65
marks.insert(3,sci)
print (marks)

heights=[198,175,140,1777]
heights.remove(1777)
heights.pop()
print(heights)
#lists are mutable

#copy by reference
# p2=p1
# copy by value
#p3=p1[:]
#p2=copy of p1

#remove -> .pop()-index , .remove()- value
#add -> .append() , .insert()
#Copy -> :(slice),copy

#Repetition
cloned_treasures=["Gold Coin"] *3
print(cloned_treasures)

#split( str-> list)
shop_stock="vanilla,lime,choclate"
print(shop_stock.split(","))

avatar=["Fire","Water","Earth","Air"]
print(",".join(avatar))