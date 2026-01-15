def digit2numbers(hundreds,tens,units):
    number = 100*hundreds + 10*tens +units
    return number

num1 = digit2numbers(hundreds=1,tens=2,units=3)
num2 = digit2numbers(units=3,tens=2,hundreds=1)
num3 = digit2numbers(tens=2,hundreds=1,units=3)

print(f"{num1 = },{num2 = },{num3 = }")