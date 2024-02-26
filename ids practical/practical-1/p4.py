# Write a program to print all even numbers within the range provided by the user.

x = int(input("Write the range in which you want to print even numbers: "))

for even in range(x):
    if(even % 2 == 0):
        print(even) 
