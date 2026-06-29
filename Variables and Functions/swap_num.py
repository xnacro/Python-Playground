# Program to swap two numbers using a temporary variable.  
a = 34
b = 67

print(f"before swapping value of a : {a}")
print(f"before swapping value of b : {b}")

c = a
a = b
b = c

print(f"after swapping value of a : {a}")
print(f"after swapping value of b : {b}")

# Program to swap two numbers without using a temporary variable. 
a = 567
b = 987

print(f"before swapping value of a : {a}")
print(f"before swapping value of b : {b}")

a, b = b, a

print(f"after swapping value of a : {a}")
print(f"after swapping value of b : {b}")