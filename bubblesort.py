# Bubblesort

def bubblesort(temp):

    i=len(temp)
    j=0
    sorted_ar=[]
    k=0
    while(j<i):
        #print(temp[j])
        k=j+1
        while(k<i):
            if(temp[j])>temp[k]:
                ex=temp[j]
                temp[j]=temp[k]
                temp[k]=ex
            k=k+1

        j=j+1
    print(temp)


arr=[10,7,11,12,2,5,1,3]
bubblesort(arr)