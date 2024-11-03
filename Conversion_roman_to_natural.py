"""
I   = 1 II  = 2
III = 3 IV  = 4
V   = 5 VI  = 6
VII = 7 VIII= 8
IX  = 9 X   = 10
L   = 50    C   = 100
D   = 500   M   = 1000
"""
def roman_to_num(num):
    global normal_number
    for j in num:
        if "cm" in num:
            normal_number += 900
            num = num.replace("cm","")
        elif "cd" in num:
            normal_number += 400
            num = num.replace("cd","")
        elif "xc" in num:
            normal_number += 90
            num = num.replace("xc","")
        elif "xl" in num:
            normal_number += 40
            num = num.replace("xl","")
        elif "ix" in num:
            normal_number += 9
            num = num.replace("ix","")
        elif "iv" in num:
            normal_number += 4
            num = num.replace("iv","")
    for i in num:
        if i == "m":
            normal_number += 1000
        elif i == "d":
            normal_number += 500
        elif i == "c":
            normal_number += 100
        elif i == "l":
            normal_number += 50
        elif i == "x":
            normal_number += 10
        elif i == "v":
            normal_number += 5
        elif i == "i":
            normal_number += 1
    return normal_number

roman_num = input("Enter roman number\t:")
normal_number = 0
print(roman_to_num(roman_num.lower()))


