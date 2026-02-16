integer_num = 10
float_num = 3.14
complex_num = 2 + 3j

print(type(integer_num))
print(type(float_num))
print(type(complex_num))

string_text = "Hello"
my_list = [1, "apple", 3.14]
my_tuple = (10, 20)

print(type(string_text))
print(type(my_list))
print(type(my_tuple))

person = {
    "name": "Odiljon",
    "age": 20
}

print(person["name"])
print(type(person))

my_set = {1, 2, 3, 3}
print(my_set)

my_set.add(4)
my_set.remove(2)
print(my_set)

frozen = frozenset([1, 2, 3])
print(type(frozen))

is_active = True
print(type(is_active))

byte_data = bytes([65, 66, 67])
byte_array = bytearray([65, 66, 67])

print(byte_data)
print(byte_array)

text_number = "123"
converted_int = int(text_number)
converted_float = float(converted_int)
converted_str = str(converted_float)
converted_list = list("ABC")

print(converted_int, converted_float, converted_str, converted_list)

a = 10
b = 3

print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b)
print(a % b)
print(a ** b)

print(a == b)
print(a != b)
print(a > b)
print(a < b)
print(a >= b)
print(a <= b)

x = True
y = False

print(x and y)
print(x or y)
print(not x)

print(5 & 3)
print(5 | 3)
print(5 ^ 3)
print(~5)

num = 5
num += 2
num -= 1
num *= 3
num /= 2
num %= 4

print(num)

list1 = [1, 2, 3]
list2 = list1

print(list1 is list2)
print(2 in list1)
print(5 not in list1)

integer_input = int(input("Enter an integer: "))
float_input = float(input("Enter a float: "))
string_input = input("Enter a string: ")

print(type(integer_input))
print(type(float_input))
print(type(string_input))