# After the 🔑
message = "    🚨🔍📱🔑secret_code✌️"
code = "SECRET_CODE✌️"

# output = # You code here
# ans=message.find('🔑')
# print(ans)

# message=message[ans+1:]
# message=message.upper()
# print(code)
# if (message == code):
#   print("You are an hacker 🎊")
# else:
#   print("Try again")


# Output
# "You are an hacker"

# "Try again"
# remove the junk
message1 = "    🚨🔍📱🔑******secret_code✌️((((("
code = "SECRET_CODE✌️"
ans=message1.find('🔑')
print(ans)

message1=message1[ans+1:].strip("*")
# print(message1)
message1=message1.upper().strip("(")
print(message1)
print(code)
if (message1 == code):
  print("You are an hacker 🎊")
else:
  print("Try again")
