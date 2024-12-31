class Sample:
    a=10
    name="python"

    def m1(self):
        print("m1")
    def m2(self):
        self.m1()

    def __init__(self): # In built python function(speacial python functions)
        # init is a constructor
        # Constructor is a type of method
        print("Constructor Calling")

class Demo:
    b=20
#creating object happens outside indentation
obj1=Sample() # 

print(obj1.a)
obj1.m1()

