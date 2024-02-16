# Write a function to display maximum of three numbers

def max_number(nums):
    max = nums[0]
    for x in nums:
        if(x > max):
            max = x
    return(max)

list = []
n = 3 # can be taken from user also

for i in range(0, n):
    num = int(input())
    list.append(num)    

print("max number is: ", max_number(list))