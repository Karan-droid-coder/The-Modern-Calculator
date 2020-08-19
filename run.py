import pyfiglet

ascii_banner = pyfiglet.figlet_format("The Modern Calculator")
print(ascii_banner)
print("                                        ─│───────────────────────│─")
print("                                         │  by chsaiujwal        │\n                                         │  instagram:-logobang  │\n                                         │  twitter:-chsaiujwal  │\n                                         │  telegram:-chsaiujwal │")
print("                                        ─│───────────────────────│─")






def addition():
	print("sum of", float(var1),"and", float(var2) , "is", float(var1)+float(var2))

def subtraction():
	print("subtraction of", float(var1),"and", float(var2) , "is", float(var1)-float(var2) )

def multiplication():
	print("product of", float(var1),"and", float(var2) , "is", float(var1)*float(var2) )

def division():
	print("division of", float(var1),"and", float(var2) , "is", float(var1)/float(var2) )

def modulus():
	print("modulus of", float(var1),"and", float(var2) , "is", float(var1)%float(var2) )

def floordivision():
	print("floor division of", float(var1),"and", float(var2) , "is", float(var1)//float(var2) )
def Exponent():
	print("Exponent of", int(var1),"and", int(var2) , "is", int(var1)**int(var2) )	


def select():
	print("which one you want to select")
	print("1. addition")
	print("2. subtraction")
	print("3. multiplication")
	print("4. division")
	print("5. modulus")
	print("6. floor division")
	print("7. Exponent")
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
		Exponent()
	else:
		select()

var1 = input("enter a number:-\n")

var2 = input("\nenter another number:-\n")

if var1.isnumeric() and var2.isnumeric():
	select()
else:
	print("please enter number")
	exit()



