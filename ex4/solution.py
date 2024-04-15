class RomanNumber:
    """
    Class of Roman numerals.

    Attributes:
        roman_map (dict): Roman numeral dictionary
        rom_value (str): Roman numeral
    """
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

    def __init__(self, rom_value):
        """
        The function initializes a new class object.
        :param rom_value (str): Roman numeral
        """
        self.rom_value = rom_value
        if not self.is_roman(rom_value):
            print("ошибка")
            self.rom_value = None

    def decimal_number(self):
        """
        Returns the decimal equivalent of the Roman number.
        :return: decimal equivalent of the Roman number
        """
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

    @staticmethod
    def is_roman(value):
        """
        Checks if the Roman numeral entry is correct.
        :param value: Roman numeral
        :return: True if the number is Roman otherwise False.
        """

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
