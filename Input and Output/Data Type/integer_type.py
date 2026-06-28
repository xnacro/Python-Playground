# Write a program to demonstrate different number data types in Python. 
 
# integer data type
int = 23
print(f"Integer Value : {int} and type : {type(int)}")

# float data type
float = 40.01
print(f"Float Value : {float} and type : {type(float)}")

# complex data type
complexx = complex(3, 4)
complexx_2 = 3 + 4j
print(f"Complex Value : {complexx} and type {type(complexx)}")
print(f"Complex Value : {complexx_2} and type {type(complexx_2)}")

# extracting values from complex data
print(f"Extracting real part from complex data : {complexx.real}")
print(f"Extracting imaginary part from complex data : {complexx.imag}")