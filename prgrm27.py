def gcd(a,b):
    while b!=0:
        a,b=b,a%b
    return a
num=int(input("Enter the first number:"))
num2=int(input("Enter the second number:"))
result=gcd(num,num2)
print("GCD is:",result)