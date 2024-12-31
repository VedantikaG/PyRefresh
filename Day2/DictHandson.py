# Dictionary


#Create an empty dictionary called dog 

dog = {}

#Add name, color, breed, legs, age to the dog dictionary 

dog = {
    "name": "Husky",
    "color": "Brown",
    "breed": "Husk",
    "legs": "straight",
    "age": 12
}

print(dog)

#Create a student dictionary and add first_name, last_name, gender, age, marital status, skills, country, city and address as keys for the dictionary 

student = {
    "first_name": "Vedantika",
    "last_name": "Ghorpade",
    "gender": "Female",
    "age": 21,
    "marital_status": "Single",
    "skills": "Python",
    "country": "India",
    "city": "Mumbai",
    "address": "Vasai"
}

print(student)

#Get the length of the student dictionary 

size = len(student)
print(size)

#Get the value of skills and check the data type, it should be a list 
print(student["skills"])
print(type(student["skills"]))
convertToList = list(student["skills"])
print(type(convertToList))


#Modify the skills values by adding one or two skills 

student["skills"] = ["Python","Java","Android Studio"]
print(student)
#Get the dictionary keys as a list 
dictKeys = list(student.keys())
print(type(dictKeys))

#Get the dictionary values as a list 
getValues= list(student.values())
print(getValues)
print(type(getValues))

#Change the dictionary to a list of tuples using items() method 

student_list = list(student.items())
print(student_list)

#Delete one of the items in the dictionary 
del student["marital_status"]
print(student)
#Delete one of the dictionaries 
del student
print(student)