list=[ ]
n=int(input("Enter the number of words in the list:"))
for i in range(0,n):
    a=input("Enter the words:")
    list.append(a)
    print(list)
length=len(list[0])
str=list[0]
for i in range(0,n):
        if len(list[i])>length:
            str=list[i]
            length=len(str)
print("The longest word:",str)
print("The length of the word is:",length)