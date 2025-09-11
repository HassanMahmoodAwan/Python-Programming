# Variables
name: str = "Hassan"
age: int = 24
isStudent: bool = False
height: float = 5.10
nullVar = None  # null value

print("Name:", name, "age: ", age, "isStudent: ", isStudent, "height: ", height)

print(f"My name is {name}", "I am {} years old".format(age), sep=" -- ")

# Type Conversion (Casting)
age_str = str(age)  # int to str
height_int = int(height)  # float to int (truncates decimal part)
isStudent_str = str(isStudent)  # bool to str ("True" or "False")
nullVar_str = str(nullVar)  # None to str ("None")

boolFlag = bool(0) # int to bool (0 is False)
boolFlag2 = bool(1) # int to bool (non-zero is True)
# -->  0, 0.0, "", None are considered False; everything else is True


# To check data type
print(type(name), type(age), type(isStudent), type(height), type(nullVar))


# Constants (by convention, use uppercase var names) --> Constants are not enforced by Python, but by convention, they shouldn't be changed
PI = 3.14159
GRAVITY = 9.81
SPEED_OF_LIGHT = 299792458
