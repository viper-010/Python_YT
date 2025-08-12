## Raising Custom errors 
In python, we can raise custom errors by using the `raise`  keyword. 

### Example 1
```python
salary = int(input("Enter salary amount: "))
print(salary)
if not 2000 < salary < 5000:
    raise ValueError("Not a valid salary")
```

#### Output 1: 
```
Enter salary amount: 3333
3333
```
#### Output 2:
```
Enter salary amount: 1
1
ERROR!
Traceback (most recent call last):
  File "<main.py>", line 4, in <module>
ValueError: Not a valid salary
````

****Sample Input****
``` 1 ```

****Your Output****
``` Enter salary amount: 1 ```

****Runtime Error****
``` SIGHUP ```
- SIGHUP stands for Signal Hang Up. It's not a Python error but rather a signal from the underlying operating system (like Linux).

****Error****
```
Traceback (most recent call last):
  File "/mnt/sol.py", line 4, in <module>
    raise ValueError("Not a valid salary")
ValueError: Not a valid salary
```

- Your Python code crashed by raising a ValueError.
- The platform's system detected the crash and terminated the process.
- SIGHUP is the signal that was reported as part of that termination process.

In the previous tutorial, we learned about different built-in exceptions in Python and why it is important to handle exceptions. However, sometimes we may need to create our own custom exceptions that serve our purpose.

----

## Defining Custom Exceptions
In Python, we can define custom exceptions by creating a new class that is derived from the built-in Exception class.

Here's the syntax to define custom exceptions:
```python
class CustomError(Exception):
  # code ...
  pass

try:
  # code ...

except CustomError:
  # code...
```

This is useful because sometimes we might want to do something when a particular exception is raised. For example, sending an error report to the admin, calling an api, etc.
