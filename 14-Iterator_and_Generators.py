def iterators():
    """Iterators are like iterating on a varaible one by one if varaible have multiple values. Can be next iterate anywhere in program.
    
    Iterable: An object on which you can loop or Iterate like a book.
    Iterator: Like a bookmark on a book, page by page.
    
    Most objects on which you loop over them are Iterables, like String, List, dict(Gives Keys), etc. you can iterator on them as well.
    
    """
    fruits = ["Mango", "Banana", "Apple"]
    
    iterator = iter(fruits)
    try:
        print(next(iterator))   # Mango
        print(next(iterator))   # Banana
        print(next(iterator))   # Apple
        print(next(iterator))    # Raise StopIteration Error.
    except StopIteration as e:
        print("Iteration Error: ", e)


def generators():
    """Generators are Special Iterators automatically created by Python when yield within Function or () is used. Its is Memory Efficient and Provide result one by one. Whereas functions return statement provide result all at once. 
    
    -> Yield is used with function instead of return. 
    """
    
    def gen_example01():
        counter = 1
        while counter < 5:
            yield counter
            counter += 1

    iterator = gen_example01()
    print(next(iterator))      # 1
    print(next(iterator))      # 2
    print(next(iterator))      # 3
    print(next(iterator))      # 4
    
    
    
    generator_comprehension = (num for num in range(2, 20) if num %2 == 0)       # Generator faster & memory Efficient compare to List, etc.
    print(next(generator_comprehension))   # 2
    print(next(generator_comprehension))   # 4
    
    for even_values in generator_comprehension:       # Returns 6 to 18 as already 2 and 4 Iterated.
        print(even_values, end="\t")
    
    
    def gen_example03():
        """As File content is large, its efficient to yield line by line instead of return all at once."""
        with open("largeFile.txt", "r") as file:
            for line in file:
                yield line
    for line in gen_example03():
        print(line)



if __name__ == "__main__":
    # iterators()
    generators()
    