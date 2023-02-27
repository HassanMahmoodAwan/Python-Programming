# No duplicate, mutable and ordered colleciton.
# It's related to Hash Tables as in Hashing It contains the key:value pair.

# List are Mutable

def dictionay(num_list):
    section = {
        "Name": "Hassan",
        "Roll No": "Sp20-Bcs-114",
        "Section": "FA20-BCS-B",
        "Subject": "Artificial Intelligence"
    }

    #Dict Item can be access
    print(section["Name"])

    # Creating the Dictonary using Constructor or method.
    MyDict = dict(names='ABC', sections="B")

    # Input using the student.
    student = {}
    for i in range(len(num_list)):
        name = input("Enter the name of student: ")
        Semester = input("Enter the Semester of Student")
        student[name] = Semester;

    print(student)

    # Merging the Dictionary using the update func.
    updated_list = {'Hamid' : '6'}
    student.update(updated_list)

    print(student)



def list(num_List):
    prime_Nos = [2, 3, 5, 7, 11, 13]
    # print(prime_Nos[:], prime_Nos[-5:-1])

    prime_Nos + [17, 19, 23]  # List are mutable which means they can be shrunk or grow
    # print(prime_Nos + [17, 19, 23])  # List are mutable which means they can be shrunk or grow
    # print(prime_Nos)  # It remains the same as initial
    prime_Nos = prime_Nos + [17, 19, 23]  # but results changes as we now assign to it and these values added.
    prime_Nos.append(29)  # added in the last.
    # print(prime_Nos)

    # Nested List
    fruits = ['apple', 'orange', 'banana']

    results = [fruits, prime_Nos]
    # print(results, len(results))  # length prints 2 as it has only two objects which individually are entire list.

    # List making using the range() function.
    # print(list(range(10)))   #Not working check it out later

    # Putting the VALUES IN another list.
    result = []
    for value in num_List:
        result.append(value)
    print(result)

    # Merging of two Data Structures
    second_list = [5, 6, 10, 8]
    result_List = num_List + second_list
    print(result_List)




def tuples(num_list):
    # Ordered, Immutable, ALLOW duplicate.
    tpl = tuple(num_list)
    print(tpl)

    # Merging the Tuple using the update func.
    updated_tuple_list = (10, 4)
    tpl.update(updated_tuple_list)

    print(tpl)

def sets(num_list):
    # No duplicate values and
    key = eval(input("Enter a number to find in the set: "))
    list_to_set = set(num_list)
    print(list_to_set)
    for i in list_to_set:
        if i == key:
            print("The index of exist no is " + str(i) + "index")
            break
    print('element not found')

    # Merging of two Data Structures
    updated_set = {2, 4, 5, 6}
    list_to_set.update(updated_set)
    print(list_to_set)



    # Main Function
def main():
    Total_No = int(input("Enter How much numbers you want to Put in Data Structures: "))
    num_List = []
    for no in range(Total_No):
        input_no = eval(input(f"Enter The {no + 1} Number: "))
        num_List.append(input_no)

    # dictionay(num_List)
    # list(num_List)
    # tuples(num_List)
    sets(num_List)




if __name__ == '__main__':
    main()