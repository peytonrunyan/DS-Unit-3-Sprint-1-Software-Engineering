# source video: https://www.youtube.com/watch?v=ZDa-Z5JzLYM
# you should watch it when you have some time

# method: fxn associated with a class

# class is a blueprint for making instances
class Employee:
    pass

# employee_1 and emp_2 are instances of Employee
employee_1 = Employee() 
emp_2 = Employee() 

# we can manually add attributes to instances
# name is an attribute in this case
employee_1.name = 'jill'
emp_2.name = 'mike'

# this can get messy when you have to give many instances to many attributes
# to set this up automatically, we use 'init' method

# -------------------------------------------------

class Employee:
    
    def __init__(self, name, favorite_animal):
        self.name = name
        self.favorite_animal = favorite_animal

# self can be confusing, so here's a quick explanation:
# employee_1 = Employee('jill','tasmanian tiger')
# the name 'employee_1' essentially replaces 'self'
# instead of 'self.name' we can say 'employe_1.name' and get the name attribute back
# same for self.favorite_animal, we can now do employee_1.favorite animal
# if we do emp_2 = Employee('mike','cat') we can do the same with emp_2
# replace self with emp_2 and you get emp_2.name = 'mike' and emp_2.favorite_animal = 'cat'

employee_1 = Employee('jill','tasmanian tiger')
emp_2 = Employee('mike','cat')

# what if I want to see the name of emp_2 and their favorite anima? One option:
print('{} {}'.format(emp_2.name, emp_2.favorite_animal))

# that could get tedious quickly. we can 'automate' this using a method
# remember from line 4, method: fxn associated with a class

# -------------------------------------------------

class Employee:
    
    def __init__(self, name, favorite_animal):
        self.name = name
        self.favorite_animal = favorite_animal
    
    # turn the function from line 42 into a method (a function within a class)
    def deets(self):
        """ 
        gives all the juicy details that we have about
        an employee
        """
        return '{} {}'.format(self.name, self.favorite_animal)
        # notice that we had to change emp_2 to self in the return statement
        # this allows us to make the function work for any instance of this class
        # also, you cannot forget 'self' in the function definition if you want it to work on an instance
        # emp_2.deet() is the same as Employee.deets(emp_2)
        # we want to get the deets about emp_2, this means that emp_2 is a positional argument
        # by using 'def deets(self):' we let python know that it should expect 1 argument to go into this function
        # it also tells it that the 1 argument is going to be the instance (e.g. emp_2 or employee_1)


print(emp_2.deets())
# emp_2 is our 1 positional argument, deets() is our method
# notice that we had to put () after deets. This is because it's a method, not an attribute