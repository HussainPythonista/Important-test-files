list1=[78,4,99,2,45,7,8,3,2,5,77]
sorted2=sorted(list1,reverse=False)
print(sorted2)


#Bubble sort
swap=[2,3,1,9,8,7,5]
for i in range(len(swap)-1,0,-1):
    for j in range(i):
     if swap[j]>swap[j+1]:
            temp=swap[j]
            swap[j]=swap[j+1]
            swap[j+1]=temp
print(swap)