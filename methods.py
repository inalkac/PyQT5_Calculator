import re
def convertText(textToConvert):
    charList = list(textToConvert)
    number1=[]
    number2=[]
    if charList[0] == '-':
        number1.append(charList[0])
        index = 1
    else: 
        index = 0
    while charList[index] not in ['+','-','*','/']:
        number1.append(charList[index])
        index+=1
    sign = charList[index]
    index+=1
    if charList[index] == '-':
        number2.append(charList[index])
    while index< len(charList):
        number2.append(charList[index])
        index+=1
    number1 = ''.join(number1)
    number2 = ''.join(number2)
    
    return [number1, sign, number2]

def verifyText(_text):
    if _text.isnumeric() or re.findall("(-)|(\d+\.?\d*) |([+-/*])|(\d+\.?\d*)",_text):
        return _text
    else:
        return ''
