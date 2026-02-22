import math
import random
from datetime import datetime, timedelta
import matplotlib.pyplot as plt

radius = 7
area = math.pi * math.pow(radius, 2)
print("Circle area:", area)

numbers = [10, 20, 30, 40, 50]
random_number = random.randint(1, 100)
random_choice = random.choice(numbers)
print("Random integer:", random_number)
print("Random choice from list:", random_choice)

current_time = datetime.now()
future_time = current_time + timedelta(days=7)
print("Current time:", current_time)
print("One week later:", future_time)

x_values = list(range(1, 6))
y_values = [math.sqrt(x) * 5 for x in x_values]

plt.plot(x_values, y_values)
plt.title("Square Root Growth")
plt.xlabel("X values")
plt.ylabel("Y values")
plt.show()