number=[]
n=int(input("Enter the number of elemenyts:"))
for i in range(0,n):
    element=int(input("Enter the element:"))
    number.append(element)
print("\n",number)
for i in range(0,n):
    if number[i]>100:
        number[i]='over'
print(number)