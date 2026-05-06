import math

# The 'math' package is a built-in module of Python that provides various mathematical operations 
# and functions including trigonometric, logarithmic (logarithm), square root finding or 
# power calculation. It also has constants like pi.

#Mathematical Operations
num = 8.99
print(round(num))
print(abs(-9.99))#Absolute - always return the positive

print('********* Math ***********')
print(math.ceil(num))
print(math.floor(num))

# Define variables
a = 5
b = 3

# Basic Arithmetic Operations
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)

# Exponential and Logarithmic Operations
exp_result = a ** b
log_result = math.log(a)
exp_base_10_result = a ** b
log_base_10_result = math.log10(100)

# Trigonometric Operations
sin_a = math.sin(math.radians(30))
cos_a = math.cos(math.radians(30))
tan_a = math.tan(math.radians(30))

sin_b = math.sin(math.radians(45))
cos_b = math.cos(math.radians(45))
tan_b = math.tan(math.radians(45))

# Hypotetical Operations
c = 3
d = 4
result = math.sqrt(c**2 + d**2)

print("Square Root of", 16, "is:", math.sqrt(16))
print("Exponentiation of", a, "to the power of", b, "is:", exp_result)
print("Logarithm of", a, "is:", log_result)
print("Exponentiation of", a, "to the power of", b, "with base 10 is:", exp_base_10_result)
print("Logarithm of", 100, "with base 10 is:", log_base_10_result)
print("Sine of", 30, "degrees is:", sin_a)
print("Cosine of", 30, "degrees is:", cos_a)
print("Tangent of", 30, "degrees is:", tan_a)
print("Sine of", 45, "degrees is:", sin_b)
print("Cosine of", 45, "degrees is:", cos_b)
print("Tangent of", 45, "degrees is:", tan_b)
print("Hypotenuse:", result)

