# For Loop (iteration value is determined at start of loop, so modifying it inside the loop body has no effect on loop’s sequence)
for value in range(1, 10, 2):
    print(value)
    
for index, value in enumerate("Hello Python"):
    print(index, value, sep="\t")
    


# While Loop (changes in Loops body will have effect on Iteration Cycle.)
while True:
    print("Infinite Loop")
    break

counter = 0
while counter < 5:
    print("Runs 5 Times")
    counter += 1
   
    

# Flow Controller (No Finally in Loops)
for char in "hello Python":  # Runs Complete, but do Nothing
    continue
    print("Char will not be Printed", char)

counter = 10
while counter > 0:
    print("Hello Python Loop: ", counter)
    if counter == 4:
        break
    counter -= 1
    continue
    print("Hello")
else:
    "If not Break, completes its flow, then Else will run"
