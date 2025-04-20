# Using default and keyword argument for the function

i = 0

def residentInfo(name="Resident", age=0, city="Not provided", id=0):
    return f"Information of {name}:\nAge: {age}\nCity: {city}\nID: {id}"

while True:
    name = input("Name of resident: ")
    age = int(input("Age of resident: "))
    city = input("Current address (City): ")
    print(f"Summary:\n{residentInfo(name, age, city, id=i)}")
    i += 1

    again = bool(int(input("Add another resident?: [1/0]: ")))
    if not again:
        break