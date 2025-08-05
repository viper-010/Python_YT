# Joining Sets
Sets in python more or less work in the same way as sets in mathematics. We can perform operations like union and intersection on the sets just like in mathematics.

- Any set method that ends with _update will:
  1.Modify the original set in-place.
  2.Returns:> None.
  
- The versions without _update will:
  1.Leave the original set unchanged.
  2.Return a new set with the result.

---
## I. union() and update() :
The union() and update() methods prints all items that are present in the two sets. The union() method returns a new set whereas update() method adds item into the existing set from another set.

### Example 1 - union(): 
#### joining both of them, leaving the repeated ones
```python
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
cities3= cities.union(cities2)
print(cities3)
print(cities)
```
#### Output:
```
{'Delhi', 'Kabul', 'Seoul', 'Tokyo', 'Madrid', 'Berlin'}
{'Delhi', 'Madrid', 'Berlin', 'Tokyo'}
 ```

### Example 2 - update():
#### updating the ones that are not there in A, without disturbing the other 
```python
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
cities3= cities.update(cities2)
print(cities3)
print(cities)
```
#### Output:
```
None
{'Delhi', 'Kabul', 'Tokyo', 'Seoul', 'Berlin', 'Madrid'}
```
---

## II. intersection and intersection_update() :
The intersection() and intersection_update() methods prints only items that are similar to both the sets. The intersection() method returns a new set whereas intersection_update() method updates into the existing set from another set.

### Example 1 - intersection(): 
#### common between them, original set remains same 
```python
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
cities3 = cities.intersection(cities2)
print(cities3)
print(cities)
``` 
#### Output:
```
{'Tokyo', 'Madrid'}
{'Delhi', 'Berlin', 'Tokyo', 'Madrid'}
 ```

### Example 2 - intersection_update(): 
****updates the one with common, modifies the original set**** (only common remians) 
```python
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
cities3 = cities.intersection_update(cities2)
print(cities3)
print(cities)
```
#### Output:
```
None
{'Tokyo', 'Madrid'}
```
---

## III. symmetric_difference and symmetric_difference_update() :
- ⊕ or △ : "A Δ B" is read as "A delta B" or "the symmetric difference of sets A and B".
- A Δ B = (A - B) U (B - A)
- A Δ B = (A U B) - (A ∩ B)

The symmetric_difference() and symmetric_difference_update() methods prints only items that are not similar to both the sets. The symmetric_difference() method returns a new set whereas symmetric_difference_update() method updates into the existing set from another set.

### Example 1 - symmetric_difference(): 
#### giving those that are not common in both 
```python
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
cities3 = cities.symmetric_difference(cities2)
print(cities3)
print(cities)
```
#### Output:
```
{'Seoul', 'Kabul', 'Berlin', 'Delhi'}
{'Tokyo', 'Berlin', 'Madrid', 'Delhi'}
 ```

### Example 2 - symmetric_difference_update(): 
#### updates the one that are not common in both, modifies the original set    
```python
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
cities3 = cities.symmetric_difference_update(cities2)
print(cities3)
print(cities)
```
#### Output:
```
None
{'Seoul', 'Delhi', 'Berlin', 'Kabul'}
 ```
---

## IV. difference() and difference_update() :
The difference() and difference_update() methods prints only items that are only present in the original set and not in both the sets. The difference() method returns a new set whereas difference_update() method updates into the existing set from another set.

### Example 1 - difference(): 
#### A-B gives not in B i.e actual A, original set remains same 
```python
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Seoul", "Kabul", "Delhi"}
cities3 = cities.difference(cities2)
print(cities3)
print(cities)
```
#### Output:
```
{'Tokyo', 'Madrid', 'Berlin'}
{'Tokyo', 'Madrid', 'Delhi', 'Berlin'}
 ```

### Example 2 - difference_update(): 
#### A-B gives not in B i.e actual A, modifies set A.
```python
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Seoul", "Kabul", "Delhi"}
cities3 = cities.difference_update(cities2)
print(cities3)
print(cities)
```
#### Output:
```
None
{'Tokyo', 'Madrid', 'Berlin'}
```
