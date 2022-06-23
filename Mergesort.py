#Merge Sort

def merge(arr):

    if(len(arr)>1):
        mid = len(arr)//2
        first = arr[:mid]
        last=arr[mid:]

        merge(first)
        merge(last)
        i = j = k = 0
        while (i< len(first) and j < len(last)) :
            if(first[i]<last[j]):
                arr[k]=first[i]
                k=k+1
                i=i+1
            elif(first[i]>last[j]):
                arr[k]=last[j]
                k=k+1
                j=j+1
            else:
                arr[k]=first[i]
                i=i+1
                j=j+1
                k=k+1
        while(i< len(first)):

            arr[k]=first[i]
            k=k+1
            i=i+1
        while(j< len(last)):
            arr[k]=last[j]
            k=k+1
            j=j+1
    return(arr)

arr=[1,4,2,-2,10]
print(merge(arr))

