# Program to show the working of Identity operators..

lst = [1, 2, 3, 4, 5]   # Python creates a brand new list at Memory Address A
lst2 = [1, 2, 3, 4, 5]  # Python creates a SEPARATE list at Memory Address B
lst3 = lst              # Python makes lst3 point directly to Memory Address A


# checking memory address of the lists
print(f"Memory Address of lst: {id(lst)}")
print(f"Memory Address of lst2: {id(lst2)}")
print(f"Memory Address of lst3: {id(lst3)}")

# using identity operators to check if the lists are the same
print(lst is lst2)  # False
print(lst is lst3)  # True
print(lst2 is not lst3) # True

