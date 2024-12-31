# Conditional : Level 1
'''
Get user input using input(“Enter your age: ”). 
If user is 18 or older, give feedback: You are old enough to drive. 
If below 18 give feedback to wait for the missing amount of years. Output: 
Enter your age: 30 
You are old enough to learn to drive. 
Output: 
Enter your age: 15 
You need 3 more years to learn to drive. 
'''
'''
age = int(input("Enter  your age: "))

if age>18:
    print("You are old enough to drive")
else:
    print("wait for the missing amount of years")
'''
'''
Compare the values of my_age and your_age using if … else. Who is older (me or you)? Use input(“Enter your age: ”) to get the age as input. 
You can use a nested condition to print 'year' for 1 year difference in age,
 'years' for bigger differences, and a custom text if my_age = your_age. Output: 
Enter your age: 30 
You are 5 years older than me. 

Get two numbers from the user using input prompt. 
If a is greater than b return a is greater than b, 
if a is less b return a is smaller than b, else a is equal to b. Output: 

Enter number one: 4 
Enter number two: 3 
4 is greater than 3 '''

'''my_age = int(input("My age: "))
your_age = int(input("Enter your age: "))
diff_age = my_age - your_age
if diff_age==1:
    if my_age>your_age:
        print("My age is greater than your age")
    else:
        print("My age is smaller then your age")
elif diff_age 
'''
##########################################################################

# Conditional: Level 2
'''Write a code which gives grade to students according to theirs scores: 
80-100, A 
70-89, B 
60-69, C 
50-59, D 
0-49, F 
'''
'''
score = int(input())
if 80<= score <=100:
    print("A garde")
elif 70<= score <= 89:
    print("B Grade")
elif 60 <= score <=69:
    print("C Grade")
elif 50<=score<=59:
    print("D Grade")
elif 0<= score <= 49:
    print("F Grade")
else:
    print("Invalid Input")
'''


'''
Check if the season is Autumn, Winter, Spring or Summer. 
If the user input is: September, October or November, 
the season is Autumn. December, January or February, the season is Winter. 
March, April or May, the season is Spring June, July or August, the season is Summer 
'''
'''
season = input(" Enter Month: ").capitalize()
if season in ["September","October","November"]:
    print("Autumn")
elif season in ["December","January","February"]:
    print("Winter")
elif season in ["March","April","May"]:
    print("Spring/Summer")
elif season in ["June","July","August"]:
    print("Summer") 
else:
    print("invalid")
'''

'''
The following list contains some fruits: 
fruits = ['banana', 'orange', 'mango', 'lemon'] 
If a fruit doesn't exist in the list add the fruit to the list and print the modified list. 
If the fruit exists print('That fruit already exist in the list') 
 '''
'''
fruits = ['banana', 'orange', 'mango', 'lemon'] 
fruit = input("Enter Fruit: ").lower()
if fruit in fruits:
    print("The fruit already exits")
else:
    fruits.append(fruit)
    print("Modified List: ",fruits)
'''
#######################################################################################

# Conditional : Level 3
'''
Here we have a person dictionary. Feel free to modify it! 

        person={ 
    'first_name': 'Python', 
    'last_name': 'Program', 
    'age': 250, 
    'country': 'India', 
    'is_marred': True, 
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'], 
    'address': { 
        'street': 'Space street', 
        'zipcode': '02210' 
    } 
    } '''

person={ 
    'first_name': 'Python', 
    'last_name': 'Program', 
    'age': 250, 
    'country': 'India', 
    'is_marred': True, 
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'], 
    'address': { 
        'street': 'Space street', 
        'zipcode': '02210' 
    } 
    } 

# Check if the person dictionary has skills key, if so print out the middle skill in the skills list.
