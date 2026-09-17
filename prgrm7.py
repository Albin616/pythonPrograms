word=input("Enter the word:")
vowels=['a','e','i','o','u','A','E','I','O','U']
vowels_list=[]
for each in word:
    if(each in vowels):
        vowels_list.append(each)
print("vowels in words are :",vowels_list)