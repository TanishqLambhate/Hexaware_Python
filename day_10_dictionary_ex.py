employees = [
    {"name": "Sneha", "experience": 2},
    {"name": "Manju"},
    {"name": "Sai Subash", "experience": 4},
    {"name": "Manasa"},
]
 
 
# Task: After 1 experience
for employee in employees:
    employee["experience"]=employee.get("experience",0)+1
    print(employee)
    


#print(employees)
 
# Output
[
    {"name": "Sneha", "experience": 3},
    {"name": "Manju",  "experience": 1},
    {"name": "Sai Subash", "experience": 5},
    {"name": "Manasa", "experience": 1},
]
# Task 2
#  Senior 5 or more, Mid-Level 3 to 5, Junior < 3
for employee in employees:
    employee["status"]=employee.get("status",0)
    print(employee["status"])
    if( employee["experience"]<3):
        employee["status"]="Junior"
    elif( 3<= employee["experience"]<5):
        employee["status"]="Mid level"
    else:
        employee["status"]="Senior"
print(employees)
    # if experience
# Output
[
    {"name": "Sneha", "experience": 3, "status": "Mid-Level"},
    {"name": "Manju", "experience": 1, "status": "Junior"},
    {"name": "Sai Subash", "experience": 5, "status": "Senior"},
    {"name": "Manasa", "experience": 1, "status": "Junior"},
]