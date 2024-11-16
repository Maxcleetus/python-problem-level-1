# To find the sum of sine series sinx = x - x^3/3! + x^5/5! - x^7/7!..........

n = int(input('enter its accuracy :' ,))
x = int(input('enter value of x :' ,))
result = 0
import math
for i in range(0,n):
    sign = (-1)**i
    result = result + ( x**(2*i + 1) / math.factorial(2*i + 1))/ sign
print(result)    
