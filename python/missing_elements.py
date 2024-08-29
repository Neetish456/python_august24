original1 = []
transported = []
missing1 = []

n = len(original1)
m = len(transported)

if m > n:
    print("The size of tranported list must be less than original list. ")
else:
    for i in range(n):
        original1.append(int(input(f"Enter the elements of Original List , item no - {i} : ")))
    for j in range(m):
        transported.append(int(input(f"Enter the elements of Transported List  , item no - {i} : ")))
    
list1 = original1.sort()
list2 = transported.sort()
k=0
j=0
if m == 0:
    missing1.append(original1)
else:
    for i in range(n):
        if original1[i] == transported[j]:
            i+=1
            j+=1
        else:
            
            missing1.append(original1[i])
            i+=1
            k+=1
print("The missing items are : \n", missing1)

