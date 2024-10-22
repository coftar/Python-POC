# class Dog:
#     def __init__(self, name, age, fur):
#         self.name = name
#         self.age = age
#         self.fur = fur


# dog1 = Dog('Rex', 5, 'brown')



# class Car:
#     def __init__(self, year, make, model)
#         self.year = year
#         self.make = make
#         self.model = model

# class Car:
#     def __init__(self,year, make, model):
#         self.year = year
#         self.make = make
#         self.model = model
    
#     def age(self):
#         return 2016 - self.year
        
# class Mustang(Car):
#     def __init__(self, year):
#         self.year = year
# Car.make = 'Ford'
# Car.model = 'Mustang'


def square(x):
    if type(x) != int and type(x) != float:
        return None 
    else:
     return x * x


print(square("steri"))