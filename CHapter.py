import sys
import random as rd
# sys.path.append(File path)
# import function   # then able to use it in your code.

import math  # library for math functions, and it is developed in C/C++ lang.
from math import sqrt  # work as same as upper work. but for specific built-in function


def evaluate(value=4, num=3):  # default value
    # num = eval(input('enter a number to have sum :'))
    sums = num + value
    return sums


def command_line_argv():  # to run go to cmd and go to path and write python3 filename argv[1] argv[2]
    if len(sys.argv) == 3:
        length = int(sys.argv[1])
        width = int(sys.argv[2])
        return evaluate(length, width)





def asserting(total=50):
    math_marks = int(input("enter the marks :"))
    assert 0 <= math_marks <= 100   # means math_marks >=0 and math_marks <=100
    total = 100
    return 'total marks in math is ', math_marks, 'out of ', total  # what it will give output on printing without
                                                                    # watching the sol.


def main():
    # print("todo here")
    value = 10
    # print(evaluate(value), type(evaluate()))
    print(type(int), round(0.00345, 4))
    print(pow(value, 2))
    exponential = math.exp(3)  # power of e, e is exponential and its value is e=2.7182, check it in calculator.
    print(exponential)
    print(sqrt(value))
    # try other math build-in func such as ceil(), floor(), sin(), tan(), degrees(), radians(), e.t.c
    print(dir(math.pow(2, 3)))  # for your guidance. there is also a help module.
    # help you about function evaluate, you can take help of any type, if you are new you can run help() for guidance.
    help(evaluate)
    print(asserting())
    print(command_line_argv())
    rand = rd.random()+2  # generate b/w 0-1.
    randint = rd.randint(1, 100)  # gen b/w 1-100
    print(rand, '\t',  randint)


if __name__ == '__main__':
    main()
    print("\t Program Ended")





