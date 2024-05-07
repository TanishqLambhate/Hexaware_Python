# In sets we cannot access element using index because it has no order
# unique,no order,mutable

colors = {"red", "blue", "red", "green", "blue"}
print(colors)
print(set(colors))
# using .add()
colors.add("red")
print(colors)

unique_colors = set()
unique_colors = {color for color in colors}
print(unique_colors)
