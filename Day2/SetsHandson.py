# Sets: Level 1
'''
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'} 
A = {19, 22, 24, 20, 25, 26} 
B = {19, 22, 20, 25, 26, 24, 28, 27} 
age = [22, 19, 24, 25, 26, 24, 25, 24] 

# Find the length of the set it_companies 
ItCompLength = len(it_companies)
print("Length of it_companies: ", ItCompLength)

#C Add 'Twitter' to it_companies
it_companies.add("Twitter")
print("Added twitter: ", it_companies) 

#Insert multiple IT companies at once to the set it_companies 
addCompanies = ["Cognizant","Adobe","Chrome"]
it_companies.update(addCompanies)
print(it_companies)

#Remove one of the companies from the set it_companies 
it_companies.remove("Twitter")
print("Removed one company: ", it_companies)

# What is the difference between remove and discard 

# remove():: method will raise an error 
# if the specified item does not exist, 
# discard() method will not.

#it_companies.remove("Twitter")
#print(it_companies)

it_companies.discard("Twitter")
print("No Error with discard: ",it_companies)

'''
#############################################################################################

'''
# Sets: Level 2

it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'} 
A = {19, 22, 24, 20, 25, 26} 
B = {19, 22, 20, 25, 26, 24, 28, 27} 
age = [22, 19, 24, 25, 26, 24, 25, 24] 

# Join A and B 
#Join A with B and B with A
Joined = A.union(B)
print("Joined Sets: ",Joined)

#Find A intersection B 

A = {19, 22, 24, 20, 25, 26} 
B = {19, 22, 20, 25, 26, 24, 28, 27}

IntersectionSet=A.intersection(B)
print(IntersectionSet)

#Is A subset of B 

print(A.issubset(B))


#Are A and B disjoint sets 
print(A.isdisjoint(B))

#What is the symmetric difference between A and B 
# The symmetric difference of two sets A and B 
# is the set of elements which are in either of the sets A or B but not in both.
# A union B : A+B- A intersection B

print("symmetric difference: ",Joined-IntersectionSet)

#Delete the sets completely 
del A,B,age

'''
############################################################################################

'''
# Sets: Level 3

it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'} 
A = {19, 22, 24, 20, 25, 26} 
B = {19, 22, 20, 25, 26, 24, 28, 27} 
age = [22, 19, 24, 25, 26, 24, 25, 24] 

#Convert the ages to a set and compare the length of the list and the set, which one is bigger? 

ConvertSetA = set(A)
print(type(A))
ConvertSetB = set(B)
print(type(B))

LengthA = len(A)
print(LengthA)
LengthB = len(B)
print(LengthB)

if LengthA>LengthB:
    print("Set A is bigger")
else:
    print("Set B is Bigger")


#Explain the difference between the following data types: string, list, tuple and set 
# Tuples like strings are immutables. 
# Lists are mutables so they can be extended or reduced at will. 
# Sets are mutable unordered sequence of unique elements whereas frozensets are immutable sets. 
# Tuples are faster and consume less memory.

#I am a teacher and I love to inspire and teach people. How many unique words have been used in the sentence? 
# Use the split methods and set to get the unique words. 

s = "I am a teacher and I love to inspire and teach people"
print(set(s.split()))
'''