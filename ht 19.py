def int_to_roman(num):
    roman_dict = {1000: 'M', 900: 'CM', 500: 'D', 400: 'CD', 100: 'C', 90: 'XC', 50: 'L', 40: 'XL', 10: 'X', 9: 'IX', 5: 'V', 4: 'IV', 1: 'I'}
    roman_num = ''
    for value in roman_dict:
        roman_num += (num // value) * roman_dict[value]
        num %= value
    return roman_num

print(int_to_roman(3003))
