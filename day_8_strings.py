msg = "Hi, all"

# Case methods
print(msg.upper())
print(msg.lower())
print(msg.title())
print(msg.capitalize())


quote = "      Dream is not something that you see in sleep, Dream is something that does not let you sleep"

print(quote)
print(quote.strip())


quote1 = "----Dream is not something-that you see in sleep, Dream is something that does not let you sleep----"
print(quote1.strip("-"))
print(quote1.lstrip("-"))
print(quote1.rstrip("-"))

# ctrl+ space -> Auto Complete

# find and replace
quote3= "Dream is not something that you see in sleep, Dream is something that does not let you sleep"
print(quote3.find('something'))

#strings are immutable
print (quote3.replace("Dream","🛌"))
print(quote3)

# slicing operator->:
quote="Dream"
print(quote[3:1])