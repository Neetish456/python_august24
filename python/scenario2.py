list1 = []
server1 = []
server2 = []

numofReq = int(input("Enter the number of requests : "))

for i in range(0,numofReq):
    
    list1.append(int(input()))
    

for i in range(numofReq):
    if i%2==0:
        server1.append(list1[i])
    else:
        server2.append(list1[i])

print(list1,"\n",server1,"\n",server2)
