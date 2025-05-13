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

## What is conda?

- conda is a powerful package manager and environment manager, used mostly in data science.
- It comes with the Anaconda distribution, which includes Python, R, and 100+ popular data science packages.
- It can install both Python libraries and non-Python dependencies (like system libraries).

Example:
```
conda install pandas
```
This also installs Pandas but manages dependencies better, especially for data science and machine learning.
