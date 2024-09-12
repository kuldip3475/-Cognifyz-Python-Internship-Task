# task 2

def cal(val,unit):
    if unit == 'C':
        return val + 273.15
    elif unit == 'F':
        return (val - 32) * 5.0/9.0 + 273
    else:
        a = " enter proper unit "
        return a
    
val = float(input(" enter temp : "))
unit = input(" enter 'C' for Celsius and enter 'F' for Fahrenheit : ")
ans = cal(val,unit)
print(ans)
