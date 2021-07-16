def squares(num):
    return (n ** 2 for n in range(1, num + 1))


print(list(squares(5)))
