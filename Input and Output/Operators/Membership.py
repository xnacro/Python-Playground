# Program to show the working of Membership operators..

lst = [1, 2, 3, 4, 5]   # Python creates a brand new list at Memory Address A
lst2 = [1, 2, 3, 4, 5]  # Python creates a SEPARATE list at Memory Address B

# using membership operators to check if the elements are present in the list
print(1 in lst)  # True
print(6 in lst)  # False
print(6 not in lst)  # True
print(1 in lst2)  # True