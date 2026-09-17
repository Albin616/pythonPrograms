number=[]
n=int(input("Enter the number of elements in the list:"))
for i in range(0,n):
    element=int(input("Enter an element:"))
    number.append(element)
print("positive number are")
for i in range(0,n):
        if(number[i]>0):
            print(number[i])