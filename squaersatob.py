def squares(a, b):
    for i in range(a, b + 1):
        yield i * i


for value in squares(2, 6):
    print(value)