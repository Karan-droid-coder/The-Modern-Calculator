import pyfiglet

ascii_banner = pyfiglet.figlet_format("The Modern Calculator")
print(ascii_banner)
print("                                        ─│───────────────────────│─")
print("                                         │  by chsaiujwal        │\n                                         │  instagram:-logobang  │\n                                         │  twitter:-chsaiujwal  │\n                                         │  telegram:-chsaiujwal │")
print("                                        ─│───────────────────────│─")






def addition():
	var1 = input("\nenter a number:-\n")

	var2 = input("\nenter another number:-\n")

	print("\n\nsum of", float(var1),"and", float(var2) , "is", float(var1)+float(var2))
	exit()

def subtraction():
	var1 = input("\nenter a number:-\n")

	var2 = input("\nenter another number:-\n")

	
	print("\n\nsubtraction of", float(var1),"and", float(var2) , "is", float(var1)-float(var2) )
	exit()

def multiplication():
	var1 = input("\nenter a number:-\n")

	var2 = input("\nenter another number:-\n")

	
	print("\n\nproduct of", float(var1),"and", float(var2) , "is", float(var1)*float(var2) )
	exit()

def division():
	var1 = input("\nenter a number:-\n")

	var2 = input("\nenter another number:-\n")

	
	print("\n\ndivision of", float(var1),"and", float(var2) , "is", float(var1)/float(var2) )
	exit()

def modulus():
	var1 = input("enter a number:-\n")

	var2 = input("\nenter another number:-\n")

	
	print("\n\nmodulus of", float(var1),"and", float(var2) , "is", float(var1)%float(var2) )
	exit()

def floordivision():
	var1 = input("\nenter a number:-\n")

	var2 = input("\nenter another number:-\n")

	
	print("\n\nfloor division of", float(var1),"and", float(var2) , "is", float(var1)//float(var2) )
	exit()

def exponent():
	var1 = input("\nenter a number:-\n")

	var2 = input("\nenter another number:-\n")

	print("\n\nExponent of", int(var1),"and", int(var2) , "is", int(var1)**int(var2) )
	exit()	

def square_area():
	var1 = input("\nplease enter square's side length:-\n")
	
	print("\n\narea of square of side "+str(var1)+" is ",float(var1)*float(var1))
	exit()

def rectangle_area():
	var1 = input("\nenter length of rectangle:-\n")

	var2 = input("\nenter breath of rectangle:-\n")

	print("\n\narea of rectangle with length ", int(var1)," and breath ", int(var2) , " is ", int(var1)*int(var2) )
	exit()	


def parallelogram_area():
	var1 = input("\nenter breath of parallelogram:-\n")

	var2 = input("\nenter height of parallelogram:-\n")

	print("\n\narea of parallelogram with breath ", int(var1)," and height ", int(var2) , " is ", int(var1)*int(var2) )	
	exit()

def circle_area():
	var1 = input("\nenter radius of circle:-\n")


	print("\n\n area of circle with radius ", int(var1)," is ",22/7*int(var1)*int(var1) )	
	exit()




def cube_volume():
	var1 = input("\nenter side of square:-\n")


	print("\n\n volume of square with side ", int(var1)," is ", int(var1)*int(var1)*int(var1) )	
	exit()

def cuboid_volume():
	var1 = input("\nenter length of cuboid:-\n")

	var2 = input("\nenter breath of cuboid:-\n")

	var3 = input("\nenter height of cuboid:-\n")

	print("\n\n volume of cuboid with length ", int(var1),", breath ", int(var2) ,", height", int(var3), " is ", int(var1)*int(var2)*int(var3) )	
	exit()

def cylinder_volume():
	var1 = input("\nenter radius of cylinder:-\n")

	var2 = input("\nenter height of cylinder:-\n")

	print("\n\n volume of cylinder with radius ", int(var1)," and height ", int(var2) , " is ", 22/7*(int(var1)*int(var1))*int(var2) )	
	exit()


def area():
	print("which one you want to select")
	print("1. area of square")
	print("2. area of rectangle")
	print("3. area of parallelogram")
	print("4. area of circle")
	print("\n99. go back")
	j=input()
	if j=="1":
		square_area()
	if j=="2":
		rectangle_area()
	if j=="3":
		parallelogram_area()
	if j=="4":
		circle_area()
	if j=="99":
		select()
	else:
		area()


def volume():
	print("which one you want to select")
	print("1. volume of cube")
	print("2. volume of cuboid")
	print("3. volume of cylinder")
	print("\n99. go back")
	l=input()
	if l=="1":
		cube_volume()
	if l=="2":
		cuboid_volume()
	if l=="3":
		cylinder_volume()
	if l=="99":
		select()
	else:
		volume()






def select():
	print("which one you want to select")
	print("1. normal calculation")
	print("2. area")
	print("3. volume")
	i=input()
	if i=="1":
		normal()
	if i=="2":
		area()
	if i=="3":
		volume()
	else:
		select()







def normal():
	print("which one you want to select")
	print("1. addition")
	print("2. subtraction")
	print("3. multiplication")
	print("4. division")
	print("5. modulus")
	print("6. floor division")
	print("7. Exponent")
	print("99. go back")
	k = input()
	if k=="1":
		addition()
	elif k=="2":
		subtraction()
	elif k=="3":
		multiplication()
	elif k=="4":
		division()
	elif k=="5":
		modulus()
	elif k=="6":
		floordivision()
	elif k=="7":
		exponent()
	elif k=="99":
		select()
	else:
		normal()

try:
	select()
except KeyboardInterrupt:
	print("\n\nyou want to exit?     Y/N ")
	z = input()
	if z=="Y" or z=="y":
		quit()
	elif z=="N" or z=="n":
		select()



