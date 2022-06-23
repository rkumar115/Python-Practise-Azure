# Move Zeros to beginning
ar=[0,1,2,3,4,5,6,7,8,1,10,20,0,59,63,0,88,0]
i=0 # start of array
j=0 # increment
while (j<len(ar)):
    if(ar[i]==0):
        i=i+1
    if(j<i):
        j=i+1
    if(ar[j]==0):
        ar[j]=ar[i]
        ar[i]=0
        j=j+1
        i=i+1
    else:
        j=j+1
print(ar)