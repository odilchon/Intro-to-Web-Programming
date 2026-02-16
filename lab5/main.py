name = "Odiljon"
print("Name:", name)

num1, num2 = 7, 4

print("Addition:", num1 + num2)
print("Subtraction:", num1 - num2)
print("Multiplication:", num1 * num2)
print("Division:", num1 / num2)

print("Before swap:", num1, num2)
num1, num2 = num2, num1
print("After swap:", num1, num2)

PI = 3.1415926
radius = 5
area = PI * radius ** 2
print("Area of circle:", area)

user_name = input("Enter your name: ")
user_age = int(input("Enter your age: "))

print(f"Hi {user_name}, you are {user_age} years old.")

a, b, c = map(int, input("Enter three numbers separated by space: ").split())

total = a + b + c
average = total / 3
product = a * b * c

print(f"Sum: {total}")
print(f"Average: {average}")
print(f"Product: {product}")
