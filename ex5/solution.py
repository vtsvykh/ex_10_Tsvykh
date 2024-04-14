
class RomanNumber:
    def __init__(self, value):
        """
        Initializes an instance of RomanNumber with the given Roman numeral string.

        Args:
            rom_value (str): The Roman numeral string.
        """
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
        """
        Returns the decimal equivalent of the Roman numeral.

        Returns:
            int: The decimal value.
        """
        if self.rom_value is None:
            return None
        roman_map = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        total = 0
        prev_value = 0
        for char in reversed(self.rom_value):
            value = roman_map[char]
            if value < prev_value:
                total -= value
            else:
                total += value
            prev_value = value

        return total

    def roman_number(self):
        """
        Преобразует десятичное число в римское.

        Args:
            num (int): Десятичное число.

        Returns:
            str: Римское число.
        """
        roman_map = {
            1: 'I',
            4: 'IV',
            5: 'V',
            9: 'IX',
            10: 'X',
            40: 'XL',
            50: 'L',
            90: 'XC',
            100: 'C',
            400: 'CD',
            500: 'D',
            900: 'CM',
            1000: 'M'
        }
        copy = self.int_value
        roman_num = ""
        for value in sorted(roman_map.keys(), reverse=True):
            while self.int_value >= value:
                roman_num += roman_map[value]
                self.int_value -= value
        self.int_value = copy
        return roman_num

    @staticmethod
    def is_roman(value):
        roman_numerals = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

        prev_value = 0
        consecutive_count = 0

        for char in value:
            if char not in roman_numerals:
                return False

            current_value = roman_numerals[char]

            if current_value > prev_value:
                if consecutive_count > 0:
                    return False
                if prev_value in [5, 50, 500]:
                    return False
                consecutive_count = 1
            elif current_value == prev_value:
                consecutive_count += 1
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



    def __repr__(self):
        return f'{self.rom_value}'




