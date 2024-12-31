'''Problem statement:  
Get the input String from user and parse it to integer, if it is not a number it will throw  
number format exception Catch it and print "Entered input is not a valid format for an integer." 
or else print the square of that number. (Refer Sample Input and Output). ''' 

'''try:
    getString = int(input("Enter Value: "))
    print(type(getString))
    print(f"The square of {getString} is {getString ** 2}.")
except ValueError:
    print("Entered input is not a valid format for an integer.")'''


'''Write a program that takes as input the size of the array and the elements in the array.  
The program then asks the user to enter a particular index and prints the element at that index.  
Index  starts from zero.  
This program may generate Array Index Out Of Bounds Exception  or NumberFormatException.   
Use exception handling mechanisms to handle this exception.'''  
'''
try:
    size = int(input("Enter Array Size: "))
    arr = []

    for i in range(size):
        element = input("Element {i}: ")
        arr.append(element)

        index = input("Enter index: ")

        print("Ele at index",index,":",arr[index])

except IndexError:
        print("Error: Index is out of bounds.")
except ValueError:
        print("Error: Invalid input. Please enter an integer for the index and elements.")
except Exception as e:
        print(f"An unexpected error occurred: {e}")

'''

'''Write a Program to take care of Number Format Exception if user enters values other than  
integer for calculating average marks of 2 students. The name of the students and marks  
in 3 subjects are taken from the user while executing the program. 
In the same Program write your own Exception classes to take care of Negative values and  
values out of range (i.e. other than in the range of 0-100) '''

''''class NegativeMarksError(Exception):
    def __init__(self):
        super()

class MarksOutOfRange(Exception):
    def __init__(self):
        super()

def get_marks():
    while True:
        try:

            marks = int(input("Enter Marks: "))

            if marks < 0 :

                raise NegativeMarksError("Marks cannot be negative")
            elif marks > 100:
                raise MarksOutOfRange("Marks should be betweek 0 to 100")
            return marks
    
        except ValueError:
            print("invalid input")
        except NegativeMarksError as ne:
            print(ne)
        except MarksOutOfRange as me:
            print(me)

def calculate_avg():
    students = []
    for i in range(2):
        name = input(f"Enter the name of student {i+1}: ")
        print(f"Enter marks for {name} in 3 subjects: ")
        marks = []
        for j in range(3):
            marks.append(get_marks())
        students.append({"name": name, "marks": marks})

    for student in students:
        avg = sum(student["marks"])/ len(student["marks"])
        print(f"Average marks of {students['name']} are: {avg:.2f}")

calculate_avg()
'''

class InvalidCountryException(Exception):
    def __init__(self):
        super()

class UserRegistration:
    def registerUser(username, userCountry):
        