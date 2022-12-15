from string import ascii_uppercase, digits
from tkinter import END
#Checking digit to document number field
def algorithm(string: str) -> str:
    printable = digits + ascii_uppercase
    string = string.upper().replace("<", "0")
    weight = [7, 3, 1]
    summation = 0
    for i in range(len(string)):
        Validation = string[i]
        if Validation not in printable:
            raise ValueError("%s contains invalid characters" % string, Validation)
        summation += printable.index(Validation) * weight[i % 3]
    summation %=10
    return summation

#It is seperating 2 lines of MRTD and sending it to algorithm  
def vertify (string0: str) -> str:
    string1 = string0[45:]
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
        return("passed")
