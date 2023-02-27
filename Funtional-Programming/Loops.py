# there are three types of Loops
# 1- For loop  :: For In, For In Range,
# 2- While Loop
# 3- Do While Loop


def for_loop():
    # Dictonory or collection of Cars with price affordability tag
    dict_cars = {'G-Wagon' : 'expensive', 'Honda HRV':'expensive',
                 'Honda Civic 2022':'expensive', 'Honda Civic 1998':'Inexpensive', 'Toyota passo 2021':'Inexpensive'}
    # For IN loop example.
    for cars in dict_cars:
        print(cars, len(cars))
    # For multiple selection and to iterate over it we need to use items() func. otherwise it will throw an error.
    for cars, tag in dict_cars.items():
        print(cars, tag, len(cars))
    # It created the copy of the collection and then iterate over it.
    # for cars, tag in dict_cars.copy().items():
    #     print(cars, tag, len(cars))

    # For LOOP with range funciton and range function
    lists = ['a', 'b', 'c']
    # for cars in range(len(dict_cars)):  # Up till, yet it does not iterate over dictionary, so I iterate over list.
    for letters in range(len(lists)):  # range only take integer, so I use len for it.
        print(lists[letters])

    print(sum(range(10))) # sum of all first 10 no (0-9).



def main():
    for_loop()


if __name__ == '__main__':
    main()
