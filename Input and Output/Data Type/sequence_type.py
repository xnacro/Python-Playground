# Write a program to demonstrate Sequence data types in Python. 

# List data type (Mutable Sequence)
lst = [1,3,5,"prince",20.01]
for i in lst:
   print(f"Original List : {i}")

# Accessing element via indexing
print(f"Positive Indexing : {lst[0]}")
print(f"Negative Indexing : {lst[-1]}")

# Modifying a list (Mutability)
lst[0] = "Anjali Gupta"
lst[1] = "Jatin Vishwakarma"
print(f"Modified List : {lst}")

# Adding items
lst.append("Janhvi")
print(f"Updated List after append: {lst}")