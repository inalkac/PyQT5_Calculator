import methods
def count(mathExpression):
    x = methods.convertText(mathExpression)
    if x[1] == '+':
        result = int(x[0]) + int(x[2])
    elif x[1] == '-':
        result = int(x[0]) - int(x[2])
    elif x[1] == "*":
        result = int(x[0]) * int(x[2])
    elif x[1] == '/':
        result = int(x[0]) / int(x[2])
    return str(result)