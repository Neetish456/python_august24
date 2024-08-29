n = int(input("Eneter the no of elements : "))
oranges = []
for i in range(n):
    oranges.append(int(input(f"Enter the sixe of the {i+1} orange : ")))

print("Oranges before swapping",oranges)

def arrange_oranges(n,list1):
    j = 0
    pivot1 = list1[-1]
    for i in range(n-1):
        if list1[i] <pivot1:
            list1[j],list1[i] = list1[i],list1[j]
            j +=1
    list1[j],list1[-i] = list1[-1],list1[j]

    arrange_oranges(n,oranges)

    print("Oranges after getting swapped ", oranges)

    