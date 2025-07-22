# break statement
The break statement enables a program to skip over a part of the code. A break statement terminates the very loop it lies within.

### Example

```python '
for i in range(1,101,1):
    print(i ,end=" ")
    if(i==50):
        break
    else:
        print("Mississippi")
print("Thank you")
```
#### Output:
```
1 Mississippi
2 Mississippi
3 Mississippi
4 Mississippi
5 Mississippi
.
.
.
49 Mississippi
50 Thank you
```
