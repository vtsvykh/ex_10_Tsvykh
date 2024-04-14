class RomanNumber:
    def __init__(self, rom_value):
        """
        Initializes an instance of RomanNumber with the given Roman numeral string.

        Args:
            rom_value (str): The Roman numeral string.
        """
        self.rom_value = rom_value
        if not self.is_roman(rom_value):
            print("ошибка")
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

    def __repr__(self):
        return f'{self.rom_value}'



