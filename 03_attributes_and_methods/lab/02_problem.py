from math import floor


class Integer:
    def __init__(self, value):
        self.value = value

    @classmethod
    def from_float(cls, value):
        if not type(value) == float:
            return "value is not a float"
        return cls(floor(value))

    @classmethod
    def from_roman(cls, value):
        return cls(cls.roman_to_int(value))

    @classmethod
    def from_string(cls, value):
        if not type(value) == str:
            return "wrong type"
        if not value.isdigit():
            return "wrong type"
        return cls(int(value))

    def add(self, integer):
        if not type(integer) == Integer:
            return "number should be an Integer instance"
        return integer.value + self.value

    @staticmethod
    def roman_to_int(value):
        rom_val = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        int_val = 0
        for i in range(len(value)):
            if i > 0 and rom_val[value[i]] > rom_val[value[i - 1]]:
                int_val += rom_val[value[i]] - 2 * rom_val[value[i - 1]]
            else:
                int_val += rom_val[value[i]]
        return int_val


# first_num = Integer(10)
# second_num = Integer.from_roman("IV")
#
# print(Integer.from_float("2.6"))
# print(Integer.from_string(2.6))
# print(first_num.add(second_num))
