0x0B-python-input_output
ALX SOFTWARE ENGINEERING

Python - Input/Output
Python provides several ways to handle input and output operations.
Here are some common methods and functions used for input and output in Python:
1. Print: The print function is used to display output on the console.
2. Input: The input function is used to get user input from the console.
It displays a prompt (optional) and waits for the user to enter a value,
which is then returned as a string.
3. File Handling: Python provides several functions and methods for working with files.
You can open a file using the #open function and perform various operations like reading,
writing, or appending to the file.
4. Writing to a File: To write to a file, you can open the file in write mode
("w") or append mode ("a") using the open function. Then you can use the write method 
to write data to the file.
5. Error Handling: When working with file I/O, it's important to handle exceptions that
 may occur. Python's try-except statement is used to catch nd handle exceptions gracefully.

Resources
Read or watch:

7.2. Reading and Writing Files
8.7. Predefined Clean-up Actions
Dive Into Python 3: Chapter 11. Files (until “11.4 Binary Files” (included))
JSON encoder and decoder
Learn to Program 8 : Reading / Writing Files
Automate the Boring Stuff with Python (ch. 8 p 180-183 and ch. 14 p 326-333)
All about py-file I/O
Learning Objectives
At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

General
Why Python programming is awesome
How to open a file
How to write text in a file
How to read the full content of a file
How to read a file line by line
How to move the cursor in a file
How to make sure a file is closed after using it
What is and how to use the with statement
What is JSON
What is serialization
What is deserialization
How to convert a Python data structure to a JSON string
How to convert a JSON string to a Python data structure

Tasks
0. Read file
mandatory
Write a function that reads a text file (UTF8) and prints it to stdout:
1. Write to a file
mandatory
Write a function that writes a string to a text file (UTF8) and returns the number of characters written:
2. Append to a file
mandatory
Write a function that appends a string at the end of a text file (UTF8) and returns the number of characters added:
3. To JSON string
mandatory
Write a function that returns the JSON representation of an object (string):
4. From JSON string to Object
mandatory
Write a function that returns an object (Python data structure) represented by a JSON string:
5. Save Object to a file
mandatory
Write a function that writes an Object to a text file, using a JSON representation:
6. Create object from a JSON file
mandatory
Write a function that creates an Object from a “JSON file”:
7. Load, add, save
mandatory
Write a script that adds all arguments to a Python list, and then save them to a file:
8. Class to JSON
mandatory
Write a function that returns the dictionary description with simple data structure (list, dictionary, string, integer and boolean) for JSON serialization of an object:
9. Student to JSON
mandatory
Write a class Student that defines a student by:
10. Student to JSON with filter
mandatory
Write a class Student that defines a student by: (based on 9-student.py)
11. Student to disk and reload
mandatory
Write a class Student that defines a student by: (based on 10-student.py)
12. Pascal's Triangle

