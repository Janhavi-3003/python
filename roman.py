empty= {'M': 1000, 'CM': 900, 'D': 500, 'CD': 400, 'C': 100, 'XC': 90, 'L': 50, 'XL': 40, 'X': 10, 'IX': 9, 'V': 5, 'IV': 4, 'I': 1}
def roman_to_int(roman_num):
    count = 0
    value = 0
    while value< len(roman_num):
        if count + 1< len(roman_num) and roman_num[value:value+2] in empty:
            value += empty[roman_num[value:value+2]]
            count+= 2
        else:
            count+= empty[roman_num[value]]
            value+= 1
    return count

print(roman_to_int('MMMIII'))

