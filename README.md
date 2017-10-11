An Introduction to Python
=========================
###### A compilation of Python basics.

This repository was created to provide an introduction to programming using Python. Below, you can find a cheatsheet of the sorts of things you'll need to write code for these programming problems.

The Basics
=========================

Data Types
--------------------------
"Data Types" are the different kinds of data you will be manipulating in Python. For now, you'll only be working with Strings and Numbers. The data types you have available to work with will change from language to language, but for now, Strings and Numbers are all that are necessary.

### Boolean
The phrase "Boolean" refers to the simplest form of information - True and False. This lets your program decide whether or not certain conditions are met.

```python
happy = True
not happy				# This returns False, meaning I am happy.
num = 10
num > 9					# This returns True, meaning num is greater than 10.
```

### Numbers
The phrase "Numbers" refers to any number you'll work with in Python. They can be positive, negative, zero, or decimal numbers. There are two major types of numbers you'll work with in Python, representing "whole" numbers, and "decimal" numbers.

### Integers
"Integers", or "ints", are the set of numbers represented *only* as whole numbers.

```python
num = 10				# I start with the number 10.

# I can subtract from this number in multiple ways.
num = num - 1			# I can set num equal to a new version of itself,
apples -= 1				# or I can specify how much I want to remove from num

# I can add to the number the same way.
num = num + 1
num += 1

# This also works for multiplication and division.
num *= 3				# 10 * 3 = 30
num /= 2				# 30 / 2 = 15

# You can also perform multiple operations in a single line.
num += 3 * 5			# 15 + (3 * 5) = 30
``` 

Trying to represent decimals as ints usually results in the information you want a fraction of being dropped off.

```python
num = 1
num /= 2				# Because num is being divided into a non-whole number (1/2)
print num				# num is now 0 instead of 0.5, since it was an integer before.
```

### Floating-Point Numbers
"Floating-Point Numbers", or "floats", are the set of numbers represented as decimals. Integers can be represented as floats, but this results in more memory consumption than necessary.

```python
num = 1.0				# When working with floats, always specify a decimal place.
num /= 2				# We've now divided num by 2, and expect 1/2 as the output.
print num
```

### Strings
The phrase "Strings" refers to a string of characters put together, like a word, sentence, or phrase. They are nominal in nature, meaning that it's not ideal to treat them as values that may be greater or less than one another in the same sense that numbers are. Usually, working with Strings means you'll be splitting it into unique data, or combining information to a human-readable form to output later.

```python
str1 = "Hello"
str2 = "World"
print str1 + ' ' + str2	# This line prints "Hello World"
```

There are *lots* of ways to work with Strings. You can trim "whitespace" characters, or split the data based on certain characters, or shorten the string based on character indices! Google is your friend - if you think working with a string might be faster using something built in, look it up!

Logic
--------------------------
"Logic" refers to the methods we use when coding to look at and manipulate data quickly, or to decide what to do with data dynamically. When we know what data we're going to be looking at beforehand, we could just write a program that works with what it expects. Realistically, we don't know what to expect though, so we try making our programs in a way that supports many use-cases. Additionally, there is a concept of "reusability" of code - this is where functions come in.

### Structure
When writing code, you have to be aware of the structure of your code. In Python, this goes doubly. In order for something to be considered a "part" of something else (like a part of a function) your code has to be properly indented. To mark the end of your line of code, you need to add a line break.

### Functions
Functions are pieces of code that you can write and call by name on the fly, instead of copying and pasting the same piece of code in multiple places. An example of a function is as follows;

```python
def func( param1, param2 ):
	# do something
	return
```

This piece of code has several parts to split up. First of all, "def" is a special python phrase meaning "define". What this does is define your "func" as a function with the code you specify. "func", however, is not a special piece of code - you can name it anything you want. "param1" and "param2" are what we call parameters; these are the things you pass to a function in order to work with data from the outside world. "return" is what you do at the end of a function. You can add a variable, or piece of data, to a return statement and it will pass that piece of data back out to whatever called the function.

### Variables
You may have noticed that in these examples, there has been a lot of use of "num" and "str". The phrase "num" and "str" aren't special Python phrases; they're just things we've decided to call our variables. You can name a variable anything that isn't considered "reserved" in the Python library. "def", for example, is a reserved word.

Variables can be changed on the fly so that you can retain information as you get it and work with it. You can pass them as parameters, print them out, or return them!

### If statements
"If" statements are declarations in the code where you decide to do something *if* a certain condition is met.

```python
num = 10
if num > 9:
	print num
```

You can also decide to do something if that condition isn't met. This is an "else" statement, and is used as a follow-up to an if statement. Else statements will not work without a corresponding if statement.

```python
num = 10
num -= 1
if num > 9:
	print num
else:
	print "too small!"
```

If you want to *only* perform an action when a condition *isn't* met, then you should write an if statement with a "not", negating the success condition.

```python
num = 10
num -= 1
if not num > 9:
	print "just small enough"
```

Resources
=========================
The information found on this repository was gathered from the following websites. If you have any difficulty following the instructions on this page or in the practice problems, referring to these sites (as well as [StackOverflow](https://stackoverflow.com/) for specific programming questions) can be a valuable resource. 

[Intro to Python](http://introtopython.org/)
[Python.org](https://www.python.org/)
[Tutorialspoint](https://www.tutorialspoint.com/python/)
[The Python Guru](http://thepythonguru.com/)
