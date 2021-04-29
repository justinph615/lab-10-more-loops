userstring = input("Gimme Number greater than 100 ")
usernum = int(userstring)

while (usernum < 100):


	print(str(usernum)+ " is less than 100. Try again")
	userstring = input(str(usernum))
	usernum = int(userstring)

 
#print(str(usernum) + " is greater than 100. Great job.")
userstring = input(str(usernum) + " is greater than 100. Great job!!!")