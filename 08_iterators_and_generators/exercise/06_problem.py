def fibonacci():
    yield 0
    yield 1
    previous_num = 0
    current_num = 1
    new_num = previous_num + current_num
    yield new_num
    while True:
        previous_num = current_num
        current_num = new_num
        new_num = previous_num + current_num
        yield new_num


generator = fibonacci()
for i in range(5):
    print(next(generator))
