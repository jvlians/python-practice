def twoSum( arr, target ):
	# This problem is a little more complex.
	# Your goal is to see if the array you're given contains any two numbers
	# that, when added, yield the sum you're looking for.

	# Your code goes here!



arr = [5, 7, 12, 3, 11, 14, 6, 1, 9, 18, 20, 22, 33, 13, 8]
target = 15
print twoSum(arr, target)
if twoSum(arr,target):
	print "success!"
else:
	print "try again!"