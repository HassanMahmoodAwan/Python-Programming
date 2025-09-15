from copy import deepcopy

def dictionary():
    """ Dict are {Mutable, No Duplicate, All-Datatypes, Passed by Reference, unOrdered} """
    
    person:dict[int | str | bool | float] = {
        "Name": "Hassan",
        "Age": 24,
        "City": "Lahore",
        "isStudent": False,
        "Height": 5.10,
        1: "Hello Python"
    }
    computer = dict(Model="Dell", Gen="I5 6th", RAM=16, Storage=756)
    computer["Model"] = "Dell Precision"
    
    # Methods 
    person.get("Age", "Not finded")
    person.get("No Key", -1)        # returns -1
    
    person.update({"Name": "Hassan Mahmood", "Profession": "Software Engineer"})
    
    len(person)
    person.items()   # Nested List
    person.keys()
    person.values()
    
    person.pop("City")
    # person.popitem()       # Pop the last Item.
    #del person["City"]      # if not in it, gives KeyError.
    # person.clear()         
    # del person             # delete varaible from memory
    
    # Shallow and DeepCopy.
    new_computer = computer
    new_computer.update({"GPU": None})
    
    deepcopy_computer = computer.copy()
    deepcopy_computer.update({"Name": "Dell Precision 3420"})
    deepcopy_computer = deepcopy(computer)
    
    
    # Dict Comprehension
    dict_comprehension = {key+1: value for key, value in enumerate(["Burger", "Pizza", "Sandwiches", "Soft Drink"])}
    print(dict_comprehension)
    
    print(person)
    
    


def sets():
    pass



if __name__ == "__main__":
    dictionary()