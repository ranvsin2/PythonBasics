list1=[10,20,30,40]
print(list1[::-1])

def reverse_second(list):
    list2=[]
    n=len(list)
    index=1
    for x in range(0,n):
        list2.insert(x,list[n-index])
        index=index+1
    print(list2)
call_list=[1,2,3,4]
reverse_second(call_list)


