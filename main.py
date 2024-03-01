symbolList = ['+', '-', '/', '*', '^']

def updateCalcList(calcList: list, i: int, newValue: str) -> list:
    calcList.remove(calcList[i])
    calcList[i - 1] = newValue
    
    return calcList


def getValue(parcel: str) -> str:
    global symbolList
    symbol = ''
    
    if parcel[0] in symbolList and parcel[0] != "-":
        symbol = parcel[0]
        parcel = parcel[1:]

    return [float(parcel), symbol]

def power(firstParcel: str, secondParcel: str) -> str:
    [firstParcel, symbol] = getValue(firstParcel)
    secondParcel = getValue(secondParcel)[0]
    finalValue = pow(firstParcel, secondParcel)
    finalValue = symbol + str(finalValue)
    
    return finalValue

def multiply(firstParcel: str, secondParcel: str) -> str:
    [firstParcel, symbol] = getValue(firstParcel)
    secondParcel = getValue(secondParcel)[0]
    finalValue = firstParcel * secondParcel
    finalValue = symbol + str(finalValue)
    
    return finalValue

def divide(firstParcel: str, secondParcel: str) -> str:
    [firstParcel, symbol] = getValue(firstParcel)
    secondParcel = getValue(secondParcel)[0]
    finalValue = firstParcel / secondParcel
    finalValue = symbol + str(finalValue)
    
    return finalValue

def add(firstParcel: str, secondParcel: str) -> str:
    [firstParcel, symbol] = getValue(firstParcel)
    secondParcel = getValue(secondParcel)[0]
    finalValue = firstParcel + secondParcel
    finalValue = symbol + str(finalValue)
    
    return finalValue

def subtract(firstParcel: str, secondParcel: str) -> str:
    [firstParcel, symbol] = getValue(firstParcel)
    secondParcel = getValue(secondParcel)[0]
    finalValue = firstParcel - secondParcel
    finalValue = symbol + str(finalValue)
    
    return finalValue

def calculator() -> int:
    global symbolList
    
    while True:
        calc = input("Insert equation: ")
        calcList = []
        currentCalc = ''
        wasLastSymbol = False
        
        if calc == "exit":
            return
        
        for index, char in enumerate(calc):
            try:
                if char not in symbolList or index == 0 or wasLastSymbol == True:
                    currentCalc += char
                else:
                    calcList.append(currentCalc)
                    currentCalc = char

            except IndexError:
                calcList.append(currentCalc)
                currentCalc = char
                
            if index == len(calc) - 1:
                calcList.append(currentCalc)
                
            wasLastSymbol = char in symbolList
                
        while len(calcList) > 1:
            for i, parcel in enumerate(calcList):
                
                if parcel[0] == "^":
                    newValue = power(calcList[i - 1], parcel)
                    calcList = updateCalcList(calcList, i, newValue)
                    
                if parcel[0] == "*":
                    newValue = multiply(calcList[i - 1], parcel)
                    calcList = updateCalcList(calcList, i, newValue)
                    
                if parcel[0] == "/":
                    newValue = divide(calcList[i - 1], parcel)
                    calcList = updateCalcList(calcList, i, newValue)
                    
                if parcel[0] == "+":
                    newValue = add(calcList[i - 1], parcel)
                    calcList = updateCalcList(calcList, i, newValue)
                    
                if i != 0 and parcel[0] == "-":
                    newValue = subtract(calcList[i - 1], parcel)
                    calcList = updateCalcList(calcList, i, newValue)

        print(calcList[0])
        
calculator()
