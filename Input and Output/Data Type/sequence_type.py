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

print("-----------------------------------------")
# Tuples (Immutable Sequence)
tpl = (21,"Prince",10.03)
print(f"Tuple : {tpl}")
print(f"Element at index 1: {tpl[1]}")

print("Note: Tuples are immutable; their values cannot be altered after creation.")

# String 
str = "Hello Prince"
print(f"String Value : {str}")
print(f"String Negative Indexing : {str[-1]}")
print(f"String Positive Indexing : {str[0]}")

# String slicing
print(str[0:5])

# String Reverse
print("Reversed value: ", str[::-1])
print("Reversed value: ","".join(reversed(str)))

rev = ""
for ch in str:
   rev = ch + rev
print("Reversed value: ", rev)