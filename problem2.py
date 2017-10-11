def concat(str1, str2):
	# Now, write a program that combines the first and second strings 
	# with a space between!
	return str1+" "+str2
	# Your code goes here!
	


str1 = "Hello"
str2 = "World"
print(concat(str1, str2))
if concat(str1, str2) == "Hello World":
	print('success!')
else:
	print('try again!')