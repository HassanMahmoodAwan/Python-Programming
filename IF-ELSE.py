def recovery_question():
    question = "What is my mother name"
    return question


def customer_record():
    name = "Hassan"
    age = 21
    cinic = '35200-12234365'
    account_pin = 2200
    account_type = "debit"
    account_balance = 5000
    return name, age, cinic, account_balance


def Pin_setup_system(pin, recovery_answer):
    key = eval(input("Enter the password to enter in a bank and check balance"))
    if key == a:
        print("you have permission to get bank account and get the credential")
        bank_balance = int(1000)
    
    elif key != a:
        forget_recovery = input("Enter the answer for your recovery question which is "+ recovery()+ " :") 
        if forget_recovery == b:
            print("Now you can change your Password")
            new_password = eval(input("Enter new password must be in 8 letters and not having special characters :"))
            a = new_password


def main():
    # print("heel")
    name = customer_record()
    print(name)
    age = name[1]
    print(age)

if __name__ == '__main__':
    main()
