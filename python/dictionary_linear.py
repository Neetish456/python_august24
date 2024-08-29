
'''
def linear_search(names, search_name):
    for i in range(len(names)):
        if names[i] == search_name:
            return i
    return -1

n = int(input('Enter input size: '))

names = []
print(f'Enter the {n} names')
for i in range(n):
    names.append(input())

print('The input data is \n', names)
search_name = input('Enter the search name: ')

index = linear_search(names, search_name)
if index == -1:
    print(f'{search_name} was not found in the list')
else:
    print(f'{search_name} was found at position {index+1}')

'''
'''

'''
dictionary1 = {}
length1 = int(input("Enter the number of students : "))

for i in range(0,length1):
    key1 = str(input("Enter the ID : "))
    value1 = str(input("Enter the name of the studen : "))
    dictionary1[key1] = value1

lookup = input("Enter the ID to be searched : ")

flag = False
keyss = list(dictionary1.keys())
#print(keyss)
for i in keyss:
    if lookup == i:
        flag = True
        break

if flag:
    print("The ID exists")
else:
    print("ID doesnt exist")