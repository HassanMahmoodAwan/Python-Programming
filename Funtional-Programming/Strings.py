# Strings Operation and some of its shorthand

def quotes():
    # For using Quotes in  the string. All method work same. (\, "''", '""')
    print('Hello! Hassan how are you. don\'t use phone more than two hours')
    print("Hello! Hassan how are you. don't use phone more than two hours")
    print('Hello! Hassan how are you. don"t use phone more than two hours')

    # For new line we can use (\n :: If you want to print \n then use r before string or  """\ """)
    print('Hello! Hassan how are you.\ndon\'t use phone more than two hours')
    print(r'Hello! Hassan how are you.\n don\'t use phone more than two hours')

    print("""\
    Usage: thingy [OPTIONS]
         -h                        Display this usage message
         -H hostname               Hostname to connect to
    """)


# Concatination and some tricks
def cat():
    one = 'Hello'
    two = '! '
    name = 'Hassan'
    greetings = one + two + name
    print(greetings)
    # Some Slicing and cat techniques
    a = name[:2]  # make Ha :: 2 index excluded
    full_name = name[0:2] + name[2:]   # Gives us full name.
    print(full_name)
    out_of_range = name[2:42]  # out of range slicing handle gracefully. started from index 2 and go till end.
    print(out_of_range)
    return one + two + name


def string_builtin_func():
    string = "Fibonacci Series"
    print(len(string))
    print(string.capitalize())
    print(string.find("on"))
    print(string.casefold())  # It works like string.lower with a feature  if i type german word make it in english
    print(string.format())
    print('acc' in string)
    print(string.upper())
    print(string.lower())
    print(string.isupper())


def main():
    # print('''Hello Hassan Kia''')
    # print(quotes())
    # cat()
    string_builtin_func()


if __name__ == '__main__':
    main()


