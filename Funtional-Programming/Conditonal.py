import sys


def gpa(name, rollno, marks, subject):
    for i in range(int(len(subject))):
        print("hello")


def main():  # main function for all code.
    student_name = input("Enter the student name : ")
    student_rollno = input("Enter the student name : ")
    marks = []
    subject = ['Operating System', 'DCCN', 'DAA', 'NC', 'DWH']
    for i in range(5):
        print("Subject: ", subject[i], end='')
        var = int(input(" enter the marks in : "))
        marks.append(var)

    print(marks)


if __name__ == '__main__':
    main()
   # print("%5d"% +"end of program")

