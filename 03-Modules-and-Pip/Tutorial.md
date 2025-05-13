# Day 3 - Modules and pip in Python!

A **module** is like a code library that allows you to borrow code written by someone else in your Python program. There are two types of modules in Python:

1. **Built-in Modules**  
   These modules are ready to import and use. They come bundled with the Python interpreter, so no installation is needed.  
   *Examples:* `math`, `random`, `datetime`

2. **External Modules**  
   These are created by third parties. You can install them using a package manager like `pip` or `conda`. Different versions of the same module may be available over time.

---

## 📦 The `pip` Command

- `pip` stands for **Pip Installs Packages**
- It is the **default package manager** for Python
- Used to install modules from [PyPI](https://pypi.org)
- Does **not manage environments** (for that, use `venv`, `virtualenv`, or `conda`)

🔧 Install a module using `pip`:

```
pip install pandas
```
This command downloads and installs the Pandas library in your current Python environment.

---

## What is Conda?

- Conda is a powerful package manager and environment manager, used mostly in data science.
- It comes with the Anaconda distribution, which includes Python, R, and 100+ popular data science packages.
- It can install both Python libraries and non-Python dependencies (like system libraries).

Example:
```
conda install pandas
```
This also installs Pandas but manages dependencies better, especially for data science and machine learning.

---

## What is a Dependency?

A dependency is a library or module that your Python project requires.
Example: If your code uses import pandas, then pandas is a dependency.

- Some libraries (like pandas) have their own dependencies (e.g., NumPy, dateutil).

### Analogy:
- Your code = Recipe 🍲
- Dependencies = Ingredients 🥕🍅
- pip/conda = Grocery delivery service 🛒

---

## What is an Environment Manager?
- An environment manager helps you:
- Create isolated environments for each project.
- Use different versions of packages across projects.
- Prevent dependency conflicts.

### Common Tools:
- venv (built-in in Python 3.3+)
- virtualenv (more features)
- conda (widely used in data science)

---

## Using a module in Python (Usage)
We use the import syntax to import a module in Python. Here is an example code:

python:
```
import pandas

# Read and work with a file named 'words.csv'
df = pandas.read_csv('words.csv')
print(df)  # This will display first few rows from the words.csv file
```

Similarly, we can install other modules and look into their documentation for usage instructions.
We will find ourselves doing this often in the later part of this course.

---
