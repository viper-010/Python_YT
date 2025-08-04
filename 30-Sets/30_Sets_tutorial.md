# Python Sets
Sets are unordered collection of data items. They store multiple items in a single variable. Set items are separated by commas and enclosed within curly brackets {}. Sets are unchangeable, meaning you cannot change items of the set once created. Sets do not contain duplicate items.

### Example 1
```python
info = {"Carla", 19, False, 5.9, 19}
print(info)
```
#### Output:
```
{False, 19, 5.9, 'Carla'}
 ```
Here we see that the items of set occur in random order and hence they cannot be accessed using index numbers. Also sets do not allow duplicate values.

### Example 2
```python
my_set = {1, 2, 3}

# You can add new elements
my_set.add(4)
print(my_set) 

# You can remove elements
my_set.remove(2)
print(my_set)
```
#### Output:
```
{1, 2, 3, 4}
{1, 3, 4}
```

### Example 3
```python
# This will cause an error because a list is mutable
my_set = {1, 2}
my_set.add([3, 4]) # TypeError: unhashable type: 'list'
```
#### Output:
```
Traceback (most recent call last):
  File "/mnt/sol.py", line 3, in <module>
    my_set.add([3, 4]) # TypeError: unhashable type: 'list'
    ~~~~~~~~~~^^^^^^^^
TypeError: unhashable type: 'list'
 ```
---
 ### Quick Quiz : Try to create an empty set. 
 - Check using the type() function whether the type of your variable is a set

### Example 1
```python
rohan = {}
print(type(rohan))
```
#### Output:
```
<class 'dict'>
 ```

### Example 2
```python
rohan = set()
print(type(rohan))
```
#### Output:
```
<class 'set'>
 ```
---
## Accessing set items:
 
### Using a For loop
You can access items of set using a for loop. 

### Example
```python
info = {"Carla", 19, False, 5.9}
for item in info:
    print(item)
  ```
#### Output:
```
False
Carla
19
5.9
```
