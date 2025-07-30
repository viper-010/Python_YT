# Python Tuples
Tuples are ordered collection of data items. They store multiple items in a single variable. Tuple items are separated by commas and enclosed within round brackets (). Tuples are unchangeable meaning we cannot alter them after creation.

---
### Example 1
```python
tuple1 = (1,2,2,3,5,4,6)
tuple2 = ("Red", "Green", "Blue")
print(tuple1)
print(tuple2)
```
#### Output:
```
(1, 2, 2, 3, 5, 4, 6)
('Red', 'Green', 'Blue')
```

### Example 2
```python
details = ("Abhijeet", 18, "FYBScIT", 9.8)
print(details)
```
#### Output:
```
('Abhijeet', 18, 'FYBScIT', 9.8)
```
---

## Special case:

### Example 1
```python
tup = (1)
print(type(tup),tup)
```
#### Output:
```
<class 'int'> 1
```

### Example 2
```python
tup = (1,)
print(type(tup),tup)
```
#### Output:
```
<class 'tuple'> (1,)
```

- When Python sees parentheses around a single item like (1), it treats them as standard mathematical parentheses for grouping expressions. It doesn't create a tuple.

Therefore, tup is simply assigned the integer 1.


- To create a tuple with only one element, you must include a trailing comma. This comma is the special syntax that tells Python you want a tuple, not just a grouped value.

Therefore, tup is assigned a tuple containing the single element 1.



