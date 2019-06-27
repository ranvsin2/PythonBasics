class Fruit:
    def __init__(self,name):
        self.name=name
        print("constructor is coming")
    def shape(self):
        print("The shape of fruit is round and name is "+self.name)
    def size(self):
        print("The size of fruit is 4 and name is " + self.name)
def main():
    apple=Fruit("apple")
    apple.shape()
    apple.size()
if __name__=="__main__":
    main()
