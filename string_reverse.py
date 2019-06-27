str1="ranvijaysingh"
str2=''
index=1
strLength=len(str1)
print("slice",str1[::-1])
for char in str1:
    print("char",char)
    print("str2",str2)
    str2=char+str2
print(str2)
inputWords="ranvijay singh"
inputWords = inputWords.split(" ")
print("phase 1",inputWords)
inputWords=inputWords[-1::-1]
inputWords=' '.join(inputWords)
print("input words",inputWords)