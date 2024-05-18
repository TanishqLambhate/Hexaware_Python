from datetime import datetime

print( datetime.now().weekday())
print( datetime.now().day)
def calc_age(birth_year):
       
    try:        
        age = datetime.now().year - int(birth_year)
        if int(birth_year)>datetime.now().year:
            raise Exception("Are you from Future?")
        if int(birth_year)<0:
            raise Exception("Negative in years")
        return f"Your age is {age}"
       
    except ValueError:
        return f"Give year in numbers 🔢"
   
    except Exception as e:
        return f"Check again {e}👨‍🚀"
    
print(calc_age(-2002))
# print(calc_age("dfd"))