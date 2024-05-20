"""Python Command Guide
Created on 03/28/2024
@author Leilani Matthews"""


############################################### PYTHON DATA TYPES & DATA STRUCTURES #################################################

'''Both Data Types and Data Structures play crucial roles in handling and organizing data in Python:

Python Data types are the classification or categorization of data items. It represents the kind of value that tells what operations can be performed on a particular data. Since everything is an object in Python programming, Python data types are classes and variables are instances (objects) of these classes. The following are the standard or built-in data types in Python:

Numeric
Sequence Type
Boolean
Set
Dictionary
Binary Types( memoryview, bytearray, bytes)

Python Data Structures are a way of organizing data so that it can be accessed more efficiently depending upon the situation. 
Data Structures are fundamentals of any programming language around which a program is built. Python helps to learn the fundamental of these data structures in a simpler way as compared to other programming languages.


Variables can store data of different types, and different types can do different things.
Python has the following data types built-in by default, in these categories:

1. TEXT TYPE	
-str: Represents text strings.
2. NUMERIC TYPES	
- int:   Represents integer numbers.
- float: Represents real numbers.
- complex: Represents the sum of a real number and an imaginary number is defined as a complex number.
3. SEQUENCE TYPES
-list:  list() function creates a list object.
-tuple: tuple is a collection of Python objects much like a list.
-range:  range() function returns a sequence of numbers, in a given range. 
4. MAPPING TYPE
-dict: Represents a key-value pair collection.
5. SET TYPES	
-set:  a set is an unordered collection of data types that is iterable, mutable, and has no duplicate elements.
-frozenset: frozen sets are immutable sets that allow you to perform various set operations such as union,      intersection, difference, and symmetric difference.
6. BOOLEAN TYPE	
-bool: Represents boolean values of `True` or `False`.
7. BINARY TYPES	
-bytes
-bytearray
-memoryview
8. NONE TYPE
-NoneType

Setting the Data Type
In Python, the data type is set when you assign a value to a variable:

Example   Data Type
x = str("Hello World")	str	
x = int(20)	int	
x = float(20.5)	float	
x = complex(1j)	complex	
x = list(("apple", "banana", "cherry"))	list	
x = tuple(("apple", "banana", "cherry"))	tuple	
x = range(6)	range	
x = dict(name="John", age=36)	dict	
x = set(("apple", "banana", "cherry"))	set	
x = frozenset(("apple", "banana", "cherry"))	frozenset	
x = bool(5)	bool	
x = bytes(5)	bytes	
x = bytearray(5)	bytearray	
x = memoryview(bytes(5))	memoryview'''

'''TEXT TYPE'''

'''- `str`: Represents text strings.
A String is a data structure in Python that represents a sequence of characters. It is an immutable data type, meaning that once you have created a string, you cannot change it. Strings are used widely in many different applications, such as storing and manipulating text data, representing names, addresses, and other types of data that can be represented as text.'''

#Python String Format() 
#Syntax: string = 'Hello, world!'

#Example 1:

# Creating a String 
# with single Quotes 
String1 = 'Welcome to the Geeks World'
print("String with the use of Single Quotes: ") 
print(String1) 

#OUTPUT: 
String with the use of Single Quotes: 
Welcome to the Geeks World

#Example 2:

#Python String count() function returns the number of occurrences of a substring within a String.
#initializing a string
my_string = "Apple"
#using string count() method
char_count = my_string.count('A')
#printing the result
print(char_count)

#OUTPUT: 
1

'''NUMERIC TYPES'''

''' - `int`: Represents integer numbers.
Python int() function returns an integer from a given object or converts a number in a given base to a decimal.'''
#Python int() Function 
#Syntax: int(x, base)

#Example:

# int() on string representation of numbers
print("int('9')) =", int('9'))
# int() on float values
print("int(9.9) =", int(9.9))
# int() on Python integer
print("int(9) =", int(9))

#OUTPUT: 
int('9')) = 9
int(9.9) = 9
int(9) = 9

#Convert base using int() in Python
# octal to decimal using int()
print("int() on 0o12 =", int('0o12', 8))
 
# binary to decimal using int()
print("int() on 0b110 =", int('0b110', 2))
 
# hexa-decimal to decimal using int()
print("int() on 0x1A =", int('0x1A', 16))

#OUTPUT:
int() on 0o12 = 10
int() on 0b110 = 6
int() on 0x1A = 26


''' - `float`: Represents real numbers.
Python float() function is used to return a floating-point number from a number or a string representation of a numeric value.'''
#Python float() 
#Syntax:  float(x)

#Example1:

# convert integer value to float
num = float(10)
print(num)

#OUTPUT: 
10.0

#Example 2:
# Python program to illustrate
# Various examples and working of float()
# for integers
print(float(21.89))
 
# for floating point numbers
print(float(8))
 
# for integer type strings
print(float("23"))
 
# for floating type strings
print(float("-16.54"))
 
# for string floats with whitespaces
print(float("     -24.45   \n"))
 
# for inf/infinity
print(float("InF"))
print(float("InFiNiTy"))
 
# for NaN
print(float("nan"))
print(float("NaN"))

#OUTPUT: 

21.89
8.0
23.0
-16.54
-24.45
inf
inf
nan
nan

'''complex: Represents the sum of a real number and an imaginary number is defined as a complex number.
   real [optional]: numeric type (including complex). It defaults to zero.
   imaginary [optional]: numeric type (including complex) .It defaults to zero.'''
#Python complex() Function
#Syntax: complex ([real[, imaginary]])

#Example:

# numeric type
# nothing is passed
z = complex()
print("complex() with no parameters:", z)
 
# integer type
# passing first parameter only
complex_num1 = complex(5)
print("Int: first parameter only", complex_num1)
 
# passing both parameters
complex_num2 = complex(7, 2)
print("Int: both parameters", complex_num2)
 
# float type
# passing first parameter only
complex_num3 = complex(3.6)
print("Float: first parameter only", complex_num3)
 
# passing both parameters
complex_num4 = complex(3.6, 8.1)
print("Float: both parameters", complex_num4)
print()
 
# type
print(type(complex_num1))

#OUTPUT: 
Nothing is passed 0j
Int: first parameter only (5+0j)
Int: both parameters (7+2j)
Float: first parameter only (3.6+0j)
Float: both parameters (3.6+8.1j)


'''SEQUENCE TYPES

list:  list() function creates a list object. Python list() function takes any iterable as a parameter and returns a list.'''

#Python list() Function 
#Syntax: list(iterable)

#Example: 

# initializing a string
string = "ABCDEF"
 
# using list() function to create a list
list1 = list(string)
 
# printing list1
print(list1)

#OUTPUT:
['A', 'B', 'C', 'D', 'E', 'F']

'''-tuple: tuple is a collection of Python objects much like a list.'''
#Python tuple() function
#Syntax: tuple(iterable)

#Example 1:

l = [1,2,3]
print(tuple(l))

#OUTPUT:
(1, 2, 3)

#Example 2:
 
# when parameter is not passed
tuple1 = tuple()
print("empty tuple:", tuple1)
 
# when an iterable(e.g., list) is passed
list1= [ 1, 2, 3, 4 ] 
tuple2 = tuple(list1)
print("list to tuple:", tuple2)
 
# when an iterable(e.g., string) is passed
string = "geeksforgeeks"; 
tuple4 = tuple(string)
print("str to tuple:", tuple4)


#OUTPUT:
empty tuple: ()
list to tuple: (1, 2, 3, 4)
str to tuple: ('g', 'e', 'e', 'k', 's', 'f', 'o', 'r', 'g', 'e', 'e', 'k', 's')


'''-range:  range() function returns a sequence of numbers, in a given range.'''

#Python range() function
#Syntax: range(start, stop, step)

#Example 1:
# printing first 6
# whole number
for i in range(6):
    print(i, end=" ")
print()

#OUTPUT:
0 1 2 3 4 5

#Example 2: 
# printing a natural
# number from 5 to 20
for i in range(5, 20):
    print(i, end=" ")

#OUTPUT
5 6 7 8 9 10 11 12 13 14 15 16 17 18 19


'''MAPPING TYPE'''

'''- `dict`: Represents a key-value pair collection. 
The dict() function is used to create a new dictionary or convert other iterable objects into a dictionary. A dictionary is a mutable data structure i.e. the data in the dictionary can be modified. 
A dictionary is an indexed data structure i.e. the contents of a dictionary can be accessed by using indexes, here in the dictionary, the key is used as an index'''

#Python dict() Function
#Python dict() Syntax
dict(**kwarg)

#Example 1:

#Creating dictionary using keyword arguments
# passing keyword arguments to dict() method 
myDict = dict(a=1, b=2, c=3, d=4) 
print(myDict) "2")

#OUTPUT:
{'a': 1, 'b': 2, 'c': 3, 'd': 4}

#Example 2:

#Creating deep-copy of the dictionary using dict()
#dict(mapping)

main_dict = {'a': 1, 'b': 2, 'c': 3} 
  
# deep copy using dict 
dict_deep = dict(main_dict) 
  
# shallow copy without dict 
dict_shallow = main_dict 
  
# changing value in shallow copy will change main_dict 
dict_shallow['a'] = 10
print("After change in shallow copy, main_dict:", main_dict) 
  
# changing value in deep copy won't affect main_dict 
dict_deep['b'] = 20
print("After change in deep copy, main_dict:", main_dict)

#OUTPUT:
After change in shallow copy, main_dict: {'a': 10, 'b': 2, 'c': 3}
After change in deep copy, main_dict: {'a': 10, 'b': 2, 'c': 3}

'''SET TYPES

-set:  a set is an unordered collection of data types that is iterable, mutable, and has no duplicate elements.'''
#Python set() Function
#Syntax: set(iterable)

#Example 1:
# creating an empty set by using set() 
s = set() 
print("Type of s is ",type(s))
#Output: Type of s is  <class 'set'>

#Example 2:
# working of set() on list 
# initializing list  
lis1 = [ 3, 4, 1, 4, 5 ] 
  
# Printing iterables before conversion 
print("The list before conversion is : " + str(lis1)) 
  
# Iterables after conversion are  
# notice distinct and elements 
print("The list after conversion is : " + str(set(lis1)))
#Output:
The list before conversion is : [3, 4, 1, 4, 5]
The list after conversion is : {1, 3, 4, 5}


'''-frozenset: frozen sets are immutable sets that allow you to perform various set operations such as union, intersection,       difference, and symmetric difference.'''
#Python frozenset()
#Syntax : frozenset(iterable_object_name)

#Example 1: 

#Working of Python frozenset()
fruits = frozenset(["apple", "banana", "orange"])
print(fruits) 
fruits.append("pink")
print(fruits) 

#OUTPUT:

frozenset({'banana', 'orange', 'apple'})
Traceback (most recent call last):
  File "C:\Users\ashub\OneDrive\Desktop\achal cahtgpt\temp.py", line 3, in <module>
    fruits.append("pink")
AttributeError: 'frozenset' object has no attribute 'append'

#Example 2: 
#Python frozenset for Tuple

# passing an empty tuple
nu = ()
 
# converting tuple to frozenset
fnum = frozenset(nu)
 
# printing empty frozenset object
print("frozenset Object is : ", fnum)

#OUTPUT:
frozenset Object is :  frozenset()

'''BOOLEAN TYPE'''
'''-bool: Represents boolean values of `True` or `False`.
bool() is a built-in function of Python programming language. It is used to convert any other data type value (string, integer, float, etc) into a boolean data type.
boolean data type can store only 2 values: True and False.
False Values: 0, NULL, empty lists, tuples, dictionaries, etc.'''


#Python bool Format() 
#Syntax: bool([x])

#Example:

x = bool(1)
print(x)
y = bool()
print(y)

#OUTPUT:
True
False

# Python program to illustrate
# built-in method bool()
 
# Returns False as x is False
x = False
print(bool(x))
 
# Returns True as x is True
x = True
print(bool(x))

#OUTPUT:
False
True

'''BINARY TYPES'''
'''-bytes: Python byte() function converts an object to an immutable byte-represented object of a given size and data.'''

#Python bytes() function
#Syntax: bytes(src, enc, err)

#Example 1: 

# python code to demonstrate
# int to bytes
 
number = 12
result = bytes(number)
 
print(result)
#OUTPUT:
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'

#Example 2: 

# Demonstrate the working of bytes() on int, iterables, none
# initializing integer and iterables

a = 4
lis1 = [1, 2, 3, 4, 5]
 
# No argument case
print ("Byte conversion with no arguments : " + str(bytes())) 
 
# conversion to bytes 
print ("The integer conversion results in : "  + str(bytes(a)))
print ("The iterable conversion results in : "  + str(bytes(lis1)))

#OUTPUT: 
Byte conversion with no arguments : b''
The integer conversion results in : b'\x00\x00\x00\x00'
The iterable conversion results in : b'\x01\x02\x03\x04\x05'


'''-bytearray: bytearray() method returns a bytearray object in Python which is an array of given bytes. It gives a mutable sequence of integers in the range 0 <= x < 256. '''
#Python | bytearray() function
#Syntax: bytearray(source, encoding, errors)

#Example 1:
#bytearray() Function on String

str = "HelloWorld"
 
# encoding the string with unicode 8 and 16
str = "Hello! World"
 
# encoding the string with unicode 8 and 16
array1 = bytearray(str, 'utf-8')
array2 = bytearray(str, 'utf-16')
 
print(array1)
print(array2)

#OUTPUT:
bytearray(b'Hello! World')
bytearray(b'\xff\xfeH\x00e\x00l\x00l\x00o\x00!\x00 \x00W\x00o\x00r\x00l\x00d\x00')

#Example 2:
#bytearray() Function on a byte Object

# Creates bytearray from byte literal
arr1 = bytearray(b"abcd")
 
# iterating the value
for value in arr1:
    print(value)
     
# Create a bytearray object
arr2 = bytearray(b"aaaacccc")
 
# count bytes from the buffer
print("Count of c is:", arr2.count(b"c"))

#OUTPUT:
97
98
99
100
Count of c is: 4

'''-memoryview: Python memoryview() function returns the memory views objects. Before learning more about memoryview() function let’s see why do we use this function.'''

#Python memoryview() Function
#Syntax: memoryview(obj)

#Example 1: 
#Python memoryview() works

byte_array = bytearray('XYZ', 'utf-8')
 
mv = memoryview(byte_array)
 
print(mv[0])
print(bytes(mv[0:1]))

#OUTPUT:
88
b'X'

#Example 2: 
# Python program to illustrate
# Modifying internal data using memory view
 
# random bytearray
byte_array = bytearray('XYZ', 'utf-8')
print('Before update:', byte_array)
 
mem_view = memoryview(byte_array)
 
# update 2nd index of mem_view to J
mem_view[2] = 74
print('After update:', byte_array)
#OUTPUT:
Before update: bytearray(b'XYZ')
After update: bytearray(b'XYJ')


'''NONE TYPE'''

'''None_Type: The NoneType object is a special type in Python that represents the absence of a value.
In other words, NoneType is the type for the None object, which is an object that contains no value or defines a null value. It is used to indicate that a variable or expression does not have a value or has an undefined value. “None” basically means the absence of a value. '''

#Check Python None Type Using type() Method
#In this example, the code employs the type() method to check if the variable x is of type NoneType. It prints “The variable is of NoneType.” if x is None; otherwise, it prints “The variable is not of NoneType.”

#Example 1: 

x = None
 
# Using type() method
if type(x)==type(None):
    print("The variable is of NoneType.")
else:
    print("The variable is not of NoneType.")
#OUTPUT:
The variable is of NoneType.


#Check Python None Using if Condition
#In this example, the code uses an if condition with the value None, which is considered as False in a boolean context. Therefore, it executes the else block and prints the value which is 10.

#Example 2: 

# Using if condition
if None:
  print(0)
else:
  print(10)
#OUTPUT: 
10


######################################################## PYTHON CONTROL FLOW ########################################################

'''In Python programming, flow control is the order in which statements or blocks of code are executed at runtime based on a condition.

The flow control statements are divided into three categories:
CONDITIONAL STATEMENTS
ITERATIVE STATEMENTS
TRANSFER STATEMENTS.'''

'''CONDITIONAL STATEMENTS: In Python, condition statements act depending on whether a given condition is true or false. You can execute different blocks of codes depending on the outcome of a condition. Condition statements always evaluate to either True or False. 

There are three types of conditional statements.
1. if statement
2. if-else
3. if-elif-else
4. nested if-else'''


'''- `if`statement: Used for conditional execution.'''

#Python if statement
#Syntax: if condition:
   # Statements to execute if
   # condition is true

if (condition):
    code1
else:
    code2
[on_true] if [expression] else [on_false]

#Example:
# python program to illustrate If statement 
  
i = 10
  
if (i > 15): 
    print("10 is less than 15") 
print("I am Not in if") 
 
#Output:
I am Not in if

'''if-else conditional statement: The if statement alone tells us that if a condition is true it will execute a block of statements and if the condition is false it won’t. But if we want to do something else if the condition is false, we can use the else statement with the if statement to execute a block of code when the if condition is false.'''

#Python If-Else statement:
#Syntax 
if (condition):
    # Executes this block if
    # condition is true
else:
    # Executes this block if
    # condition is false

#Example:
# python program to illustrate If else statement 
#!/usr/bin/python 
  
i = 20
if (i < 15): 
    print("i is smaller than 15") 
    print("i'm in if Block") 
else: 
    print("i is greater than 15") 
    print("i'm in else Block") 
print("i'm not in if and not in else Block") 

#Output:
i is greater than 15
i'm in else Block
i'm not in if and not in else Block


'''if-elif-else: The if-elif statement is shortcut of if..else chain. While using if-elif statement at the end else block is added which is performed if none of the above if-elif statement is true.'''

#Python if-elif Statement 
#Syntax: if (condition): statementelif (condition): statement..else: statement

#Example:
# if-elif statement example
letter = "A"
 
if letter == "B":
    print("letter is B")
 
elif letter == "C":
    print("letter is C")
 
elif letter == "A":
    print("letter is A")
 
else:
    print("letter isn't A, B or C")    
#Output:
letter is A


'''nested if-else: There come situations in real life when we need to make some decisions and based on these decisions, we decide what should we do next. Similar situations arise in programming also where we need to make some decisions and based on these decisions we will execute the next block of code. This is done with the help of decision-making statements in Python.'''

#Python nested if statement
#Syntax:

if (condition1):
   # Executes when condition1 is true
   if (condition2): 
      # Executes when condition2 is true
   # if Block is end here
# if Block is end here

#Example: 
# Python program to demonstrate nested if statement 
   
num = 15
if num >= 0: 
    if num == 0: 
        print("Zero") 
    else: 
        print("Positive number") 
else: 
    print("Negative number") 

#Output:
Positive number


'''ITERATIVE STATEMENTS: In Python, iterative statements allow us to execute a block of code repeatedly as long as the condition is True. We also call it a loop statements.

Python provides us the following two loop statement to perform some actions repeatedly.
1. for loop
2. while loop'''

'''-for loop: For Loops in Python are a special type of loop statement that is used for sequential traversal. Python For loop is used for iterating over an iterable like a String, Tuple, List, Set, or Dictionary. '''

#Python for loop Syntax :
for var in iterable:
    # statements

#Example 1: 
# Iterating over dictionary
print("Dictionary Iteration")

d = dict()

d['xyz'] = 123
d['abc'] = 345
for i in d:
    print("% s % d" % (i, d[i]))

#Ouput:
Dictionary Iteration
xyz  123
abc  345


#Example 2:
# Iterating over a String
print("String Iteration")

s = "Geeks"
for i in s:
    print(i)

#Output:
String Iteration
G
e
e
k
s


'''while loop: Python While Loop is used to execute a block of statements repeatedly until a given condition is satisfied. When the condition becomes false, the line immediately after the loop in the program is executed.'''

#Syntax of while loop in Python
while expression:
    statement(s)

#Example 1:

# Python program to illustrate 
# while loop 
count = 0
while (count < 3): 
    count = count + 1
    print("Hello World")

#Output:
Hello World
Hello World
Hello World

#Example 2:

# Python program to demonstrate 
# while-else loop 
  
i = 0
while i < 4: 
    i += 1
    print(i) 
else:  # Executed because no break in for 
    print("No Break\n") 
  
i = 0
while i < 4: 
    i += 1
    print(i) 
    break
else:  # Not executed as there is a break 
    print("No Break") 
Output
1
2
3
4
No Break

1


'''TRANSFER STATEMENTS: transfer statements are used to alter the program’s way of execution in a certain manner. For this purpose, we use three types of transfer statements.

1. break statement
2. continue statement
3. pass statements'''


'''- `break`: Exits out of the closest enclosing loop.
Python break is used to terminate the execution of the loop. 
break statement is used to bring the control out of the loop when some external condition is triggered. break statement is put inside the loop body (generally after if condition). It terminates the current loop, i.e., the loop in which it appears, and resumes execution at the next statement immediately after the end of that loop. If the break statement is inside a nested loop, the break will terminate the innermost loop.'''

#Python break() Function
#Python break() Syntax:

#Example 1: 
for i in range(10): 
    print(i) 
    if i == 2: 
        break

#Output:
0
1
2

#Example 2: 
num = 0
for i in range(10): 
    num += 1
    if num == 8: 
        break
    print("The num has value:", num) 
print("Out of loop")

#Output:
The num has value: 1
The num has value: 2
The num has value: 3
The num has value: 4
The num has value: 5
The num has value: 6
The num has value: 7
Out of loop


'''- `continue statement skips the rest of the current loop iteration. Python continue statement skips the execution of the program block after the continue statement and forces the control to start the next iteration.'''

#Python Continue Statement
#Syntax:
while True:
    ...
    if x == 10:
        continue
    print(x)

#Example 1:
# loop from 1 to 10
for i in range(1, 11):
 
    # If i is equals to 6,
    # continue to next iteration
    # without printing
    if i == 6:
        continue
    else:
        # otherwise print the value
        # of i
        print(i, end=" ")

OUTPUT: 
1 2 3 4 5 7 8 9 10 

#Example 2: 
# prints all the elements in the nested list 
# except for the ones with value 3
nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
 
for i in nested_list:
    for j in i:
        if j == 3:
            continue
        print(j)

#OUTPUT: 
1
2
4
5
6
7
8
9

'''pass statements is a null statement. But the difference between pass and comment is that comment is ignored by the interpreter whereas pass is not ignored'''

#Syntax of the pass statement
pass

#Excample 1: 
#Use of pass keyword in Conditional statement

li =['a', 'b', 'c', 'd']
 
for i in li:
    if(i =='a'):
        pass
    else:
        print(i)

#Output:
b
c
d


#Example 2: 
# Using pass as a placeholder inside an if statement
x = 5
if x > 10:
    pass
else:
    print("x is less than or equal to 10")
 
# Using pass in a function definition as a 
# placeholder for implementation
def my_function():
    pass
 
# Using pass in a class definition as
# a placeholder for implementation
 
class MyClass:
    def __init__(self):
        pass

#Output:
x is less than or equal to 10


################################################   PYTHON FUNCTIONS   ##########################################################

'''Python Functions is a block of statements that return the specific task. The idea is to put some commonly or repeatedly done tasks together and make a function so that instead of writing the same code again and again for different inputs, we can do the function calls to reuse code contained in it over and over again.

Some Benefits of Using Functions
* Increase Code Readability 
* Increase Code Reusability'''


'''Python Function Declaration
The syntax to declare a function is: 
Keyword (def)
Function name (function_name)
Body of Statement (#statement)
Function return (return expression)'''


'''Creating a Function in Python
We can define a function in Python, using the def keyword. We can add any type of functionalities and properties to it as we require. By the following example, we can understand how to write a function in Python.'''

# A simple Python function
def fun():
    print("Welcome to GFG")

'''Calling a Function in Python
After creating a function in Python we can call it by using the name of the functions Python followed by parenthesis containing parameters of that particular function. Below is the example for calling def function Python.'''

# A simple Python function
def fun():
    print("Welcome to GFG")


# Driver code to call a function
fun()

#Output:
Welcome to GFG

'''Python Function with Parameters
If you have experience in C/C++ or Java then you must be thinking about the return type of the function and data type of arguments. That is possible in Python as well (specifically for Python 3.5 and above).'''

#Python Function Syntax with Parameters
 def function_name(parameter: data_type) -> return_type:
    """Docstring"""
    # body of the function
    return expression

'''The following example uses arguments and parameters that you will learn later in this article so you can come back to it again if not understood.'''

def add(num1: int, num2: int) -> int:
    """Add two numbers"""
    num3 = num1 + num2

    return num3

# Driver code
num1, num2 = 5, 15
ans = add(num1, num2)
print(f"The addition of {num1} and {num2} results {ans}.")

#Output:
The addition of 5 and 15 results 20.

'''Python Function Arguments
Arguments are the values passed inside the parenthesis of the function. A function can have any number of arguments separated by a comma.

In this example, we will create a simple function in Python to check whether the number passed as an argument to the function is even or odd.'''

# A simple Python function to check
# whether x is even or odd
def evenOdd(x):
    if (x % 2 == 0):
        print("even")
    else:
        print("odd")


# Driver code to call the function
evenOdd(2)
evenOdd(3)

#Output:
even
odd

'''Types of Python Function Arguments
Python supports various types of arguments that can be passed at the time of the function call. In Python, we have the following function argument types in Python:

Default argument
Keyword arguments (named arguments)
Positional arguments
Arbitrary arguments (variable-length arguments *args and **kwargs)'''


'''Default Arguments
A default argument is a parameter that assumes a default value if a value is not provided in the function call for that argument. The following example illustrates Default arguments to write functions in Python.'''

# Python program to demonstrate
# default arguments
def myFun(x, y=50):
    print("x: ", x)
    print("y: ", y)

# Driver code (We call myFun() with only
# argument)
myFun(10)

#Output:
x:  10
y:  50

'''Keyword Arguments
The idea is to allow the caller to specify the argument name with values so that the caller does not need to remember the order of parameters.'''

# Python program to demonstrate Keyword Arguments
def student(firstname, lastname):
    print(firstname, lastname)

# Keyword arguments
student(firstname='Geeks', lastname='Practice')
student(lastname='Practice', firstname='Geeks')

#Output:
Geeks Practice
Geeks Practice

'''Positional Arguments
We used the Position argument during the function call so that the first argument (or value) is assigned to name and the second argument (or value) is assigned to age. By changing the position, or if you forget the order of the positions, the values can be used in the wrong places, as shown in the Case-2 example below, where 27 is assigned to the name and Suraj is assigned to the age.'''

def nameAge(name, age):
    print("Hi, I am", name)
    print("My age is ", age)


# You will get correct output because 
# argument is given in order
print("Case-1:")
nameAge("Suraj", 27)
# You will get incorrect output because
# argument is not in order
print("\nCase-2:")
nameAge(27, "Suraj")

#Output:
Case-1:
Hi, I am Suraj
My age is  27
Case-2:
Hi, I am 27
My age is  Suraj


'''Arbitrary Keyword  Arguments
In Python Arbitrary Keyword Arguments, *args, and **kwargs can pass a variable number of arguments to a function using special symbols. There are two special symbols:

*args in Python (Non-Keyword Arguments)
**kwargs in Python (Keyword Arguments)'''

#Example 1: Variable length non-keywords argument
# Python program to illustrate
# *args for variable number of arguments
def myFun(*argv):
    for arg in argv:
        print(arg)

myFun('Hello', 'Welcome', 'to', 'GeeksforGeeks')

#Output:
Hello
Welcome
to
GeeksforGeeks

#Example 2: Variable length keyword arguments

# Python program to illustrate
# *kwargs for variable number of keyword arguments

def myFun(**kwargs):
    for key, value in kwargs.items():
        print("%s == %s" % (key, value))


# Driver code
myFun(first='Geeks', mid='for', last='Geeks')
Output:

first == Geeks
mid == for
last == Geeks


'''Docstring
The first string after the function is called the Document string or Docstring in short. This is used to describe the functionality of the function. The use of docstring in functions is optional but it is considered a good practice.

The below syntax can be used to print out the docstring of a function.'''

#Syntax: print(function_name.__doc__)
#Example: Adding Docstring to the function


# A simple Python function to check
# whether x is even or odd


def evenOdd(x):
    """Function to check if the number is even or odd"""
    
    if (x % 2 == 0):
        print("even")
    else:
        print("odd")

# Driver code to call the function
print(evenOdd.__doc__)

#Output:
Function to check if the number is even or odd

#######################################################    PYTHON LISTS    #######################################################

'''Python Lists are just like dynamically sized arrays, declared in other languages (vector in C++ and ArrayList in Java). In simple language, a Python list is a collection of things, enclosed in [ ] and separated by commas. 

The list is a sequence data type which is used to store the collection of data. Tuples and String are other types of sequence data types.'''

'''                                                Creating a List in Python
Lists in Python can be created by just placing the sequence inside the square brackets[]. Unlike Sets, a list doesn’t need a built-in function for its creation of a list. '''

# Creating Python List using [].

Var = ["Hello", "World"] 
print(Var)

#Output:
['Hello', 'World']

#Example 1: Creating a list in Python

# Python program to demonstrate 
# Creation of List 
  
# Creating a List 
List = [] 
print("Blank List: ") 
print(List) 
  
# Creating a List of numbers 
List = [10, 20, 14] 
print("\nList of numbers: ") 
print(List) 
  
# Creating a List of strings and accessing 
# using index 
List = ["Geeks", "For", "Geeks"] 
print("\nList Items: ") 
print(List[0]) 
print(List[2]) 

#Output
Blank List: 
[]

List of numbers: 
[10, 20, 14]

List Items: 
Geeks
Geeks

#Example 2:  Creating a list with multiple distinct or duplicate elements
'''A list may contain duplicate values with their distinct positions and hence, multiple distinct or duplicate values can be passed as a sequence at the time of list creation.'''

# Creating a List with 
# the use of Numbers 
# (Having duplicate values) 
List = [1, 2, 4, 4, 3, 3, 3, 6, 5] 
print("\nList with the use of Numbers: ") 
print(List) 
  
# Creating a List with 
# mixed type of values 
# (Having numbers and strings) 
List = [1, 2, 'Geeks', 4, 'For', 6, 'Geeks'] 
print("\nList with the use of Mixed Values: ") 
print(List) 

#Output
List with the use of Numbers: 
[1, 2, 4, 4, 3, 3, 3, 6, 5]

List with the use of Mixed Values: 
[1, 2, 'Geeks', 4, 'For', 6, 'Geeks']


'''                                                Accessing elements from the List
In order to access the list items refer to the index number. Use the index operator [ ] to access an item in a list. The index must be an integer. Nested lists are accessed using nested indexing. '''

#Example 1: Accessing elements from list


# Python program to demonstrate 
# accessing of element from list 
  
# Creating a List with 
# the use of multiple values 
List = ["Geeks", "For", "Geeks"] 
  
# accessing a element from the 
# list using index number 
print("Accessing a element from the list") 
print(List[0]) 
print(List[2])
 
#Output
Accessing a element from the list
Geeks
Geeks

'''                                                 Getting the size of Python list
Python len() is used to get the length of the list.'''

# Creating a List 
List1 = [] 
print(len(List1)) 
  
# Creating a List of numbers 
List2 = [10, 20, 14] 
print(len(List2)) 
#Output
0
3

'''                                                Taking Input of a Python List
We can take the input of a list of elements as string, integer, float, etc. But the default one is a string.'''

# input size of the list 
n = int(input("Enter the size of list : ")) 
# store integers in a list using map, 
# split and strip functions 
lst = list(map(int, input("Enter the integer\ 
elements:").strip().split()))[:n] 
  
# printing the list 
print('The list is:', lst)    

#Output:
Enter the size of list : 4
Enter the integer elements: 6 3 9 10
The list is: [6, 3, 9, 10]

'''                                                Adding Elements to a Python List
Method 1: Using append() method
Elements can be added to the List by using the built-in append() function. Only one element at a time can be added to the list by using the append() method, for the addition of multiple elements with the append() method, loops are used. Tuples can also be added to the list with the use of the append method because tuples are immutable. Unlike Sets, Lists can also be added to the existing list with the use of the append() method.''' 

# Python program to demonstrate  
# Addition of elements in a List 
   
# Creating a List 
List = [1,2,3,4] 
print("Initial List: ") 
print(List) 
  
# Addition of Element at  
# specific Position 
# (using Insert Method) 
List.insert(3, 12) 
List.insert(0, 'Geeks') 
print("\nList after performing Insert Operation: ") 
print(List) 
#Output
Initial List: 
[1, 2, 3, 4]

List after performing Insert Operation: 
['Geeks', 1, 2, 3, 12, 4]

'''                                                Reversing a List

Method 1:  A list can be reversed by using the reverse() method in Python.'''


'''Using the reversed() function:
The reversed() function returns a reverse iterator, which can be converted to a list using the list() function.'''

my_list = [1, 2, 3, 4, 5] 
reversed_list = list(reversed(my_list)) 
print(reversed_list) 
#Output
[5, 4, 3, 2, 1]


'''                                                 Removing Elements from the List
Method 1: Using remove() method
Elements can be removed from the List by using the built-in remove() function but an Error arises if the element doesn’t exist in the list. Remove() method only removes one element at a time, to remove a range of elements, the iterator is used. The remove() method removes the specified item.'''

# Python program to demonstrate 
# Removal of elements in a List 
  
# Creating a List 
List = [1, 2, 3, 4, 5, 6, 
        7, 8, 9, 10, 11, 12] 
print("Initial List: ") 
print(List) 
  
# Removing elements from List 
# using Remove() method 
List.remove(5) 
List.remove(6) 
print("\nList after Removal of two elements: ") 
print(List) 
#Output
Initial List: 
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
List after Removal of two elements: 
[1, 2, 3, 4, 7, 8, 9, 10, 11, 12]

'''                                               Slicing of a List
We can get substrings and sublists using a slice. In Python List, there are multiple ways to print the whole list with all the elements, but to print a specific range of elements from the list, we use the Slice operation. 

Slice operation is performed on Lists with the use of a colon(:).'''

# Python program to demonstrate 
# Removal of elements in a List 
  
# Creating a List 
List = ['G', 'E', 'E', 'K', 'S', 'F', 
        'O', 'R', 'G', 'E', 'E', 'K', 'S'] 
print("Initial List: ") 
print(List) 
  
# Print elements of a range 
# using Slice operation 
Sliced_List = List[3:8] 
print("\nSlicing elements in a range 3-8: ") 
print(Sliced_List) 
  
# Print elements from a 
# pre-defined point to end 
Sliced_List = List[5:] 
print("\nElements sliced from 5th "
      "element till the end: ") 
print(Sliced_List) 
  
# Printing elements from 
# beginning till end 
Sliced_List = List[:] 
print("\nPrinting all elements using slice operation: ") 
print(Sliced_List) 

#Output
Initial List: 
['G', 'E', 'E', 'K', 'S', 'F', 'O', 'R', 'G', 'E', 'E', 'K', 'S']

Slicing elements in a range 3-8: 
['K', 'S', 'F', 'O', 'R']

Elements sliced from 5th element till the end: 
['F', 'O', 'R', 'G', 'E', 'E', 'K', 'S']

Printing all elements using slice operation: 
['G', 'E', 'E', 'K', 'S', 'F', 'O', 'R', 'G', 'E', 'E', 'K', 'S']

'''                                                List Comprehension
Python List comprehensions are used for creating new lists from other iterables like tuples, strings, arrays, lists, etc. A list comprehension consists of brackets containing the expression, which is executed for each element along with the for loop to iterate over each element. 

Syntax:

newList = [ expression(element) for element in oldList if condition ]'''

# Python program to demonstrate list 
# comprehension in Python 
  
# below list contains square of all 
# odd numbers from range 1 to 10 
odd_square = [x ** 2 for x in range(1, 11) if x % 2 == 1] 
print(odd_square) 
#Output
[1, 9, 25, 49, 81]


'''Note:  

Python provides several built-in data structures that you can use to organize and manipulate data. Here are some of the most commonly used ones:

Lists: Lists are ordered collections of items. They can contain elements of different data types, and you can add, remove, or modify items in a list. Some common methods for lists include:

append(x): Adds an item to the end of the list.
extend(iterable): Extends the list by appending items from an iterable.
insert(i, x): Inserts an item at a specific position.
remove(x): Removes the first occurrence of an item with a specific value.
pop([i]): Removes and returns an item at a given position.
index(x[, start[, end]]): Returns the index of the first occurrence of an item with a specific value.
count(x): Returns the number of occurrences of an item.
sort(): Sorts the list in place.
reverse(): Reverses the order of elements in the list.
copy(): Creates a shallow copy of the list1.'''

#######################################################    PYTHON STRING    #######################################################

'''A String is a data structure in Python Programming that represents a sequence of characters. It is an immutable data type, meaning that once you have created a string, you cannot change it. Python String are used widely in many different applications, such as storing and manipulating text data, representing names, addresses, and other types of data that can be represented as text.

What is a String in Python?
Python Programming does not have a character data type, a single character is simply a string with a length of 1. '''


'''String Data Type in Python

Creating a String in Python

Strings in Python can be created using single quotes or double quotes or even triple quotes. Let us see how we can define a string in Python or how to write string in Python.

In this example, we will demonstrate different ways to create a Python String. We will create a string using single quotes (‘ ‘), double quotes (” “), and triple double quotes (“”” “””). The triple quotes can be used to declare multiline strings in Python.'''

#Example:

# Creating a String
# with single Quotes
String1 = 'Welcome to the Geeks World'
print("String with the use of Single Quotes: ")
print(String1)

# Creating a String
# with double Quotes
String1 = "I'm a Geek"
print("\nString with the use of Double Quotes: ")
print(String1)

# Creating a String
# with triple Quotes
String1 = '''I'm a Geek and I live in a world of "Geeks"'''
print("\nString with the use of Triple Quotes: ")
print(String1)

# Creating String with triple
# Quotes allows multiple lines
String1 = '''Geeks
            For
            Life'''
print("\nCreating a multiline String: ")
print(String1)

#Output: 
String with the use of Single Quotes: 
Welcome to the Geeks World
String with the use of Double Quotes: 
I'm a Geek
String with the use of Triple Quotes: 
I'm a Geek and I live in a world of "Geeks"
Creating a multiline String: 
Geeks
            For
            Life

'''Deleting a character

Python strings are immutable, that means we cannot delete a character from it. When we try to delete thecharacter using the del keyword, it will generate an error.'''

# Python Program to delete
# character of a String

String1 = "Hello, I'm a Geek"
print("Initial String: ")
print(String1)

print("Deleting character at 2nd Index: ")
del String1[2]
print(String1)

#Output:
Initial String: 
Hello, I'm a Geek
Deleting character at 2nd Index: 
Traceback (most recent call last):
  File "e:\GFG\Python codes\Codes\demo.py", line 9, in <module>
    del String1[2]
TypeError: 'str' object doesn't support item deletion


'''In this example, we will first slice the string up to the character that we want to delete and then concatenate the remaining string next from the deleted character.'''

# Python Program to Delete
# characters from a String

String1 = "Hello, I'm a Geek"
print("Initial String: ")
print(String1)

# Deleting a character
# of the String
String2 = String1[0:2] + String1[3:]
print("\nDeleting character at 2nd Index: ")
print(String2)

#Output: 
Initial String: 
Hello, I'm a Geek
Deleting character at 2nd Index: 
Helo, I'm a Geek

'''Formatting of Strings
Strings in Python or string data type in Python can be formatted with the use of format() method which is a very versatile and powerful tool for formatting Strings. Format method in String contains curly braces {} as placeholders which can hold arguments according to position or keyword to specify the order.

Example 1:

In this example, we will declare a string which contains the curly braces {} that acts as a placeholders and provide them values to see how string declaration position matters.'''

# Python Program for
# Formatting of Strings

# Default order
String1 = "{} {} {}".format('Geeks', 'For', 'Life')
print("Print String in default order: ")
print(String1)

# Positional Formatting
String1 = "{1} {0} {2}".format('Geeks', 'For', 'Life')
print("\nPrint String in Positional order: ")
print(String1)

# Keyword Formatting
String1 = "{l} {f} {g}".format(g='Geeks', f='For', l='Life')
print("\nPrint String in order of Keywords: ")
print(String1)

#Output: 
Print String in default order: 
Geeks For Life
Print String in Positional order: 
For Geeks Life
Print String in order of Keywords: 
Life For Geeks

'''Example 2:

Integers such as Binary, hexadecimal, etc., and floats can be rounded or displayed in the exponent form with the use of format specifiers.'''


# Formatting of Integers
String1 = "{0:b}".format(16)
print("\nBinary representation of 16 is ")
print(String1)

# Formatting of Floats
String1 = "{0:e}".format(165.6458)
print("\nExponent representation of 165.6458 is ")
print(String1)

# Rounding off Integers
String1 = "{0:.2f}".format(1/6)
print("\none-sixth is : ")
print(String1)

#Output: 
Binary representation of 16 is 
10000
Exponent representation of 165.6458 is 
1.656458e+02
one-sixth is : 
0.17

######################################################    PYTHON SET    #############################################################

'''Python Set is an unordered collection of data types that is iterable, mutable, and has no duplicate elements. The order of elements in a set is undefined though it may consist of various elements. The major advantage of using a set, as opposed to a list, is that it has a highly optimized method for checking whether a specific element is contained in the set. Here, we will see what is a set in Python and also see different examples of set Python.

Creating a Set in Python
Python Sets can be created by using the built-in set() function with an iterable object or a sequence by placing the sequence inside curly braces, separated by a ‘comma’.

Note: A Python set cannot have mutable elements like a list or dictionary, as it is immutable. '''

# Creating a Set
set1 = set()
print("Initial blank Set: ")
print(set1)

# Creating a Set with the use of a String
set1 = set("GeeksForGeeks")
print("\nSet with the use of String: ")
print(set1)

String = 'GeeksForGeeks'
set1 = set(String)
print("\nSet with the use of an Object: ")
print(set1)

# Creating a Set with the use of a List
set1 = set(["Geeks", "For", "Geeks"])
print("\nSet with the use of List: ")
print(set1)

# Creating a Set with the use of a tuple
t = ("Geeks", "for", "Geeks")
print("\nSet with the use of Tuple: ")
print(set(t))

# Creating a Set with the use of a dictionary
d = {"Geeks": 1, "for": 2, "Geeks": 3}
print("\nSet with the use of Dictionary: ")
print(set(d))

#OUTPUT: 
Initial blank Set: 
set()

Set with the use of String: 
{'e', 'G', 's', 'F', 'o', 'r', 'k'}

Set with the use of an Object: 
{'e', 'G', 's', 'F', 'o', 'r', 'k'}

Set with the use of List: 
{'For', 'Geeks'}

Set with the use of Tuple: 
{'for', 'Geeks'}

Set with the use of Dictionary: 
{'for', 'Geeks'}

'''Time complexity: O(n), where n is the length of the input string, list, tuple or dictionary.
Auxiliary space: O(n), where n is the length of the input string, list, tuple or dictionary.

A Python set contains only unique elements but at the time of set creation, multiple duplicate values can also be passed. Order of elements in a Python set is undefined and is unchangeable. Type of elements in a set need not be the same, various mixed-up data type values can also be passed to the set. '''

# Creating a Set with a List of Numbers
# (Having duplicate values)
set1 = set([1, 2, 4, 4, 3, 3, 3, 6, 5])
print("\nSet with the use of Numbers: ")
print(set1)

# Creating a Set with a mixed type of values
# (Having numbers and strings)
set1 = set([1, 2, 'Geeks', 4, 'For', 6, 'Geeks'])
print("\nSet with the use of Mixed Values")
print(set1)

#Output
Set with the use of Numbers: 
{1, 2, 3, 4, 5, 6}

Set with the use of Mixed Values
{1, 2, 4, 6, 'Geeks', 'For'}

'''Accessing a Set in Python
Set items cannot be accessed by referring to an index, since sets are unordered the items has no index. But you can loop through the Python hash set items using a for loop, or ask if a specified value is present in a set, by using the in keyword.'''

# Creating a set
set1 = set(["Geeks", "For", "Geeks."])
print("\nInitial set")
print(set1)

# Accessing element using
# for loop
print("\nElements of set: ")
for i in set1:
    print(i, end=" ")

# Checking the element
# using in keyword
print("\n")
print("Geeks" in set1)

#Output
Initial set
{'Geeks.', 'For', 'Geeks'}

Elements of set: 
Geeks. For Geeks 

True

'''Removing Elements from the Set in Python
Below are some of the ways by which we can remove elements from the set in Python:

Using remove() Method or discard() Method
Using pop() Method
Using clear() Method
Using remove() Method or discard() Method
Elements can be removed from the Sets in Python by using the built-in remove() function but a KeyError arises if the element doesn’t exist in the hashset Python. To remove elements from a set without KeyError, use discard(), if the element doesn’t exist in the set, it remains unchanged.'''

# Creating a Set
set1 = set([1, 2, 3, 4, 5, 6,
            7, 8, 9, 10, 11, 12])
print("Initial Set: ")
print(set1)

# Removing elements from Set  using Remove() method
set1.remove(5)
set1.remove(6)
print("\nSet after Removal of two elements: ")
print(set1)

# Removing elements from Set using Discard() method
set1.discard(8)
set1.discard(9)
print("\nSet after Discarding two elements: ")
print(set1)

# Removing elements from Set using iterator method
for i in range(1, 5):
    set1.remove(i)
print("\nSet after Removing a range of elements: ")
print(set1)

#Output
Initial Set: 
{1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12}

Set after Removal of two elements: 
{1, 2, 3, 4, 7, 8, 9, 10, 11, 12}

Set after Discarding two elements: 
{1, 2, 3, 4, 7, 10, 11, 12}

Set after Removing a range of elements: 
{7, 10, 11, 12}

'''Using pop() Method
Pop() function can also be used to remove and return an element from the set, but it removes only the last element of the set. 

Note: If the set is unordered then there’s no such way to determine which element is popped by using the pop() function. '''

# Python program to demonstrate
# Deletion of elements in a Set

# Creating a Set
set1 = set([1, 2, 3, 4, 5, 6,
            7, 8, 9, 10, 11, 12])
print("Initial Set: ")
print(set1)

# Removing element from the
# Set using the pop() method
set1.pop()
print("\nSet after popping an element: ")
print(set1)

Output
Initial Set: 
{1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12}

Set after popping an element: 
{2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12}

'''Using clear() Method
To remove all the elements from the set, clear() function is used. '''

#Creating a set
set1 = set([1,2,3,4,5])
print("\n Initial set: ")
print(set1)

# Removing all the elements from 
# Set using clear() method
set1.clear()
print("\nSet after clearing all the elements: ")
print(set1)

#Output
 Initial set: 
{1, 2, 3, 4, 5}

Set after clearing all the elements: 
set()

'''Frozen Sets in Python
Frozen sets in Python are immutable objects that only support methods and operators that produce a result without affecting the frozen set or sets to which they are applied. While elements of a set can be modified at any time, elements of the frozen set remain the same after creation. 

If no parameters are passed, it returns an empty frozenset.'''


# Python program to demonstrate
# working of a FrozenSet

# Creating a Set
String = ('G', 'e', 'e', 'k', 's', 'F', 'o', 'r')

Fset1 = frozenset(String)
print("The FrozenSet is: ")
print(Fset1)

# To print Empty Frozen Set
# No parameter is passed
print("\nEmpty FrozenSet: ")
print(frozenset())

#Output
The FrozenSet is: 
frozenset({'F', 's', 'o', 'G', 'r', 'e', 'k'})

Empty FrozenSet: 
frozenset()

######################################################    PYTHON TUPLE    #############################################################

'''Python Tuple is a collection of Python Programming objects much like a list. The sequence of values stored in a tuple can be of any type, and they are indexed by integers.  Values of a tuple are syntactically separated by ‘commas‘. Although it is not necessary, it is more common to define a tuple by closing the sequence of values in parentheses. This helps in understanding the Python tuples more easily.

Creating a Tuple
In Python Programming, tuples are created by placing a sequence of values separated by ‘comma’ with or without the use of parentheses for grouping the data sequence.

Note: Creation of Python tuple without the use of parentheses is known as Tuple Packing.  

Python Program to Demonstrate the Addition of Elements in a Tuple'''

# Creating an empty Tuple
Tuple1 = ()
print("Initial empty Tuple: ")
print(Tuple1)

# Creating a Tuple
# with the use of string
Tuple1 = ('Geeks', 'For')
print("\nTuple with the use of String: ")
print(Tuple1)

# Creating a Tuple with
# the use of list
list1 = [1, 2, 4, 5, 6]
print("\nTuple using List: ")
print(tuple(list1))

# Creating a Tuple
# with the use of built-in function
Tuple1 = tuple('Geeks')
print("\nTuple with the use of function: ")
print(Tuple1)

#Output: 
poster
×
Initial empty Tuple: 
()

Tuple with the use of String: 
('Geeks', 'For')

Tuple using List: 
(1, 2, 4, 5, 6)

Tuple with the use of function: 
('G', 'e', 'e', 'k', 's') 

'''Creating a Tuple with Mixed Datatypes.
Python Tuples can contain any number of elements and of any datatype (like strings, integers, list, etc.). Tuples can also be created with a single element, but it is a bit tricky. Having one element in the parentheses is not sufficient, there must be a trailing ‘comma’ to make it a tuple.'''


# Creating a Tuple
# with Mixed Datatype
Tuple1 = (5, 'Welcome', 7, 'Geeks')
print("\nTuple with Mixed Datatypes: ")
print(Tuple1)

# Creating a Tuple
# with nested tuples
Tuple1 = (0, 1, 2, 3)
Tuple2 = ('python', 'geek')
Tuple3 = (Tuple1, Tuple2)
print("\nTuple with nested tuples: ")
print(Tuple3)

# Creating a Tuple
# with repetition
Tuple1 = ('Geeks',) * 3
print("\nTuple with repetition: ")
print(Tuple1)

# Creating a Tuple
# with the use of loop
Tuple1 = ('Geeks')
n = 5
print("\nTuple with a loop")
for i in range(int(n)):
    Tuple1 = (Tuple1,)
    print(Tuple1)

#Output: 
Tuple with Mixed Datatypes: 
(5, 'Welcome', 7, 'Geeks')

Tuple with nested tuples: 
((0, 1, 2, 3), ('python', 'geek'))

Tuple with repetition: 
('Geeks', 'Geeks', 'Geeks')

Tuple with a loop
('Geeks',)
(('Geeks',),)
((('Geeks',),),)
(((('Geeks',),),),)
((((('Geeks',),),),),)

'''Python Tuple Operations
Here, below are the Python tuple operations.

Accessing of Python Tuples
Concatenation of Tuples
Slicing of Tuple
Deleting a Tuple
Accessing of Tuples
In Python Programming, Tuples are immutable, and usually, they contain a sequence of heterogeneous elements that are accessed via unpacking or indexing (or even by attribute in the case of named tuples). Lists are mutable, and their elements are usually homogeneous and are accessed by iterating over the list.

Note: In unpacking of tuple number of variables on the left-hand side should be equal to a number of values in given tuple a. '''

# Accessing Tuple
# with Indexing
Tuple1 = tuple("Geeks")
print("\nFirst element of Tuple: ")
print(Tuple1[0])


# Tuple unpacking
Tuple1 = ("Geeks", "For", "Geeks")

# This line unpack
# values of Tuple1
a, b, c = Tuple1
print("\nValues after unpacking: ")
print(a)
print(b)
print(c)

#Output: 

First element of Tuple: 
G

Values after unpacking: 
Geeks
For
Geeks

'''Concatenation of Tuples
Concatenation of tuple is the process of joining two or more Tuples. Concatenation is done by the use of ‘+’ operator. Concatenation of tuples is done always from the end of the original tuple. Other arithmetic operations do not apply on Tuples. 

Note- Only the same datatypes can be combined with concatenation, an error arises if a list and a tuple are combined.'''

# Concatenation of tuples
Tuple1 = (0, 1, 2, 3)
Tuple2 = ('Geeks', 'For', 'Geeks')

Tuple3 = Tuple1 + Tuple2

# Printing first Tuple
print("Tuple 1: ")
print(Tuple1)

# Printing Second Tuple
print("\nTuple2: ")
print(Tuple2)

# Printing Final Tuple
print("\nTuples after Concatenation: ")
print(Tuple3)

#Output: 
Tuple 1: 
(0, 1, 2, 3)

Tuple2: 
('Geeks', 'For', 'Geeks')

Tuples after Concatenation: 
(0, 1, 2, 3, 'Geeks', 'For', 'Geeks')

'''Slicing of Tuple
Slicing of a Tuple is done to fetch a specific range or slice of sub-elements from a Tuple. Slicing can also be done to lists and arrays. Indexing in a list results to fetching a single element whereas Slicing allows to fetch a set of elements. 

Note- Negative Increment values can also be used to reverse the sequence of Tuples. '''

# Slicing of a Tuple

# Slicing of a Tuple
# with Numbers
Tuple1 = tuple('GEEKSFORGEEKS')

# Removing First element
print("Removal of First Element: ")
print(Tuple1[1:])

# Reversing the Tuple
print("\nTuple after sequence of Element is reversed: ")
print(Tuple1[::-1])

# Printing elements of a Range
print("\nPrinting elements between Range 4-9: ")
print(Tuple1[4:9])

#Output: 

Removal of First Element: 
('E', 'E', 'K', 'S', 'F', 'O', 'R', 'G', 'E', 'E', 'K', 'S')

Tuple after sequence of Element is reversed: 
('S', 'K', 'E', 'E', 'G', 'R', 'O', 'F', 'S', 'K', 'E', 'E', 'G')

Printing elements between Range 4-9: 
('S', 'F', 'O', 'R', '

'''Deleting a Tuple
Tuples are immutable and hence they do not allow deletion of a part of it. The entire tuple gets deleted by the use of del() method. 

Note- Printing of Tuple after deletion results in an Error. '''

# Deleting a Tuple

Tuple1 = (0, 1, 2, 3, 4)
del Tuple1

print(Tuple1)

#Output
Traceback (most recent call last): 
File "/home/efa50fd0709dec08434191f32275928a.py", line 7, in 
print(Tuple1) 
NameError: name 'Tuple1' is not defined


#################################################    PYTHON DICTIONARY   ########################################################

'''A Python dictionary is a data structure that stores the value in key:value pairs.

Example:

As you can see from the example, data is stored in key:value pairs in dictionaries, which makes it easier to find values.'''


Dict = {1: 'Geeks', 2: 'For', 3: 'Geeks'} 
print(Dict)

#Output:
poster
{1: 'Geeks', 2: 'For', 3: 'Geeks'}

'''Python Dictionary Syntax
dict_var = {key1 : value1, key2 : value2, …..}'''

'''What is a Dictionary in Python?
Dictionaries in Python is a data structure, used to store values in key:value format. This makes it different from lists, tuples, and arrays as in a dictionary each key has an associated value.

Note: As of Python version 3.7, dictionaries are ordered and can not contain duplicate keys.

How to Create a Dictionary
In Python, a dictionary can be created by placing a sequence of elements within curly {} braces, separated by a ‘comma’.

The dictionary holds pairs of values, one being the Key and the other corresponding pair element being its Key:value.

Values in a dictionary can be of any data type and can be duplicated, whereas keys can’t be repeated and must be immutable. 

Note – Dictionary keys are case sensitive, the same name but different cases of Key will be treated distinctly. 

The code demonstrates creating dictionaries with different types of keys. The first dictionary uses integer keys, and the second dictionary uses a mix of string and integer keys with corresponding values. This showcases the flexibility of Python dictionaries in handling various data types as keys.'''

Dict = {1: 'Geeks', 2: 'For', 3: 'Geeks'} 
print("\nDictionary with the use of Integer Keys: ") 
print(Dict) 
  
Dict = {'Name': 'Geeks', 1: [1, 2, 3, 4]} 
print("\nDictionary with the use of Mixed Keys: ") 
print(Dict) 

#Output
Dictionary with the use of Integer Keys: 
{1: 'Geeks', 2: 'For', 3: 'Geeks'}
Dictionary with the use of Mixed Keys: 
{'Name': 'Geeks', 1: [1, 2, 3, 4]}


'''Dictionary Example
A dictionary can also be created by the built-in function dict(). An empty dictionary can be created by just placing curly braces{}. 

Different Ways to Create a Python Dictionary
The code demonstrates different ways to create dictionaries in Python. It first creates an empty dictionary, and then shows how to create dictionaries using the dict() constructor with key-value pairs specified within curly braces and as a list of tuples.'''

Dict = {} 
print("Empty Dictionary: ") 
print(Dict) 
  
Dict = dict({1: 'Geeks', 2: 'For', 3: 'Geeks'}) 
print("\nDictionary with the use of dict(): ") 
print(Dict) 
  
Dict = dict([(1, 'Geeks'), (2, 'For')]) 
print("\nDictionary with each item as a pair: ") 
print(Dict) 

#Output:
Empty Dictionary: 
{}
Dictionary with the use of dict(): 
{1: 'Geeks', 2: 'For', 3: 'Geeks'}
Dictionary with each item as a pair: 
{1: 'Geeks', 2: 'For'}

'''Nested Dictionaries

Example: The code defines a nested dictionary named ‘Dict’ with multiple levels of key-value pairs. It includes a top-level dictionary with keys 1, 2, and 3. The value associated with key 3 is another dictionary with keys ‘A,’ ‘B,’ and ‘C.’ This showcases how Python dictionaries can be nested to create hierarchical data structures.'''

Dict = {1: 'Geeks', 2: 'For', 
        3: {'A': 'Welcome', 'B': 'To', 'C': 'Geeks'}} 
  
print(Dict) 

#Output:
{1: 'Geeks', 2: 'For', 3: {'A': 'Welcome', 'B': 'To', 'C': 'Geeks'}}

'''Adding Elements to a Dictionary
The addition of elements can be done in multiple ways. One value at a time can be added to a Dictionary by defining value along with the key e.g. Dict[Key] = ‘Value’.

Updating an existing value in a Dictionary can be done by using the built-in update() method. Nested key values can also be added to an existing Dictionary. 

Note- While adding a value, if the key-value already exists, the value gets updated otherwise a new Key with the value is added to the Dictionary.

Example: Add Items to a Python Dictionary with Different DataTypes

The code starts with an empty dictionary and then adds key-value pairs to it. It demonstrates adding elements with various data types, updating a key’s value, and even nesting dictionaries within the main dictionary. The code shows how to manipulate dictionaries in Python.'''

Dict = {} 
print("Empty Dictionary: ") 
print(Dict) 
Dict[0] = 'Geeks'
Dict[2] = 'For'
Dict[3] = 1
print("\nDictionary after adding 3 elements: ") 
print(Dict) 
  
Dict['Value_set'] = 2, 3, 4
print("\nDictionary after adding 3 elements: ") 
print(Dict) 
  
Dict[2] = 'Welcome'
print("\nUpdated key value: ") 
print(Dict) 
Dict[5] = {'Nested': {'1': 'Life', '2': 'Geeks'}} 
print("\nAdding a Nested Key: ") 
print(Dict) 

#Output:

Empty Dictionary: 
{}
Dictionary after adding 3 elements: 
{0: 'Geeks', 2: 'For', 3: 1}
Dictionary after adding 3 elements: 
{0: 'Geeks', 2: 'For', 3: 1, 'Value_set': (2, 3, 4)}
Updated key value: 
{0: 'Geeks', 2: 'Welcome', 3: 1, 'Value_set': (2, 3, 4)}
Adding a Nested Key: 
{0: 'Geeks', 2: 'Welcome', 3: 1, 'Value_set': (2, 3, 4), 5: 
{'Nested': {'1': 'Life', '2': 'Geeks'}}}

'''Accessing Elements of a Dictionary
To access the items of a dictionary refer to its key name. Key can be used inside square brackets. 

Access a Value in Python Dictionary
The code demonstrates how to access elements in a dictionary using keys. It accesses and prints the values associated with the keys ‘name’ and 1, showcasing that keys can be of different data types (string and integer).'''


Dict = {1: 'Geeks', 'name': 'For', 3: 'Geeks'} 
print("Accessing a element using key:") 
print(Dict['name']) 
print("Accessing a element using key:") 
print(Dict[1]) 

#Output:
Accessing a element using key:
For
Accessing a element using key:
Geeks

'''Accessing an Element of a Nested Dictionary
To access the value of any key in the nested dictionary, use indexing [] syntax.

Example: The code works with nested dictionaries. It first accesses and prints the entire nested dictionary associated with the key ‘Dict1’. Then, it accesses and prints a specific value by navigating through the nested dictionaries. Finally, it retrieves and prints the value associated with the key ‘Name’ within the nested dictionary under ‘Dict2’.'''

Dict = {'Dict1': {1: 'Geeks'}, 
        'Dict2': {'Name': 'For'}} 
  
print(Dict['Dict1']) 
print(Dict['Dict1'][1]) 
print(Dict['Dict2']['Name']) 

#Output:
{1: 'Geeks'}
Geeks
For

'''Deleting Elements using ‘del’ Keyword
The items of the dictionary can be deleted by using the del keyword as given below.

Example: The code defines a dictionary, prints its original content, and then uses the ‘del’ statement to delete the element associated with key 1. After deletion, it prints the updated dictionary, showing that the specified element has been removed.'''


Dict = {1: 'Geeks', 'name': 'For', 3: 'Geeks'} 
  
print("Dictionary =") 
print(Dict) 
del(Dict[1])  
print("Data after deletion Dictionary=") 
print(Dict) 

#Output
Dictionary ={1: 'Geeks', 'name': 'For', 3: 'Geeks'}
Data after deletion Dictionary={'name': 'For', 3: 'Geeks'}

'''Multiple Dictionary Operations in Python
The code begins with a dictionary ‘dict1’ and creates a copy ‘dict2’. It then demonstrates several dictionary operations: clearing ‘dict1’, accessing values, retrieving key-value pairs and keys, removing specific key-value pairs, updating a value, and retrieving values. These operations showcase how to work with dictionaries in Python.'''

dict1 = {1: "Python", 2: "Java", 3: "Ruby", 4: "Scala"} 
dict2 = dict1.copy() 
print(dict2) 
dict1.clear() 
print(dict1) 
print(dict2.get(1)) 
print(dict2.items()) 
print(dict2.keys()) 
dict2.pop(4) 
print(dict2) 
dict2.popitem() 
print(dict2) 
dict2.update({3: "Scala"}) 
print(dict2) 
print(dict2.values()) 

#Output:
{1: 'Python', 2: 'Java', 3: 'Ruby', 4: 'Scala'}
{}
Python
dict_items([(1, 'Python'), (2, 'Java'), (3, 'Ruby'), (4, 'Scala')])
dict_keys([1, 2, 3, 4])
{1: 'Python', 2: 'Java', 3: 'Ruby'}
{1: 'Python', 2: 'Java'}
{1: 'Python', 2: 'Java', 3: 'Scala'}
dict_values(['Python', 'Java', 'Scala'])


##############################################    INPUT AND OUTPUT IN PYTHON    #######################################################

'''Understanding input and output operations is fundamental to Python programming. With the print() function, you can display output in various formats, while the input() function enables interaction with users by gathering input during program execution.'''

#Example 1: 

'''Using % Operator
We can use ‘%’ operator. % values are replaced with zero or more value of elements. The formatting using % is similar to that of ‘printf’ in the C programming language.

%d –integer
%f – float
%s – string
%x –hexadecimal
%o – octal'''

# Taking input from the user
num = int(input("Enter a value: "))

add = num + 5

# Output
print("The sum is %d" %add)
Output

Enter a value: 50The sum is 55


#Example 2: 
'''Take Conditional Input from user in Python

In this example, the program prompts the user to enter their age. The input is converted to an integer using the int() function. Then, the program uses conditional statements to check the age range and prints a message based on whether the user is a minor, an adult, or a senior citizen.'''


# Prompting the user for input
age_input = input("Enter your age: ")

# Converting the input to an integer
age = int(age_input)

# Checking conditions based on user input
if age < 0:
    print("Please enter a valid age.")
elif age < 18:
    print("You are a minor.")
elif age >= 18 and age < 65:
    print("You are an adult.")
else:
    print("You are a senior citizen.")
Output

Enter your age: 22
You are an adult.

#Example 3:
'''Find DataType of Input in Python
In the given example, we are printing the type of variable x. We will determine the type of an object in Python.'''

a = "Hello World"
b = 10
c = 11.22
d = ("Geeks", "for", "Geeks")
e = ["Geeks", "for", "Geeks"]
f = {"Geeks": 1, "for":2, "Geeks":3}

print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))
print(type(f))

#Output
<class 'str'>
<class 'int'>
<class 'float'>
<class 'tuple'>
<class 'list'>
<class 'dict'>


#################################################    PYTHON FILE HANDLING   ########################################################

'''Python File Handling
Python supports file handling and allows users to handle files i.e., to read and write files, along with many other file handling options, to operate on files. The concept of file handling has stretched over various other languages, but the implementation is either complicated or lengthy, like other concepts of Python, this concept here is also easy and short. Python treats files differently as text or binary and this is important. Each line of code includes a sequence of characters, and they form a text file. Each line of a file is terminated with a special character, called the EOL or End of Line characters like comma {,} or newline character. It ends the current line and tells the interpreter a new one has begun. Let’s start with the reading and writing files. '''

'''Python File Open
Before performing any operation on the file like reading or writing, first, we have to open that file. For this, we should use Python’s inbuilt function open() but at the time of opening, we have to specify the mode, which represents the purpose of the opening file.'''

f = open(filename, mode)

'''Where the following mode is supported:

r: open an existing file for a read operation.
w: open an existing file for a write operation. If the file already contains some data, then it will be overridden but if the file is not present then it creates the file as well.
a:  open an existing file for append operation. It won’t override existing data.
r+:  To read and write data into the file. The previous data in the file will be overridden.
w+: To write and read data. It will override existing data.
a+: To append and read data from the file. It won’t override existing data.'''

'''Working in Read mode'''

#Example:

# a file named "geek", will be opened with the reading mode.
file = open('geek.txt', 'r')
 
# This will print every line one by one in the file
for each in file:
    print (each)

#Output:
Hello world
GeeksforGeeks
123 456


'''Working in Write Mode'''

#Example:

# Python code to create a file
file = open('geek.txt','w')
file.write("This is the write command")
file.write("It allows us to write in a particular file")
file.close()

#Output:
This is the write commandIt allows us to write in a particular file

'''Working of Append Mode'''

#Example:

# Python code to illustrate append() mode
file = open('geek.txt', 'a')
file.write("This will add this line")
file.close()

#Output:
This is the write commandIt allows us to write in a particular fileThis will add this line

'''Implementing all the functions in File Handling'''

#Example:

import os
 
def create_file(filename):
    try:
        with open(filename, 'w') as f:
            f.write('Hello, world!\n')
        print("File " + filename + " created successfully.")
    except IOError:
        print("Error: could not create file " + filename)
 
def read_file(filename):
    try:
        with open(filename, 'r') as f:
            contents = f.read()
            print(contents)
    except IOError:
        print("Error: could not read file " + filename)
 
def append_file(filename, text):
    try:
        with open(filename, 'a') as f:
            f.write(text)
        print("Text appended to file " + filename + " successfully.")
    except IOError:
        print("Error: could not append to file " + filename)
 
def rename_file(filename, new_filename):
    try:
        os.rename(filename, new_filename)
        print("File " + filename + " renamed to " + new_filename + " successfully.")
    except IOError:
        print("Error: could not rename file " + filename)
 
def delete_file(filename):
    try:
        os.remove(filename)
        print("File " + filename + " deleted successfully.")
    except IOError:
        print("Error: could not delete file " + filename)
 
 
if __name__ == '__main__':
    filename = "example.txt"
    new_filename = "new_example.txt"
 
    create_file(filename)
    read_file(filename)
    append_file(filename, "This is some additional text.\n")
    read_file(filename)
    rename_file(filename, new_filename)
    read_file(new_filename)
    delete_file(new_filename)

#Output:
File example.txt created successfully.
Hello, world!
Text appended to file example.txt successfully.
Hello, world!
This is some additional text.
File example.txt renamed to new_example.txt successfully.
Hello, world!
This is some additional text.
File new_example.txt deleted successfully.


#############################################    PYTHON EXCEPTION HANDLING     ########################################################

'''Error in Python can be of two types i.e. Syntax errors and Exceptions. Errors are problems in a program due to which the program will stop the execution. On the other hand, exceptions are raised when some internal events occur which change the normal flow of the program. 

Different types of exceptions in python:
In Python, there are several built-in Python exceptions that can be raised when an error occurs during the execution of a program. Here are some of the most common types of exceptions in Python. 

* TypeError: This exception is raised when an operation or function is applied to an object of the wrong type, such as adding a string to an integer.
* NameError: This exception is raised when a variable or function name is not found in the current scope.
* IndexError: This exception is raised when an index is out of range for a list, tuple, or other sequence types.
* KeyError: This exception is raised when a key is not found in a dictionary.
* ValueError: This exception is raised when a function or method is called with an invalid argument or input, such as trying to convert a string to an integer when the string does not represent a valid integer.
* AttributeError: This exception is raised when an attribute or method is not found on an object, such as trying to access a non-existent attribute of a class instance.
* IOError: This exception is raised when an I/O operation, such as reading or writing a file, fails due to an input/output error.
* ZeroDivisionError: This exception is raised when an attempt is made to divide a number by zero.
* ImportError: This exception is raised when an import statement fails to find or load a module.
These are just a few examples of the many types of exceptions that can occur in Python. It’s important to handle exceptions properly in your code using try-except blocks or other error-handling techniques, in order to gracefully handle errors and prevent the program from crashing.

Difference between Syntax Error and Exceptions
Syntax Error: As the name suggests this error is caused by the wrong syntax in the code. It leads to the termination of the program.''' 

#Example: 

'''There is a syntax error in the code . The ‘if' statement should be followed by a colon (:), and the ‘print' statement should be indented to be inside the ‘if' block.'''


amount = 10000
if(amount > 2999)
print("You are eligible to purchase Dsa Self Paced")

#Output: 
 File "\home\file.py", line 130
    if(amount > 2999)
                     ^
SyntaxError: invalid syntax


#Example:

 '''TypeError: This exception is raised when an operation or function is applied to an object of the wrong type. Here’s an example:
 Here a ‘TypeError’ is raised as both the datatypes are different which are being added.'''

x = 5
y = "hello"
z = x + y

#Output: 
Traceback (most recent call last):
  File "7edfa469-9a3c-4e4d-98f3-5544e60bff4e.py", line 4, in <module>
    z = x + y
TypeError: unsupported operand type(s) for +: 'int' and 'str'


#Example: 
'''Try and Except Statement – Catching Exceptions
Try and except statements are used to catch and handle exceptions in Python. Statements that can raise exceptions are kept inside the try clause and the statements that handle the exception are written inside except clause.

Here we are trying to access the array element whose index is out of bound and handle the corresponding exception.'''

a = [1, 2, 3]
try: 
    print ("Second element = %d" %(a[1]))
 
    print ("Fourth element = %d" %(a[3]))
except:
    print ("An error occurred")

#Output
Second element = 2
An error occurred

'''Try with Else Clause
In Python, you can also use the else clause on the try-except block which must be present after all the except clauses. The code enters the else block only if the try clause does not raise an exception.

The code defines a function AbyB(a, b) that calculates c as ((a+b) / (a-b)) and handles a potential ZeroDivisionError. It prints the result if there’s no division by zero error. Calling AbyB(2.0, 3.0) calculates and prints -5.0, while calling AbyB(3.0, 3.0) attempts to divide by zero, resulting in a ZeroDivisionError, which is caught and “a/b results in 0” is printed.'''

def AbyB(a , b):
    try:
        c = ((a+b) / (a-b))
    except ZeroDivisionError:
        print ("a/b result in 0")
    else:
        print (c)
AbyB(2.0, 3.0)
AbyB(3.0, 3.0)

#Output:
-5.0
a/b result in 0 

'''Advantages of Exception Handling:
Improved program reliability: By handling exceptions properly, you can prevent your program from crashing or producing incorrect results due to unexpected errors or input.
Simplified error handling: Exception handling allows you to separate error handling code from the main program logic, making it easier to read and maintain your code.
Cleaner code: With exception handling, you can avoid using complex conditional statements to check for errors, leading to cleaner and more readable code.
Easier debugging: When an exception is raised, the Python interpreter prints a traceback that shows the exact location where the exception occurred, making it easier to debug your code.

Disadvantages of Exception Handling:
Performance overhead: Exception handling can be slower than using conditional statements to check for errors, as the interpreter has to perform additional work to catch and handle the exception.
Increased code complexity: Exception handling can make your code more complex, especially if you have to handle multiple types of exceptions or implement complex error handling logic.
Possible security risks: Improperly handled exceptions can potentially reveal sensitive information or create security vulnerabilities in your code, so it’s important to handle exceptions carefully and avoid exposing too much information about your program.'''



###############################################      PYTHON MODULES      ######################################################

'''Python Module is a file that contains built-in functions, classes,its and variables. There are many Python modules, each with its specific work.

In this article, we will cover all about Python modules, such as How to create our own simple module, Import Python modules, From statements in Python, we can use the alias to rename the module, etc.

What is Python Module
A Python module is a file containing Python definitions and statements. A module can define functions, classes, and variables. A module can also include runnable code.

Grouping related code into a module makes the code easier to understand and use. It also makes the code logically organized.'''

'''Create a Python Module
To create a Python module, write the desired code and save that in a file with .py extension. Let’s understand it better with an example:'''

#Example:

'''Let’s create a simple calc.py in which we define two functions, one add and another subtract.'''

# A simple module, calc.py
def add(x, y):
    return (x+y)
 
def subtract(x, y):
    return (x-y)

'''Import module in Python
We can import the functions, and classes defined in a module to another module using the import statement in some other Python source file.

When the interpreter encounters an import statement, it imports the module if the module is present in the search path.

Note: A search path is a list of directories that the interpreter searches for importing a module.

For example, to import the module calc.py, we need to put the following command at the top of the script.'''

#Syntax to Import Module in Python

import module

#Importing modules in Python Example
# importing  module calc.py
import calc
 
print(calc.add(10, 2))

#Output:
12

#Python Import from Module

# importing sqrt() and factorial from the
# module math
from math import sqrt, factorial
 
# if we simply do "import math", then
# math.sqrt(16) and math.factorial()
# are required.
print(sqrt(16))
print(factorial(6))

#Output: 
4.0
720

'''Location Python Modules'''

# importing sys module
import sys
 
# importing sys.path
print(sys.path)

#Output:

[‘/home/nikhil/Desktop/gfg’, ‘/usr/lib/python38.zip’, ‘/usr/lib/python3.8’, ‘/usr/lib/python3.8/lib-dynload’, ”, ‘/home/nikhil/.local/lib/python3.8/site-packages’, ‘/usr/local/lib/python3.8/dist-packages’, ‘/usr/lib/python3/dist-packages’, ‘/usr/local/lib/python3.8/dist-packages/IPython/extensions’, ‘/home/nikhil/.ipython’]

'''Renaming the Python Module
We can rename the module while importing it using the keyword.'''

Syntax:  Import Module_name as Alias_name

# importing sqrt() and factorial from the
# module math
import math as mt
 
# if we simply do "import math", then
# math.sqrt(16) and math.factorial()
# are required.
print(mt.sqrt(16))
print(mt.factorial(6))

#Output
4.0
720

'''Python Built-in modules
There are several built-in modules in Python, which you can import whenever you like.'''

# importing built-in module math
import math
 
# using square root(sqrt) function contained 
# in math module
print(math.sqrt(25)) 
 
# using pi function contained in math module
print(math.pi) 
 
# 2 radians = 114.59 degrees
print(math.degrees(2))  
 
# 60 degrees = 1.04 radians
print(math.radians(60))  
 
# Sine of 2 radians
print(math.sin(2))  
 
# Cosine of 0.5 radians
print(math.cos(0.5))  
 
# Tangent of 0.23 radians
print(math.tan(0.23)) 
 
# 1 * 2 * 3 * 4 = 24
print(math.factorial(4))  
 
# importing built in module random
import random
 
# printing random integer between 0 and 5
print(random.randint(0, 5))  
 
# print random floating point number between 0 and 1
print(random.random())  
 
# random number between 0 and 100
print(random.random() * 100)  
 
List = [1, 4, True, 800, "python", 27, "hello"]
 
# using choice function in random module for choosing 
# a random element from a set such as a list
print(random.choice(List)) 
 
 
# importing built in module datetime
import datetime
from datetime import date
import time
 
# Returns the number of seconds since the
# Unix Epoch, January 1st 1970
print(time.time())  
 
# Converts a number of seconds to a date object
print(date.fromtimestamp(454554))  

#Output:
5.0
3.14159265359
114.591559026
1.0471975512
0.909297426826
0.87758256189
0.234143362351
24
3
0.401533172951
88.4917616788
True
1461425771.87

################################################     PYTHON LIBRARIES    ######################################################

'''A Python library is a collection of related modules. It contains bundles of code that can be used repeatedly in different programs. It makes Python Programming simpler and convenient for the programmer. As we don’t need to write the same code again and again for different programs. Python libraries play a very vital role in fields of Machine Learning, Data Science, Data Visualization, etc.

Working of Python Library

As is stated above, a Python library is simply a collection of codes or modules of codes that we can use in a program for specific operations. We use libraries so that we don’t need to write the code again in our program that is already available. But how it works. Actually, in the MS Windows environment, the library files have a DLL extension (Dynamic Load Libraries). When we link a library with our program and run that program, the linker automatically searches for that library. It extracts the functionalities of that library and interprets the program accordingly. That’s how we use the methods of a library in our program. '''

'''Python standard library
The Python Standard Library contains the exact syntax, semantics, and tokens of Python. It contains built-in modules that provide access to basic system functionality like I/O and some other core modules. Most of the Python Libraries are written in the C programming language. The Python standard library consists of more than 200 core modules. All these work together to make Python a high-level programming language. Python Standard Library plays a very important role. Without it, the programmers can’t have access to the functionalities of Python. But other than this, there are several other libraries in Python that make a programmer’s life easier. Let’s have a look at some of the commonly used libraries:

1. TensorFlow
2. Matplotlib
3. Pandas
4. Numpy
5. Scipy
6. Scrapy
7. Scikit-learn
8. PyGame
9. PyTorch
10.PyBrain


TensorFlow: This library was developed by Google in collaboration with the Brain Team. It is an open-source library used for high-level computations. It is also used in machine learning and deep learning algorithms. It contains a large number of tensor operations. Researchers also use this Python library to solve complex computations in Mathematics and Physics.'''

#Example: Given below is an example using Varaible. 

# importing tensorflow
import tensorflow as tf
 
# creating nodes in computation graph
node = tf.Variable(tf.zeros([2,2]))
 
# running computation graph
with tf.Session() as sess:
 
    # initialize all global variables 
    sess.run(tf.global_variables_initializer())
 
    # evaluating node
    print("Tensor value before addition:\n",sess.run(node))
 
    # elementwise addition to tensor
    node = node.assign(node + tf.ones([2,2]))
 
    # evaluate node again
    print("Tensor value after addition:\n", sess.run(node))

#Output:
Tensor value before addition:
 [[ 0.  0.]
 [ 0.  0.]]
Tensor value after addition:
 [[ 1.  1.]
 [ 1.  1.]]


'''Matplotlib: This library is responsible for plotting numerical data. And that’s why it is used in data analysis. It is also an open-source library and plots high-defined figures like pie charts, histograms, scatterplots, graphs, etc.'''

#Example:

'''Scatter Plot in Matplotlib
By importing matpltlib. plot () we created a scatter plot. It defines x and y coordinates, then plots the points in blue and displays the plot.''' 

import matplotlib.pyplot as plt
 
x =[5, 7, 8, 7, 2, 17, 2, 9,
    4, 11, 12, 9, 6] 
 
y =[99, 86, 87, 88, 100, 86, 
    103, 87, 94, 78, 77, 85, 86]
 
plt.scatter(x, y, c ="blue")
 
# To show the plot
plt.show()


'''Pandas: Pandas are an important library for data scientists. It is an open-source machine learning library that provides flexible high-level data structures and a variety of analysis tools. It eases data analysis, data manipulation, and cleaning of data. Pandas support operations like Sorting, Re-indexing, Iteration, Concatenation, Conversion of data, Visualizations, Aggregations, etc.'''

#Example:

#Creating a Pandas DataFrame.

# import pandas as pd
import pandas as pd
 
# list of strings
lst = ['Geeks', 'For', 'Geeks', 'is', 
            'portal', 'for', 'Geeks']
 
# Calling DataFrame constructor on list
df = pd.DataFrame(lst)
print(df)

'''Numpy: The name “Numpy” stands for “Numerical Python”. It is the commonly used library. It is a popular machine learning library that supports large matrices and multi-dimensional data. It consists of in-built mathematical functions for easy computations. Even libraries like TensorFlow use Numpy internally to perform several operations on tensors. Array Interface is one of the key features of this library.'''

#Example:

#Creating a Numpy Array.

# Python program for
# Creation of Arrays

import numpy as np
 
# Creating a rank 1 Array
arr = np.array([1, 2, 3])
print("Array with Rank 1: \n",arr)
 
# Creating a rank 2 Array
arr = np.array([[1, 2, 3],
                [4, 5, 6]])
print("Array with Rank 2: \n", arr)
 
# Creating an array from tuple
arr = np.array((1, 3, 2))
print("\nArray created using "
      "passed tuple:\n", arr)
Run on IDE

#Output:
Array with Rank 1: 
 [1 2 3]
Array with Rank 2: 
 [[1 2 3]
 [4 5 6]]

Array created using passed tuple:
 [1 3 2

'''SciPy: The name “SciPy” stands for “Scientific Python”. It is an open-source library used for high-level scientific computations. This library is built over an extension of Numpy. It works with Numpy to handle complex computations. While Numpy allows sorting and indexing of array data, the numerical data code is stored in SciPy. It is also widely used by application developers and engineers.'''

#Example: 

'''Exploratory Data Analysis (EDA)
Use descriptive statistics from SciPy’s stats module to gain insights into the dataset.
Calculate measures such as mean, median, standard deviation, skewness, kurtosis, etc.'''

from scipy import stats
data = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
# Calculate mean and standard deviation
mean_val = np.mean(data)
std_dev = np.std(data)
# Perform basic statistical tests
t_stat, p_value = stats.ttest_1samp(data, popmean=5)
print("t_stat:" , t_stat)
print("p_value:", p_value) 

#Output:
t_stat: 0.0
p_value: 1.0

'''Scrapy: It is an open-source library that is used for extracting data from websites. It provides very fast web crawling and high-level screen scraping. It can also be used for data mining and automated testing of data.'''

#Example:

'''Creating Items to be passed over files.
One more thing to note is that we will require a description of what our item will contain in items.py file. Hence our items.py file contains the below-given code:'''

import scrapy
 
class ScrapytutorialItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
     
    # only one field that it of Quote.
    Quote = scrapy.Field()

'''Scikit-learn: It is a famous Python library to work with complex data. Scikit-learn is an open-source library that supports machine learning. It supports variously supervised and unsupervised algorithms like linear regression, classification, clustering, etc. This library works in association with Numpy and SciPy.'''

#Example: 

'''Load a Dataset'''

# load the iris dataset as an example 
from sklearn.datasets import load_iris 
iris = load_iris() 
  
# store the feature matrix (X) and response vector (y) 
X = iris.data 
y = iris.target 
  
# store the feature and target names 
feature_names = iris.feature_names 
target_names = iris.target_names 
  
# printing features and target names of our dataset 
print("Feature names:", feature_names) 
print("Target names:", target_names) 
  
# X and y are numpy arrays 
print("\nType of X is:", type(X)) 
  
# printing first 5 input rows 
print("\nFirst 5 rows of X:\n", X[:5])

#Output: 
Feature names: ['sepal length (cm)','sepal width (cm)',
                'petal length (cm)','petal width (cm)']
Target names: ['setosa' 'versicolor' 'virginica']
Type of X is: 
First 5 rows of X:
 [[ 5.1  3.5  1.4  0.2]
 [ 4.9  3.   1.4  0.2]
 [ 4.7  3.2  1.3  0.2]
 [ 4.6  3.1  1.5  0.2]
 [ 5.   3.6  1.4  0.2]]


'''PyGame: This library provides an easy interface to the Standard Directmedia Library (SDL) platform-independent graphics, audio, and input libraries. It is used for developing video games using computer graphics and audio libraries along with Python programming language.'''

#Example: 

'''Drawing a solid polygon'''

# Importing pygame module
import pygame
from pygame.locals import *
 
# initiate pygame and give permission
# to use pygame's functionality.
pygame.init()
 
# create the display surface object
# of specific dimension.
window = pygame.display.set_mode((600, 600))
 
# Fill the scree with white color
window.fill((255, 255, 255))
 
# Using draw.rect module of
# pygame to draw the outlined polygon
pygame.draw.polygon(window, (255, 0, 0), 
                    [[300, 300], [100, 400],
                     [100, 300]])
 
# Draws the surface object to the screen.
pygame.display.update()


'''PyTorch: PyTorch is the largest machine learning library that optimizes tensor computations. It has rich APIs to perform tensor computations with strong GPU acceleration. It also helps to solve application issues related to neural networks.'''

#Example: 
'''In the Python example below we join two one-dimensional tensors using torch.stack() method.'''

# Python 3 program to demonstrate torch.stack() method 
# for two one dimensional tensors 
# importing torch 
import torch 
  
# creating tensors 
x = torch.tensor([1.,3.,6.,10.]) 
y = torch.tensor([2.,7.,9.,13.]) 
  
# printing above created tensors 
print("Tensor x:", x) 
print("Tensor y:", y) 
  
# join above tensor using "torch.stack()" 
print("join tensors:") 
t = torch.stack((x,y)) 
  
# print final tensor after join 
print(t) 
  
print("join tensors dimension 0:") 
t = torch.stack((x,y), dim = 0) 
print(t) 
  
print("join tensors dimension 1:") 
t = torch.stack((x,y), dim = 1) 
print(t) 

#Output:
Tensor x: tensor([ 1.,  3.,  6., 10.])
Tensor y: tensor([ 2.,  7.,  9., 13.])
join tensors:
tensor([[ 1.,  3.,  6., 10.],
        [ 2.,  7.,  9., 13.]])
join tensors dimension 0:
tensor([[ 1.,  3.,  6., 10.],
        [ 2.,  7.,  9., 13.]])
join tensors dimension 1:
tensor([[ 1.,  2.],
        [ 3.,  7.],
        [ 6.,  9.],
        [10., 13.]])

'''Explanation: In the above code tensors x and y are one-dimensional each having four elements.  The final concatenated tensor is a 2D tensor. As the dimension is 1, we can stack the tensors with dimensions 0 and 1. When dim =0 the tensors are stacked increasing the number of rows. When dim =1 the tensors are transposed and stacked along the column.'''


'''PyBrain: The name “PyBrain” stands for Python Based Reinforcement Learning, Artificial Intelligence, and Neural Networks library. It is an open-source library built for beginners in the field of Machine Learning. It provides fast and easy-to-use algorithms for machine learning tasks. It is so flexible and easily understandable and that’s why is really helpful for developers that are new in research fields.'''

#Example:

'''In this example, the input has a size equal to 2 and the target has a size equal to 1.'''

# Python program to create a dataset 
# using PyBrain 
  
# Importing SupervisedDataSet from  
# pybrain.datasets 
from pybrain.datasets import SupervisedDataSet 
  
# Creating SupervisedDataSet 
supervised_dataset = SupervisedDataSet(2, 1) 
  
# Print 
print(dataSet) 

#############################################    PYTHON WEB DEVELOPMENT   #####################################################

'''Python Django is a web framework that allows to quickly create efficient web pages. Django is also called batteries included framework because it provides built-in features such as Django Admin Interface, default database – SQLite3, etc. When you’re building a website, you always need a similar set of components: a way to handle user authentication (signing up, signing in, signing out), a management panel for your website, forms, a way to upload files, etc. Django gives you ready-made components to use.

Why Django Framework?
Excellent documentation and high scalability.
Used by Top MNCs and Companies, such as Instagram, Disqus, Spotify, Youtube, Bitbucket, Dropbox, etc. and the list is never-ending.
Easiest Framework to learn, rapid development, and Batteries fully included. Django is a rapid web development framework that can be used to develop fully fleshed web applications in a short period of time.
The last but not least reason to learn Django is Python, Python has a huge library and features such as Web Scraping, Machine Learning, Image Processing, Scientific Computing, etc. One can integrate all this with web applications and do lots and lots of advanced stuff.

Why Django Framework?
Excellent documentation and high scalability.
Used by Top MNCs and Companies, such as Instagram, Disqus, Spotify, Youtube, Bitbucket, Dropbox, etc. and the list is never-ending.
Easiest Framework to learn, rapid development, and Batteries fully included. Django is a rapid web development framework that can be used to develop fully fleshed web applications in a short period of time.
The last but not least reason to learn Django is Python, Python has a huge library and features such as Web Scraping, Machine Learning, Image Processing, Scientific Computing, etc. One can integrate all this with web applications and do lots and lots of advanced stuff.
Django Architecture
Django is based on MVT (Model-View-Template) architecture which has the following three parts – 

Model: The model is going to act as the interface of your data. It is responsible for maintaining data. It is the logical data structure behind the entire application and is represented by a database (generally relational databases such as MySql, Postgres).

View: The View is the user interface that you see in your browser when you render a website. It is represented by HTML/CSS/Javascript and Jinja files.

Template: A template consists of static parts of the desired HTML output as well as some special syntax describing how dynamic content will be inserted. To check more, visit – Django Templates.

Setting up the Virtual Environment
Most of the time when you’ll be working on some Django projects, you’ll find that each project may need a different version of Django. This problem may arise when you install Django in a global or default environment. To overcome this problem we will use virtual environments in Python. This enables us to create multiple different Django environments on a single computer. To create a virtual environment type the below command in the terminal.'''

python3 -m venv ./name
'''Here the name suggests the name of the virtual environment. Let’s create our virtual environment with the name as venv only. So the command to create it will be – '''

python3 -m venv ./venv

'''After running the above command you will see a folder named venv with the following sub-directories.
After creating the virtual environment let’s activate it. To activate it type the below command in the terminal.'''

source ./venv/bin/activate
'''In the above command ./ is used to tell the current working directory.'''

'''Congratulations on mastering the fundamentals of Python! Remember, learning to code is a continuous journey filled with challenges and rewards. Keep exploring, keep practicing, and don't be afraid to experiment. The world of programming is a vast and exciting and you now have the skills to navigate it with confidence. Happy Coding!

