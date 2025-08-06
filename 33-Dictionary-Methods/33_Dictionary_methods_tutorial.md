# Dictionary Methods
Dictionary uses several built-in methods for manipulation. They are listed below

---
## update():
The update() method updates the value of the key provided to it if the item already exists in the dictionary, else it creates a new key-value pair.

### Example
```python
info = {'name':'Karan', 'age':19, 'eligible':True}
print(info)
info.update({'age':20})
info.update({'DOB':2001})
print(info)
```
#### Output:
```
{'name': 'Karan', 'age': 19, 'eligible': True}
{'name': 'Karan', 'age': 20, 'eligible': True, 'DOB': 2001}
 ```
---
## Removing items from dictionary:
There are a few methods that we can use to remove items from dictionary.

---
## clear():
The clear() method removes all the items from the list. 
### Example
```python
info = {'name':'Karan', 'age':19, 'eligible':True}
info.clear()
print(info)
```
#### Output:
```
{}
 ```
---
## pop():
The pop() method removes the key-value pair whose key is passed as a parameter.

### Example 1:
```python
info = {'name':'Karan', 'age':19, 'eligible':True}
info.pop('eligible')
print(info)
```
#### Output:
```
{'name': 'Karan', 'age': 19}
 ```
The pop() method removes an item with a specified key and returns the value of that item. This is useful when you want to remove an item but also need to use its value immediately. It also allows you to provide a default value if the key might not exist.

- ****Action****: Removes an item and returns its value.
- ****Handles Missing Keys****: Yes, you can provide a default value to avoid an error.

### Example 2:
```python
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

# pop() removes the item and gives you its value
removed_model = car.pop("model")

print(f"The removed model was: {removed_model}")
print(f"The dictionary now: {car}")

# Safely "pop" a key that doesn't exist by providing a default
color = car.pop("color", "Not Found")
print(f"The color was: {color}")
```
#### Output:
```
The removed model was: Mustang
The dictionary now: {'brand': 'Ford', 'year': 1964}
The color was: Not Found
 ```

---
## popitem(): 
The popitem() method removes the last key-value pair from the dictionary.
### Example:
```python
info = {'name':'Karan', 'age':19, 'eligible':True, 'DOB':2003}
info.popitem()
print(info)
```
#### Output:
```
{'name': 'Karan', 'age': 19, 'eligible': True}
 ```
---
## del:
we can also use the del keyword to remove a dictionary item. 

### Example 1
```python
info = {'name':'Karan', 'age':19, 'eligible':True, 'DOB':2003}
del info['age']
print(info)
```
#### Output:
```
{'name': 'Karan', 'eligible': True, 'DOB': 2003}
 ```

If key is not provided, then the del keyword will delete the dictionary entirely.

### Example 2
```python
info = {'name':'Karan', 'age':19, 'eligible':True, 'DOB':2003}
del info
print(info)
```
#### Output:
```
NameError: name 'info' is not defined
```
