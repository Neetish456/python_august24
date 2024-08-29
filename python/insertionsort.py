def insertionsort(array):
    for i in range(1,len(array)):
        element = array[i]
        j = i - 1
        while j >= 0 and element < array[j]:
            array[j+1] = array[j]
            j = j-1
        array[j+1] = element

    
array = []
n = int(input("Enter thje size of the array "))
print("Enter the array elements : ")
for i in range(0,n):
    array.append(int(input()))

print("The array before implenet insertion sort \n" , array)

insertionsort(array)

print("The array after impleneting inserrtion sort \n", array)