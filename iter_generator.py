class Countdown:
    def __init__(self, start):
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < 0:
            raise StopIteration
        value = self.current
        self.current -= 1
        return value


for num in Countdown(3):
    print(num)

nums = [10, 20, 30]
iterator = iter(nums)

print(next(iterator))
print(next(iterator))
print(next(iterator))


def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b


for num in fibonacci(7):
    print(num)


def even_numbers(n):
    for i in range(0, n + 1, 2):
        yield i


print(list(even_numbers(10)))
