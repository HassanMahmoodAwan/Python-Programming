# List like an array. [ "Duplicate", "All DataTypes Allowed", "Ordered", "Mutable", "List-wise Op", "Passed by Reference" ]
from typing import Any

def lists() -> Any:
    array: list[int | str | ...] = [10, 12.2, "Hassan", True, None, "check"]
    list((10, 20, 30)) # Using Constructor, But need to convert Tuple to list
    
    len(array)
    array[2:3]   # gives only one Element.
    array[::]    # Whole List.
    array[-1]
    
    # Replaced Actual value
    array[2:3] = list((10,20,30))
    array[-1] = [20, 20]   # Nested
    array[-1:] = [20, 20]  # works
    array[-1::] = [20, 40] # Same as upper. 
    
    print(array)



if __name__ == "__main__":
    lists()