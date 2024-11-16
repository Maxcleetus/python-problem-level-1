#check whether the number is armstrong or not

n = int(input("enter a number:",))
length = len(str(n))
temp = n 
sum = 0 
while temp > 0:
    digit = temp % 10
    sum = sum + digit**length
    temp = temp//10
if sum == n:
    print("armstrong number")
else:
    print("not an armstrong number")   

