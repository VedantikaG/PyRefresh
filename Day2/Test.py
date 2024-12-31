a=10
b=10
if a>b:
    print("Greater")
elif a<b:
    print("Lesser")
elif a==b:
    print("Equals")
else:
    pass

# Iternery 
# True if condition else FALSE

print("True") if a==b else print("False")

##############################################

a = int(input())
b= int(input())
c = a+b
if c//2==0:
    print("Even Number")
elif c//2!=0:
    print("Odd it is")
else:
    print("try again")
