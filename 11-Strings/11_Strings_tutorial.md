# What are strings?
In python, anything that you enclose between single or double quotation marks is considered a string. A string is essentially a sequence or array of textual data. Strings are used when working with Unicode characters. 
* """ and ''' helps to carry out the string in what format we needed.
### Example
```python
name = "Harry"
print("Hello, " + name)
```
#### Output:
```
Hello, Harry
```
**Note**: It does not matter whether you enclose your strings in single or double quotes, the output remains the same. 

Sometimes, the user might need to put quotation marks in between the strings. Example, consider the sentence: He said, “I want to eat an apple”.

How will you print this statement in python?: 
```He said, "I want to eat an apple".```
We will definitely use single quotes for our convenience
```python
print('He said, "I want to eat an apple".')

other ways:

print('He said, \"I want to eat an apple\".')
print("He said, \"I want to eat an apple\".")
print('''He said, "I want to eat an apple".''')
print("""He said, "I want to eat an apple".""")
```
---

## Multiline Strings
If our string has multiple lines, we can create them like this: 
```python 
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)
```
---

## Accessing Characters of a String
In Python, string is like an array of characters. We can access parts of string by using its index which starts from 0.\
Square brackets can be used to access elements of the string.

```python 
print(name[0])
print(name[1])

```
---

## Looping through the string
We can loop through strings using a for loop like this: 
```python
for character in name:
    print(character)
```

* Above code prints all the characters in the string name one by one!
* So it's printing each character individually, with each print() call putting it on a new line.

---

