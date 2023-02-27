
def fibonacci(n2, n1, exit_point, fib_list):
    fib_list.append(n1)
    fib_list.append(n2)
    for i in range(exit_point):
         result = n2+n1
         fib_list.append(result)
         n1 = n2
         n2 = result

    print(fib_list)



def main():
    no1 = eval(input("Enter a no1: "))
    no2 = eval(input("Enter a no2: "))
    exit_point = eval(input("Enter the exit point: "))
    fib_list = []

    fibonacci(no2, no1, exit_point, fib_list)


if __name__ == '__main__':
    main()