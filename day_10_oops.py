# Idea
# Object Oriented Programming
# Modeling our problem as real-world objects
 
# Car
# What makes a car?
# 1. engine
# 2. wheels
# 3. name
# 4. doors
 
 
#  Car
# 1. engine - v8
# 2. wheels - 4
# 3. name - Ferrari
# 4. doors - 2
 
 
# 1. engine - v4
# 2. wheels - 4
# 3. name - Alto
# 4. doors - 4
 
 
#  Car -> blueprint | Class blueprint object
 
 
class Car:
    def __init__(
        self, name, engine, wheels, doors
    ):  # creating object calls init (constructor)
        self.name = name
        self.engine = engine
        self.wheels = wheels
        self.doors = doors
    def horn(self):
        return f"{self.name} says Vromm Vroom!!"
 
 
ferrari = Car("Ferrari", "v8", 4, 2)  # object
alto = Car("Alto", "v4", 4, 4)  # object
 
print(ferrari.name, ferrari.wheels)
print(ferrari.horn())

# numeric seprator by python
# x=1_00_000

class bank:
    def __init__(self,acc_no,name,balance):
        self.acc_no=acc_no
        self.name=name
        self.balance=balance
    def display_balance(self):
        return f"{self.name} has ₹ {self.balance} in account"
    def withdraw(self,amount):
        if self.balance-amount>=0:
            self.balance=self.balance-amount
            return f"Success Your balance is {self.display_balance()}"
        else:
            return f"Insufficient funds. {self.display_balance()}"
    def deposit(self,amount):
        if amount>=0:
            self.balance=self.balance+amount
            return f"Success {self.display_balance()}"
        else:
            return f"Invalid amount {self.display_balance()}"
    
    # def apply_interest(self):
    #     # accumulated_interest_amt = self.balance * bank.interest_rate
    #     self.balance += accumulated_interest_amt
    #     return f"Interest received. ₹{accumulated_interest_amt}"
 


Tanishq=bank(101,"Tanishq",10000000000000)
print(Tanishq.name,Tanishq.acc_no)
print (Tanishq.display_balance())
print(Tanishq.withdraw(10_000))         #success.Your balance is :60000
print (Tanishq.display_balance())
print (Tanishq.deposit(459))

class Circle:
    pi = 3.14
 
    def __init__(self, radius):
        self.radius = radius
 
    @staticmethod
    def perimeter(radius):
        return 2 * Circle.pi * radius
 
    @classmethod
    def from_diameter(cls, diameter):
        pass
 
    def calculate_area(self):
        return Circle.pi * self.radius**2
 
 
# Normal function but inside class | no access to self
print(Circle.perimeter(2))
 
# Instance method
circle1 = Circle(4)
print(circle1.calculate_area())
 
 
# Class method - to construct the object
# circle_from_dia = Circle.from_diameter(10)
# print(circle_from_dia.calculate_area())  # 78.5

class bank2:
    interest_rate=0.02
    no_of_accounts=0
    def __init__(self,acc_no,name,balance):
        self.acc_no=acc_no
        self.name=name
        self.balance=balance
        bank2.no_of_accounts+=1

    def display_balance(self):
        return f"{self.name} has ₹ {self.balance} in account"
    def withdraw(self,amount):
        if self.balance-amount>=0:
            self.balance=self.balance-amount
            return f"Success Your balance is {self.display_balance()}"
        else:
            return f"Insufficient funds. {self.display_balance()}"
    def deposit(self,amount):
        if amount>=0:
            self.balance=self.balance+amount
            return f"Success {self.display_balance()}"
        else:
            return f"Invalid amount {self.display_balance()}"
    
    def apply_interest(self):
        accumulated_interest_amt = self.balance * bank2.interest_rate
        self.balance += accumulated_interest_amt
        return f"Interest received. ₹{accumulated_interest_amt}"
    @classmethod
    def update_interest_rate(cls, updated_rate):
        cls.interest_rate=updated_rate
        return f"success"
    @staticmethod
    def get_total_no_of_accounts():
        return f"in total you have {bank2.no_of_accounts}"

sneha=bank2(128,"Sneha",100000)
Siva=bank2(128,"Siva",100000)
# Siva=bank2(128,"Siva",100000)
#get_total_no_of_accounts(),update_interest_rate()
# Class method - to construct the object
circle_from_dia = bank2.update_interest_rate(10)
print(bank2.interest_rate)
print(sneha.apply_interest()) 
print(sneha.display_balance()) 
print(bank2.get_total_no_of_accounts()) 

#Access specifiers
# Task  5
class SavingsAccount(bank2):
    interest_rate = 0.05
 
    def apply_interest(self):
        interest_amount = self.balance * self.interest_rate
        self.balance += interest_amount
        return interest_amount
 
 
sabesh = SavingsAccount(131, "Sabesh", 80_000)
 
print(sabesh.apply_interest())  # 5%
print(sabesh.get_balance())
 
 
# Task 6
# withdraw - transaction_fee - 10 Rupee
class CurrentAccount:
    pass
 
   
tanishq = CurrentAccount(132, "Tanishq", 90_000)
 
print(tanishq.withraw(1_000))
print(tanishq.withraw(10_000))
print(tanishq.get_balance())

#dir(x)
class Cat:
    def __init__(self, name, speed):
        self.__name = name
        self.__speed = speed
 
    # Override - (human readable)
    def __str__(self):
        # Human readable
        return f"Hi, I am {self.__name} with speed {self.__speed}"
 
    # Override -  (debugging)
    def __repr__(self):
        # Human readable
        return f"Cat('{self.__name}', {self.__speed})"
 
    def __add__(self, other):
        return self.__speed + other.__speed
 
    # Polymorphism:  Method overriding
    def speak(self):
        return "Meow!! 🐈"
 
 
pichu = Cat("pichu", 30)
snowbell = Cat("snowbell", 10)
 
print(pichu)
print(repr(pichu))
print(repr(snowbell))
 
print(pichu + snowbell)
 
# x = [5, 6, 7]
# print(dir(x))

# be carefull when to use self and class variable
# when we just want to access the variable we use self and when we want to change we use class variable
