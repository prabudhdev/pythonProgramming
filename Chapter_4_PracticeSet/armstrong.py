n = int(input("Enter a number:"))
sum = 0
num = n
while num > 0:
    digit = num % 10
    sum+= digit ** 3 
    num //= 10
if n == sum:
     print("The number is an Armstrong number.")
else:
    print("The number is not an Armstrong number.")