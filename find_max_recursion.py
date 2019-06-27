def find_max(l):
    if len(l)==1:
        return l[0]
    v1=l[0]
    v2=find_max(l[1:])
    if v1 > v2:
        return v1
    else:
        return v2
if __name__=="__main__":
    list1=[10]
    max_one_el=find_max(list1)
    print("The max with list 1 is",max_one_el)
    list2=[30,20,10,90]
    max_multi_el=find_max(list2)
    print("The max of list 2 is ",max_multi_el)

