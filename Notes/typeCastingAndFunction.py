#Type casting is a way to convert one data type into another data type. In python, we can use the following functions to perform type casting.

a = 55
print("Type of a",type(a))

b = 5.5
print("Type of b",type(b))

c = "Hello"
print("Type of c",type(c))

print(str(a))
print(int(a))
print(float(a))

#Input function.


name = input("Enter your name : ")
print("Hello",name)

a = input("Enter a number : ")
b = input("Enter another number : ")
print(a + b) # it will concatenate the two numbers as strings.

#For sum and other arithmetic operations, we need to convert the input values into integers or floats.

def get_int(prompt):
    while True:
        value = input(prompt)
        try:
            return int(value)
        except ValueError:
            print("Please enter a valid integer.")


a = get_int("Enter a number : ")
b = get_int("Enter another number : ")
print(a + b)
