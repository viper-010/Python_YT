# 05 - Comments, Escape sequence & Print in Python

Today we will talk about Comments, Escape Sequences and little bit more about print statement in Python.
We will also throw some light on Escape Sequences


## Python Comments
A comment is a part of the coding file that the programmer does not want to execute, rather the programmer uses it to either explain a block of code or to avoid the execution of a specific part of code while testing.


## Single-Line Comments:

To write a comment just add a ‘#’ at the start of the line.

#### Example 1

```python
#This is a 'Single-Line Comment'
print("This is a print statement.")
``` 

Output:

```markup
This is a print statement. 
``` 

#### Example 2

```python
print("Hello World !!!") #Printing Hello World
```

Output:

```markup
Hello World !!!
``` 

#### Example 3:

```python
print("Python Program")
#print("Python Program")
``` 

Output: 

```markup
Python Program
```
---

## Multi-Line Comments:

To write multi-line comments you can use ‘#’ at each line or you can use the multiline string.

**Example 1:** The use of ‘#’.

```python
#It will execute a block of code if a specified condition is true.
#If the condition is false then it will execute another block of code.
p = 7
if (p > 5):
    print("p is greater than 5.")
else:
    print("p is not greater than 5.")
```

Output:

```markup
p is greater than 5.
```

**Example 2:** The use of multiline string.

```python
"""This is an if-else statement.
It will execute a block of code if a specified condition is true.
If the condition is false then it will execute another block of code."""
p = 7
if (p > 5):
    print("p is greater than 5.")
else:
    print("p is not greater than 5.")
```

Output:

```markup
p is greater than 5.
```
---

## Escape Sequence Characters

- To insert characters that cannot be directly used in a string, we use an escape sequence character.
- An escape sequence character is a backslash  `\`  followed by the character you want to insert.

- An example of a character that cannot be directly used in a string is a double quote inside a string that is surrounded by double quotes:

```python
print("This doesnt "execute")
print("This will \" execute")
```
--- 

## More on Print statement
The syntax of a print statement looks something like this:

```python
print(object(s), sep=separator, end=end, file=file, flush=flush)
```

## Other Parameters of Print Statement 

### 1. object(s):
- What you want to print
- Things to print
- You can print one or multiple objects (strings, numbers, variables, etc.)
- Any object, and as many as you like. Will be converted to string before printed

#### Example
```python
print("Hello")
print("Name:", "Rohan", 25)
```

Output: 

```markup
Hello
Name: Rohan 25
```
---

### 2. sep:
- Separator between multiple objects
- Default is a space ' '
- Specify how to separate the objects, if there is more than one. Default is ' '

#### Example 1
```python
print("Rohan", "TA", sep="-")
```

Output: 

```markup
Rohan-TA
```

- You can use sep='' to remove any space between printed objects:

#### Example 2
```python
print("A", "B", "C", sep="")
```

Output: 

```markup
ABC
```
---

### 3. end:
- What to print at the end of the line
- Default is newline '\n' (line feed)

#### Example 1
```python
print("Hello", end=" ")
print("World!")
```

Output: 

```markup
Hello World!
```
#### Example 2
```python
print("Loading", end="...")
print("Done")
```

Output: 

```markup
Loading...Done
```
---

### 4. file:
- Where to print (default: console)
- Where to send output
- An object with a write method. Default is sys.stdout

#### Example
You can redirect the output to a file
```python
with open("output.txt", "w") as f:
    print("Saving to file", file=f)
```
This will write "Saving to file" into output.txt instead of showing in the terminal.

Output: 

```markup
Saving to file
```
---

### 5. flush:
- Whether to forcibly flush the output
- A boolean value. If True, it forces the stream to be flushed immediately, which is useful in buffering scenarios.
- Default is False


#### Example
Useful when printing logs in real-time (like progress bars).
```python
import time

for i in range(3):
    print(i, end=' ', flush=True)
    time.sleep(1)
```

Output (printed immediately without buffering):

```markup
0 1 2 
```
---
