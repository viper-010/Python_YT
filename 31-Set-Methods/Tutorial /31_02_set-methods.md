# Set Methods
There are several in-built methods used for the manipulation of set. They are explained below

---
## isdisjoint() 
- **no common**
- The isdisjoint() method checks if items of given set are present in another set. This method returns False if items are present, else it returns True.

### Example
```python
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
print(cities.isdisjoint(cities2))
```
#### Output:
```
False
```
---

## issuperset() 
- **parent set**
- The issuperset() method checks if all the items of a particular set are present in the original set. It returns True if all the items are present, else it returns False.

### Example
```python
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Seoul", "Kabul"}
print(cities.issuperset(cities2))
cities3 = {"Seoul", "Madrid","Kabul"}
print(cities.issuperset(cities3))
```
#### Output:
```
False
False
```
---
## issubset()
- **child set**
- The issubset() method checks if all the items of the original set are present in the particular set. It returns True if all the items are present, else it returns False.

### Example
```python
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Delhi", "Madrid"}
print(cities2.issubset(cities))
```
#### Output:
```
True
```
---
## add()
- **only 1 argument**
- If you want to add a single item to the set use the add() method.

### Example
```python
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities.add("Helsinki")
print(cities)
```
#### Output:
```
{'Tokyo', 'Helsinki', 'Madrid', 'Berlin', 'Delhi'}
```
---
## update()
- **multiple arguments**
- **always expects an iterable** 
- If you want to add more than one item, simply create another set or any other iterable object(list, tuple, dictionary), and use the update() method to add it into the existing set.

### Example 1
```python
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Helsinki", "Warsaw", "Seoul"}
cities.update(cities2)
print(cities)
```
#### Output:
```
{'Seoul', 'Berlin', 'Delhi', 'Tokyo', 'Warsaw', 'Helsinki', 'Madrid'}
```
### Example 2
```python
set_A = {1, 2, 3}
list_B = [3, 4, 5] # Note the duplicate '3'
tuple_C = ('a', 'b')

# Update set_A with all items from list_B and tuple_C
set_A.update(list_B, tuple_C)

print(set_A)
```
#### Output:
```
{1, 2, 3, 4, 5, 'a', 'b'}
```
---

## remove()/discard()
We can use remove() and discard() methods to remove items form list.

**remove():** 
- removes the item (only 1 argument) 
- if the item is not present then throws an error 

**discard():**
- removes the item (only 1 argument)
- if the item is not present then it doesn't throws any error, gives the same original set

### Example 1
```python 
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities.remove("Tokyo")
print(cities)
```
#### Output:
```
{'Delhi', 'Berlin', 'Madrid'}
 ```

### Example 2
```python
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities.remove("Seoul")
print(cities)
```
#### Output:
```
KeyError: 'Seoul' 
```

### Example 3
```python
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities.discard("Seoul")
print(cities)
```
#### Output:
```
{'Tokyo', 'Berlin', 'Madrid', 'Delhi'}
```

---
## pop()
- Removes any random item
- Error is thrown out when there is an empty set 
- This method removes the last item of the set but the catch is that we don’t know which item gets popped as sets are unordered.
- You can access the popped item if you assign the pop() method to a variable.

### Example
```python
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
item = cities.pop()
print(cities)
print(item)
```
#### Output:
```
{'Tokyo', 'Delhi', 'Berlin'}
Madrid
```
---

## del
- del is not a method, rather it is a keyword.
- deletes the entitre set

### Example
```python
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
del cities
print(cities)
```
#### Output:
```
NameError: name 'cities' is not defined
```

We get an error because our entire set has been deleted and there is no variable called cities which contains a set.

What if we don’t want to delete the entire set, we just want to delete all items within that set?

---
## clear()
This method clears all items in the set and prints an empty set.

### Example
```python
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities.clear()
print(cities)
```
#### Output:
```
set()
```
---
## Check if item exists
You can also check if an item exists in the set or not.

### Example
```python
info = {"Carla", 19, False, 5.9}
if "Carla" in info:
    print("Carla is present.")
else:
    print("Carla is absent.")
  ```
#### Output:
```
Carla is present.
```

