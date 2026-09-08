car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.values()

print(x) #before the change

car.update({"year" : 2020})
car.update({"colour" : "Green"})

print(x)