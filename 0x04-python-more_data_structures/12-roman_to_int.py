#!/usr/bin/python3
def roman_to_int(roman_string):
    num = 0
    roman_int = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    for i in range(len(roman_string)):
        current = roman_int[roman_string[i]]
        nexto = roman_int[roman_string[i + 1]]
        if current >= nexto:
            num += current
        else:
            num -= current
