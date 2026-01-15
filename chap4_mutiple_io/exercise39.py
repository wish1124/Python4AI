def digit2numbers(hundreds,tens,units):
    number = 100*hundreds + 10*tens +units
    return number

num1 = digit2numbers(3,2,1)
num2 = digit2numbers(1,3,2)
num3 = digit2numbers(2,1,3)

print(f"{num1 = },{num2 = }, {num3 = }")