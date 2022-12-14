from string import ascii_uppercase, digits
from tkinter import END
import pycountry
from googletrans import Translator
import time
import datetime

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

def decode(dict):
    translator = Translator()
    dict1 = dict["line1"]
    dict2 = dict["line2"]
    issc = dict1["issuing_country"]
    lastname = dict1["last_name"]
    givenname = dict1["given_name"]
    passport = dict2["passport_number"]
    country = dict2["country_code"]
    birth = dict2["birth_date"]
    sex = dict2["sex"]
    exd = dict2["expiration_date"]
    pn = dict2["personal_number"]
    line1decode = "P<" + issc + lastname + "<<" + givenname.replace(' ','<')
    line1decoded1 = line1decode.ljust(44,'<')
    line2decode = passport + str(algorithm(passport)) + country + birth + str(algorithm(birth)) + sex +exd + str(algorithm(exd)) + pn + "<<<<<<" + str(algorithm(pn))
    decoded = line1decoded1 +";"+line2decode
    return decoded

if __name__ == '__main__':
    st = time.perf_counter()
    #a = datetime.datetime.now()
    print(vertify("P<QATSIMMONS<<LILYANA<LOUISA<<<<<<<<<<<<<<<<;S864944W87QAT6902070M0107183CB354885V<<<<<<7"))
    et = time.perf_counter()
    #b = datetime.datetime.now()
    elapsed_time = et - st
    #c = b - a 
    print('Execution time:', elapsed_time, 'seconds')
    #print(c.microseconds)