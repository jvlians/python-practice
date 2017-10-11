An Introduction to Python: Lv. 2
=========================
###### A compilation of second-level Python basics.

This repository was created to provide an introduction to programming using Python. Below, you can find a cheatsheet of the sorts of things you'll need to write code for these programming problems.

The Complex
=========================

Data Structures
--------------------------
Data Structures are things that hold data in different ways. Depending on the data structure you're working with, there are unique advantages. Some data structures make it easy to write data, others make it easy to retrieve data, and others still make it easy to destroy data. In these examples, you won't be extraordinarily concerned with speed, but in the real world, data gets big *fast*. It's important to know what to use, and when to use it.

Logic
--------------------------
You should already know the most basic structure of a program, and how to write code. However, what if you're given a data structure whose size you aren't aware of? What if you're given lots of data at once and don't want to look at it individually? This is where we get into concepts of iteration and recursion.

### For Statements
A "for" statement is something that helps us do the same operation to many things, one at a time. The basic structure of a for statement is as follows;

```python
for letter in 'Word':
	print "Current letter: ", letter

fruits = ['apple', 'banana', 'mango', 'strawberry', 'kiwi', 'grape', 'tomato']
for fruit in fruits:
	print "Current fruit: ", fruit

for index in range(len(fruits)):
	print "Fruit at index %d is %s" % (index, fruits[index])
```

Resources
=========================
The information found on this repository was gathered from the following websites. If you have any difficulty following the instructions on this page or in the practice problems, referring to these sites (as well as [StackOverflow](https://stackoverflow.com/) for specific programming questions) can be a valuable resource. 

[Intro to Python](http://introtopython.org/)
[Python.org](https://www.python.org/)
[Tutorialspoint](https://www.tutorialspoint.com/python/)
[The Python Guru](http://thepythonguru.com/)
