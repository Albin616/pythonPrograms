list=[ ]
n=int(input("Enter the limit"))
for i in range(0,n):
    num=int(input("Enter the numbers:"))
    list.append(num)
print(list)
sum=0
for i in range(0,n):
      sum=sum+list[i]
print("Sum of elements is:",sum)