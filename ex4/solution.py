class RomanNumber:
    def __init__(self, rom_value):
        if self.is_roman(rom_value):
            self.rom_value = rom_value
        else:
            print('ошибка')
            self.rom_value = None

    def decimal_number(self):
        val = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        result = 0
        for i in range(len(self.rom_value)):
            if i > 0 and val[self.rom_value[i]] > val[self.rom_value[i - 1]]:
                result += val[self.rom_value[i]] - 2 * val[self.rom_value[i - 1]]
            else:
                result += val[self.rom_value[i]]
        return result

    @staticmethod
    def is_roman(value):
        roman_numerals = {
            'M': 1000,
            'CM': 900,
            'D': 500,
            'CD': 400,
            'C': 100,
            'XC': 90,
            'L': 50,
            'XL': 40,
            'X': 10,
            'IX': 9,
            'V': 5,
            'IV': 4,
            'I': 1
        }
        i = 0
        total = 0
        while i < len(value):
            if i + 1 < len(value) and value[i:i + 2] in roman_numerals:
                total += roman_numerals[value[i:i + 2]]
                i += 2
            else:
                # обрабатываем одиночные символы
                if value[i] in roman_numerals:
                    total += roman_numerals[value[i]]
                    i += 1
                else:
                    # если встречаем символ вне словаря, возвращаем False
                    return False
        return total <= 3999 and total > 0

    def __repr__(self):
        return f'{self.rom_value}'

num_1 = RomanNumber('VI')
print(num_1.rom_value)
print(num_1.decimal_number())
print(num_1)
num_2 = RomanNumber('IIII')
print(num_2.rom_value)
num_3 = RomanNumber('XXIV')
print(num_3.decimal_number())
num_4 = RomanNumber('QER2')
nums = []
nums.append(num_1)
nums.append(num_2)
nums.append(num_3)
nums.append(num_4)
print(nums)
print(RomanNumber.is_roman('IIIII'))
print(RomanNumber.is_roman('MMМMMLXXXVI'))

