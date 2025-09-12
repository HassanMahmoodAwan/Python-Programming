# If-Else 
if True:
    print("Hello Python!")
else:
    "Not Executed"

    
marks: int = 73
if marks >= 80 and marks <= 100:
    "Exellent"
elif marks >= 70:
    "Good Result"
else:
    "Need Improvment"
    

# Variable Scope (have global scope, not block scope)
if True:
    a = 20
print(a)


# Match-Case (Limitation: Doesnot provide range in cases)
age = 24
match age:
    case 24:
        "Time to Learn"
    case 30:
        "Time to think retirement"
    case _:
        "Enjoy"
    
    
