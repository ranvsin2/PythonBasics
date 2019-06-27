def binary_search(arr,l,r,item):
    if l<r:
        mid=int(l+(r-l)/2)
        print("The mid is:",mid)
        if arr[mid]==item:
            return mid
        elif arr[mid] < item:
            return binary_search(arr,arr[mid+1],r,item)
        else:
            return binary_search(arr,l,arr[mid-1],item)
    else:
        return -1

arr = [2,4,8,11,29,35,67]
item=int(input("Enter the element to be searched: "))
result=binary_search(arr,0,len(arr)-1,item)
if(result==-1):
    print("Element Not found")
else:
    print("Element found at index :",result)
