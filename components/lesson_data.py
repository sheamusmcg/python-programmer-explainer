"""Lesson catalog for the Python Programmer Explainer."""

from __future__ import annotations


LESSONS = [
    {
        "id": 1,
        "slug": "introduction",
        "title": "Introduction: Variables, Printing, and Types",
        "short_title": "Introduction",
        "icon": ":material/waving_hand:",
        "page": "pages/01_introduction.py",
        "source_notebook": "lesson_1_introduction.ipynb",
        "colab_url": "https://colab.research.google.com/drive/1ufloJqo7hWJNmh7fBPOSlSnB-0v2a9OK",
        "objective": "Store information in variables, print it, and inspect basic Python types.",
        "why_it_matters": (
            "Everything else in Python builds on this lesson. Variables let you name values, "
            "printing lets you see what your program is doing, and types explain why Python "
            "treats text, numbers, and true-or-false values differently."
        ),
        "notebook_summary": (
            "The notebook starts with variables and a hello-world style print workflow, then "
            "moves into Python's native data types, `type()` and `isinstance()`, variable naming "
            "rules, naming conventions, and a first look at common beginner errors."
        ),
        "key_topics": [
            "Variables and assignment",
            "Printing values",
            "Strings, integers, floats, and booleans",
            "`type()` and `isinstance()`",
            "Readable variable names",
            "Common syntax and runtime errors",
        ],
        "concept": (
            "A Python program starts with values. You give values names with variables, "
            "then use those names later in calculations, messages, conditions, and functions. "
            "Python figures out the type from the value you assign, which is why the same "
            "assignment pattern can hold text, numbers, decimals, or true-or-false values. "
            "Once a value has a good name, the rest of your code becomes easier to read."
        ),
        "mental_model": (
            "Think of a variable as a labeled box. The label is the variable name, and "
            "the thing inside the box is the current value. When you assign a new value to "
            "the same name, you are replacing what is in the box, not creating a permanent "
            "fact about the program."
        ),
        "example_title": "A tiny student profile",
        "example_code": """name = "Alice"
age = 30
is_student = True

print("Name:", name)
print("Age:", age)
print("Student:", is_student)
print("The age variable is a", type(age))""",
        "walkthrough": [
            "`name`, `age`, and `is_student` are variables.",
            "Strings use quotes, integers are whole numbers, and booleans are `True` or `False`.",
            "`print()` sends values to the output area.",
            "`type()` lets you ask Python what kind of value you have.",
        ],
        "challenge": {
            "title": "Make your own profile card",
            "prompt": (
                "Create variables named `name`, `age`, and `is_student`. Then print three "
                "readable lines that include those values."
            ),
            "starter_code": """name = "Ada"
age = 36
is_student = True

# Print a short profile using the variables above.
""",
            "hints": [
                "Use `print()` once for each line.",
                "A line like `print(\"Name:\", name)` prints a label and the variable value.",
                "`is_student` should contain the boolean value `True` or `False`, not the string \"True\".",
            ],
            "solution": """name = "Ada"
age = 36
is_student = True

print("Name:", name)
print("Age:", age)
print("Student:", is_student)""",
            "checks": [
                {"type": "name_exists", "name": "name"},
                {"type": "name_exists", "name": "age"},
                {"type": "namespace_type", "name": "is_student", "expected_type": "bool"},
                {"type": "output_contains", "text": "Name:"},
                {"type": "output_contains", "text": "Age:"},
            ],
        },
        "deep_dive": [
            "Run the original variable and printing cells.",
            "Change the example values and rerun the notebook cells.",
            "Use `type()` on every variable you create.",
        ],
    },
    {
        "id": 2,
        "slug": "operators",
        "title": "Operators: Math, Comparisons, and Logic",
        "short_title": "Operators",
        "icon": ":material/calculate:",
        "page": "pages/02_operators.py",
        "source_notebook": "lessson-2-operators.ipynb",
        "colab_url": "https://colab.research.google.com/drive/1TyDIX44rqhlMRrSmlDrz8-fWQnh3iq-1",
        "objective": "Use operators to calculate values, compare results, and combine conditions.",
        "why_it_matters": (
            "Operators are how programs turn stored values into useful answers. They let you "
            "calculate totals, compare outcomes, update counters, and build the conditions that "
            "later drive `if` statements and loops."
        ),
        "notebook_summary": (
            "The notebook introduces arithmetic operators, floor division, modulo, logical "
            "operators, compound assignment, identity checks with `is`, membership checks with "
            "`in`, and how different data types behave with different operations."
        ),
        "key_topics": [
            "Arithmetic operators",
            "Floor division and modulo",
            "Comparison and logical operators",
            "Compound assignment",
            "Identity and membership operators",
            "Operator behavior across data types",
        ],
        "concept": (
            "Operators are the symbols and keywords that make Python do work: arithmetic "
            "operators calculate, comparison operators return booleans, and logical "
            "operators combine booleans into bigger decisions. These small expressions are "
            "the building blocks for larger program behavior, from calculating totals to "
            "deciding whether a user has met a requirement."
        ),
        "mental_model": (
            "An operator is a small action word. `+` says add, `>` says compare, and "
            "`and` says both conditions must be true. Read an expression like a tiny sentence: "
            "`score >= 70 and completed_project` means the score condition and the project "
            "condition both need to hold."
        ),
        "example_title": "A budget check",
        "example_code": """price = 45
tax = 4.50
budget = 60

total = price + tax
can_buy = total <= budget

print("Total:", total)
print("Within budget:", can_buy)
print("Need discount:", total > budget)""",
        "walkthrough": [
            "`price + tax` uses arithmetic to calculate a new number.",
            "`total <= budget` compares two values and returns a boolean.",
            "The boolean result can drive later decisions in your program.",
        ],
        "challenge": {
            "title": "Check whether a learner passed",
            "prompt": (
                "Create a variable named `passed`. It should be `True` only when `score` "
                "is at least 70 and `completed_project` is `True`. Print the result."
            ),
            "starter_code": """score = 82
completed_project = True

# Create a boolean named passed.

print("Passed:", passed)
""",
            "hints": [
                "Use `>=` to check whether the score is high enough.",
                "Use `and` to require both conditions.",
                "The final expression can be assigned directly to `passed`.",
            ],
            "solution": """score = 82
completed_project = True

passed = score >= 70 and completed_project

print("Passed:", passed)""",
            "checks": [
                {"type": "name_exists", "name": "passed"},
                {"type": "expr_equals", "expr": "passed", "value": True},
                {"type": "output_contains", "text": "Passed:"},
            ],
        },
        "deep_dive": [
            "Try arithmetic, comparison, logical, and compound assignment operators.",
            "Change the score and project values to see the boolean flip.",
            "Explain in your own words why `and` is different from `or`.",
        ],
    },
    {
        "id": 3,
        "slug": "control-structures",
        "title": "Control Structures: If Statements and Loops",
        "short_title": "Control Structures",
        "icon": ":material/account_tree:",
        "page": "pages/03_control_structures.py",
        "source_notebook": "lesson_3_control_structures.ipynb",
        "colab_url": "https://colab.research.google.com/drive/1piL7cU3GZqXI_8CqFXuhKD8soraltDp_",
        "objective": "Control what runs, when it runs, and how many times it runs.",
        "why_it_matters": (
            "Without control structures, code only runs from top to bottom once. This lesson "
            "is where programs start to feel intelligent: they can choose a path, repeat work, "
            "stop early, and respond to changing values."
        ),
        "notebook_summary": (
            "The notebook covers `if`, `elif`, and `else`, explains why indentation matters in "
            "Python, then introduces `for` loops, `range()`, `break`, `while` loops, and the "
            "logic behind repeated execution."
        ),
        "key_topics": [
            "`if`, `elif`, and `else`",
            "Indentation and code blocks",
            "`for` loops",
            "`range()`",
            "`break`",
            "`while` loops",
        ],
        "concept": (
            "Control structures let your code make decisions and repeat work. `if`, `elif`, "
            "and `else` choose a path. `for` and `while` loops repeat a block of code. "
            "The important shift is that your program no longer does exactly the same thing "
            "every time; it reacts to data, conditions, and repeated collections."
        ),
        "mental_model": (
            "A control structure is a fork or loop in the road. Indentation tells Python "
            "which instructions belong to that road. If the condition is true, Python takes "
            "one branch. If a loop still has values left, Python circles back and runs the "
            "indented block again."
        ),
        "example_title": "Classify scores",
        "example_code": """scores = [92, 67, 81, 74]

for score in scores:
    if score >= 90:
        print(score, "excellent")
    elif score >= 70:
        print(score, "passing")
    else:
        print(score, "needs practice")""",
        "walkthrough": [
            "`for score in scores` visits each number in the list.",
            "The indented lines run once per score.",
            "The `if` / `elif` / `else` chain chooses exactly one message.",
        ],
        "challenge": {
            "title": "Count warm days",
            "prompt": (
                "Loop through `temperatures` and count how many days are at least 75 degrees. "
                "Store the count in `warm_days` and print it."
            ),
            "starter_code": """temperatures = [72, 81, 68, 77, 90, 65]
warm_days = 0

# Loop through temperatures and update warm_days.

print("Warm days:", warm_days)
""",
            "hints": [
                "Use a `for temperature in temperatures:` loop.",
                "Inside the loop, use an `if` statement.",
                "Increase the counter with `warm_days += 1`.",
            ],
            "solution": """temperatures = [72, 81, 68, 77, 90, 65]
warm_days = 0

for temperature in temperatures:
    if temperature >= 75:
        warm_days += 1

print("Warm days:", warm_days)""",
            "checks": [
                {"type": "expr_equals", "expr": "warm_days", "value": 3},
                {"type": "output_contains", "text": "Warm days:"},
            ],
        },
        "deep_dive": [
            "Run the intentional error cells so indentation errors become familiar.",
            "Rewrite one `if` example with different threshold values.",
            "Trace a loop by writing down the variable value after each pass.",
        ],
    },
    {
        "id": 4,
        "slug": "data-structures",
        "title": "Data Structures: Lists, Dictionaries, Tuples, and Sets",
        "short_title": "Data Structures",
        "icon": ":material/data_object:",
        "page": "pages/04_data_structures.py",
        "source_notebook": "Lesson_4_data_structures.ipynb",
        "colab_url": "https://colab.research.google.com/drive/1SlA4PPB3IuD-ISgRaUs7DZuETgpx0ARF",
        "objective": "Choose containers that match the kind of data you need to organize.",
        "why_it_matters": (
            "Real programs rarely work with one value at a time. Data structures let you keep "
            "related values together, retrieve the right item, update collections, and model "
            "records that are more useful than loose variables."
        ),
        "notebook_summary": (
            "The notebook introduces Python's core containers: lists, tuples, sets, and "
            "dictionaries. It spends extra time on list syntax, zero indexing, list methods, "
            "tuple immutability, and the idea that methods are functions attached to objects."
        ),
        "key_topics": [
            "Lists and indexing",
            "List methods such as `append()` and `sort()`",
            "Zero indexing",
            "Tuples and immutability",
            "Sets and uniqueness",
            "Dictionaries and key-value lookup",
        ],
        "concept": (
            "Data structures hold collections of values. Lists keep ordered items, dictionaries "
            "map keys to values, tuples protect fixed records, and sets keep unique items. "
            "Choosing the right structure helps your code say what kind of collection you "
            "mean, instead of forcing every problem into a pile of separate variables."
        ),
        "mental_model": (
            "A list is a row of numbered slots. A dictionary is a label maker. A set is a "
            "deduplicator. A tuple is a record you do not plan to change. When you ask for "
            "`students[0]`, you are using position; when you ask for `scores['Ada']`, you "
            "are using a meaningful key."
        ),
        "example_title": "Track a small course roster",
        "example_code": """students = ["Ada", "Grace", "Linus"]
scores = {"Ada": 95, "Grace": 88, "Linus": 91}
unique_scores = set(scores.values())

students.append("Guido")
scores["Guido"] = 90

print("First student:", students[0])
print("Grace score:", scores["Grace"])
print("Unique scores:", sorted(unique_scores))""",
        "walkthrough": [
            "List indexes start at 0, so `students[0]` gets the first item.",
            "Dictionary lookups use keys, such as `scores[\"Grace\"]`.",
            "`set()` removes duplicates from a collection.",
        ],
        "challenge": {
            "title": "Build a tiny inventory",
            "prompt": (
                "Create a dictionary named `inventory` with `apples`, `bananas`, and `oranges`. "
                "Add 2 apples, then print the final apple count."
            ),
            "starter_code": """inventory = {
    "apples": 4,
    "bananas": 6,
    "oranges": 3,
}

# Add 2 apples.

print("Apples:", inventory["apples"])
""",
            "hints": [
                "Use the key `\"apples\"` to access that value.",
                "You can update the value with `inventory[\"apples\"] += 2`.",
                "The final apple count should be 6.",
            ],
            "solution": """inventory = {
    "apples": 4,
    "bananas": 6,
    "oranges": 3,
}

inventory["apples"] += 2

print("Apples:", inventory["apples"])""",
            "checks": [
                {"type": "expr_equals", "expr": "inventory['apples']", "value": 6},
                {"type": "output_contains", "text": "Apples:"},
            ],
        },
        "deep_dive": [
            "Practice list indexing and list methods.",
            "Build a dictionary and retrieve values by key.",
            "Compare what happens when you put duplicate values in a list versus a set.",
        ],
    },
    {
        "id": 5,
        "slug": "functions",
        "title": "Functions: Reusable Recipes",
        "short_title": "Functions",
        "icon": ":material/function:",
        "page": "pages/05_functions.py",
        "source_notebook": "Lesson_5_Functions.ipynb",
        "colab_url": "https://colab.research.google.com/drive/1VI5cOsXYDBrLPx2RTZdpdtixVtl-GdmI",
        "objective": "Write reusable functions with parameters, return values, and default arguments.",
        "why_it_matters": (
            "Functions are the first big step from writing individual lines of code to designing "
            "programs. They help you avoid repetition, name a task clearly, test one piece at a "
            "time, and reuse logic with different inputs."
        ),
        "notebook_summary": (
            "The notebook builds from a `calculate_average` function into arguments, return "
            "values, positional and keyword arguments, default arguments, built-in functions, "
            "and a larger exercise that combines variables, lists, functions, and conditionals "
            "to analyze weekly temperatures."
        ),
        "key_topics": [
            "`def` and function bodies",
            "Parameters and arguments",
            "`return` values",
            "Positional and keyword arguments",
            "Default arguments",
            "Built-in functions",
        ],
        "concept": (
            "A function packages a task so you can run it again with different inputs. "
            "Parameters receive input values, the body does the work, and `return` sends "
            "a result back to the caller. Good functions also make programs easier to read "
            "because the function name explains the purpose of several lines of code at once."
        ),
        "mental_model": (
            "A function is a recipe card. The parameters are ingredients, the body is the "
            "instructions, and the return value is the finished dish. Calling the function "
            "is like using the recipe with a specific set of ingredients; the same recipe can "
            "produce a result for many different inputs."
        ),
        "example_title": "Calculate an average",
        "example_code": """def calculate_average(numbers):
    total = sum(numbers)
    count = len(numbers)
    return total / count

temperatures = [72, 75, 79, 68]
average_temperature = calculate_average(temperatures)

print("Average:", average_temperature)""",
        "walkthrough": [
            "`def` starts a function definition.",
            "`numbers` is a parameter that receives the list you pass in.",
            "`return` gives the calculated result back to the rest of the program.",
        ],
        "challenge": {
            "title": "Write a discount function",
            "prompt": (
                "Define a function named `apply_discount(price, percent)`. It should return "
                "the price after removing the discount percentage."
            ),
            "starter_code": """def apply_discount(price, percent):
    # Return the discounted price.
    pass

final_price = apply_discount(100, 20)
print("Final price:", final_price)
""",
            "hints": [
                "A 20 percent discount means the customer pays 80 percent.",
                "Convert the percentage to a decimal with `percent / 100`.",
                "One formula is `price * (1 - percent / 100)`.",
            ],
            "solution": """def apply_discount(price, percent):
    return price * (1 - percent / 100)

final_price = apply_discount(100, 20)
print("Final price:", final_price)""",
            "checks": [
                {"type": "expr_equals", "expr": "apply_discount(100, 20)", "value": 80.0},
                {"type": "expr_equals", "expr": "apply_discount(50, 10)", "value": 45.0},
                {"type": "output_contains", "text": "Final price:"},
            ],
        },
        "deep_dive": [
            "Run the average-temperature examples from the notebook.",
            "Try positional arguments, keyword arguments, and default arguments.",
            "Write one function that calls another function.",
        ],
    },
    {
        "id": 6,
        "slug": "modules-and-libraries",
        "title": "Modules and Libraries: Importing More Power",
        "short_title": "Modules",
        "icon": ":material/extension:",
        "page": "pages/06_modules_and_libraries.py",
        "source_notebook": "Lesson_6_modules_and_libraries.ipynb",
        "colab_url": "https://colab.research.google.com/drive/1-kBACCtaplXo_q-T_E26R1gU9ADvld94",
        "objective": "Import standard-library modules and call functions from them.",
        "why_it_matters": (
            "Python becomes much more powerful when you stop writing everything from scratch. "
            "Modules and libraries let you reuse reliable tools, organize your own code, and "
            "understand how larger Python projects are assembled."
        ),
        "notebook_summary": (
            "The notebook frames modules as code reuse, then walks through importing `math`, "
            "dot notation, aliases with `as`, importing specific functions, namespace tradeoffs, "
            "and file I/O concepts that prepare you to work outside a single notebook."
        ),
        "key_topics": [
            "Code reuse",
            "`import module`",
            "Dot notation",
            "Module aliases",
            "`from module import name`",
            "Namespaces and file I/O",
        ],
        "concept": (
            "A module is a Python file full of reusable code. A library is a collection of "
            "modules. `import` lets your program use code someone else already wrote. "
            "Dot notation, such as `math.sqrt`, keeps it clear which module a function or "
            "constant came from."
        ),
        "mental_model": (
            "Importing is like checking out a tool from a toolbox. Once the tool is on your "
            "bench, you can call it by name. If you import the whole toolbox, you reach into "
            "it with dot notation; if you import one specific tool, you can use that tool "
            "directly."
        ),
        "example_title": "Use the math module",
        "example_code": """import math

radius = 3
area = math.pi * radius ** 2
root = math.sqrt(25)

print("Area:", round(area, 2))
print("Square root:", root)""",
        "walkthrough": [
            "`import math` loads the standard `math` module.",
            "`math.pi` accesses a constant from that module.",
            "`math.sqrt()` calls a function from that module.",
        ],
        "challenge": {
            "title": "Calculate a circle area",
            "prompt": (
                "Import `math`, define `circle_area(radius)`, and return the area of a circle. "
                "Use `math.pi` and exponentiation."
            ),
            "starter_code": """# Import the module you need.

def circle_area(radius):
    # Return the circle area.
    pass

print("Area:", round(circle_area(2), 2))
""",
            "hints": [
                "The area formula is pi times radius squared.",
                "Use `import math` at the top.",
                "The exponent operator is `**`.",
            ],
            "solution": """import math

def circle_area(radius):
    return math.pi * radius ** 2

print("Area:", round(circle_area(2), 2))""",
            "checks": [
                {"type": "expr_close", "expr": "circle_area(2)", "value": 12.566370614359172, "tolerance": 0.001},
                {"type": "expr_close", "expr": "circle_area(5)", "value": 78.53981633974483, "tolerance": 0.001},
                {"type": "output_contains", "text": "Area:"},
            ],
        },
        "deep_dive": [
            "Use `math.sqrt`, `math.pi`, and other module members.",
            "Practice `import module` versus `from module import name`.",
            "Look for one standard-library module that would help a daily task.",
        ],
    },
    {
        "id": 7,
        "slug": "objects",
        "title": "Objects and Classes: Modeling Things",
        "short_title": "Objects",
        "icon": ":material/category:",
        "page": "pages/07_objects.py",
        "source_notebook": "Lesson_7_0bjects.ipynb",
        "colab_url": "https://colab.research.google.com/drive/1XbrQHF9IDd3K3LDsBlv9C-rKX9USkrA8",
        "objective": "Create classes with attributes and methods.",
        "why_it_matters": (
            "Objects help you model things that have both data and behavior. Once programs get "
            "bigger, classes give you a way to keep related details and actions together instead "
            "of scattering them across unrelated variables and functions."
        ),
        "notebook_summary": (
            "The notebook introduces classes through a `Car` example, then explains instances, "
            "attributes, methods, `__init__`, `self`, class methods versus functions, core OOP "
            "principles, inheritance, child classes, and `super()`."
        ),
        "key_topics": [
            "Classes and instances",
            "Attributes",
            "Methods",
            "`__init__`",
            "`self`",
            "Inheritance and `super()`",
        ],
        "concept": (
            "A class is a blueprint for creating objects. Objects bundle data and behavior: "
            "attributes store state, and methods define what the object can do. This is useful "
            "when a thing in your program has details you need to remember and actions you "
            "want it to perform."
        ),
        "mental_model": (
            "A class is the cookie cutter. Each object is one cookie made from that cutter, "
            "with its own details. The class defines what every object can have and do, while "
            "each instance carries its own values, like one car's make, model, year, and speed."
        ),
        "example_title": "A simple Car class",
        "example_code": """class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def get_info(self):
        return f"{self.year} {self.make} {self.model}"

car = Car("Toyota", "Corolla", 2020)
print(car.get_info())""",
        "walkthrough": [
            "`__init__` runs when a new object is created.",
            "`self` means this specific object.",
            "Attributes like `self.make` store object-specific data.",
            "Methods are functions that live inside a class.",
        ],
        "challenge": {
            "title": "Create a Book class",
            "prompt": (
                "Define a `Book` class with `title`, `author`, and `pages`. Add a method "
                "`summary()` that returns a readable sentence."
            ),
            "starter_code": """class Book:
    def __init__(self, title, author, pages):
        # Store the attributes.
        pass

    def summary(self):
        # Return a sentence that includes title, author, and pages.
        pass

book = Book("Python Basics", "Ada", 120)
print(book.summary())
""",
            "hints": [
                "Store each input as `self.title`, `self.author`, and `self.pages`.",
                "Use an f-string in `summary()`.",
                "The method should return a string instead of printing directly.",
            ],
            "solution": """class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def summary(self):
        return f"{self.title} by {self.author} has {self.pages} pages."

book = Book("Python Basics", "Ada", 120)
print(book.summary())""",
            "checks": [
                {"type": "name_exists", "name": "Book"},
                {"type": "output_contains", "text": "Python Basics"},
                {"type": "expr_contains", "expr": "Book('Deep Python', 'Grace', 240).summary()", "text": "Deep Python"},
                {"type": "expr_contains", "expr": "Book('Deep Python', 'Grace', 240).summary()", "text": "Grace"},
                {"type": "expr_contains", "expr": "Book('Deep Python', 'Grace', 240).summary()", "text": "240"},
            ],
        },
        "deep_dive": [
            "Run the notebook's Car examples.",
            "Add a method that changes an object's state.",
            "Compare attributes with methods in your own words.",
        ],
    },
    {
        "id": 8,
        "slug": "try-except",
        "title": "Try / Except: Handling Errors Gracefully",
        "short_title": "Try / Except",
        "icon": ":material/report:",
        "page": "pages/08_try_except.py",
        "source_notebook": "Lesson_8_try.ipynb",
        "colab_url": "https://colab.research.google.com/drive/1ol4qJewLT7VESzlIDLSWfMrpP8w03Kob",
        "objective": "Use exceptions to recover from predictable problems.",
        "why_it_matters": (
            "Errors are normal in real programs. Exception handling lets you turn a crash into "
            "a helpful response, especially when input, files, calculations, or external data "
            "do not behave the way you expected."
        ),
        "notebook_summary": (
            "The notebook explains what exceptions are, shows intentional failing cells, then "
            "introduces `try` and `except`, handling `ZeroDivisionError`, catching additional "
            "error types, `finally`, user input with `input()`, and a brief move into external "
            "libraries with pandas."
        ),
        "key_topics": [
            "Exceptions",
            "`try` and `except`",
            "Specific error types",
            "`finally`",
            "User input",
            "External libraries",
        ],
        "concept": (
            "Exceptions are Python's way of saying something went wrong while the program "
            "was running. `try` lets you attempt risky code, and `except` lets you respond "
            "without crashing the whole program. The goal is not to hide errors; it is to "
            "handle expected problems in a way that keeps the user and the program oriented."
        ),
        "mental_model": (
            "A `try` block is a safety mat. You still attempt the move, but you have a plan "
            "for what happens if it fails. The `except` block is that plan: it catches a "
            "specific kind of fall and lets the program recover or explain the problem."
        ),
        "example_title": "Avoid division crashes",
        "example_code": """def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Cannot divide by zero"

print(safe_divide(10, 2))
print(safe_divide(10, 0))""",
        "walkthrough": [
            "The risky division happens inside `try`.",
            "If `b` is zero, Python raises `ZeroDivisionError`.",
            "The `except` block catches that specific error and returns a helpful message.",
        ],
        "challenge": {
            "title": "Parse an integer safely",
            "prompt": (
                "Define `parse_age(text)`. It should return an integer when possible and "
                "return `None` when the text cannot be converted."
            ),
            "starter_code": """def parse_age(text):
    # Try converting text to an integer.
    pass

print(parse_age("42"))
print(parse_age("not a number"))
""",
            "hints": [
                "The conversion function is `int(text)`.",
                "Invalid text raises `ValueError`.",
                "Return `None` from the `except ValueError:` block.",
            ],
            "solution": """def parse_age(text):
    try:
        return int(text)
    except ValueError:
        return None

print(parse_age("42"))
print(parse_age("not a number"))""",
            "checks": [
                {"type": "expr_equals", "expr": "parse_age('42')", "value": 42},
                {"type": "expr_equals", "expr": "parse_age('not a number')", "value": None},
                {"type": "output_contains", "text": "42"},
            ],
        },
        "deep_dive": [
            "Run the notebook cells that intentionally fail.",
            "Catch `ZeroDivisionError` and `ValueError` separately.",
            "Write a helpful message for a user instead of showing a stack trace.",
        ],
    },
    {
        "id": 9,
        "slug": "pythonic-code",
        "title": "Pythonic Code: Clear, Compact, and Readable",
        "short_title": "Pythonic Code",
        "icon": ":material/auto_fix_high:",
        "page": "pages/09_pythonic_code.py",
        "source_notebook": "Lesson_9_pythonic_code.ipynb",
        "colab_url": "https://colab.research.google.com/drive/1-CPoSm2nETBUOokDJH_k5l5RVNi8XSD4",
        "objective": "Rewrite common patterns using idiomatic Python.",
        "why_it_matters": (
            "Once you can write Python that works, the next step is writing Python other people "
            "can read quickly. Pythonic code is not about being clever; it is about using the "
            "language's common patterns to make intent easier to see."
        ),
        "notebook_summary": (
            "The notebook revisits earlier skills and rewrites them in a more idiomatic style. "
            "It covers list comprehensions, dictionary comprehensions, when not to compress a "
            "loop, f-strings, formatting numbers, and nested data structures such as lists of "
            "dictionaries and dictionaries of lists."
        ),
        "key_topics": [
            "List comprehensions",
            "Dictionary comprehensions",
            "Readable loops versus compact code",
            "f-strings",
            "Number formatting",
            "Nested data structures",
        ],
        "concept": (
            "Pythonic code is code that uses Python's strengths: direct loops, clear names, "
            "list comprehensions, dictionary comprehensions, unpacking, and built-in tools. "
            "It is not about making code shorter at all costs; it is about making the intent "
            "more obvious to someone who reads Python regularly."
        ),
        "mental_model": (
            "Pythonic code usually says the idea directly. It removes ceremony so the useful "
            "part is easier to see. A list comprehension, for example, reads like `make this "
            "new value for each old value`, which matches the shape of the idea."
        ),
        "example_title": "Replace a loop with a comprehension",
        "example_code": """numbers = [1, 2, 3, 4, 5]

squares = [number * number for number in numbers]
even_squares = [square for square in squares if square % 2 == 0]

print("Squares:", squares)
print("Even squares:", even_squares)""",
        "walkthrough": [
            "A list comprehension creates a new list in one expression.",
            "The first part says what to keep or transform.",
            "The `for` part says where values come from.",
            "The optional `if` part filters values.",
        ],
        "challenge": {
            "title": "Make clean city names",
            "prompt": (
                "Use a list comprehension to create `clean_cities`, where each city name is "
                "title-cased and blank strings are removed."
            ),
            "starter_code": """cities = ["new york", "", "san francisco", "boston", ""]

# Create clean_cities with a list comprehension.

print(clean_cities)
""",
            "hints": [
                "Use `.title()` to title-case a string.",
                "Use `if city` at the end of the comprehension to skip blank strings.",
                "The result should contain three city names.",
            ],
            "solution": """cities = ["new york", "", "san francisco", "boston", ""]

clean_cities = [city.title() for city in cities if city]

print(clean_cities)""",
            "checks": [
                {"type": "expr_equals", "expr": "clean_cities", "value": ["New York", "San Francisco", "Boston"]},
                {"type": "output_contains", "text": "New York"},
            ],
        },
        "deep_dive": [
            "Rewrite a loop as a list comprehension.",
            "Try a dictionary comprehension.",
            "Ask whether the shorter version is also clearer; if not, keep the loop.",
        ],
    },
    {
        "id": 10,
        "slug": "json-apis-environments",
        "title": "JSON, APIs, and Environments",
        "short_title": "JSON and APIs",
        "icon": ":material/api:",
        "page": "pages/10_json_apis_and_environments.py",
        "source_notebook": "Lesson_10_json_apis_and_environments.ipynb",
        "colab_url": "https://colab.research.google.com/drive/1QFKQo5jGs3PPplGjamxxgXfGi5MhsHLY",
        "objective": "Parse JSON-like data, understand API responses, and know why environment variables matter.",
        "why_it_matters": (
            "This is where Python starts connecting to the outside world. JSON, APIs, virtual "
            "environments, package installs, and environment variables are the tools that move "
            "you from notebook exercises toward real projects."
        ),
        "notebook_summary": (
            "The notebook explains JSON as a common data exchange format, converts JSON text "
            "with `json.loads()` and `json.dumps()`, reads nested JSON, introduces API requests "
            "and status codes, discusses API keys and respectful usage, then covers virtual "
            "environments, `pip`, `requirements.txt`, and environment variables."
        ),
        "key_topics": [
            "JSON objects and arrays",
            "`json.loads()` and `json.dumps()`",
            "Nested JSON",
            "API requests and status codes",
            "Virtual environments and `pip`",
            "Environment variables",
        ],
        "concept": (
            "JSON is a text format that programs use to exchange structured data. APIs often "
            "send JSON responses. Environment variables keep configuration, secrets, and "
            "deployment settings outside your source code. Together, these ideas let your "
            "Python code work with services, files, keys, and project settings beyond the "
            "notebook."
        ),
        "mental_model": (
            "JSON is a shipping box for data. APIs deliver the box. Environment variables "
            "hold private labels and settings you do not want hard-coded. Your job is to open "
            "the box, understand its nested structure, and pull out the fields your program "
            "actually needs."
        ),
        "example_title": "Read nested JSON data",
        "example_code": """import json

raw = '{"name": "Ada", "languages": ["Python", "SQL"], "active": true}'
data = json.loads(raw)

print("Name:", data["name"])
print("First language:", data["languages"][0])
print("Active:", data["active"])""",
        "walkthrough": [
            "`json.loads()` converts JSON text into Python data structures.",
            "JSON objects become dictionaries.",
            "JSON arrays become lists.",
            "After parsing, you use normal dictionary keys and list indexes.",
        ],
        "challenge": {
            "title": "Extract an API-style value",
            "prompt": (
                "Parse the JSON string, then create `city` and `temperature` variables from "
                "the nested response. Print a readable weather sentence."
            ),
            "starter_code": """import json

raw_response = '''
{
  "weather": {
    "city": "Boston",
    "temperature": 71
  }
}
'''

# Parse raw_response and extract city and temperature.

print(f"{city}: {temperature} degrees")
""",
            "hints": [
                "Use `json.loads(raw_response)`.",
                "The city is inside the `weather` dictionary.",
                "Use dictionary keys in two steps: first `data[\"weather\"]`, then `[...]` again.",
            ],
            "solution": """import json

raw_response = '''
{
  "weather": {
    "city": "Boston",
    "temperature": 71
  }
}
'''

data = json.loads(raw_response)
city = data["weather"]["city"]
temperature = data["weather"]["temperature"]

print(f"{city}: {temperature} degrees")""",
            "checks": [
                {"type": "expr_equals", "expr": "city", "value": "Boston"},
                {"type": "expr_equals", "expr": "temperature", "value": 71},
                {"type": "output_contains", "text": "Boston"},
            ],
        },
        "deep_dive": [
            "Parse nested JSON and trace the dictionary/list path.",
            "Inspect an API response shape before writing code against it.",
            "Use the notebook to discuss why API keys belong in environment variables.",
        ],
    },
]


LESSONS_BY_ID = {lesson["id"]: lesson for lesson in LESSONS}


def get_lesson(lesson_id: int) -> dict:
    """Return lesson metadata by numeric id."""
    return LESSONS_BY_ID[lesson_id]


def get_next_lesson(lesson_id: int) -> dict | None:
    """Return the next lesson, if one exists."""
    for index, lesson in enumerate(LESSONS):
        if lesson["id"] == lesson_id and index + 1 < len(LESSONS):
            return LESSONS[index + 1]
    return None


def get_previous_lesson(lesson_id: int) -> dict | None:
    """Return the previous lesson, if one exists."""
    for index, lesson in enumerate(LESSONS):
        if lesson["id"] == lesson_id and index > 0:
            return LESSONS[index - 1]
    return None
