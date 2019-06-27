def linear_search(arr,item):
    for i in range(0,len(arr)):
        if(arr[i]==item):
            return i
    return -1
arr=[1,8,9,4,5]
item=int(input("Enter the value : "))
getvalue=linear_search(arr,item)
if(getvalue==-1):
    print("Element is not present")
else:
    print("The item is found at the index",getvalue)
