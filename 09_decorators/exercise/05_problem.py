def cache(func):
    def wrapper(*args, **kwargs):
        key = args[0]
        if key not in wrapper.log:
            wrapper.log[key] = func(*args, **kwargs)
        return wrapper.log[key]

    wrapper.log = {}
    return wrapper


@cache
def fibonacci(n):
    if n < 2:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


fibonacci(3)
print(fibonacci.log)

fibonacci(4)
print(fibonacci.log)
