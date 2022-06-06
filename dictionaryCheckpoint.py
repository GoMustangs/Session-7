school = {"Andy's ID": 1, "Carly's ID": 2, "Stephany's ID": 3, "Bryce's ID": 4}

print(school)

id = int(input("put in the ID of the studen you are looking for \n the program will print 'True' or 'False' if we do or do not have that student \n what id are you looking for? "))

contains_1 = id in school.values()
print(contains_1)