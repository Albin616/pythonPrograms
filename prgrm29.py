list1=list(map(int,input("Enter the first list:").split()))
list2=list(map(int,input("Enter the second list:").split()))


if len(list1)==len(list2):
    print("Both list are of same length")
else:
    print("Both list are of different length")
if sum(list1)==sum(list2):
    print("Both list are of same sum",sum(list1))
else:
    print("Both list are of different sum")
    common=set(list1)&set(list2)
if common:
    print("Common occurance are:",common)
else:
    print("No common occurance")