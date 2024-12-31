# The following is a list of 10 students ages: 

ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24] 

# Sort the list and find the min and max age 

ages.sort()
print(ages)
MinAge = ages[0]
MaxAge = ages[-1]
print("Minimum age: ", MinAge )
print("Maximum age: ", MaxAge )

# Add the min age and the max age again to the list 
ages.append(MinAge)
print(ages)

ages.append(MaxAge)
print(ages)

# Find the median age (one middle item or two middle items divided by two) 

mid = len(ages)
drop = mid % 2
if drop == 0:
    median = mid//2
    print(ages[median])
else:
    median1 = mid//2
    median2 = (mid//2)+1

    print(ages[median1])
    print(ages[median2])

# Find the average age (sum of all items divided by their number ) 
avgAge = sum(ages)//len(ages)
print("Average Age: ", avgAge)

# Find the range of the ages (max minus min) 


