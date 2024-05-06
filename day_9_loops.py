# stars=5
# strs=1
# while stars>strs:
    
#     print("✨"*strs)
#     strs=strs+1
    
# Black Formatter (PEP)
# ctrl + ,  -> Settings
# format on save -> On
countdown=5

# for countdown in range(6):
#     print(countdown) # 0 - 5

# for countdown in range(1,6):
#     print(countdown)

# for countdown in range(1,6,2):
#     print(countdown)

# for countdown in range(1,6):
#     print("✨"*countdown)
    
# Task 3:Double Player stats
# player_stats=[10,20,30]
# # player stats double
i=0
# print(type(player_stats))
# print(player_stats[0])
# print(len(player_stats))
# for i in range(len(player_stats)):
#     player_stats[i]=player_stats[i]*2
    
# print(player_stats)

player_stats = [10, 20, 30]
new_stats = []
for i in player_stats:
    new_stats.append(2 * i)
print(new_stats)

#list comprehension-copy of result
#Double the player stat for each stat in players_stats

 
powered_up_stats_1 =[stat * 2 for stat in player_stats]
print(powered_up_stats_1)
print(player_stats)

# Task 4.1 - for loop
avengers = [
    "Hulk",
    "Iron man",
    "Black widow",
    "Captain america",
    "Spider man",
    "Thor",
]
 
 
# Output
# [4, 8, 11, 15, 10, 4]
length=[]
avenger=0
# Task 4.1 - for loop
for avenger in avengers:
   length.append(len(avenger))
print(length)
# Task 4.2 - List comprehension
length=[len(avenger) for avenger in avengers]
print(length)

# Output
# [
#     "Black widow",
#     "Captain america",
# ]
 
 
# Task 5.1 - for loop
# large_count = []
# for count in letters_count:
#     if count > 10:
#         large_count.append(count)
# print(large_count)
big_names=[]
for avenger in avengers:
#    length.append(len(avenger))
   if len(avenger)>10:
      big_names.append(avenger)
print(big_names)
 
# Task 5.2 - List comprehension

big_names=[avenger.upper() for avenger in avengers if len(avenger)>10]
print (big_names)






















# # Repeat a set of steps - Loops
 
 
# # DRY - Dont Repeat Yourself
# countdown = 1
 
# # print(countdown)
# # countdown = countdown + 1
# # print(countdown)
# # countdown = countdown + 1
# # print(countdown)
# # countdown = countdown + 1
# # print(countdown)
# # countdown = countdown + 1
# # print(countdown)
 
# countdown = 1
# # while (condition):
# while countdown < 6:
#     print(countdown)
#     countdown = countdown + 1
 
 
# # Task 1: Build pattern | Clue: *
# no_of_stars = 5
 
# curr_star = 1
 
# while curr_star < no_of_stars:
#     print("✨" * curr_star)
#     curr_star = curr_star + 1
 
# # Output
# # ✨
# # ✨✨
# # ✨✨✨
# # ✨✨✨✨
# # ✨✨✨✨✨
 
# # Black Formatter (PEP)
# # ctrl + ,  -> Settings
# # format on save -> On
 
# # while vs for
 
# # countdown = 1
# # # while (condition):
# # while countdown < 6:
# #     print(countdown)
# #     countdown = countdown + 1
 
# # range starts at 0
# # for countdown in range(6):
# #     print(countdown) # 0 - 5
 
 
# # range(<start>, <end>, <skip>)
# for countdown in range(1, 6):
#     print(countdown)
 
# for countdown in range(1, 6, 2):
#     print(countdown)
 
 
# # Task 2: Build pattern | Clue: *
# no_of_stars = 5
 
# for curr_stars in range(1, no_of_stars + 1):
#     print("✨" * curr_stars)
 
# # Output
# # ✨
# # ✨✨
# # ✨✨✨
# # ✨✨✨✨
# # ✨✨✨✨✨
 
# # Similar slice syntax
# # range(3)        | range(end)
# # range(1, 3)     | range(start, end)
# # range(1, 50, 2) | range(start, end, skip)
 
 
# # Task 3: Double Player stats
# player_stats = [10, 20, 30]
# # Player stats double
 
 
# # player_stats[0] = player_stats[0]*2
# # player_stats[1] = player_stats[1]*2
# # player_stats[2] = player_stats[2]*2
 
# # idx = 0
# # while idx < len(player_stats):
# #     player_stats[idx] = player_stats[idx] * 2
# #     idx = idx + 1
 
# # print(player_stats)
# # Output
# # [20, 40, 60]
 
# # for idx in range(len(player_stats)):
# #     player_stats[idx] = player_stats[idx] * 2
 
# # print(player_stats)
 
# # for idx in range(len(player_stats)):
# #     player_stats[idx] *= 2
 
# # print(player_stats)
 
# # Good
# # player_stats = [10, 20, 30]  # should not change
# # powered_up_stats = []  # add to list
# # for idx in range(len(player_stats)):
# #     powered_up_stats.append(player_stats[idx] * 2)
 
# # print(powered_up_stats)
# # print(player_stats)
 
 
# player_stats = [10, 20, 30]
# powered_up_stats = []
# for stat in player_stats:
#     powered_up_stats.append(stat * 2)
 
# print(powered_up_stats)  # [20, 40, 60]
# print(player_stats)  # [10, 20, 30]
 
 
# # List comprehension - copy of the result
# powered_up_stats_1 = [stat * 2 for stat in player_stats]
# # Double the player stat for each stat in players_stats
# print(powered_up_stats_1)
# print(player_stats)
 
 
# avengers = [
#     "Hulk",
#     "Iron man",
#     "Black widow",
#     "Captain america",
#     "Spider man",
#     "Thor",
# ]
 
# # Output
# # [4, 8, 11, 15, 10, 4]
 
# # Task 4.1 - for loop
 
# avengers_name_length = []
# for avenger in avengers:
#     avengers_name_length.append(len(avenger))
# print(avengers_name_length)
 
# # Task 4.2 - List comprehension
# # len of avenger for each avenger in avengers
 
# avengers_nl = [len(avenger) for avenger in avengers]
# print(avengers_nl)
 
 
# letters_count = [4, 8, 11, 15, 10, 4]
 
# large_count = []
# for count in letters_count:
#     if count > 10:
#         large_count.append(count)
# print(large_count)
 
# # Select count from letters_count where count > 10
# # Give me count for each count in letters_count where count > 10
# large_count_1 = [count for count in letters_count if count > 10]
# print(large_count_1)
 
 
# avengers = [
#     "Hulk",
#     "Iron man",
#     "Black widow",
#     "Captain america",
#     "Spider man",
#     "Thor",
# ]
 
# # Output
# # [
# #     "Black widow",
# #     "Captain america",
# # ]
 
 
# # Task 5.1 - for loop
 
 
# # Task 5.2 - List comprehension