class Sample:
    def m1(self):
        print("m1")

class Demo(Sample):
    def m2(self):
        print("m2")

class Test(Sample):
    def m3(self):
        print("m3")

obj1 = Demo()
obj1.m1()
obj1.m2()
#obj1.m3()