#nested datastructures
people = [
    {"name": "Harry", "house": "Gryffindor"},
    {"name": "Cho", "house": "Ravenclaw"},
    {"name": "Draco", "house": "Slytherin"},
    {"name": "fungus", "house": "Ravenclaw"}
]

#lambda says what sort() have to sort
people.sort(key = lambda person: person["name"]) 

print(people)