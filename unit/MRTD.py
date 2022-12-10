from string import ascii_uppercase, digits
from tkinter import END
def algorithm(string: str) -> str:
    printable = digits + ascii_uppercase
    string = string.upper().replace("<", "0")
    weight = [7, 3, 1]
    summation = 0
    for i in range(len(string)):
        c = string[i]
        if c not in printable:
            raise ValueError("%s contains invalid characters" % string, c)
        summation += printable.index(c) * weight[i % 3]
    summation %=10
    return summation

def vertify (string1: str) -> str:
    passport = string1[0:9]
    passport_vertify_code = int(string1[9])
    birth = string1[13:19]
    birth_vertify_code = int(string1[19])
    validity = string1[21:27]
    validity_vertify_code = int(string1[27])
    personal_code = string1[28:43]
    personal_vertify_code = int(string1[43])

    if algorithm(passport) != passport_vertify_code:
        return("passport info error")
    elif algorithm(birth) != birth_vertify_code:
        return("birth date info error")
    elif algorithm(validity) != validity_vertify_code:
        return("validity info error")
    elif algorithm(personal_code) != personal_vertify_code:
        return("personal code error")
    else:
        return("verification passed")

    