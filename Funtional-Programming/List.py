# List are mutable which mean you can change its value later on whereas strings are immutable.

def list():
      prime_Nos = [2, 3, 5, 7, 11, 13]
      print(prime_Nos[:], prime_Nos[-5:-1])
      prime_Nos + [17, 19, 23]   # List are mutable which means they can be shrunk or grow
      print(prime_Nos + [17, 19, 23])   # List are mutable which means they can be shrunk or grow
      print(prime_Nos)  # It remains the same as initial
      prime_Nos = prime_Nos + [17, 19, 23]  # but results changes as we now assign to it and these values added.
      prime_Nos.append(29) # added in the last.
      print(prime_Nos)

      # Nested List
      fruits = ['apple', 'orange', 'banana']

      results = [fruits, prime_Nos]
      print(results, len(results))  # length prints 2 as it has only two objects which individually are entire list.

      # List making using the range() function.
      print(list(range(10)))   #Not working check it out later

def main():
    list()


if __name__ == '__main__':
    main()