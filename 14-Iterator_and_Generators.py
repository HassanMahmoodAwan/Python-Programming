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
    """"""


if __name__ == "__main__":
    iterators()
    