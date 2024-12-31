'''class EligibleError(Exception):
    def __init__(self):
        super()

class Sample:
    def test(self, age, percentage):
        if age<=17 or percentage<=60:
            raise EligibleError("Not Eligible for Registration")
        else:
            print("Registration Success
                  ")

obj1 = Sample()
try:
    obj1.test(16,67):
except EligibleError as e:
    print'''