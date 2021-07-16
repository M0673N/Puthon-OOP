def genrange(start, end):
    return (num for num in range(start, end + 1))


print(list(genrange(1, 10)))
