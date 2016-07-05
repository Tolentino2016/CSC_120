##month = int(input('Enter month (numeric): '))
##day = int(input('Enter day: '))
##year = int(input('Enter two digit year: '))
##if (month * day) == year:
##	print("This date is magic!")
##else:
##	print("This date is not magic.")

##integer = int(input("Enter a nonnegative integer:"))
##i = 1
##while i != "stop":
##	i *= integer
##print(i)

##integer = int(input("Enter a nonnegative integer:"))
##n = 0
##while n < 0: 
##	integer = int(input("Enter a nonnegative integer:"))
##	n *= integer
##print(n)

##integer = int(input("Enter a nonnegative integer:"))
##n = 0
##for n in range(1, integer + 1): 
##	n *= integer
##print(n)

##def factorial(n):
##    f = 1
##    while (n > 0):
##        f = f * n
##        n = n - 1
##    return f
##
##integer = int(input("Enter a nonnegative integer:"))
##n = 0
##for n in range(1, integer + 1): 
##	integer *= integer
##print(n)


integer = int(input("Enter a nonnegative integer:"))
n = 1
while integer > 0:
	n *= integer
	integer = integer - 1
print(n)
