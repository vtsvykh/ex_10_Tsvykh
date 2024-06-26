class RomanNumber:
    """
    Class of Roman numerals.

    Attributes:
        roman_map (dict): Roman numeral dictionary
        rom_value (str or int): Roman numeral
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

    def __init__(self, value):
        """
        The function initializes a new class object.
        :param value (str or int): Roman numeral
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

    def roman_number(self):
        """
        Returns the equivalent of the Roman number in decimal form.
        :return: equivalent of the Roman number in decimal form
        """
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
        """
        Checks if the Roman numeral entry is correct.
        :param value (str): Roman numeral
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

    @staticmethod
    def is_int(value):
        """
        Checks whether it is possible to convert a decimal number into Roman form.
        :param value (int): Integer value
        :return: True if you can or False, you can't.
        """
        if not isinstance(value, int) or value < 1 or value > 3999:
            return False
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
