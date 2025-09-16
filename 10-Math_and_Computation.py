import math

print(math.e, math.pi, math.nan, math.inf)

math.inf > 999999999  # True
math.isinf(math.inf)  # True
math.isfinite(math.inf)   # False, True if its not NaN or Infinite.

print(
    math.sqrt(144),     # 12
    math.log(3, 10),    # log of 3 with base 10
    math.log10(3),      # same as upper 
    math.pow(3, 2),     # 9
    math.ceil(3.1),     # 4
    math.floor(3.10),   # 3
    math.factorial(5),  # 120
    
    sep="\n"
    )



# Random
import random

print(
    random.randint(2, 20),
    random.random(),           # 0 to 1 --> float
    random.sample([20, 30, 40, 50, 11, 22, 33, "Python"], k=4),      # Random list of length 4 from provided list.
    random.choice([11,20, 30, 40, "Hassan"]),                        # Random value from the list.

                  
    sep="\n"              
    )