from dsl import S, L

RUN = True  # marks an MCQ whose correct option must equal the code's real output

LEVELS = [
# ═══════════════════════════ LEVEL 1 ═══════════════════════════
L("Python Basics", "Meet Python, learn how its code is written and run your first programs.", [
  S("What is Python?", "Your first look at Python and what it is used for.",
    """Python is a programming language — a way to give instructions to a computer using words
    that are close to plain English. It is free, runs on every major computer, and is known for
    being easy to read.""",
    points=["Created by Guido van Rossum and released in 1991",
            "Used for websites, data analysis, AI, automation and games",
            "Used by Google, Netflix, NASA and millions of developers"],
    key="A program is a list of instructions that the computer follows from top to bottom.",
    ex=[('print("Python is fun!")', "Python is fun!",
         ["This single line is a complete Python program.", "It tells Python to show the text on the screen."])],
    rules=["Python is an interpreted language: it runs your code line by line.",
           "Python files end with .py, for example hello.py.",
           "Python is case-sensitive: Print and print are different."],
    q=[("What is Python?", ["A snake-themed video game", "A programming language", "A web browser", "A computer brand"], 1,
        "Python is a programming language used to give instructions to computers."),
       ("Which file extension do Python files use?", [".pt", ".pyt", ".py", ".python"], 2,
        "Python source files end in .py."),
       ("How does Python run your code?", ["All at once, randomly", "Line by line, from top to bottom", "Bottom to top", "Only the last line"], 1,
        "Python is interpreted and executes statements one after another from the top."),
       ("Which of these is Python commonly used for?", ["Only making phone calls", "Data analysis and AI", "Only printing documents", "Charging batteries"], 1,
        "Python is hugely popular for data analysis, AI, web development and automation.")]),

  S("Python Syntax", "How Python code is written: lines, indentation and case.",
    """Syntax means the rules for writing code that Python understands. Python's syntax is famously
    clean: each instruction usually sits on its own line, and indentation (spaces at the start of a
    line) is used to group code together.""",
    points=["One statement per line — no semicolons needed",
            "Indentation (4 spaces) shows which lines belong together",
            "Names are case-sensitive: age, Age and AGE are three different names"],
    syntax="""
    statement_one
    if condition:
        indented_statement
    statement_two""",
    syn=["Normal statements start at the left edge.", "A line ending with : starts a block.", "The block's lines are indented by 4 spaces."],
    ex=[("""
    print("Line 1")
    print("Line 2")
    if 5 > 2:
        print("Five is bigger than two")""",
         """
    Line 1
    Line 2
    Five is bigger than two""",
         ["Each print is a separate statement on its own line.", "The indented print belongs to the if line above it."])],
    rules=["Indent with 4 spaces consistently inside a block.",
           "Don't indent lines randomly — unexpected indentation causes an IndentationError.",
           "Spelling and capital letters matter: Print() is not the same as print()."],
    mistake=("""
    print("Hello")
        print("World")""",
             "The second line is indented for no reason, so Python raises IndentationError: unexpected indent."),
    q=[("What does Python use to group lines of code into a block?", ["Curly braces { }", "Indentation", "Semicolons", "Parentheses"], 1,
        "Python uses indentation, usually 4 spaces, to define blocks."),
       ("Are name and Name the same in Python?", ["Yes, always", "No, Python is case-sensitive", "Only inside print()", "Only for numbers"], 1,
        "Python treats uppercase and lowercase letters as different."),
       ("What happens if you indent a line for no reason?", ["Nothing", "It runs twice", "IndentationError", "It becomes a comment"], 2,
        "Unexpected indentation raises an IndentationError."),
       ("Do Python statements need to end with a semicolon?", ["Yes, always", "No", "Only print statements", "Only on Windows"], 1,
        "Python statements normally end at the end of the line — no semicolon needed.")]),

  S("Comments", "Write notes in your code that Python ignores.",
    """A comment is a note for humans. Python ignores it completely. Comments start with the #
    symbol, and everything after # on that line is skipped.""",
    key="Use comments to explain why your code does something, not to repeat what it obviously does.",
    syntax="""
    # This is a full-line comment
    code_here  # This is an inline comment""",
    ex=[("""
    # Show a welcome message
    print("Welcome!")  # this part is ignored
    # print("This line will not run")""",
         "Welcome!",
         ["The first and last lines are comments, so they never run.", "Text after # on the print line is also ignored."]),
        ('''
    """
    This is a multi-line string.
    It is often used as a long comment.
    """
    print("Done")''', "Done",
         ["Triple quotes create a string that spans many lines.", "When it isn't stored anywhere, Python simply ignores it."])],
    rules=["Every comment line needs its own # (or use triple quotes for long notes).",
           "Comments don't affect how your program runs.",
           "You can 'switch off' a line of code by putting # in front of it."],
    q=[("Which symbol starts a comment in Python?", ["//", "#", "--", "/*"], 1,
        "In Python, everything after # on a line is a comment."),
       ("What will this code print?", ["Hi\nBye", "Hi", "Bye", "Nothing"], 1,
        "The second print is commented out, so only Hi is shown.", 'print("Hi")\n# print("Bye")', RUN),
       ("What does Python do with comments?", ["Prints them", "Ignores them", "Saves them to a file", "Raises an error"], 1,
        "Comments are ignored by Python; they are only for people reading the code."),
       ("What is a good use of a comment?", ["Making the program faster", "Explaining why code does something", "Storing passwords", "Changing variable values"], 1,
        "Comments explain intent so other people (and future you) understand the code.")]),

  S("print()", "Show text, numbers and results on the screen.",
    """print() is a built-in function that displays output. Whatever you put inside its parentheses
    is shown on the screen, followed by a new line.""",
    syntax="""
    print(value)
    print(value1, value2, sep=" ", end="\\n")""",
    syn=["Text must be inside quotes.", "Separate several values with commas.", "sep sets what goes between values; end sets what goes at the end."],
    ex=[("""
    print("Hello, World!")
    print(42)
    print(2 + 3)""",
         """
    Hello, World!
    42
    5""", ["Text needs quotes; numbers don't.", "Python works out 2 + 3 before printing it."]),
        ("""
    print("I am", 20, "years old")
    print("a", "b", "c", sep="-")
    print("Same", end=" ")
    print("line")""",
         """
    I am 20 years old
    a-b-c
    Same line""", ["Commas add a space between values by default.", "sep=\"-\" puts a dash between values.", "end=\" \" stops print from starting a new line."])],
    rules=["print is lowercase — Print() causes a NameError.",
           "Text must be wrapped in matching quotes: \"hi\" or 'hi'.",
           "print() with nothing inside prints an empty line."],
    mistake=('print("Hello)', "The closing quote is missing, so Python raises a SyntaxError."),
    q=[("What does print() do in Python?", ["Takes user input", "Displays output", "Creates a variable", "Ends the program"], 1,
        "print() shows whatever you put inside the parentheses on the screen."),
       ("What will this code display?", ["2 + 3", "\"5\"", "5", "Error"], 2,
        "Without quotes Python treats 2 + 3 as maths and prints the result.", "print(2 + 3)", RUN),
       ("What is the output?", ["a b", "a-b", "ab", "a,b"], 1,
        "sep=\"-\" places a dash between the values.", 'print("a", "b", sep="-")', RUN),
       ("What happens with print(\"Hi)?", ["Prints Hi", "Prints Hi)", "SyntaxError", "Prints nothing"], 2,
        "The string is never closed, which is a syntax error.")]),

  S("Basic Python Program", "Put the basics together into a complete little program.",
    """A program combines several statements to do a job. Python runs them in order, top to bottom.
    Even a short program can store values, do calculations and show results.""",
    key="Good programs are easy to read: clear names, one step per line and helpful comments.",
    ex=[("""
    # A tiny receipt program
    item = "Notebook"
    price = 45
    quantity = 3
    total = price * quantity
    print("Item:", item)
    print("Total:", total)""",
         """
    Item: Notebook
    Total: 135""",
         ["Lines 2–4 store values with names (you'll learn these as variables next).",
          "Line 5 calculates the total.", "The last two lines show the results."])],
    rules=["Programs run from the first line to the last unless told otherwise.",
           "A value must be created before it is used.",
           "Break problems into small, simple steps."],
    mistake=("""
    print(total)
    total = 10""", "total is used before it is created, so Python raises a NameError."),
    q=[("In what order does Python run a simple program?", ["Random order", "Bottom to top", "Top to bottom", "Shortest line first"], 2,
        "Python executes statements from the top of the file to the bottom."),
       ("What will this program print?", ["6", "2 * 3", "23", "Error"], 0,
        "a * b multiplies 2 by 3.", "a = 2\nb = 3\nprint(a * b)", RUN),
       ("Why does this fail?\nprint(x)\nx = 5", ["print is misspelled", "x is used before it is created", "5 is not a number", "It doesn't fail"], 1,
        "Python runs top to bottom, so x doesn't exist yet when print(x) runs."),
       ("Which makes a program easier to read?", ["One very long line", "Clear names and comments", "Random indentation", "No spaces at all"], 1,
        "Readable names, one step per line and comments make code easier to understand.")]),
]),

# ═══════════════════════════ LEVEL 2 ═══════════════════════════
L("Variables & Data Types", "Store values in variables and understand the kinds of data Python works with.", [
  S("Variables", "Give names to values so you can reuse them.",
    """A variable is a name that refers to a value — like a labelled box. You create a variable by
    assigning a value with the = sign. You can then use the name anywhere you need the value.""",
    syntax="variable_name = value",
    syn=["The name goes on the left.", "The value goes on the right.", "= means \"store\", not \"is equal to\"."],
    ex=[("""
    name = "Asha"
    age = 21
    print(name)
    print(age)""", "Asha\n21", ["name stores text and age stores a number.", "print(name) shows the value, not the word name."]),
        ("""
    score = 10
    score = 15
    print(score)
    x, y = 1, 2
    print(x + y)""", "15\n3", ["Assigning again replaces the old value.", "You can assign several variables in one line."])],
    rules=["A variable is created the first time you assign to it.",
           "A variable can be reassigned to a new value (even a different type).",
           "Using a variable that doesn't exist causes a NameError."],
    mistake=('5 = number', "The name must be on the left: number = 5."),
    q=[("Which line correctly creates a variable?", ["city = \"Pune\"", "\"Pune\" = city", "city == \"Pune\"", "var city = \"Pune\""], 0,
        "The variable name goes on the left of a single =."),
       ("What does this print?", ["10", "15", "25", "score"], 1,
        "The second assignment replaces 10 with 15.", "score = 10\nscore = 15\nprint(score)", RUN),
       ("What is printed?", ["a + b", "34", "7", "Error"], 2,
        "a is 3 and b is 4, so a + b is 7.", "a = 3\nb = 4\nprint(a + b)", RUN),
       ("What does = do in Python?", ["Checks equality", "Stores a value in a variable", "Adds numbers", "Prints a value"], 1,
        "A single = assigns (stores) a value. Equality is checked with ==.")]),

  S("Variable Naming Rules", "What names are allowed — and what makes a good name.",
    """Variable names must follow a few rules, or Python will refuse to run your code. Beyond the
    rules, good names describe what the value means.""",
    points=["Can contain letters, digits and underscores (_)",
            "Must start with a letter or underscore — never a digit",
            "No spaces or symbols like - @ $",
            "Can't be a Python keyword such as if, for, class or True"],
    key="Python style uses snake_case: lowercase words joined with underscores, like total_price.",
    ex=[("""
    user_name = "Ravi"
    _count = 3
    level2 = True
    print(user_name, _count, level2)""", "Ravi 3 True", ["All three names follow the rules."]),
        ("""
    total = 5
    Total = 50
    print(total, Total)""", "5 50", ["Names are case-sensitive, so these are two different variables."])],
    rules=["2nd_place, my-name and first name are all invalid names.",
           "Prefer descriptive names: student_count is better than sc.",
           "Constants are written in CAPITALS by convention, e.g. MAX_SPEED = 120."],
    mistake=("class = \"A\"", "class is a reserved keyword, so it can't be used as a variable name."),
    q=[("Which is a valid variable name?", ["2fast", "my name", "user_age", "class-1"], 2,
        "Names may use letters, digits and underscores but can't start with a digit or contain spaces or hyphens."),
       ("Why is 'for = 5' invalid?", ["for is a keyword", "5 is too small", "Names must be capitalised", "It is valid"], 0,
        "for is a reserved Python keyword."),
       ("Which naming style does Python recommend for variables?", ["camelCase", "snake_case", "kebab-case", "UPPERCASE for all"], 1,
        "PEP 8 recommends lowercase snake_case for variable names."),
       ("Are count and Count the same variable?", ["Yes", "No", "Only for numbers", "Only inside functions"], 1,
        "Python is case-sensitive, so they are different names.")]),

  S("Integers", "Whole numbers and maths with them.",
    """An integer (type int) is a whole number with no decimal point — positive, negative or zero.
    Python integers can be as large as you like.""",
    ex=[("""
    apples = 12
    debt = -40
    big = 1_000_000
    print(apples + 3)
    print(debt)
    print(big)""", "15\n-40\n1000000", ["Underscores make big numbers easier to read; Python ignores them.", "Integers can be negative."]),
        ("""
    print(7 // 2)
    print(7 % 2)
    print(2 ** 10)""", "3\n1\n1024", ["// is floor division (drops the decimal part).", "% gives the remainder.", "** raises to a power."])],
    rules=["Integers never have a decimal point: 5 is an int, 5.0 is not.",
           "Dividing two integers with / always gives a float: 6 / 2 is 3.0.",
           "Don't write leading zeros like 007 — that's a SyntaxError."],
    q=[("Which of these is an integer?", ["3.5", "\"7\"", "-12", "2.0"], 2,
        "-12 is a whole number without a decimal point."),
       ("What does this print?", ["3.5", "3", "4", "1"], 1,
        "// is floor division and drops the fractional part.", "print(7 // 2)", RUN),
       ("What is the result of 6 / 2?", ["3", "3.0", "\"3\"", "Error"], 1,
        "The / operator always returns a float.", "print(6 / 2)", RUN),
       ("What does 2 ** 3 calculate?", ["6", "8", "5", "23"], 1,
        "** is the power operator: 2 × 2 × 2 = 8.")]),

  S("Floats", "Numbers with a decimal point.",
    """A float is a number with a decimal point, like 3.14 or -0.5. Floats are used for measurements,
    prices and anything that isn't a whole number.""",
    ex=[("""
    price = 49.99
    pi = 3.14159
    print(price * 2)
    print(round(pi, 2))""", "99.98\n3.14", ["round(value, 2) rounds to 2 decimal places."]),
        ("""
    print(0.1 + 0.2)
    print(round(0.1 + 0.2, 2))""", "0.30000000000000004\n0.3", ["Computers store floats approximately, so tiny errors can appear.", "Use round() when displaying results."])],
    rules=["Mixing an int and a float gives a float: 2 + 1.5 is 3.5.",
           "Use a dot, not a comma, for decimals: 2.5 not 2,5.",
           "Don't compare floats for exact equality after calculations — round first."],
    mistake=("price = 2,5", "This creates a tuple (2, 5), not the number two and a half. Use 2.5."),
    q=[("Which value is a float?", ["10", "\"10.5\"", "10.5", "True"], 2,
        "10.5 has a decimal point and no quotes."),
       ("What does this print?", ["3", "3.5", "\"3.5\"", "Error"], 1,
        "An int plus a float gives a float.", "print(2 + 1.5)", RUN),
       ("What does round(3.14159, 2) return?", ["3.1", "3.14", "3.142", "3"], 1,
        "round(x, 2) keeps two digits after the decimal point."),
       ("Why might 0.1 + 0.2 not print exactly 0.3?", ["Python has a bug", "Floats are stored approximately", "0.1 is an integer", "print rounds numbers"], 1,
        "Floats use binary approximations, so tiny rounding errors appear.")]),

  S("Strings", "Text values written inside quotes.",
    """A string (type str) is a piece of text. You create one by putting characters inside single
    quotes '...' or double quotes "...". Strings can be joined with + and repeated with *.""",
    ex=[("""
    first = "Meera"
    last = 'Shah'
    full = first + " " + last
    print(full)
    print("ha" * 3)""", "Meera Shah\nhahaha", ["+ joins (concatenates) strings.", "* repeats a string."]),
        ('''
    quote = "It's a great day"
    poem = """Roses are red,
    Violets are blue."""
    print(quote)
    print(poem)''', "It's a great day\nRoses are red,\nViolets are blue.", ["Use double quotes when the text contains an apostrophe.", "Triple quotes allow text over several lines."])],
    rules=["Opening and closing quotes must match.",
           "\"5\" is a string, 5 is a number — they behave differently.",
           "You can't add a string and a number directly: \"Age: \" + 20 is a TypeError."],
    mistake=('print("Age: " + 20)', "Convert the number first: \"Age: \" + str(20)."),
    q=[("Which of these is a string?", ["42", "True", "'42'", "4.2"], 2,
        "Anything inside quotes is a string, even digits."),
       ("What is printed?", ["2 + 3", "5", "23", "Error"], 2,
        "Both are strings, so + joins them.", 'print("2" + "3")', RUN),
       ("What does \"ab\" * 2 produce?", ["ab2", "abab", "Error", "ab ab"], 1,
        "Multiplying a string repeats it."),
       ("What happens with \"Age: \" + 20?", ["Age: 20", "TypeError", "Age:20", "20"], 1,
        "You can't join str and int with + — convert with str() first.")]),

  S("Booleans", "True and False — the values of yes/no questions.",
    """A boolean (type bool) has only two possible values: True or False. Booleans come from
    comparisons and are used to make decisions.""",
    ex=[("""
    is_logged_in = True
    has_paid = False
    print(is_logged_in)
    print(10 > 3)
    print(5 == 6)""", "True\nTrue\nFalse", ["Comparisons produce booleans.", "True and False start with capital letters."]),
        ("""
    print(bool(0))
    print(bool(7))
    print(bool(""))
    print(bool("hi"))""", "False\nTrue\nFalse\nTrue", ["0 and empty strings count as False.", "Most other values count as True."])],
    rules=["Write True and False with a capital first letter — true is a NameError.",
           "\"True\" in quotes is a string, not a boolean.",
           "Booleans behave like numbers: True is 1 and False is 0."],
    q=[("Which value is a boolean?", ["\"True\"", "True", "true", "'yes'"], 1,
        "True with a capital T and no quotes is a boolean."),
       ("What does this print?", ["True", "False", "10", "Error"], 1,
        "10 is not less than 3.", "print(10 < 3)", RUN),
       ("What is bool(0)?", ["True", "False", "0", "None"], 1,
        "Zero is considered False."),
       ("How many values can a boolean have?", ["1", "2", "10", "Unlimited"], 1,
        "A boolean is either True or False.")]),

  S("type()", "Ask Python what kind of value something is.",
    """type() tells you the data type of any value or variable. It's a handy way to check what
    you're working with, especially when a result surprises you.""",
    syntax="type(value)",
    ex=[("""
    print(type("hi"))
    print(type(7))
    print(type(2.5))
    print(type(True))""", "<class 'str'>\n<class 'int'>\n<class 'float'>\n<class 'bool'>", ["type() returns the class (kind) of the value."]),
        ("""
    x = 10
    print(type(x))
    x = "ten"
    print(type(x))
    print(type(x) == str)""", "<class 'int'>\n<class 'str'>\nTrue", ["A variable's type follows its current value.", "You can compare a type with ==."])],
    rules=["type() inspects a value; it doesn't change it.",
           "type(\"5\") is str even though it looks like a number.",
           "isinstance(x, int) is another common way to check types."],
    q=[("What does type(3.0) return?", ["<class 'int'>", "<class 'float'>", "<class 'str'>", "<class 'number'>"], 1,
        "3.0 has a decimal point, so it's a float."),
       ("What is printed?", ["<class 'int'>", "<class 'str'>", "<class 'bool'>", "5"], 1,
        "\"5\" is in quotes, so it's a string.", 'print(type("5"))', RUN),
       ("What does type() do?", ["Converts a value", "Shows a value's data type", "Deletes a variable", "Types text on screen"], 1,
        "type() reports the data type of a value."),
       ("What is printed?", ["<class 'int'>", "<class 'str'>", "<class 'bool'>", "<class 'float'>"], 2,
        "True is a boolean.", "print(type(True))", RUN)]),

  S("Type Conversion", "Turn one data type into another with int(), float(), str() and bool().",
    """Sometimes you need a value as a different type — for example, turning the text "20" into the
    number 20. Python's conversion functions create a new value of the type you ask for.""",
    syntax="""
    int(value)
    float(value)
    str(value)
    bool(value)""",
    ex=[("""
    age_text = "20"
    age = int(age_text)
    print(age + 1)
    print(float("3.5") * 2)
    print("Score: " + str(99))""", "21\n7.0\nScore: 99", ["int() turns text into a whole number.", "float() turns text into a decimal number.", "str() turns a number into text so it can be joined."]),
        ("""
    print(int(7.9))
    print(int("  42 "))
    print(float(5))""", "7\n42\n5.0", ["int() on a float cuts off the decimal (it doesn't round).", "Spaces around digits are allowed."])],
    rules=["int(\"hello\") or int(\"3.5\") raise ValueError — the text must look like a whole number.",
           "Converting doesn't change the original variable; store the result.",
           "int() truncates toward zero: int(-2.7) is -2."],
    mistake=('int("3.5")', "Convert to float first: int(float(\"3.5\")) gives 3."),
    q=[("Which function converts \"42\" into a whole number?", ["str()", "float()", "type()", "int()"], 3,
        "int() converts a value to an integer."),
       ("What does this print?", ["7.9", "8", "7", "Error"], 2,
        "int() drops the decimal part instead of rounding.", "print(int(7.9))", RUN),
       ("What happens with int(\"hello\")?", ["Returns 0", "ValueError", "Returns \"hello\"", "Returns None"], 1,
        "The text isn't a number, so Python raises ValueError."),
       ("How do you join \"Total: \" with the number 5?", ["\"Total: \" + 5", "\"Total: \" + str(5)", "\"Total: \" - 5", "int(\"Total: \") + 5"], 1,
        "str(5) converts the number to text so + can join them.")]),
]),

# ═══════════════════════════ LEVEL 3 ═══════════════════════════
L("Input & Operators", "Read what the user types and work with Python's operators.", [
  S("input()", "Ask the user a question and use their answer.",
    """input() pauses the program, shows a prompt and waits for the user to type something and
    press Enter. Whatever they type is returned as a string.""",
    syntax='answer = input("Your question: ")',
    ex=[("""
    name = input("What is your name? ")
    print("Hello,", name)""", "What is your name? Ravi\nHello, Ravi", ["The prompt is shown to the user.", "Their reply is stored in name."], {"stdin": ["Ravi"]}),
        ("""
    age = int(input("Age: "))
    print("Next year you will be", age + 1)""", "Age: 18\nNext year you will be 19", ["input() always returns text.", "int() converts it so you can do maths."], {"stdin": ["18"]})],
    rules=["input() ALWAYS returns a string, even if the user types digits.",
           "Convert with int() or float() before doing maths.",
           "Add a space at the end of the prompt so the answer doesn't touch it."],
    mistake=("""
    age = input("Age: ")
    print(age + 1)""", "age is a string, so age + 1 raises a TypeError. Use int(input(...))."),
    q=[("What does input() return?", ["A number", "A string", "A boolean", "Nothing"], 1,
        "input() always returns the typed text as a string."),
       ("How do you read a whole number from the user?", ["int(input())", "input(int())", "number(input())", "input().int"], 0,
        "Wrap input() in int() to convert the reply."),
       ("What is shown by input(\"Age: \")?", ["Nothing", "The word input", "Age: ", "An error"], 2,
        "The text inside input() is displayed as the prompt."),
       ("A user types 5. What does input() give you?", ["5", "\"5\"", "5.0", "True"], 1,
        "It's the string \"5\" until you convert it.")]),

  S("Arithmetic Operators", "Do maths: + - * / // % **",
    """Arithmetic operators perform calculations on numbers. Python follows the usual maths order:
    brackets first, then powers, then * / // %, then + and -.""",
    points=["+ addition, - subtraction, * multiplication", "/ division (always a float)",
            "// floor division, % remainder (modulus)", "** exponent (power)"],
    ex=[("""
    a, b = 17, 5
    print(a + b, a - b, a * b)
    print(a / b)
    print(a // b, a % b)
    print(b ** 2)""", "22 12 85\n3.4\n3 2\n25", ["17 / 5 is 3.4.", "17 // 5 is 3 and the remainder 17 % 5 is 2."]),
        ("""
    print(2 + 3 * 4)
    print((2 + 3) * 4)
    print(10 % 2 == 0)""", "14\n20\nTrue", ["* happens before +.", "Brackets change the order.", "x % 2 == 0 is a classic even-number check."])],
    rules=["Dividing by zero raises ZeroDivisionError.",
           "Use brackets to make the order of operations obvious.",
           "% is useful for checking even/odd numbers and wrapping around."],
    q=[("What is 17 % 5?", ["3", "2", "3.4", "12"], 1,
        "% gives the remainder: 17 = 3 × 5 + 2."),
       ("What does this print?", ["20", "14", "24", "9"], 1,
        "Multiplication happens before addition: 3 × 4 = 12, plus 2.", "print(2 + 3 * 4)", RUN),
       ("Which operator gives a power?", ["^", "**", "*", "//"], 1,
        "** is exponentiation in Python; ^ is something else."),
       ("What is 9 // 2?", ["4.5", "4", "5", "1"], 1,
        "// is floor division and drops the decimal part.")]),

  S("Comparison Operators", "Compare values and get True or False.",
    """Comparison operators compare two values and always produce a boolean: True or False. They
    are the building blocks of decisions.""",
    points=["== equal to,  != not equal to", "> greater than,  < less than", ">= greater or equal,  <= less or equal"],
    ex=[("""
    print(5 > 3)
    print(4 == 5)
    print(4 != 5)
    print(7 >= 7)""", "True\nFalse\nTrue\nTrue", ["Each comparison gives True or False."]),
        ("""
    age = 16
    print(age >= 18)
    print("apple" == "Apple")
    print(1 < age < 20)""", "False\nFalse\nTrue", ["String comparison is case-sensitive.", "Python lets you chain comparisons."])],
    rules=["== compares; a single = assigns. Mixing them up is a very common bug.",
           "Comparing numbers and strings with < raises a TypeError.",
           "Chained comparisons like 0 < x < 10 are allowed."],
    mistake=("if age = 18:", "Use == to compare: if age == 18:"),
    q=[("Which operator checks if two values are equal?", ["=", "==", "!=", "=>"], 1,
        "== compares values; = assigns."),
       ("What does 7 >= 7 give?", ["True", "False", "7", "Error"], 0,
        ">= is True when the left side is greater than or equal to the right."),
       ("What is printed?", ["True", "False", "Error", "None"], 1,
        "Comparisons between strings are case-sensitive.", 'print("cat" == "Cat")', RUN),
       ("What does != mean?", ["Equal", "Not equal", "Greater than", "Assign"], 1,
        "!= returns True when the values are different.")]),

  S("Assignment Operators", "Shortcuts like += and -= for updating variables.",
    """Assignment operators store a value in a variable. Besides =, Python has shortcuts that update
    a variable using its current value.""",
    points=["x += 3 means x = x + 3", "x -= 3 means x = x - 3", "x *= 3, x /= 3, x //= 3, x %= 3, x **= 3 work the same way"],
    ex=[("""
    score = 10
    score += 5
    print(score)
    score -= 3
    print(score)
    score *= 2
    print(score)""", "15\n12\n24", ["Each line updates score using its previous value."]),
        ("""
    msg = "Hi"
    msg += "!"
    print(msg)
    n = 7
    n //= 2
    print(n)""", "Hi!\n3", ["+= also works with strings.", "//= does floor division in place."])],
    rules=["The variable must already exist before using += (otherwise NameError).",
           "Python has no ++ or -- operators; use += 1 and -= 1.",
           "x /= 2 always turns x into a float."],
    mistake=("count++", "Python has no ++ operator. Write count += 1."),
    q=[("What does x += 4 mean?", ["x = 4", "x = x + 4", "x == x + 4", "x = x * 4"], 1,
        "+= adds to the current value."),
       ("What is printed?", ["5", "15", "50", "10"], 1,
        "10 + 5 = 15.", "x = 10\nx += 5\nprint(x)", RUN),
       ("How do you add 1 to count in Python?", ["count++", "count += 1", "++count", "count =+ 1"], 1,
        "Python doesn't have ++; use += 1."),
       ("What is printed?", ["8", "12", "4", "2"], 1,
        "4 × 3 = 12.", "n = 4\nn *= 3\nprint(n)", RUN)]),

  S("Logical Operators", "Combine conditions with and, or and not.",
    """Logical operators combine booleans. and needs both sides True, or needs at least one side
    True, and not flips True to False and False to True.""",
    points=["A and B → True only if both are True", "A or B → True if either is True", "not A → the opposite of A"],
    ex=[("""
    age = 20
    has_ticket = True
    print(age >= 18 and has_ticket)
    print(age < 12 or has_ticket)
    print(not has_ticket)""", "True\nTrue\nFalse", ["Both conditions are True, so and gives True.", "has_ticket is True, so or gives True."]),
        ("""
    temp = 35
    print(temp > 30 and temp < 40)
    print(temp < 0 or temp > 45)""", "True\nFalse", ["and checks a range.", "Neither side is True, so or gives False."])],
    rules=["Python writes the words and, or, not — not && or ||.",
           "and stops early if the left side is False; or stops early if the left side is True.",
           "Use brackets to make complex conditions clear."],
    q=[("What is True and False?", ["True", "False", "None", "Error"], 1,
        "and needs both sides to be True."),
       ("What is True or False?", ["True", "False", "None", "Error"], 0,
        "or needs just one side to be True."),
       ("What does this print?", ["True", "False", "5", "Error"], 1,
        "5 > 3 is True, so not makes it False.", "print(not 5 > 3)", RUN),
       ("Which is Python's logical AND?", ["&&", "and", "&", "AND"], 1,
        "Python uses the keyword and.")]),

  S("Membership Operators", "Check if something is inside a collection with in and not in.",
    """Membership operators test whether a value appears inside a string, list or other collection.
    in returns True if it is found; not in returns True if it isn't.""",
    syntax="""
    value in collection
    value not in collection""",
    ex=[("""
    fruits = ["apple", "mango", "kiwi"]
    print("mango" in fruits)
    print("grape" in fruits)
    print("grape" not in fruits)""", "True\nFalse\nTrue", ["in searches the list for the value."]),
        ("""
    word = "python"
    print("th" in word)
    print("P" in word)""", "True\nFalse", ["With strings, in looks for a substring.", "The search is case-sensitive."])],
    rules=["in works with strings, lists, tuples, sets and dictionaries.",
           "For dictionaries, in checks the keys, not the values.",
           "Membership checks are case-sensitive for strings."],
    q=[("What does this print?", ["True", "False", "Error", "None"], 0,
        "3 is one of the list items.", "print(3 in [1, 2, 3])", RUN),
       ("What is \"z\" not in \"pizza\"?", ["True", "False", "Error", "None"], 1,
        "\"pizza\" contains z, so not in is False."),
       ("What does this print?", ["True", "False", "Error", "py"], 1,
        "Membership is case-sensitive: \"Py\" isn't in \"python\".", 'print("Py" in "python")', RUN),
       ("For a dictionary, what does in check?", ["Values", "Keys", "Both", "Length"], 1,
        "key in my_dict checks the keys.")]),

  S("Identity Operators", "Check if two names point to the very same object with is.",
    """is checks whether two variables refer to the same object in memory — not just equal values.
    is not is the opposite. The most common use is checking for None.""",
    syntax="""
    a is b
    a is not b""",
    ex=[("""
    a = [1, 2]
    b = [1, 2]
    c = a
    print(a == b)
    print(a is b)
    print(a is c)""", "True\nFalse\nTrue", ["a and b have equal values but are two separate lists.", "c is another name for the same list as a."]),
        ("""
    result = None
    print(result is None)
    print(result is not None)""", "True\nFalse", ["Always compare with None using is."])],
    rules=["== compares values; is compares identity.",
           "Use is for None, True and False checks: if x is None:",
           "Don't use is to compare numbers or strings — use ==."],
    q=[("What does is check?", ["Equal values", "Same object in memory", "Same type", "Same length"], 1,
        "is compares identity: are both names the same object?"),
       ("What is printed?", ["True", "False", "Error", "None"], 1,
        "They are two different list objects, even though their values match.", "a = [1]\nb = [1]\nprint(a is b)", RUN),
       ("What's the recommended way to check for None?", ["x == None", "x is None", "x = None", "None(x)"], 1,
        "PEP 8 recommends is None."),
       ("What is printed?", ["True", "False", "Error", "[1]"], 0,
        "b refers to the same list as a.", "a = [1]\nb = a\nprint(a is b)", RUN)]),
]),

# ═══════════════════════════ LEVEL 4 ═══════════════════════════
L("Conditional Statements", "Make your programs take decisions with if, elif and else.", [
  S("if", "Run code only when a condition is True.",
    """An if statement runs a block of code only when its condition is True. If the condition is
    False, Python skips the block.""",
    syntax="""
    if condition:
        code_to_run""",
    syn=["The condition is any expression that is True or False.", "The line ends with a colon.", "The block underneath is indented."],
    ex=[("""
    age = 20
    if age >= 18:
        print("You can vote")
    print("Done")""", "You can vote\nDone", ["age >= 18 is True, so the indented line runs.", "\"Done\" isn't indented, so it always runs."]),
        ("""
    stock = 0
    if stock == 0:
        print("Out of stock")
        print("Check back later")""", "Out of stock\nCheck back later", ["Every indented line belongs to the if block."])],
    rules=["Don't forget the colon at the end of the if line.",
           "Indent the block consistently (4 spaces).",
           "Use == to compare, not =."],
    mistake=("""
    if score > 50
        print("Pass")""", "The colon is missing after the condition — SyntaxError."),
    q=[("What must end an if line?", ["A semicolon ;", "A colon :", "A period .", "Nothing"], 1,
        "if, elif and else lines end with a colon."),
       ("What is printed?", ["Hot", "Nothing", "Error", "35"], 0,
        "35 > 30 is True, so the block runs.", 't = 35\nif t > 30:\n    print("Hot")', RUN),
       ("When does the code inside an if run?", ["Always", "When the condition is True", "When the condition is False", "Never"], 1,
        "The block runs only if the condition is True."),
       ("How does Python know which lines belong to the if?", ["Curly braces", "Indentation", "The word end", "Line numbers"], 1,
        "Indented lines below the if form its block.")]),

  S("elif", "Check another condition when the first one is False.",
    """elif (short for 'else if') lets you test more conditions, one after another. Python checks
    them from top to bottom and runs only the first block whose condition is True.""",
    syntax="""
    if condition1:
        ...
    elif condition2:
        ...
    elif condition3:
        ...""",
    ex=[("""
    marks = 72
    if marks >= 90:
        print("Grade A")
    elif marks >= 75:
        print("Grade B")
    elif marks >= 60:
        print("Grade C")""", "Grade C", ["72 isn't >= 90 or >= 75.", "72 >= 60 is True, so Grade C prints.", "Once a branch runs, the rest are skipped."]),
        ("""
    light = "yellow"
    if light == "green":
        print("Go")
    elif light == "yellow":
        print("Slow down")
    elif light == "red":
        print("Stop")""", "Slow down", ["Only the matching branch runs."])],
    rules=["elif must come after an if — it can't stand alone.",
           "You can have as many elif branches as you need.",
           "Order matters: put the most specific conditions first."],
    q=[("What does elif mean?", ["else if", "end if", "elevate if", "either if"], 0,
        "elif is short for else if."),
       ("What is printed?", ["High", "Medium", "High\nMedium", "Nothing"], 1,
        "50 > 80 is False; 50 > 30 is True.", 'x = 50\nif x > 80:\n    print("High")\nelif x > 30:\n    print("Medium")', RUN),
       ("How many branches of an if/elif chain can run?", ["All of them", "At most one", "Two", "Exactly three"], 1,
        "Python stops at the first True condition."),
       ("Can elif be used without an if before it?", ["Yes", "No", "Only in loops", "Only once"], 1,
        "elif must follow an if (or another elif).")]),

  S("else", "Run a fallback block when no condition is True.",
    """else catches everything that didn't match. It has no condition of its own and runs only when
    the if (and any elif) conditions were all False.""",
    syntax="""
    if condition:
        ...
    else:
        ...""",
    ex=[("""
    temp = 15
    if temp > 25:
        print("It's hot")
    else:
        print("It's cool")""", "It's cool", ["15 > 25 is False, so the else block runs."]),
        ("""
    n = 7
    if n % 2 == 0:
        print(n, "is even")
    else:
        print(n, "is odd")""", "7 is odd", ["Exactly one of the two blocks always runs."])],
    rules=["else never has a condition: else x > 5: is a SyntaxError.",
           "else must be the last branch in the chain.",
           "if/else guarantees exactly one block runs."],
    mistake=("else n > 5:", "else takes no condition. Use elif n > 5: if you need one."),
    q=[("When does else run?", ["Always", "When all previous conditions are False", "When the if is True", "Never"], 1,
        "else is the fallback when nothing above matched."),
       ("What is printed?", ["Big", "Small", "Big\nSmall", "Nothing"], 1,
        "3 > 10 is False, so else runs.", 'n = 3\nif n > 10:\n    print("Big")\nelse:\n    print("Small")', RUN),
       ("Does else take a condition?", ["Yes", "No", "Only with numbers", "Only after elif"], 1,
        "else has no condition — just else:"),
       ("Where must else appear?", ["First", "Anywhere", "Last in the chain", "Before elif"], 2,
        "else always comes after if and any elif branches.")]),

  S("Nested if", "Put one if statement inside another.",
    """A nested if is an if statement inside the block of another if. The inner condition is only
    checked when the outer condition is True.""",
    syntax="""
    if outer_condition:
        if inner_condition:
            ...""",
    ex=[("""
    age = 20
    has_id = True
    if age >= 18:
        if has_id:
            print("Entry allowed")
        else:
            print("Please show ID")
    else:
        print("Too young")""", "Entry allowed", ["The outer if checks age.", "Only then does the inner if check the ID."])],
    rules=["Each level of nesting adds 4 more spaces of indentation.",
           "Deep nesting is hard to read — often and can replace a nested if.",
           "An inner else pairs with the inner if at the same indentation."],
    q=[("When is the inner condition checked?", ["Always", "Only if the outer condition is True", "Only if the outer is False", "Never"], 1,
        "The inner if sits inside the outer block."),
       ("What is printed?", ["A", "B", "C", "Nothing"], 1,
        "x > 0 is True, then x > 10 is False, so the inner else runs.", 'x = 5\nif x > 0:\n    if x > 10:\n        print("A")\n    else:\n        print("B")\nelse:\n    print("C")', RUN),
       ("What often replaces a simple nested if?", ["A loop", "The and operator", "A comment", "print()"], 1,
        "if a: if b: can usually be written as if a and b:"),
       ("How is a nested block shown?", ["With extra indentation", "With brackets", "With a semicolon", "With #"], 0,
        "Each nested level is indented further.")]),

  S("Multiple Conditions", "Combine and, or and not inside if statements.",
    """Real decisions often depend on several facts at once. Use and, or and not to combine
    conditions in a single if.""",
    ex=[("""
    age = 25
    member = False
    if age >= 18 and member:
        print("Member discount")
    elif age >= 18 or member:
        print("Standard price")
    else:
        print("Child price")""", "Standard price", ["age >= 18 and member is False because member is False.", "age >= 18 or member is True."]),
        ("""
    day = "Sunday"
    if day == "Saturday" or day == "Sunday":
        print("Weekend!")
    if not day == "Monday":
        print("Not Monday")""", "Weekend!\nNot Monday", ["Each side of or must be a full comparison."])],
    rules=["Write full comparisons on both sides: day == \"Sat\" or day == \"Sun\".",
           "and is evaluated before or — use brackets when mixing them.",
           "x in (\"Sat\", \"Sun\") is a neat alternative to many ors."],
    mistake=('if day == "Saturday" or "Sunday":', "\"Sunday\" alone is always True, so this condition is always True. Compare both: day == \"Saturday\" or day == \"Sunday\"."),
    q=[("What is printed?", ["Yes", "No", "Error", "Nothing"], 1,
        "5 > 3 is True but 2 > 4 is False, so and is False.", 'if 5 > 3 and 2 > 4:\n    print("Yes")\nelse:\n    print("No")', RUN),
       ("Why is if x == 1 or 2: a bug?", ["It's a SyntaxError", "2 on its own is always True", "or can't be used in if", "It isn't a bug"], 1,
        "The right side is just 2, which is truthy, so the condition is always True."),
       ("Which runs first in a and b or c?", ["or", "and", "Left to right always", "Neither"], 1,
        "and has higher precedence than or."),
       ("What's a neat way to check if day is Sat or Sun?", ["day in (\"Sat\", \"Sun\")", "day == \"Sat\" and \"Sun\"", "day = \"Sat\" or \"Sun\"", "day is \"Sat\", \"Sun\""], 0,
        "Membership with in tests against several values cleanly.")]),
]),

# ═══════════════════════════ LEVEL 5 ═══════════════════════════
L("Loops", "Repeat actions with for and while, and control loops with break, continue and pass.", [
  S("for", "Repeat code once for every item in a sequence.",
    """A for loop goes through a sequence — like a string or a list — one item at a time, running
    its block once per item. The loop variable holds the current item.""",
    syntax="""
    for item in sequence:
        code_using_item""",
    ex=[("""
    for letter in "cat":
        print(letter)""", "c\na\nt", ["letter takes each character in turn."]),
        ("""
    colours = ["red", "green", "blue"]
    for c in colours:
        print("I like", c)
    print("Loop finished")""", "I like red\nI like green\nI like blue\nLoop finished", ["The block runs once per list item.", "The un-indented line runs after the loop ends."])],
    rules=["The for line ends with a colon and the body is indented.",
           "The loop variable can have any name; choose a meaningful one.",
           "Changing the loop variable inside the loop doesn't change the sequence."],
    q=[("How many times does this loop run?\nfor x in \"hey\":", ["1", "2", "3", "4"], 2,
        "\"hey\" has 3 characters."),
       ("What is printed?", ["1 2 3", "1\n2\n3", "123", "[1, 2, 3]"], 1,
        "Each print starts a new line.", "for n in [1, 2, 3]:\n    print(n)", RUN),
       ("What does the loop variable hold?", ["The loop count", "The current item", "The whole list", "Nothing"], 1,
        "It holds the item for the current repetition."),
       ("What ends the for line?", [";", ":", ".", "{"], 1,
        "Like if, a for line ends with a colon.")]),

  S("while", "Repeat code as long as a condition stays True.",
    """A while loop keeps running its block while a condition is True. It's useful when you don't
    know in advance how many times you need to repeat.""",
    syntax="""
    while condition:
        code
        update_something""",
    ex=[("""
    count = 1
    while count <= 3:
        print("Count:", count)
        count += 1
    print("Done")""", "Count: 1\nCount: 2\nCount: 3\nDone", ["The condition is checked before every repetition.", "count += 1 moves the loop towards stopping."]),
        ("""
    money = 100
    while money >= 30:
        money -= 30
        print("Bought one, left:", money)""", "Bought one, left: 70\nBought one, left: 40\nBought one, left: 10", ["The loop stops once money is below 30."])],
    rules=["Make sure something inside the loop eventually makes the condition False.",
           "A loop whose condition never becomes False is an infinite loop.",
           "If the condition is False at the start, the body never runs."],
    mistake=("""
    i = 0
    while i < 5:
        print(i)""", "i never changes, so this loops forever. Add i += 1 inside the loop."),
    q=[("When does a while loop stop?", ["After 10 runs", "When its condition becomes False", "Never", "After one run"], 1,
        "It repeats while the condition is True."),
       ("What is printed?", ["0 1 2", "0\n1\n2", "1\n2\n3", "0\n1\n2\n3"], 1,
        "It prints 0, 1, 2 and stops when i becomes 3.", "i = 0\nwhile i < 3:\n    print(i)\n    i += 1", RUN),
       ("What causes an infinite loop?", ["Using print", "A condition that never becomes False", "Using a colon", "Indentation"], 1,
        "If nothing changes the condition, the loop never ends."),
       ("When is a while loop a better choice than for?", ["When you know the exact list", "When you repeat until something happens", "Never", "Only for strings"], 1,
        "while suits 'repeat until' situations.")]),

  S("range()", "Generate sequences of numbers for loops.",
    """range() produces a sequence of whole numbers. It's most often used with for to repeat
    something a set number of times.""",
    syntax="""
    range(stop)
    range(start, stop)
    range(start, stop, step)""",
    syn=["stop is NOT included.", "start defaults to 0.", "step defaults to 1 and can be negative."],
    ex=[("""
    for i in range(3):
        print(i)""", "0\n1\n2", ["range(3) gives 0, 1, 2 — three numbers, starting at 0."]),
        ("""
    print(list(range(2, 6)))
    print(list(range(0, 10, 3)))
    print(list(range(5, 0, -1)))""", "[2, 3, 4, 5]\n[0, 3, 6, 9]\n[5, 4, 3, 2, 1]", ["list() lets you see all numbers at once.", "A negative step counts down."])],
    rules=["The stop value is never included: range(1, 5) ends at 4.",
           "range() only works with integers.",
           "range(5) runs a loop exactly 5 times."],
    q=[("What numbers does range(4) produce?", ["1, 2, 3, 4", "0, 1, 2, 3", "0, 1, 2, 3, 4", "4"], 1,
        "It starts at 0 and stops before 4."),
       ("What is printed?", ["[1, 2, 3]", "[1, 2, 3, 4]", "[2, 3]", "[0, 1, 2, 3]"], 0,
        "range(1, 4) stops before 4.", "print(list(range(1, 4)))", RUN),
       ("What is printed?", ["[0, 2, 4, 6]", "[0, 2, 4]", "[2, 4, 6]", "[0, 1, 2]"], 1,
        "Start 0, step 2, stop before 6.", "print(list(range(0, 6, 2)))", RUN),
       ("How many times does for i in range(10): run?", ["9", "10", "11", "1"], 1,
        "range(10) has 10 numbers: 0 to 9.")]),

  S("break", "Stop a loop early.",
    """break immediately ends the loop it's in. Python jumps to the first line after the loop. It's
    useful when you've found what you were looking for.""",
    ex=[("""
    for n in [3, 8, 12, 5]:
        if n > 10:
            print("Found", n)
            break
        print("Checked", n)""", "Checked 3\nChecked 8\nFound 12", ["When n is 12 the loop stops.", "5 is never checked."]),
        ("""
    while True:
        word = input("Type stop: ")
        if word == "stop":
            break
    print("Bye")""", "Type stop: go\nType stop: stop\nBye", ["while True loops forever until break runs."], {"stdin": ["go", "stop"]})],
    rules=["break only exits the innermost loop it is in.",
           "Code after break in the same block never runs.",
           "while True + break is a common pattern for 'repeat until'."],
    q=[("What does break do?", ["Skips one item", "Ends the loop immediately", "Pauses the program", "Restarts the loop"], 1,
        "break exits the loop right away."),
       ("What is printed?", ["0\n1\n2", "0\n1", "0\n1\n2\n3", "Nothing"], 1,
        "When i is 2, break runs before printing.", "for i in range(5):\n    if i == 2:\n        break\n    print(i)", RUN),
       ("In nested loops, which loop does break stop?", ["All loops", "The innermost loop it's in", "The outer loop", "None"], 1,
        "break only exits the loop that directly contains it."),
       ("What pattern repeats until break?", ["for i in range(0):", "while True:", "if True:", "while False:"], 1,
        "while True runs forever unless break stops it.")]),

  S("continue", "Skip the rest of this repetition and move to the next.",
    """continue skips whatever is left in the loop body for the current item and jumps straight to
    the next repetition. The loop itself keeps going.""",
    ex=[("""
    for n in range(1, 6):
        if n == 3:
            continue
        print(n)""", "1\n2\n4\n5", ["When n is 3, print is skipped.", "The loop carries on with 4 and 5."]),
        ("""
    for word in ["hi", "", "there", ""]:
        if word == "":
            continue
        print(word.upper())""", "HI\nTHERE", ["Empty strings are skipped."])],
    rules=["continue doesn't stop the loop — break does.",
           "In a while loop, make sure the counter updates before continue, or you'll loop forever.",
           "Use continue to skip unwanted items early and keep code flat."],
    q=[("What does continue do?", ["Ends the loop", "Skips to the next repetition", "Repeats the same item", "Prints a value"], 1,
        "It jumps to the next iteration."),
       ("What is printed?", ["0\n1\n2", "0\n2", "1", "0\n1"], 1,
        "1 is skipped.", "for i in range(3):\n    if i == 1:\n        continue\n    print(i)", RUN),
       ("break vs continue: which keeps the loop running?", ["break", "continue", "Both", "Neither"], 1,
        "continue keeps looping; break stops."),
       ("What is printed?", ["1\n3", "1\n2\n3", "2", "1\n2"], 0,
        "Even numbers are skipped.", "for n in [1, 2, 3]:\n    if n % 2 == 0:\n        continue\n    print(n)", RUN)]),

  S("pass", "A placeholder that does nothing.",
    """pass is a statement that does nothing at all. Python needs at least one line inside every
    block, so pass lets you leave a block empty for now.""",
    ex=[("""
    for i in range(3):
        pass
    print("Loop ran, did nothing")""", "Loop ran, did nothing", ["The loop runs three times but its body does nothing."]),
        ("""
    score = 40
    if score > 50:
        pass  # TODO: add reward later
    else:
        print("Keep trying")""", "Keep trying", ["pass keeps the if block valid while you plan it."])],
    rules=["An empty block without pass is an IndentationError.",
           "pass is different from continue: pass does nothing and the code below it still runs.",
           "pass is common in empty functions and classes too."],
    mistake=("""
    if x > 5:
    print("done")""", "The if block is empty. Add pass (or real code) inside it."),
    q=[("What does pass do?", ["Ends the loop", "Nothing — it's a placeholder", "Skips to the next item", "Raises an error"], 1,
        "pass is a no-op statement."),
       ("Why would you use pass?", ["To speed up code", "To leave a block empty for now", "To print nothing", "To delete code"], 1,
        "Python requires a statement in every block."),
       ("What is printed?", ["a\nb", "b", "a", "Nothing"], 0,
        "pass does nothing, so both prints run.", 'for x in ["a", "b"]:\n    pass\n    print(x)', RUN),
       ("What happens with an empty if block and no pass?", ["Nothing", "IndentationError", "It runs forever", "It prints None"], 1,
        "Python expects an indented block.")]),

  S("Nested Loops", "Put a loop inside another loop.",
    """A nested loop is a loop inside another loop. For every single repetition of the outer loop,
    the inner loop runs completely.""",
    syntax="""
    for outer in sequence1:
        for inner in sequence2:
            ...""",
    ex=[("""
    for row in range(1, 3):
        for col in range(1, 4):
            print(row, col)""", "1 1\n1 2\n1 3\n2 1\n2 2\n2 3", ["The inner loop runs 3 times for each outer value.", "2 × 3 = 6 lines in total."]),
        ("""
    for i in range(1, 4):
        print("*" * i)""", "*\n**\n***", ["A simple pattern without nesting — compare it with the version above."]),
        ("""
    for i in range(1, 4):
        line = ""
        for j in range(i):
            line += "#"
        print(line)""", "#\n##\n###", ["The inner loop builds a line of i symbols."])],
    rules=["Total runs = outer count × inner count.",
           "Use different loop variable names (i, j or row, col).",
           "break inside the inner loop only stops the inner loop."],
    q=[("How many times does the inner print run?\nfor a in range(2):\n    for b in range(3):\n        print(a, b)", ["2", "3", "5", "6"], 3,
        "2 outer × 3 inner = 6."),
       ("What is printed?", ["1 1\n1 2\n2 1\n2 2", "1 2\n1 2", "1\n2\n1\n2", "11\n12\n21\n22"], 0,
        "For each i, j goes through 1 and 2.", "for i in [1, 2]:\n    for j in [1, 2]:\n        print(i, j)", RUN),
       ("Which loop finishes completely for each outer repetition?", ["The outer loop", "The inner loop", "Neither", "Both at once"], 1,
        "The inner loop runs fully every time the outer loop repeats."),
       ("Why use different names like i and j?", ["Python requires it", "So the loops don't overwrite each other's variable", "To make it faster", "No reason"], 1,
        "Reusing the same name in both loops causes confusing bugs.")]),
]),
]
