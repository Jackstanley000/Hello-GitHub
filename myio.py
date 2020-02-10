# three data types at input

# string
phrase = input("enter a string: ")
print("You said " + phrase)
print(f"You said {phrase}")

# float
someFloat = float(input("enter a float: "))
print("You entered a float: " + str(someFloat))
print(f"You entered float: {someFloat}")

# int
someInt = float(input("Enter an int: "))
print("You entered int: " + str(someInt))
print(f"you entered int: {someInt}")

# string interpolation is sweet
print(f"Do Python inline, like this: {someFloat} * {someInt} = {someFloat * someInt}")
