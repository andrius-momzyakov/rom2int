import argparse
from __init__ import ROMAN_DIGIT_MAP

parser = argparse.ArgumentParser()
parser.add_argument("num", type=int)
args = parser.parse_args()
s_num = str(args.num)
parsed = {}
l = len(s_num)
exponent = l - 1

exp_digits = {
    0: {1: "I", 5: "V", 10: "X"},
    1: {1: "X", 5: "L", 10: "C"},
    2: {1: "C", 5: "D", 10: "M"},
    3: {1: "M", 5: "V_", 10: "X_"},
}


for idx, dig in enumerate(s_num):
    parsed[exponent-idx] = dig

def compose_roman_digit(exponent: int, digit: int,):
    roman = ""
    if digit < 4:
        for i in range(digit):
            roman += exp_digits[exponent][1]
    elif digit == 4: # V
        roman += exp_digits[exponent][1] + exp_digits[exponent][5]
    elif digit == 5:
        roman += exp_digits[exponent][5] 
    elif 6 <= digit < 9: 
        roman += exp_digits[exponent][5] 
        for i in range(6, digit + 1):
            roman += exp_digits[exponent][1]
    elif digit == 9:
        roman += exp_digits[exponent][1] + exp_digits[exponent][10]
    return roman
    

roman = ""
for key, dig in parsed.items():
    digit = int(dig)
    roman += compose_roman_digit(exponent=key, digit=digit)

            
print(roman)