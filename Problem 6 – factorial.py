factorial = 1
num = int(input("Enter an integer: "))
if (num < 0):
    print("Factorial of a negative number can not be calculated")
elif num == 0:
    print("The factorial of 0 is", 1)
for i in range(1,num+1):
    factorial = factorial * i
print("The factorial of", num, "is", factorial)

# Kelly Beltran
# 02-19-24
# Problem 6: an integer is entered, once entered if number is <0 message is printed
# if 0 is entered factorial of 1 in printed, any other number entered factorial is calculated
