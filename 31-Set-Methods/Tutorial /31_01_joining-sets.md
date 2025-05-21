# Joining Sets
Sets in python more or less work in the same way as sets in mathematics. We can perform operations like union and intersection on the sets just like in mathematics.

---
## I. union() and update() :
The union() and update() methods prints all items that are present in the two sets. The union() method returns a new set whereas update() method adds item into the existing set from another set.

### Example 1 - union(): 
#### joining both of them, leaving the repeated ones
```python
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
cities3 = cities.union(cities2)
print(cities3)
```
#### Output:
```
{'Tokyo', 'Madrid', 'Kabul', 'Seoul', 'Berlin', 'Delhi'}
 ```

### Example 2 - 
#### update(): updating the one that are not there in that, without disturbing the other 
```python
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
cities.update(cities2)
print(cities)
```
#### Output:
```
{'Berlin', 'Madrid', 'Tokyo', 'Delhi', 'Kabul', 'Seoul'}
```
---

## II. intersection and intersection_update() :
The intersection() and intersection_update() methods prints only items that are similar to both the sets. The intersection() method returns a new set whereas intersection_update() method updates into the existing set from another set.

### Example 1 - interaction(): common between them, remains the original set 
```python
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
cities3 = cities.intersection(cities2)
print(cities3)
``` 
#### Output:
```
{'Madrid', 'Tokyo'}
 ```

### Example 2 - intersection_update(): updates the one with common, modifies the original set 
```python
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
cities.intersection_update(cities2)
print(cities)
```
#### Output:
```
{'Tokyo', 'Madrid'}
```
---

## III. symmetric_difference and symmetric_difference_update() :
The symmetric_difference() and symmetric_difference_update() methods prints only items that are not similar to both the sets. The symmetric_difference() method returns a new set whereas symmetric_difference_update() method updates into the existing set from another set.

### Example 1 - symmetric_difference(): giving those that are not common in both 
```python
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
cities3 = cities.symmetric_difference(cities2)
print(cities3)
```
#### Output:
```
{'Seoul', 'Kabul', 'Berlin', 'Delhi'}
 ```

### Example 2 - symmetric_difference_update(): updates the one that are not common in both, 
###             modifies the original set  
```python
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
cities.symmetric_difference_update(cities2)
print(cities)
```
#### Output:
```
{'Kabul', 'Delhi', 'Berlin', 'Seoul'}
 ```
---

## IV. difference() and difference_update() :
The difference() and difference_update() methods prints only items that are only present in the original set and not in both the sets. The difference() method returns a new set whereas difference_update() method updates into the existing set from another set.

### Example 1 - difference(): A-B gives not in B i.e actual A, remains the original set 
```python
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Seoul", "Kabul", "Delhi"}
cities3 = cities.difference(cities2)
print(cities3)
```
#### Output:
```
{'Tokyo', 'Madrid', 'Berlin'}
 ```

### Example 2 - difference_update(): A-B gives not in B i.e actual B, modifies set A
```python
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Seoul", "Kabul", "Delhi"}
print(cities.difference(cities2))
```
#### Output:
```
{'Tokyo', 'Berlin', 'Madrid'}
```
