# List Methods
---
## list.sort()
This method sorts the list in ascending order. The original list is updated

### Example 1
```python
colors = ["voilet", "indigo", "blue", "green"]
colors.sort()
print(colors)

num = [4,2,5,3,6,1,2,1,2,8,9,7]
num.sort()
print(num)
```
#### Output:
```
['blue', 'green', 'indigo', 'voilet']
[1, 1, 2, 2, 2, 3, 4, 5, 6, 7, 8, 9]
```
What if you want to print the list in descending order?
We must give reverse=True as a parameter in the sort method.

### Example 2
```python
colors = ["voilet", "indigo", "blue", "green"]
colors.sort(reverse=True)
print(colors)

num = [4,2,5,3,6,1,2,1,2,8,9,7]
num.sort(reverse=True)
print(num)
```
#### Output:
```
['voilet', 'indigo', 'green', 'blue']
[9, 8, 7, 6, 5, 4, 3, 2, 2, 2, 1, 1]
 ```

- The reverse parameter is set to False by default, This is the exact same result you would get from just calling r.sort() with no arguments.

**Note**: Do not mistake the reverse parameter with the reverse method.

---
## reverse()
This method reverses the order of the list. 

### Example
```python
colors = ["voilet", "indigo", "blue", "green"]
colors.reverse()
print(colors)

num = [4,2,5,3,6,1,2,1,2,8,9,7]
num.reverse()
print(num)
```
#### Output:
```
['green', 'blue', 'indigo', 'voilet']
[7, 9, 8, 2, 1, 2, 1, 6, 3, 5, 2, 4]
 ```
---

## index()
This method returns the index of the first occurrence of the list item.
### Example
```python
colors = ["voilet", "green", "indigo", "blue", "green"]
print(colors.index("green"))

num = [4,2,5,3,6,1,2,1,3,2,8,9,7]
print(num.index(3))
```
#### Output:
```
1
3
 ```
---

## count()
Returns the count of the number of items with the given value.
### Example
```python
colors = ["voilet", "green", "indigo", "blue", "green"]
print(colors.count("green"))

num = [4,2,5,3,6,1,2,1,3,2,8,9,7]
print(num.count(2))
```
#### Output:
```
2
3
 ```
---

## copy()
- Returns copy of the list. This can be done to perform operations on the list without modifying the original list. 
- The .copy() method creates a brand new, separate list in memory. It's a true copy.
  
- In this case, colors and newlist would be two completely independent lists. Modifying the original colors list would have no effect on newlist.

### Example 1
```python
colors = ["voilet", "green", "indigo", "blue"]
newlist = colors.copy()
print(colors)
colors.append("red")
print(newlist)
print(colors)
```
#### Output:
```
['voilet', 'green', 'indigo', 'blue']
['voilet', 'green', 'indigo', 'blue']
['voilet', 'green', 'indigo', 'blue', 'red']
```

### Example 2
- What if we are not using copy()
- In this program, newlist = colors does not create a new list. It just makes the variable newlist point to the exact same list object in memory as colors.
- Because both variables refer to the same list, when you modify the list using one variable (like colors.append("red")), the change is visible through both.
  
```python
colors = ["voilet", "green", "indigo", "blue"]
newlist = colors
print(colors)
colors.append("red")
print(newlist)
print(colors)
```
#### Output:
```
['voilet', 'green', 'indigo', 'blue']
['voilet', 'green', 'indigo', 'blue', 'red']
['voilet', 'green', 'indigo', 'blue', 'red']
```
  
---

## append():
This method appends items to the end of the existing list.

### Example 1
```python
colors = ["voilet", "indigo", "blue"]
colors.append("green")
print(colors)
```
#### Output:
```
['voilet', 'indigo', 'blue', 'green']
 ```

- If you try to append() a list of multiple items, the entire list itself will be added as a single nested element
- Adds its argument as a single element
  
### Example 2
```python
list_a = [1]
list_a.append([2, 3, 4])
print(f"Using append: {list_a}")
```
#### Output:
```
Using append: [1, [2, 3, 4]]
```

- The single argument you are passing to append() is the list [2]
- Doesn't look inside the argument you give it. It just takes the entire object
  
### Example 3
```python
list_b = [1]
list_b.append([2])
print(f"Using extend: {list_b}")
```
#### Output:
```
Using append: [1, [2]]
```
---

## insert():
This method inserts an item at the given index. User has to specify index and the item to be inserted within the insert() method.

### Example
```python
colors = ["voilet", "indigo", "blue"]
#           [0]        [1]      [2]

colors.insert(1, "green")   #inserts item at index 1
# updated list: colors = ["voilet", "green", "indigo", "blue"]
#       indexs              [0]       [1]       [2]      [3]

print(colors)
```
#### Output:
```
['voilet', 'green', 'indigo', 'blue']
 ```
---

## extend():
This method adds an entire list or any other collection datatype (set, tuple, dictionary) to the existing list.

### Example
```python
#add a list to a list
colors = ["voilet", "indigo", "blue"]
rainbow = ["green", "yellow", "orange", "red"]
colors.extend(rainbow)
print(colors)
```
#### Output:
```
['voilet', 'indigo', 'blue', 'green', 'yellow', 'orange', 'red']
 ```
---
## Concatenating two lists
You can simply concatenate two lists to join two lists.

### Example
```python
colors = ["voilet", "indigo", "blue", "green"]
colors2 = ["yellow", "orange", "red"]
print(colors + colors2)
```
#### Output:
```
['voilet', 'indigo', 'blue', 'green', 'yellow', 'orange', 'red']
```
