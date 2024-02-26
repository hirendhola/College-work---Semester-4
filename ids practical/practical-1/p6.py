# Write a function to display digit at unit place of a given number

def unit_place(x):
    ans = x % 10
    return ans

print(unit_place(int(input("enter number: "))))