# write a program to print the series 1 + x^2/2 + x^3/3 + x^n/n

n = int(input('enter length:' ,))
x = int(input('enter value of x :' ,))
sum = 1
for i in range(2,n+1):
    sum = sum + (x ** i) / i
print(sum)    
