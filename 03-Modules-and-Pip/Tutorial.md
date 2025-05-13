Day 3 - Modules and pip in Python!
A module is like a code library that we can borrow from to make our Python programs more powerful. Python provides a vast number of modules to simplify programming tasks.

There are two types of modules in Python:

Built-in Modules
These modules come pre-installed with the Python interpreter. You don’t need to install them separately.
Examples: math, random, datetime

External Modules
These are created by third parties and can be installed using package managers like pip or conda. These modules are not included by default with Python and may be updated or versioned differently over time.

The pip Command
pip stands for Pip Installs Packages.

It is the default package manager for Python.

You can use it to install libraries/modules from the Python Package Index (PyPI).

pip does not manage environments — tools like venv, virtualenv, or conda are used for that.

Example – Installing Pandas:
bash
Copy
Edit
pip install pandas
What is conda?
conda is both a package manager and an environment manager, popular in data science and machine learning communities.

It comes bundled with the Anaconda distribution, which includes Python, R, and 100+ commonly used data science libraries.

It can install both Python and non-Python dependencies (e.g., system libraries like OpenBLAS or CUDA).

Example – Installing Pandas using conda:
bash
Copy
Edit
conda install pandas
This also installs Pandas, often handling complex dependencies better than pip.

🔗 What is a Dependency?
A dependency is any library or module that your code needs to function correctly.

Example: If your script uses import pandas, then pandas is a dependency.
Pandas itself depends on other libraries like NumPy and dateutil — those are its dependencies.

🧠 Analogy
Your code = Recipe 🍲

Dependencies = Ingredients 🥕🍅

pip/conda = Grocery Delivery Services 🛒

They bring all the packages (ingredients) needed to cook (run) your code!

What is an Environment Manager?
An environment manager allows you to:

Create isolated environments for each project.

Use different versions of the same library for different projects.

Avoid dependency conflicts.

🔧 Common Environment Tools
venv (built-in from Python 3.3+)

virtualenv (third-party tool with more features)

conda (popular in the data science ecosystem)

Using a Module in Python (Usage)
We use the import statement to include a module in our Python script. Here's a simple example:

python
Copy
Edit
import pandas

# Read and work with a file named 'words.csv'
df = pandas.read_csv('words.csv')
print(df)  # This will display the contents of words.csv
You can explore module documentation to understand functions, classes, and usage patterns.

We will be doing this frequently as we progress through the course!

