my_tuple = (1, "apple", 5.2)

try:
    # Element index starts from 0, so element 3 is at index 2
    index = my_tuple.index(3)
    print("Index of element 3:", index)
except ValueError:
    print("Element 3 not found in the tuple.")

