# Dictionary are used for JSON  files
# Its a KEY: VALUE pair 

a1 = {id: 101, "name":"python","loc": "Mumbai"}
print(a1)
print(type(a1))

a1[id] = 102
print(a1)

a1["sal"] = 1000
print(a1)

print(a1["loc"])

b1 = {
    101: "Java",
    102: "Python",
    103: {
        "Python": "Pandas",
        "Java": "Sprint"
    }
}
print(b1[103]["Python"])