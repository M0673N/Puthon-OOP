n = int(input())


def print_diamond(size):
    for i in range(size):
        print(" " * (size - i - 1) + ("* " * (i + 1)).strip())
    for i in range(size - 2, -1, -1):
        print(" " * (size - i - 1) + ("* " * (i + 1)).strip())


print_diamond(n)
