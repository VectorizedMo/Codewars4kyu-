import string
import math

def NCR(k,r):
    return math.factorial(k)/((math.factorial(r))*(math.factorial(k-r)))

def expand(expr:str):
    Coefficient1 = ""
    Coefficient2 = ""
    Variable = ""
    breaknum = 0
    exprlist = list(expr)
    Exponent = ""
    NegativeFlag = False
    for i in range(exprlist.index("^")+1, len(exprlist)):
        Exponent += exprlist[i]
    exprlist.pop(0)
    Answer = ""
    for i in range(exprlist.index("^"), len(exprlist)+1):
        exprlist.pop(len(exprlist)-1)
    if exprlist[0] == "-":
        exprlist.pop(0)
        NegativeFlag = True
    if Exponent == "0":
        return "1"
    if "+" in exprlist:
        for i in range(exprlist.index("+")+1, len(exprlist)):
            Coefficient2 += exprlist[i]
        for j in range(exprlist.index("+")):
            if exprlist[j].isnumeric() or exprlist[j] in "-":
                Coefficient1 += exprlist[j]
            else:
                Variable = exprlist[j]
    else:
        for i in range(exprlist.index("-"), len(exprlist)):
            Coefficient2 += exprlist[i]
        for j in range(exprlist.index("-")):
            if exprlist[j].isnumeric() or exprlist[j] in "+":
                Coefficient1 += exprlist[j]
            else:
                Variable = exprlist[j]
    if Coefficient1 == "":
        Coefficient1 = "1"
    elif Coefficient1 == "-":
        Coefficient1 = "-1"
    if NegativeFlag:
        Coefficient1 = "-" + Coefficient1
    for i in range(int(Exponent)+1):
        BC = NCR(int(Exponent), i)
        Coefficient = str(int((BC * pow(int(Coefficient1), int(Exponent)-i) * pow(int(Coefficient2), i))))
        if int(Coefficient) == 0:
            continue
        elif int(Coefficient) > 0:
            if i != 0:
                Coefficient = "+" + str(Coefficient)
        Exponent2 = str(int(Exponent)-i)
        if Coefficient == "1":
            Coefficient = ""
        if Coefficient == "-1" and i == 0:
            Coefficient = "-"
        if i != 0:
            if Coefficient == "+1" and int(Exponent2) > 0:
                Coefficient = "+"
            if Coefficient == "-1" and int(Exponent2) > 0:
                Coefficient = "-"
        if Exponent2 == "0":
            Answer += Coefficient
        elif Exponent2 == "1":
            Answer += Coefficient + Variable
        else:
            Answer += Coefficient + Variable + "^" + Exponent2
    return Answer
