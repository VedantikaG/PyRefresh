
# Exercises: Level 1 

# Declare an empty list 

emplist=[]

print(emplist)

# Declare a list with more than 5 items 

fiveItemList = ["Mumbai", "Pune", "Bangalore", "Maharashtra", "India","USA", "Denmark", "Thailand"," japan"]
print(fiveItemList)

# Find the length of your list 

print(len(fiveItemList))

# Get the first item, the middle item and the last item of the list 

print(fiveItemList[0]) # 1st
print(fiveItemList[2]) # Middle
print(fiveItemList[-1]) # Last

# Declare a list called mixed_data_types, put your(name, age, height, marital status, address)

mixed_data_types = ["Vedantika", 21, 5.4, "Single", "Mumbai"] 
print(mixed_data_types)

# Declare a list variable named it_companies and assign initial values Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon. 
 
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle","Amazon"]

# Print the list using print() 

print("IT Companies: ", it_companies)

# Print the number of companies in the list 

print(len(it_companies))

# Print the first, middle and last company

print("First Company: ", it_companies[0])
x= len(it_companies)
y = int(x//2)
print("Middle Company: ", it_companies[y])
print("Last Company: ", it_companies[-1])

# Print the list after modifying one of the companies 
it_companies.insert(1, "Accenture")
print(it_companies)

# Add an IT company to it_companies 

it_companies.append("Cognizant")
print(it_companies)

# Insert an IT company in the middle of the companies list 

it_companies.insert(y, "Ajio")
print(it_companies)

# Change one of the it_companies names to uppercase (IBM excluded!) 

upperList = [u.upper() for u in it_companies]
print(upperList)

# Join the it_companies with a string '#;  ' 
'''

it_companies.append("#;")
print(it_companies)
'''
# Check if a certain company exists in the it_companies list. 

company = "Apple"

if company ==  "Apple" in it_companies:
    print("Voila!!, This Company Exits")
else:
    print("Aree!! Comapny does not exist")

# Sort the list using sort() method 
it_companies.sort()
print("Sorted List: " , it_companies)

# Reverse the list in descending order using reverse() method 
it_companies.sort(reverse=True)
print("Sorted Reverse List: " , it_companies)


# Slice out the first 3 companies from the list 
firstThree = it_companies[:3]
print(firstThree)

# Slice out the last 3 companies from the list 
lastThree = it_companies[-3:]
print(lastThree)

# Slice out the middle IT company or companies from the list 

length = len(it_companies)
drop = length % 2
if drop == 0:
    middle_company = [it_companies[length//2],it_companies[(length//2)+1]]
elif drop!=0:
    middle_company = [it_companies[length//2]]

print(middle_company)

# Remove the first IT company from the list 

RemoveITCompany=it_companies.remove("Apple")
print(RemoveITCompany)

# Remove the middle IT company or companies from the list 

print(it_companies)
midNum= len(it_companies)//2
print(it_companies[midNum])


# Remove the last IT company from the list 
RemLastCompany = it_companies[:-1]
print(RemLastCompany)

# Remove all IT companies from the list 
RemAllCompany = it_companies.clear()
print(RemAllCompany)

# Destroy the IT companies list 
del it_companies

'''
Join the following lists: 
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux'] 
back_end = ['Node','Express', 'MongoDB'] 
'''
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux'] 
back_end = ['Node','Express', 'MongoDB']

front_end.extend(back_end)
print(front_end)

'''
After joining the lists in question 26. 
Copy the joined list and assign it to a variable full_stack, 
then insert Python and SQL after Redux. 
'''
full_stack = front_end.copy()
print(full_stack)
 
index_last = full_stack.index("MongoDB")
full_stack.insert(index_last + 1, "Python")
full_stack.insert(index_last + 2, "SQL")
print(full_stack)












'''

Slice out the last 3 companies from the list 

Slice out the middle IT company or companies from the list 

Remove the first IT company from the list 

Remove the middle IT company or companies from the list 

Remove the last IT company from the list 

Remove all IT companies from the list 

Destroy the IT companies list 

Join the following lists: 
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux'] 
back_end = ['Node','Express', 'MongoDB'] 

After joining the lists in question 26. Copy the joined list and assign it to a variable full_stack, then insert Python and SQL after Redux. 

Exercises: Level 2 

The following is a list of 10 students ages: 

ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24] 

Sort the list and find the min and max age 

Add the min age and the max age again to the list 

Find the median age (one middle item or two middle items divided by two) 

Find the average age (sum of all items divided by their number ) 

Find the range of the ages (max minus min) 

Compare the value of (min - average) and (max - average), use abs() method 

Find the middle country(ies) in the [countries list] 

Divide the countries list into two equal lists if it is even if not one more country for the first half. 

['China', 'Russia', 'USA', 'India', 'Sweden', 'Norway', 'Denmark']. Unpack the first three countries and the rest as scandic countries. 

 '''

 