def FindParantheses(formula:str):
    Parentheses = []
    for index, char in enumerate(formula):
        if char == '(':
            Parentheses.append(index)
            Parentheses.append(len(formula) - "".join(list(reversed(formula))).find(")")-1)
            break
    return ''.join([formula[i] for i in range(len(formula)) if i > Parentheses[0] and i < Parentheses[1] and formula[i] != " "]), Parentheses


def FindValue(formula:str):
    formula = ''.join([char for char in formula if char != " "])
    tempformula = ""
    for index,char in enumerate(formula):
        if char == "-" and index > 0 and formula[index-1] not in "+*/-":tempformula+='+'
        tempformula += char
    formula = tempformula
    Operators = []
    OperatorString = "+/*-"
    OperatorFunctions = [lambda x,y: x+y, lambda x,y: x/y, lambda x,y: x*y, lambda x,y: x-y]
    Values = []
    OperandStr = ''
    Value = 0
    for index, value in enumerate(formula):
        if value not in OperatorString:
            OperandStr += value
        elif value == "-":
            if OperandStr:Values.append(OperandStr)
            OperandStr = "-"
            continue
        else:
            if OperandStr:Values.append(OperandStr)
            OperandStr = ""
            Operators.append(value)
    else:
        Values.append(OperandStr)
    while "-" in Values:
        index = Values.index("-")
        count = 0
        for i in range(index, len(Values)):
            if Values[i] == "-":
                count += 1
            else:
                break
        if (count+1)%2 == 0:
            for i in range(index, index+count):
                Values.pop(index)
            Values[index] = ''.join([char for char in Values[index] if char != "-"])
        else:
            for i in range(index, index+count):
                Values.pop(index)
    count = 0
    for index, operator in enumerate(Operators):
        if operator == "*" or operator == "/":
            Value = OperatorFunctions[OperatorString.index(operator)](float(Values[index-count]), float(Values[index+1-count]))
            Values.pop(index-count)
            Values.pop(index-count)
            Values.insert(index-count,Value)
            count += 1
    Value = sum([float(value) for value in Values])                                        
    return Value

def evaluate(expression):
    if "(" not in expression:
        return FindValue(expression)
    string = expression
    mainval = FindParantheses(string)
    val = mainval[0]
    PreviousVals = [(string,mainval[1])]
    while "(" in val:
        mainval = FindParantheses(val)
        PreviousVals.append((val, mainval[1]))
        val = mainval[0]
    MainValue = FindValue(val)
    PreviousVals = list(reversed(PreviousVals))
    TempString = ""
    for sequence in PreviousVals:
        for i in range(len(sequence[0])):
            if i >= sequence[1][0] and i <= sequence[1][1]:
                break
            else:
                TempString += sequence[0][i]
        for i in range(len(str(MainValue))):
            TempString += str(MainValue)[i]
        for i in range(sequence[1][1]+1, len(sequence[0])):
            TempString += sequence[0][i]
        MainValue = FindValue(TempString)
        TempString = ""
    return MainValue

def FindAreas(expression):
    Operators = []
    formula = ''.join([char for char in expression if char != " "])
    if "("not in formula or ")" not in formula:
        return [formula]
    def FindNextBracket(index):
        for i in range(index+1, len(formula)):
            if formula[i] == "(":
                return True
            elif formula[i] == ")":
                return False
        else:
            return True
    string = ''
    AreasList = []
    firstindex = 0
    Intervals = []
    Done = False
    for index, char in enumerate(formula):
        if char != '(':
            if char == ")" and FindNextBracket(index):
                Intervals.append((firstindex, index))
                Done = False
                continue
        else:
            if not Done:firstindex = index
            Done = True
    if len(Intervals) == 1:
        return [formula]
    def OutsideInterval(index,interval):
        if index < interval[0] or index > interval[1]:
            return True
        else:
            return False
    for index, char in enumerate(formula):
        for interval in Intervals:
            if not OutsideInterval(index, interval):
                if char != "(":
                    if char == ")" and FindNextBracket(index):
                        string += char
                        AreasList.append(string)
                        string = ''
                        break
                    string += char
                else:
                    string += char
                break
        else:
            if char in "*/+":
                Operators.append(char)
            if char not in "*/":
                string += char
            if char == "-" and index > 0:
                Operators.append('+')
    return AreasList, Operators

def calc(expression):
    if "(" not in expression or ")" not in expression:
        return evaluate(expression)
    Areas = FindAreas(expression)
    if len(Areas) == 1:
        return evaluate(Areas[0])
    Values = [evaluate(Area) for Area in Areas[0]]
    Operators = Areas[1]
    OperatorString = "+/*-"
    OperatorFunctions = [lambda x,y: x+y, lambda x,y: x/y, lambda x,y: x*y, lambda x,y: x-y]
    count = 0
    if "*" or "/" in Operators:
        for index, operator in enumerate(Operators):
            if operator == "*" or operator == "/":
                Value = OperatorFunctions[OperatorString.index(operator)](float(Values[index-count]), float(Values[index+1-count]))
                Values.pop(index-count)
                Values.pop(index-count)
                Values.insert(index-count,Value)
                count += 1
        FinalVal = sum([float(element) for element in Values])
    else:
        FinalVal = sum(Values)
    return FinalVal
