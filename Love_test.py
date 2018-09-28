#asking for the names
name_one = input("What is your name?")
name_two = input("What is your lovers name?")


name_one = name_one.lower().strip()
name_two = name_two.lower().strip()

#printing result
print(name_one)
print(name_two)

#finding out if the names are equal, greater or lesser
if name_one == name_two:
	print("Crazy, this is not good")
elif name_one > name_two:
	print("Good love")
elif name_one < name_two:
	print("Bad love")

#control if the names are the same
if name_one == name_two:
	print("You have the same name")

#checking the lenghts of the names 	

if len(name_one) > len(name_two):
	print(name_one + " " + "is dominant in your relation")

else:
	print(name_two + " " + "is dominant in your relation")

	
#checking the similarity percentage based on the lenghts of the names
difference = len(name_one) - len(name_two)

difference_two = abs(difference)

if difference_two < 1:
	print("Perfect match, 100% match")

elif difference_two < 2:
	print("Almost a perfect match, keep working on your relation, 80% match")
	
elif difference_two < 3:
	print("You have to work harder to get a good relationship, 60% match")
	
elif difference_two < 4:
	print("I don't think this is the right lover for you, 40% match")
	
elif difference_two < 5:
	print("You should find someone else, 20% match")

else:
	print("Love is not your destiny, 0% match")
	