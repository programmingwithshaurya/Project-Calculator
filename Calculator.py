from os import system

system("cls")

print("This is An Calculator")

print("1.Addition")
print("2.Subtraction")
print("3.Multiplication")
print("4.Division")

opt1 = int(input("Enter an Option"))


# Option 1
if opt1 == 1:
	print("Enter Your First Number")
	add1 = int(input())
	print("Enter Your Second Number")
	add2 = int(input())

	add_3_total = add1+add2

	print("Sum is " + str(add_3_total))


#===================================================#


if opt1 == 2:
	print("Enter Your First Number")
	sub1 = int(input())
	print("Enter Your Second Number")
	sub2 = int(input())

	sub_3_total = sub1-sub2

	print("Subract is " + str(sub_3_total))


#==================================================#

if opt1 == 3:
	print("Enter Your First Number")
	mul1 = int(input())
	print("Enter Your Second Number")
	mul2 = int(input())

	mul3_total = mul1+mul2

	print("Multiplication is " + str(mul3_total))


#================================================#

if opt1 == 4:
	print("Enter Your First Number")
	div1 = int(input())
	print("Enter Your Second Number")
	div2 = int(input())

	div3_total = div1+div2

	print("Division is " + str(div3_total))

