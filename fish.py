class Fish:
    def __init__(self,first_name,last_name="fish",skeleton="bone",eyelids=False):
        self.first_name=first_name
        self.last_name=last_name
        self.skeleton=skeleton
        self.eyelids=eyelids
    def swim(self):
        print("This Fish is swimming")
    def swim_backwards(self):
        print("This fish swim backwards")
class Trout(Fish):
    def __init__(self,water="freshwater"):
        self.water=water
        super().__init__(self)
terry=Trout()
terry.first_name="Terry"
terry.swim()
terry.swim_backwards()
print("====coming in super wala keywords=====")
print(terry.water)
print(terry.first_name +"----"+ terry.last_name+"----"+terry.skeleton)
class clownfish(Fish):
    def live_catch(self):
        print("coming in clown fish block")
casey=clownfish('casey')
print(casey.first_name)
casey.live_catch()
class Shark(Fish):
    def __init__(self,first_name,last_name="shark",skeleton="cartilage",eyelids=True):
        self.first_name=first_name
        self.last_name=last_name
        self.skeleton=skeleton
        self.eyelids=eyelids
    def swim_backwards(self):
         print("This cannot swim backwards")
rohu=Shark("shrkies")
print("shark calls come here")
print(rohu.first_name+"==="+rohu.last_name+"==="+rohu.skeleton+"====="+str(rohu.eyelids))
rohu.swim()
rohu.swim_backwards()

