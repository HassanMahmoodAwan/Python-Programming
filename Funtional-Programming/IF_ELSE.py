# There is a function which can be used instead of IF-else which is ()  but it can be used of only two conditions.
def if_else():
    total = 30
    a = int(total)
    # In one string If wanted to use variable to we use {}.
    gained_marks = eval(input(f"Enter the obtained marks in Programming b/w 0- {total} : "))
    if ((gained_marks / total) * 100) >= 50:
        print("You have successfully passed the exam and promoted to new subject")
        if ((gained_marks / total) * 100) >= 90:
            print("You got 4.0 GPA ")
        elif ((gained_marks / total) * 100) >= 85:
            print("You got 3.7 GPA")
        elif ((gained_marks / total) * 100) >= 80:
            print("You got 3.3 GPA")
        elif ((gained_marks / total) * 100) >= 75:
            print("You got 3.0 GPA")
        elif ((gained_marks / total) * 100) >= 70:
            print("You got 2.7 GPA")
        elif ((gained_marks / total) * 100) >= 65:
            print("You got 2.3 GPA")
        elif ((gained_marks / total) * 100) >= 60:
            print("You got 2.0 GPA")
        elif ((gained_marks / total) * 100) >= 55:
            print("You got 1.7 GPA")
        elif ((gained_marks / total) * 100) >= 50:
            print("You got 1.3 GPA")

    else:
        print('Oops! You didn\'t qualify for the next semester as it is prerequisites')


def main():
    if_else()


if __name__ == '__main__':
    main()
