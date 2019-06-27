class Shark():
    def swim(self):
        print("shark can swim")
    def swim_backwards(self):
        print("shark can swim backwards")
class Clownfish():
    def swim(self):
        print("clownfish can swim")
    def swim_backwards(self):
        print("clownfish can swim backwards")
sammy=Shark()
sammy.swim()
sammy.swim_backwards()
casey=Clownfish()
casey.swim()
casey.swim_backwards()
for fish in (sammy,casey):
    fish.swim()
    fish.swim_backwards()