a = int(input(" Enter Value of a: "))
b = int(input(" Ente rthe value of b: "))

try:
    print(a+b/2)
except ZeroDivisionError as e:
    print("Second parameter Value Should not be Zero")
except Exception as e1:
    print("")

print("End of the Program")