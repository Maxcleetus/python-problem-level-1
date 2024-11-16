#write a python program to print the series 1 + 2/2! + 3/3!....+ n/n!

n = int(input("enter length : " ,))
import math
sum = 1
for i in range(2,n+1):
    sum = sum + i/math.factorial(i)
print(sum)    