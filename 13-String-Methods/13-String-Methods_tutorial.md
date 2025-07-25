# String methods
Python provides a set of built-in methods that we can use to alter and modify the strings.
- Strings are immutable.
- That's correct. Strings in Python are immutable, which means once a string is created, its contents cannot be changed in place.
- "Immutable" Means in Practice, If you have a string and you want to modify it, Python doesn't alter the original string. Instead, it creates a completely new string with the changes.

---
## upper() 
The upper() method converts a string to upper case.

### Example
```python
str1 = "AbcDEfghIJ"
print(str1.upper())
```
#### Output:
```
ABCDEFGHIJ
 ```
---

## lower()
The lower() method converts a string to lower case.

### Example
```python
str1 = "AbcDEfghIJ"
print(str1.lower())
```
#### Output:
```
abcdefghij
 ```
---

## title() 
The title() method capitalizes each letter of the word within the string.

### Example
```python
str1 = "He's name is Dan. Dan is an honest man."
print(str1.title())
```
#### Output:
```
He'S Name Is Dan. Dan Is An Honest Man.
```
---

## isupper() 
The isupper() method returns True if all the characters in the string are upper case, else it returns False. 

### Example 
```python
str1 = "WORLD HEALTH ORGANIZATION" 
print(str1.isupper())
```
#### Output:
```
True
 ```
---

## islower() 
The islower() method returns True if all the characters in the string are lower case, else it returns False. 

### Example
```python
str1 = "hello world"
print(str1.islower())
```
#### Output:
```
True
 ```
---

## istitle() 
The istitile() returns True only if the first letter of each word of the string is capitalized, else it returns False.

### Example 1
```python
str1 = "World Health Organization" 
print(str1.istitle())
```
#### Output:
```
True
 ```

### Example 2
```python
str2 = "To kill a Mocking bird"
print(str2.istitle())
```
#### Output:
```
False
 ```
---

## capitalize() 
The capitalize() method turns only the first character of the string to uppercase and the rest other characters of the string are turned to lowercase. The string has no effect if the first character is already uppercase.

### Example
```python
str1 = "hello"
capStr1 = str1.capitalize()
print(capStr1)
str2 = "hello WorlD"
capStr2 = str2.capitalize()
print(capStr2)
```
#### Output:
```
Hello
Hello world
```
---

## swapcase() 
The swapcase() method changes the character casing of the string. Upper case are converted to lower case and lower case to upper case.

### Example
```python
str1 = "Python is a Interpreted Language" 
print(str1.swapcase())
```
#### Output:
```
pYTHON IS A iNTERPRETED lANGUAGE
 ```
---

## startswith() 
The endswith() method checks if the string starts with a given value. If yes then return True, else return False. 

### Example 1
```python
str1 = "Python is a Interpreted Language" 
print(str1.startswith("Python"))
```
#### Output:
```
True
 ```

### Example 2
```python
str1 = "Welcome to the Console !!!"
# Checks if the slice "to the Console !!!" starts with "to"
print(str1.startswith("to", 8))
```
#### Output:
```
True
```
---
## endswith() 
The endswith() method checks if the string ends with a given value. If yes then return True, else return False. 

### Example 1 
```python
str1 = "Welcome to the Console !!!"
print(str1.endswith("!!!"))
```
#### Output:
```
True
```
We can even also check for a value in-between the string by providing start and end index positions.

### Example 2
```python
str1 = "Welcome to the Console !!!"
print(str1.endswith("to", 4, 10))
```
#### Output:
```
True
 ```
---

## strip() 
The strip() method removes any white spaces before and after the string.

### Example 1
```python
str2 = " Silver Spoon "
print(str2.strip)
```
#### Output:
```
Silver Spoon
```

### Example 2
```python
text = "-.,.Hello, World-.,."
# Removes any leading/trailing hyphens, commas, or periods
cleaned_text = text.strip(".,")
print(cleaned_text)
```
#### Output:
```
-.,.Hello, World-
```
---

## rstrip() 
the rstrip() removes any trailing characters (ending).

### Example 1
```python
str3 = "Hello !!!"
print(str3.rstrip("!"))
```
### Output:
```
Hello
 ```

- When used without an argument, rstrip() removes spaces, tabs (\t), and newlines (\n) from the end of a string.
- This is useful for cleaning the right side of data.

### Example 2
```python
text = "   Hello, World!   \n"
cleaned_text = text.rstrip()
# The single quotes show where the string now ends
print(f"'{cleaned_text}'")
```
### Output:
```
'   Hello, World!'
```

### Example 3
```python
# Example: Stripping a file extension and extra characters
filename = "document.txt.bak"
cleaned_filename = filename.rstrip(".bak")
print(cleaned_filename)
```
### Output:
```
document.txt
```
---

## replace() 
The replace() method replaces all occurences of a string with another string.

### Example
```python
str2 = "Silver Spoon"
print(str2.replace("Sp", "M"))
```
#### Output:
```
Silver Moon
 ```
---

## split() 
The split() method splits the given string at the specified instance and returns the separated strings as list items.

### Example
```python
str2 = "Silver Spoon"
print(str2.split(" "))      #Splits the string at the whitespace " ".
```
#### Output:
```
['Silver', 'Spoon']
```
---

## center() 
The center() method aligns the string to the center as per the parameters given by the user.

### Example 1
```python
str1 = "Welcome to the Console!!!"
print(str1.center(50))
```
#### Output:
```
            Welcome to the Console!!!
 ```

We can also provide padding character. It will fill the rest of the fill characters provided by the user.

### Example 2
```python
str1 = "Welcome to the Console!!!"
print(str1.center(50, "."))
```
#### Output:
```
............Welcome to the Console!!!.............
 ```
---

## count() 
The count() method returns the number of times the given value has occurred within the given string.
### Example
```python
str2 = "Abracadabra"
countStr = str2.count("a")
print(countStr)
```
#### Output:
```
4
```
---

## find() 
The find() method searches for the first occurrence of the given value and returns the index where it is present. If given value is absent from the string then return -1.

### Example 1
```python
str1 = "He's name is Dan. He is an honest man."
print(str1.find("is"))
```
#### Output:
```
10
 ```

As we can see, this method is somewhat similar to the index() method. The major difference being that index() raises an exception if value is absent whereas find() does not.

### Example 2
```python
str1 = "He's name is Dan. He is an honest man."
print(str1.find("Daniel"))
```
#### Output:
```
-1
 ```
---

## index() 
The index() method searches for the first occurrence of the given value and returns the index where it is present. If given value is absent from the string then raise an exception.

### Example 1
```python
str1 = "He's name is Dan. Dan is an honest man."
print(str1.index("Dan"))
```
#### Output:
```
13
 ```

As we can see, this method is somewhat similar to the find() method. The major difference being that index() raises an exception if value is absent whereas find() does not.

### Example 2
```python
str1 = "He's name is Dan. Dan is an honest man."
print(str1.index("Daniel"))
```
#### Output:
```
ValueError: substring not found
 ```
---

## isalnum() 
The isalnum() method returns True only if the entire string only consists of A-Z, a-z, 0-9. If any other characters or punctuations are present, then it returns False.

### Example 
```python
str1 = "WelcomeToTheConsole"
print(str1.isalnum())
```
#### Output:
```
True
 ```
---

## isalpha() 
The isalnum() method returns True only if the entire string only consists of A-Z, a-z. If any other characters or punctuations or numbers(0-9) are present, then it returns False.

### Example :
```python
str1 = "Welcome"
print(str1.isalpha())
```
#### Output:
```
True
 ```
---

## isprintable() 
- The isprintable() method returns True if all the values within the given string are printable, if not, then return False.
- Printable characters include letters, numbers, punctuation, and spaces. 
- Non-printable characters are control characters like newlines (\n) and tabs (\t).

### Example 1
```python
str1 = "Hello, World! 123"
print(str1.isprintable())
```
#### Output:
```
True
 ```

### Example 2
```python
# The newline character \n is not printable
str2 = "Hello, World!\n"
print(str2.isprintable())
```
#### Output:
```
False
 ```
---

## isspace() 
- The isspace() method returns True only and only if the string contains white spaces, else returns False.
- Whitespace characters include spaces, tabs (\t), and newlines (\n).

### Example 1
```python
str1 = "        "       #using Spacebar
print(str1.isspace())
str2 = "        "       #using Tab
print(str2.isspace())
```
#### Output:
```
True
True
 ```

### Example 2
```python
# A string with only spaces
str1 = "   "
print(str1.isspace())

# A string with spaces, a tab, and a newline
str2 = " \t \n "
print(str2.isspace())
```
#### Output:
```
True
True
 ```

### Example 3
```python
# Contains letters
str3 = "Hello World"
print(str3.isspace())

# Is an empty string
str4 = ""
print(str4.isspace())
```
#### Output:
```
False
False
 ```
---
