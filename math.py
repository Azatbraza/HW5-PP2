import math
import random
import statistics

angle = math.radians(30)
print(math.sin(angle))
print(math.cos(angle))
print(math.tan(angle))


even_number = random.randrange(0, 100, 2)
print(even_number)


numbers = [random.randint(1, 100) for _ in range(10)]

print("Numbers:", numbers)
print("Mean:", statistics.mean(numbers))
print("Median:", statistics.median(numbers))
