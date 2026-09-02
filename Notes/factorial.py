num = int(input("Enter your number :"))
factorial = 1

while num < 0:
    print("Factorial does not exist for negative numbers")
    

for i in range(1, num + 1):
    factorial *= i

print(f"The factorial of {num} is {factorial}")