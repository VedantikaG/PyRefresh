
'''
# Tuples: Level 1

#Create an empty tuple 
myTuple = ()
print(type(myTuple))

#Create a tuple containing names of your sisters and your brothers (imaginary siblings are fine)
# # Join brothers and sisters tuples and assign it to siblings  
#SiblingNames = ("Hrishikesh","Jaysingh","Kshitij","Mrinalini","Madhura")
Sisters = ("Mrinalini","Madhura")
brothers = ("Hrishikesh","Jaysinh","Kshitij")
print(Sisters+brothers)

#How many siblings do you have? 
sibling = Sisters+brothers
print(len(sibling))

#Modify the siblings tuple and add the name of your father and mother and assign it to family_members 
familyNames = sibling.append("Mummy","Pappa")
print(familyNames)
'''
#################################################################################

# Tuples : Level 2

SiblingNames = (("Hrishikesh","Jaysingh","Kshitij"),("Mrinalini","Madhura"))
#Sisters = ("Mrinalini","Madhura")
#brothers = ("Hrishikesh","Jaysinh","Kshitij")

#Unpack siblings and parents from family_members 
brothers,Sisters  = SiblingNames
print(Sisters)

#Create fruits, vegetables and animal products tuples. Join the three tuples and assign it to a variable called food_stuff_tp. 

fruits = ("Mango", "Apple","Banana","Orange","Strawberry","Grapes","Avocado")
vegetables = ("Tomato","Onion","Spinach","corriender","Cabbage")
animal = ("Chicken","Fish","Crabs","Beef")

food_stuff_tp = fruits+vegetables+animal
print("Three Tuples joined: ",food_stuff_tp)

#Change the about food_stuff_tp tuple to a food_stuff_lt list 
food_stuff_lt = list(food_stuff_tp)
print(type(food_stuff_lt))

#Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list. 

'''
size = len(food_stuff_tp)
mid = size%2

if mid==0:'''

#Slice out the first three items and the last three items from food_staff_lt list 

#Delete the food_staff_tp tuple completely 

#Check if an item exists in tuple: 

#Check if 'Estonia' is a nordic country 

#Check if 'Iceland' is a nordic country 
#nordic_countries = ('Denmark', 'India','Iceland', 'Norway', 'Sweden') 