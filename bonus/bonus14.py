from bonus.parsers14 import parse
from bonus.converters14 import convert 


feet_inches = input("Enter feet and inches: ")



def convert(feet, inches):
    meters = feet * 0.3048 + inches * 0.0254
    return meters

parsed = parse(feet_inches)

result = convert(parsed['feet'], parsed['inches'])

print(f"{parsed['feet']} feet and {parsed['inches']} inches is equal to {result}")


if result < 1:
    print("Kid is too small.")
else:
    print("Kid can use the slide.")