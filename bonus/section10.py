
password = input("Enter new password:  ")

result = {}

if len(password) >= 8:
    result["Length"] = True
else:
    result["Length"] = False


digit = False
for i in password:
    if i.isdigit():
        digit = True

result["digits"] = digit 

upper = False
for x in password:
    if x.isupper():
        upper = True

result["upper - case"] = upper

print(result)


if all(result.values()):
    print("Strong Password")
else:
    print("Weak Password")
