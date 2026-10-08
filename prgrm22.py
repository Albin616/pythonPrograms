dict1={}
dict2={}
n1=int(input("Enter the number of elements in the first dictionary:"))
for i in range(n1):
    key=input("Enter key:")
    value=input("Enter value:")
    dict1[key]=value
n2=int(input("Enter the number of elements in the second dictionary:"))
for i in range(n2):
     key=input("Enter key:")
     value=input("Enter value:")
     dict2[key]=value
print(dict1)
print(dict2)
dict1.update(dict2)
print("Merged dictionary:",dict1)