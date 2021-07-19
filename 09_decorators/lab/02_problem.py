def vowel_filter(function):
    def wrapper():
        result = []
        for char in function():
            if char.lower in "aoueiy":
                result.append(char)
        return result

    return wrapper


@vowel_filter
def get_letters():
    return ["a", "b", "c", "d", "e"]


print(get_letters())
