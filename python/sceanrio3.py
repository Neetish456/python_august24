#problem statement rotation a word clock wise

def finder(n):
    if n.find(word1):
        return 1
    else:
        return -1


word1 = str(input("Enter The string to be rotated : "))
index1 = int(input("Enter the index of the letter from which you'd like to roate the string : "))

rotated1 = ""

for i in range(index1,len(word1)):
    rotated1 = rotated1 + word1[i]
for j in range(0,index1 ):
    rotated1 = rotated1 + word1[j]
temp1 = rotated1 + rotated1
print(f'The given string {word1} , the rotated string "{rotated1}" ')
print(temp1)

if finder(temp1):
    print("It exists")
else:
    print("nope")



    
