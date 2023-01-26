str1=input("Enter the sentence: ")
str2=str1.split(",")
print(len(str2))
print(str2)
count=[]
for i in range(len(str2)):
    str3=(str2[i].split(" "))
    print(str3)
    count.append(len(str3))
print(max(count))
str1=input("Enter the sentence: ")
str2=str1.split(",")
print(len(str2))
print(str2)
count=[]
for i in range(len(str2)):
    str3=(str2[i].split(" "))
    print(str3)
    count.append(len(str3))
print(max(count))
