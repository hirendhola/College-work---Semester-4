# Write a program to compute the factorial of a number given by the user. (while)
x = int(input("Write number to find factorial: "))

ans = 1 # ans
i = x # current number 

while i >= 1:
    ans *= i
    i -= 1

print("Factorial is:", ans)
