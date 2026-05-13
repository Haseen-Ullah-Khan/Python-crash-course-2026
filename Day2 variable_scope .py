#Variable Scope in Python

# #local variable 
def func1():
    text="Programming is easy "
    print(text)

func1() # when we call a function , it will print the text in a output terminal 
#print(text) # but when we print the variable name text outside the function , it will raise an error .

# Non_local variable 
def func2():
    text2="Python programming is easy "
    def inside_func():
        print(text2)
    inside_func()

# func2() # we define a nested function in func2 , the variable text2 is declared in th func2 function , but we can access it in the nested function.that's called non local variable

# Global variable 
def func3():
    global name  # we initialize the variable name as global , as it can be accessed from any where in the program 
    name="Haseen Ullah Khan "
    print(f"This is accessed from inside of the function {name } ")

func3() 
print(f"This is accessed from out side of the function {name} ")
# Note**********************************************************
"""Modifying the global variable inside a function in Python
When we try to modify a global variable inside a function it gives an error, as functions can only access.""" 
 # by using  global variable cannot change the value of the non local variable . you can only do this by using the non_local keyword , the changes in the inner side function can reflect in the outer side function
 # by accessing the non_local variable in the nested (inner) function .the variable in the nested function is now called 'enclosed variable'

"""You can change only the non local variable by the nested funtion by using the nonlocal keyword"""
def A():
    name="Haseen"
    print(f"Before effecting the variable name {name}")
    def B():
        nonlocal name 
        name=name+"Khan"
        print(f"After effecting the non_local variable by the nested function {name}")
    B()
    print(f"name variable in the outer function after effecting by the nested function {name}")

A()
""" Here is the Alternate way to effect the Non_local variable from the nested function
"""
def A1():
    A1.a=5
    print("Before effecting",A1.a)
    def B():
        A1.a=6
        print("effecting by inner function ",A1.a)
    B()
    print("After effecting it by nested function ",A1.a)
A1()

#****************important note*******************

# a. Built-in scope: This is the scope of all the keywords. This is the largest scope. These load when the interpreter starts and we can access them from any part.
# b. Global scope: This is the scope of the variables that are created outside the functions. These can be accessed from any part of the program.
# c. Local scope: This is the scope of the variables created inside the functions. These exist only while the function is executing. We cannot access them outside the function
# d. Enclosed or nonlocal scope: This case occurs when we have nested functions. The variables in the outer function are neither global nor local to the inner function. These have nonlocal scope.