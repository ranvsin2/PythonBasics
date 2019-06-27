def find_max(l):
    max=0
    for x in l:
        if x > max:
            max=x
    return max
if __name__=="__main__":
    list=[10,20,30,40]
    maxNumber=find_max(list)
    print(maxNumber)
