# Functions have their own scope, meaning variables defined inside a function are local to it. 
from typing import Any

def hello_world():
    return "Hello World"


def sum(a:int, b:int = 40) -> float | int:
    return a + b
print(sum(b=10, a=20))


# Variable Scope of the Function
var = "Hello"
def do_something() -> None:
    # print(var)             # It works only when within func no lateron declaration of var varaible, otherwise give error
    var = "Hello Python"
    print(var)
do_something()
print(var)

age = 24
def update_age():
    global age
    age += 1
    print(age)
update_age()
print(age)     # Updated Age.



# Arguments Types
def args_example(*args) -> tuple[int, float] | Any:
    print(args, type(args))     # Returns Tuple
    return 10, 20, 30           # Returns Tuple
args_example('A', 'B', 'C', 'D')

def kwargs_example(**kwargs) -> dict[str, str|int]:       # Key will be str and value will be str or int.
    print(kwargs, type(kwargs))                 # Returns Dict
    return {"key01": "Value01", "key02": 02.2}  # Returns Dict
kwargs_example(Name="Hassan", Age= 24)       # Key will not come in Str quotes
    
def combine_example(*args, **kwargs) -> None:
    print(args, type(args))
    print(kwargs, type(kwargs))
combine_example(10, 20, 30, Name="Hassan", Age= 24)  # Works



# Anonymous Function (Use only once, doesnot need to re-use)
addition = lambda x, y = 30 : x + y
print(addition(10))

print(lambda : "Hello Python")      # Returns Function Reference as it doesn't called with ()
print((lambda : "Hello World!")())  # Function Called