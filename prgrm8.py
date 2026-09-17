str=input("Enter the string:")
search=input("Enter the words to be searched:")
x=str.split(" ")
count=0
for i in x:
    if(i==search):
        count=count+1
print("Total occurence of the word is:",count)