def square(num):
    return num ** 2

print("Square of 5:", square(5))

def sum_all(numbers):
    total = 0
    for num in numbers:
        total += num
    return total

print("Sum of list:", sum_all([1, 2, 3, 4, 5]))


def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

print("Fibonacci(6):", fibonacci(6))

def is_prime(num):
    if num <= 1:
        return False

    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False

    return True

print("Is 7 prime?", is_prime(7))
print("Is 10 prime?", is_prime(10))