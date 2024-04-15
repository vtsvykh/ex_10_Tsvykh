class RomanNumber:
    roman_map = {
        'I': 1,
        'IV': 4,
        'V': 5,
        'IX': 9,
        'X': 10,
        'XL': 40,
        'L': 50,
        'XC': 90,
        'C': 100,
        'CD': 400,
        'D': 500,
        'CM': 900,
        'M': 1000
    }

    def __init__(self, value):
        self.value = value
        if isinstance(value, str):
            if RomanNumber.is_roman(value):
                self.rom_value = value
                self.int_value = self.decimal_number()
            else:
                print("ошибка")
                self.int_value = None
                self.rom_value = None

        else:
            if isinstance(value, int):
                if RomanNumber.is_int(value):
                    self.int_value = value
                    self.rom_value = self.roman_number()
                else:
                    print("ошибка")
                    self.int_value = None
                    self.rom_value = None

    def decimal_number(self):
        if self.rom_value is None:
            return None

        total = 0
        prev_value = 0
        for sign in reversed(self.rom_value):
            value = RomanNumber.roman_map[sign]
            if value < prev_value:
                total -= value
            else:
                total += value
            prev_value = value
        return total

    def roman_number(self):
        copy = self.int_value
        roman_num = ''
        new_dict = {
            value: key for key, value in RomanNumber.roman_map.items()
        }
        for value in sorted(new_dict.keys(), reverse=True):
            while self.int_value >= value:
                roman_num += new_dict[value]
                self.int_value -= value
        self.int_value = copy
        return roman_num

    @staticmethod
    def is_roman(value):

        if value in RomanNumber.roman_map:
            return True

        prev_value = 0
        consecutive_count = 0

        for sign in value:
            if sign not in RomanNumber.roman_map:
                return False

            current_value = RomanNumber.roman_map[sign]

            if current_value > prev_value:
                if consecutive_count > 0:
                    return False
                if prev_value in [5, 50, 500]:
                    return False
                consecutive_count = 1
            elif current_value == prev_value:
                consecutive_count += 1
                if prev_value in [5, 50, 500]:
                    return False
                if consecutive_count > 3:
                    return False
            else:
                consecutive_count = 0

            prev_value = current_value

        return True

    @staticmethod
    def is_int(value):
        if not isinstance(value, int) or value < 1 or value > 3999:
            return False
        return True

    def __add__(self, other):
        if not isinstance(other, RomanNumber):
            return NotImplemented
        return RomanNumber(self.decimal_number() + other.decimal_number())

    def __sub__(self, other):
        if not isinstance(other, RomanNumber):
            return NotImplemented
        return RomanNumber(self.decimal_number() - other.decimal_number())

    def __mul__(self, other):
        if not isinstance(other, RomanNumber):
            return NotImplemented
        return RomanNumber(self.decimal_number() * other.decimal_number())

    def __truediv__(self, other):
        if not isinstance(other, RomanNumber):
            return NotImplemented
        return RomanNumber(self.decimal_number() // other.decimal_number())

    def __floordiv__(self, other):
        if isinstance(other, RomanNumber):
            return RomanNumber(self.int_value // other.int_value)

    def __mod__(self, other):
        if isinstance(other, RomanNumber):
            return RomanNumber(self.int_value % other.int_value)

    def __pow__(self, other):
        if isinstance(other, RomanNumber):
            return RomanNumber(self.int_value ** other.int_value)

    def __str__(self):
        """
        Displaying information about a class object to users.
        """
        return f'{self.rom_value}'

    def __repr__(self):
        """
        Displaying information about a class object in debugging mode.
        """
        return self.__str__()
