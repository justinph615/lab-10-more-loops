maximum_stories = 20

userinput = input("On what floor of the building is your office? ")

floor = int(userinput)

while (floor > maximum_stories):


	userinput = input("I'm sorry. You entered " + str(floor) + ". We only have " + str(maximum_stories) + " floors in our building. Please Try again. ")

	floor = int(userinput)



print("Nice! Your office is located on floor " + str(floor))