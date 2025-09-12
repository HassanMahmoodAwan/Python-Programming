var = "Hello world"
multiline_str = """
This is multi-line String.
"""

# String Slicing ( var[start:stop:step] )
var[0]
var[-1]   # access last character
var[0:]   # From index 0 to end
var[::]   # Copy the whole string
var[::-1] # Reverse the string
var[0:7:2] # From index 0 to 6, step 2

# String Methods (Not in-place)
len(var)        

var.lower()      # to lowercase
var.upper()      # uppercase
var.capitalize()  # First letter uppercase
var.title()      # First letter of each word uppercase 

var.strip()      # Remove whitespace 
var.replace("world", "Python") # Replace substring
var.split(" ")  # Split string into list by delimiter
var.join(["Hello", "Python"]) # Join list of strings with var as separator
print(var.join(["Hello ", " Python"]))

var.index("o")  # Find index of first occurrence.
# var.index("X")  --> returns Value Error.
var.find("X")  # same as Index, but returns -1 if not found

print( var.count("l"))   # Count of occurrences
print( var.isalpha() )   # Check if all characters are alphabetic (no special chars or spaces)
print( var.isdigit() )   # Check if all characters are digits
print( var.isalnum() )   # Check if all characters are alphanumeric (no special chars or spaces, but can have digits)
print( var.isspace() )   # Check if all characters are whitespace




