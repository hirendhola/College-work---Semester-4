mylist = []
tupple = ( 1,2,3, 'data', 'science', 2, 3 )
size = int(input("Enter size of List: "))
for i in range(size):
    x = int(input("Enter {} value: ".format(i+1)))
    mylist.append(x)
print(mylist)

# 7.Display sum of numbers given in the above created list.

print(f"sum of all the elementis {sum(mylist)}")

#8. Remove duplicate elements from the above created list.

removed_duplicate_set = set(mylist)
print(f"without duplicate {list(removed_duplicate_set)}")

# 9. Extend the list with the tuple created above. (extend method of list)
mylist.extend(tupple)
print(f"extended list: {mylist}")
