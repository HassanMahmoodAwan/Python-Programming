# Arithmatic Operators: +, -, *, /, //, %, ** (BEDMAS Rule --> left to Right) In Exponent, its Right to Left
a: int = 10
b: float = 20.1
result = a + b * 4 / 6 ** 2 + (5 - 3)
print(result)
print(9 // 4, 9 / 4) # // -> Int, / -> always Float


# Relational Opertors: >, <, <=, >= , ==, !=, <<, >>   --> (return Boolean)
print(a >= b, a != b, a <= b, a < b, sep=", ")
print( 10.0 == 10 )
print(True == bool(1), "True" == str(bool(1)) )


# Logical Operators: and, or, not   --> (return Boolean)
print(10 < 20 and 20 > 10)    # both needs to be True.
print( 10 > 20 or 20 > 10)
print(not 10 < 20 and 20 > 10)


# Mapping Operators: in, not in, is, is not    --> (return Boolean)
print("ss" in "Hassan")
print("A" not in "Hassan")  # True, case Sensative.

x = 10
y = 10     # Pointing to same location as x
z = 10.0      

print(x is y)
print(y is z)  # False, different Object reference.
print(x is z)  # False,  //       //       //