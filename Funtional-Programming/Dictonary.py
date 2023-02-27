# No duplicate, mutable and ordered colleciton.
# Its related to Hash Tables as in Hashing It contains the key:value pair.


def dict():
    section = {
        "Name": "Hassan",
        "Roll No":"Sp20-Bcs-114",
        "Section":"FA20-BCS-B",
        "Subject":"Artificial Intelligence"
    }

    #Dict Item can be access
    print(section["name"])

    # Creating the Dictonary using Constructor or method.
    MyDict = dict(name='ABC', section="B")

def main():
    dict()


if __name__ == '__main__':
    main()