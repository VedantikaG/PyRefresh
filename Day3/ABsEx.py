from abc import ABC,abstractmethod

class Accounts:
    def savings(self):
        print("Zero saving accounts")

class Loans(ABC):
    @abstractmethod
    def pl(self):
        print("Personal Loan")

class Final(Loans):
    def pl(self):
        print("Personal Loan")

obj1 = Final()
obj1.pl()
