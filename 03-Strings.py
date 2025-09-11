var = "Hello world!"
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

# String Methods
len(var)         # Length of the string

var.lower()      # to lowercase
var.upper()      # uppercase
var.capitalize()  # First letter uppercase
var.title()      # First letter of each word uppercase

var.strip()      # Remove whitespace
var.replace("world", "Python") # Replace substring not in-place
var.split(" ")  # Split string into list by delimiter
var.join(["Hello", "Python"]) # Join list of strings with var as separator

var.index("o")  # Find index of first occurrence of substring
var.index("X") # returns Value Error.
var.find("X")  # same as Index, but returns -1 if not found

var.count("l")  # Count of occurrences
var.isalpha()   # Check if all characters are alphabetic
var.isdigit()   # Check if all characters are digits
var.isalnum()   # Check if all characters are alphanumeric
var.isspace()   # Check if all characters are whitespace




