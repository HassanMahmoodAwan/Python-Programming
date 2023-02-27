# Using the Match-Case conditional statement and using operators like (+, -, *, /, //, **, square, pow, (), %)


def basic_Calculator(num_List):
    print("Enter the number")
    input_No = input("Enter the Symbol which you want to use as a operator: ")

    match input_No:
        case '+':
            print('The sum of two numbers is: ', num_List[0]+num_List[1])
        case '-':
            print('The minus of two numbers is: ', num_List[0] - num_List[1])
        case '*':
            print('The multiply of two numbers is: ', num_List[0] * num_List[1])
        case '/':
            print('The divide of two numbers is: ', num_List[0] / num_List[1])
        case '//':
            print('The divide without points of two numbers is: ', num_List[0] // num_List[1])
        case '%':
            print('The percentage of No1 with No2 is: ', num_List[0] % num_List[1])
        case '**':
            print('The power first no which is second no is: ', num_List[0] ** num_List[1])



def main():
    Total_Numbers = int(input("Enter How much numbers you want to enter right now give two: "))
    num_List = []
    for no in range(Total_Numbers):
        input_no = eval(input(f"Enter The {no+1} Number: "))
        num_List.append(input_no)

    basic_Calculator(num_List)



if __name__ == '__main__':
    main()