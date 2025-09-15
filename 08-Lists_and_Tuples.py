# List like an array. [ "Duplicate", "All DataTypes Allowed", "Ordered", "Mutable", "List-wise Op", "Passed by Reference" ]
from typing import Any
from copy import deepcopy

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
    
    
    # Methods (InPlace)
    array.append(393.3) # appended at last
    array.insert(3, 13) # add new one.
    array.insert(20, "Hassan") # If index exceed len of list, append at last
    array.extend(["54243"]) # provide a list appended at the last
    
    array.pop() # remove from last.
    array.pop(-1)
    # array.remove("not in list")  --> Error Value Error.
    del array[5]             
    # del array           # will delete the whole varaible from memory
    # array.clear()       # only empty the list.
    
    array.reverse()
    array[::-1]      # Slicing not inplace.
    
    print(array.count(20))
    print(array.index(True))       # If not returns -1.
    
    temp_array = [10, 40, 7, 3.3, 10212, 2]
    temp_array.sort(reverse=False)           # Only works when homogenious DataTypes.
    print(temp_array)
    del temp_array
    
    
    # Shallow ( Changing one will change other ) and DeepCopy( Chaning one will not effect other ).
    shallowcopy_array = array
    shallowcopy_array.append("changed both array")
    
    deepcopy_array = array.copy()
    deepcopy_array.append("not changes the copied array.")
    deepcopy_array = deepcopy(array)

    
    # List Comprehension
    even_num_array = [num for num in range(1, 20, 1) if num % 2 == 0]
    print(even_num_array)
    
    
    print(array)


if __name__ == "__main__":
    lists()