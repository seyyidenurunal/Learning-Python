person = {
    "adi" : "Ayşe Nur",
    "soyadi": "Çelik",
    "yaş" : "25",
}

print("1__________")

person["color"] = "red"

print(person)

print("2__________")

print(person)


print("3___________")


print(dir(person))
print(help(person.get))


print("4____________")

if "yemek" in person:
    print(person["yemek"])
else:
    print("Bulunamadı.")

if "adi" in person:
    print(person["adi"])
else:
    print("Bulunamadı.")

print("5____________")


print(person.get("yemek", False))

print(person.get("adi", False))


print("6____________")


print(type(person))


print("7____________")   

print(person.items())

for element in person.items():
    print(element)

for element in person.items():
    print(element[0]) #anahtar

for element in person.items():
    print(element[1]) #değer


print("8____________")   


for anahtar, değer in person.items():
    print(anahtar, "=", değer)


print("8____________")  


print(person.keys())

for key in person.keys():
    print(person[key])


print("9____________")  


print(person.values())

for value in person.values():
    print(value)


print("10____________")  

#person[123] ="deneme"

person[123] = ["deneme", 1 , 2 , 3 ]

print(person[123])





