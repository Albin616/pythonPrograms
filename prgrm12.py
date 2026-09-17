numbers=[]
n=int(input("enter number of elements:"))
for i in range(0,n):
    num=int(input("enter the number:"))
    numbers.append(num)
print("Original list:",numbers)
updated_list=[]
for i in range(0,n):
    if numbers[i]%2!=0:
        updated_list.append(numbers[i])
print("updated list:",updated_list)