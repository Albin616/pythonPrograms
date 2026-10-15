dict={}
n=int(input("Enter the number of elements:"))
for i in range(n):
    key=input("Enter the key of the element:")
    value=input("Enter the value of the element:")
    dict[key]=value
print("Dictionary is:",dict)
dict_asc=sorted(dict.items())
print("Dictionary in ascending order:",dict_asc)
dict_desc=sorted(dict.items(),reverse=True)
print("Dictionary in descending order:",dict_desc)
