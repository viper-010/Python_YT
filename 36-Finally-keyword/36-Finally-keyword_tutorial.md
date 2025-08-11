# Finally Clause
The finally code block is also a part of exception handling. When we handle exception using the try and except block, we can include a finally block at the end. The finally block is always executed, so it is generally used for doing the concluding tasks like closing file resources or closing database connection or may be ending the program execution with a delightful message.

## Syntax:
```
try:
   #statements which could generate 
   #exception
except:
   #solution of generated exception
finally:
    #block of code which is going to 
    #execute in any situation
```

The finally block is executed irrespective of the outcome of try……except…..else blocks\
One of the important use cases of finally block is in a function which returns a value.

---
### Example:
```python
try:
    num = int(input("Enter an integer: "))
except ValueError:
    print("Number entered is not an integer.")
else:
    print("Integer Accepted.")
finally:
    print("This block is always executed.")
 ```

#### Output 1:
```
Enter an integer: 19
Integer Accepted.
This block is always executed.
```
#### Output 2:
```
Enter an integer: 3.142
Number entered is not an integer.
This block is always executed.
```

- The finally block is designed by Python to run no matter what. Its entire purpose is to execute essential "cleanup" code, and it wouldn't be very useful if a return statement could just skip it.

## The Purpose: Guaranteed Cleanup
Think about actions that must happen before a function is truly finished, regardless of success or failure. A common example is closing a file that you've opened.

If return made the function exit immediately, the file would be left open, which could lead to data corruption or resource leaks. The finally clause was created specifically to solve this problem by guaranteeing that cleanup code always runs.

## A Simple Analogy: Locking the Door
Imagine your function is a set of instructions for leaving your house.

- try: You try to grab your wallet.

- except: What you do if you can't find your wallet.

- return: Your decision to leave the house.

- finally: The one thing you must do before you go: lock the front door.

Whether you find your wallet (try) or not (except), you still have to lock the door (finally) on your way out. Python's logic works the same way: it reaches a return statement, prepares the exit value, executes the finally block, and then officially leaves the function.
