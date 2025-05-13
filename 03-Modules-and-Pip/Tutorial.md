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

```bash
pip install pandas
'''bash
This command downloads and installs the Pandas library in your current Python environment.
