def binary_search(arr,l,r,item):
    while l<=r:
        mid=int(l+(r-l)/2)
        print("The mid is :",mid)
        if(arr[mid]==item):
            return mid
        elif(arr[mid]<item):
            l=mid+1
        else:
            r=mid-1
    return -1
arr = [2,4,8,11,29,35,67]
item=int(input("Enter the element to be searched: "))
result=binary_search(arr,0,len(arr)-1,item)
print(result)
