class Shark:
    #class variable
    animal_type="fish"
    location="bangalore"
    #constructor
    def __init__(self,name,age):
        self.name=name
        self.age=age

    # Method with instance variable followers
    def set_followers(self,followers):
        print("The user has "+str(followers)+" followers")
def main():
    sammy=Shark('shark',10)
    print(sammy.age)
    print(sammy.name)
    print(sammy.animal_type)
    print(sammy.location)
    sammy.set_followers(90)
if __name__== main():
    main()


