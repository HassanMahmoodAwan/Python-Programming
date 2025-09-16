""" Exception: Program Syntactically Correct but Internal Event (Dynamic Error) stop flow of the program.

Advantages:     { Reliable, Easy Debugging, CleanerCode, Readable}
Disadvantages:  { slow Performance, lengthy}

Some main types of Exception:
--> ZeroDivisionError: When any number divided by 0.
--> KeyError:          If key doesnot exist. 
--> IndexError:        Index doesnot Exist Error.           
--> TypeError          Operation cannot be perform on that Type.
--> ValueError         Occured if Type Casting Failed.

"""

try:
    a = 10
    b = 20
    print(a + b)
    print(a + "b")
except Exception as e:
    print("Exception occurs: ", e)
    
    
try:
    divsion = 22 / 0
except ZeroDivisionError as e:
    print("As dividing any number by zero: ", e)
else:
    "works when No exception occurs"
finally:
    "Excecute every time dispite error occurs or not"


try:
    sum = 10 + "-20"
except TypeError as e:
    print("Error occured as Type Mis-matches: ", e)
    

try:
    obj = {2.4: 24}
    print(obj["not exsist"])
except KeyError as e:
    print("Key doesnot exist: ", e)


try:
    f:int = "20sd"    # Doesnot give error? why?
    int(input("Enter the Number value otherwise value Error: "))
except ValueError as e:
    print("Inapprpriate Type: ", e)


try:
    temp_str = "Hello Python"
    temp_str[23423]
except IndexError as e:
    print("Index doesnot Exsist: ", e)
    
    

try:
    raise KeyError("Key Error Occured")
except KeyError as e:
    print("Error Occured: ", e)             # Error Occured: 'Kye Error Occured'

