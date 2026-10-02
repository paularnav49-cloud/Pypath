from dsl import S, L

RUN = True

LEVELS = [
# ═══════════════════════════ LEVEL 10 ═══════════════════════════
L("Functions", "Package code into reusable, named blocks that take inputs and give back results.", [
  S("Defining Functions", "Create your own function with def.",
    """A function is a named block of code that does one job. You define it once with def and can
    then run it as many times as you like. Functions keep programs organised and avoid repetition.""",
    syntax="""
    def function_name():
        code_inside_function""",
    syn=["def starts the definition.", "The name is followed by () and a colon.", "The body is indented."],
    ex=[("""
    def greet():
        print("Hello!")
        print("Welcome to PyPath")

    greet()
    greet()""", "Hello!\nWelcome to PyPath\nHello!\nWelcome to PyPath", ["Defining a function doesn't run it.", "Each greet() call runs the whole body."])],
    rules=["A function must be defined before it is called.",
           "Function names follow the same rules as variables (snake_case).",
           "An empty function needs pass in its body."],
    mistake=("""
    say_hi()
    def say_hi():
        print("hi")""", "say_hi is called before it exists, so Python raises NameError."),
    q=[("Which keyword defines a function?", ["func", "def", "function", "define"], 1, "Functions are defined with def."),
       ("Does defining a function run its code?", ["Yes", "No — it runs when called", "Only the first line", "Only if it has a return"], 1, "The body runs only when you call the function."),
       ("What is printed?", ["Hi", "Hi\nHi", "Nothing", "Error"], 1, "The function is called twice.", 'def f():\n    print("Hi")\n\nf()\nf()', RUN),
       ("What must follow the function name in a def line?", ["()", "() and :", ";", "{ }"], 1, "def name(): — brackets then a colon.")]),

  S("Calling Functions", "Run a function by writing its name with brackets.",
    """To call (run) a function, write its name followed by parentheses. Python jumps into the
    function, runs its body, then comes back and continues where it left off.""",
    ex=[("""
    def line():
        print("----------")

    print("Start")
    line()
    print("Middle")
    line()
    print("End")""", "Start\n----------\nMiddle\n----------\nEnd", ["After the function finishes, Python returns to the next line."]),
        ("""
    def step_one():
        print("Step 1")

    def run_all():
        step_one()
        print("Step 2")

    run_all()""", "Step 1\nStep 2", ["Functions can call other functions."])],
    rules=["Without brackets you refer to the function instead of calling it: greet vs greet().",
           "You can call a function from inside another function.",
           "Built-ins like print() and len() are called exactly the same way."],
    q=[("How do you call a function named show?", ["show", "show()", "call show", "def show()"], 1, "Brackets call the function."),
       ("What is printed?", ["A\nB\nC", "B\nA\nC", "A\nC\nB", "A\nC"], 0, "Python runs b() in the middle.", 'def b():\n    print("B")\n\nprint("A")\nb()\nprint("C")', RUN),
       ("Can a function call another function?", ["Yes", "No", "Only built-ins", "Only once"], 0, "Functions can call any other function.")]),

  S("Parameters", "Let a function accept input values.",
    """Parameters are variables listed inside the brackets of a function definition. They act as
    placeholders for the values you pass in when you call the function.""",
    syntax="""
    def function_name(param1, param2):
        ...""",
    ex=[("""
    def greet(name):
        print("Hello,", name)

    greet("Asha")
    greet("Ravi")""", "Hello, Asha\nHello, Ravi", ["name is a parameter — it takes whatever value is passed in."]),
        ("""
    def rectangle_area(width, height):
        print(width * height)

    rectangle_area(4, 5)""", "20", ["A function can have several parameters, separated by commas."])],
    rules=["Parameters exist only inside the function.",
           "Calling with the wrong number of values raises TypeError.",
           "Give parameters descriptive names."],
    mistake=('def greet(name):\n    print(name)\n\ngreet()', "greet expects one value, so this raises TypeError: missing 1 required positional argument."),
    q=[("What is a parameter?", ["A value printed by a function", "A variable in the function definition that receives input", "A type of loop", "A return value"], 1, "Parameters are named in the def line."),
       ("What is printed?", ["7", "34", "x + y", "Error"], 0, "3 + 4 = 7.", "def add(x, y):\n    print(x + y)\n\nadd(3, 4)", RUN),
       ("What happens if you call def f(a, b) as f(1)?", ["b becomes 0", "TypeError", "It works", "b becomes None"], 1, "A required argument is missing.")]),

  S("Arguments", "Positional and keyword arguments.",
    """Arguments are the actual values you pass when calling a function. Positional arguments are
    matched by order. Keyword arguments are matched by name, so their order doesn't matter.""",
    syntax="""
    func(value1, value2)          # positional
    func(param2=value2, param1=value1)  # keyword""",
    ex=[("""
    def describe(name, age):
        print(f"{name} is {age}")

    describe("Asha", 21)
    describe(age=30, name="Ravi")
    describe("Meera", age=25)""", "Asha is 21\nRavi is 30\nMeera is 25", ["Positional: matched by position.", "Keyword: matched by name.", "You can mix them — positional first."])],
    rules=["Positional arguments must come before keyword arguments.",
           "Parameter = name in the definition; argument = value in the call.",
           "Keyword arguments make calls with many values easier to read."],
    mistake=('describe(name="Asha", 21)', "A positional argument can't follow a keyword argument — SyntaxError."),
    q=[("What is printed?", ["1 2", "2 1", "Error", "a b"], 1, "Keyword arguments are matched by name.", "def f(a, b):\n    print(a, b)\n\nf(b=1, a=2)", RUN),
       ("What's the difference between a parameter and an argument?", ["None", "Parameter is in the definition; argument is the value passed in the call", "Arguments are only numbers", "Parameters are only strings"], 1, "Parameters receive arguments."),
       ("Which call is invalid?", ["f(1, 2)", "f(a=1, b=2)", "f(1, b=2)", "f(a=1, 2)"], 3, "Positional arguments can't come after keyword ones.")]),

  S("Default Parameters", "Give parameters a value to use when none is passed.",
    """A default parameter has a value that's used if the caller leaves that argument out. This
    makes a function flexible while keeping simple calls short.""",
    syntax="""
    def func(param=default_value):
        ...""",
    ex=[("""
    def greet(name, greeting="Hello"):
        print(f"{greeting}, {name}!")

    greet("Asha")
    greet("Ravi", "Namaste")
    greet("Meera", greeting="Hi")""", "Hello, Asha!\nNamaste, Ravi!\nHi, Meera!", ["When greeting isn't given, \"Hello\" is used."])],
    rules=["Parameters with defaults must come after parameters without them.",
           "Don't use a mutable default like [] — use None and create the list inside.",
           "print() itself uses defaults: sep=\" \" and end=\"\\n\"."],
    mistake=("def f(a=1, b):\n    pass", "Non-default parameter b follows a default one — SyntaxError."),
    q=[("What is printed?", ["2", "3", "6", "Error"], 2, "Only x is passed, so n uses its default 3: 2 * 3 = 6.", "def mul(x, n=3):\n    print(x * n)\n\nmul(2)", RUN),
       ("What is printed?", ["10", "5", "15", "Error"], 0, "The passed 5 replaces the default.", "def f(x, y=1):\n    print(x * y)\n\nf(2, 5)", RUN),
       ("Which definition is valid?", ["def f(a=1, b):", "def f(a, b=1):", "def f(=1):", "def f(a b=1):"], 1, "Defaults go after required parameters.")]),

  S("return", "Send a result back from a function.",
    """return ends a function and sends a value back to the place where it was called. That value
    can be stored in a variable, printed or used in another calculation.""",
    syntax="""
    def func(...):
        return value""",
    ex=[("""
    def square(n):
        return n * n

    result = square(4)
    print(result)
    print(square(3) + square(2))""", "16\n13", ["square(4) becomes the value 16.", "Returned values can be used in expressions."]),
        ("""
    def min_max(nums):
        return min(nums), max(nums)

    low, high = min_max([4, 9, 1])
    print(low, high)

    def no_return():
        x = 1

    print(no_return())""", "1 9\nNone", ["Return several values as a tuple.", "A function without return gives back None."])],
    rules=["Code after return in the same block never runs.",
           "print shows a value; return hands it back. They're not the same.",
           "A function without return returns None."],
    mistake=("""
    def add(a, b):
        print(a + b)

    total = add(1, 2) * 2""", "add prints but doesn't return, so add(1, 2) is None and None * 2 raises TypeError. Use return a + b."),
    q=[("What does return do?", ["Prints a value", "Sends a value back to the caller", "Restarts the function", "Ends the program"], 1, "return passes a result back."),
       ("What is printed?", ["5", "10", "None", "Error"], 1, "double(5) returns 10.", "def double(x):\n    return x * 2\n\nprint(double(5))", RUN),
       ("What is printed?", ["1", "None", "Error", "0"], 1, "No return statement means None.", "def f():\n    x = 1\n\nprint(f())", RUN),
       ("What is printed?", ["A\nB", "A", "B", "Nothing"], 1, "Code after return never runs.", 'def f():\n    return "A"\n    print("B")\n\nprint(f())', RUN)]),

  S("*args", "Accept any number of positional arguments.",
    """Putting * before a parameter name collects any number of positional arguments into a tuple.
    By convention it's called args.""",
    syntax="""
    def func(*args):
        for item in args:
            ...""",
    ex=[("""
    def total(*numbers):
        print(numbers)
        return sum(numbers)

    print(total(1, 2, 3))
    print(total(10))
    print(total())""", "(1, 2, 3)\n6\n(10,)\n10\n()\n0", ["All arguments land in a tuple.", "Zero arguments is fine too."]),
        ("""
    nums = [4, 5, 6]
    print(*nums)
    print(max(*nums))""", "4 5 6\n6", ["* in a call does the opposite: it unpacks a list into separate arguments."])],
    rules=["The name after * can be anything; args is just a convention.",
           "*args must come after normal parameters.",
           "Inside the function, args is a tuple."],
    q=[("What type is args inside def f(*args)?", ["list", "tuple", "dict", "set"], 1, "*args collects arguments into a tuple."),
       ("What is printed?", ["3", "(1, 2, 3)", "6", "Error"], 0, "len counts the three arguments.", "def f(*args):\n    print(len(args))\n\nf(1, 2, 3)", RUN),
       ("What does print(*[1, 2]) show?", ["[1, 2]", "1 2", "*[1, 2]", "Error"], 1, "* unpacks the list into two arguments.")]),

  S("**kwargs", "Accept any number of keyword arguments.",
    """Putting ** before a parameter collects any keyword arguments into a dictionary. By convention
    it's called kwargs (keyword arguments).""",
    syntax="""
    def func(**kwargs):
        for key, value in kwargs.items():
            ...""",
    ex=[("""
    def profile(**info):
        for key, value in info.items():
            print(f"{key}: {value}")

    profile(name="Asha", city="Pune", level=3)""", "name: Asha\ncity: Pune\nlevel: 3", ["info is a dictionary of the keyword arguments."]),
        ("""
    def show(a, *args, **kwargs):
        print(a, args, kwargs)

    show(1, 2, 3, x=4)""", "1 (2, 3) {'x': 4}", ["Order: normal params, then *args, then **kwargs."])],
    rules=["kwargs is a dict inside the function.",
           "** in a call unpacks a dict into keyword arguments: f(**settings).",
           "Order of parameters: regular, *args, keyword-only, **kwargs."],
    q=[("What type is kwargs?", ["list", "tuple", "dict", "str"], 2, "**kwargs collects into a dictionary."),
       ("What is printed?", ["{'a': 1}", "(1,)", "a=1", "Error"], 0, "kwargs holds the keyword arguments.", "def f(**kwargs):\n    print(kwargs)\n\nf(a=1)", RUN),
       ("What's the right order in a definition?", ["**kwargs, *args", "*args, **kwargs", "Any order", "kwargs, args"], 1, "*args comes before **kwargs.")]),

  S("Scope", "Where variables live: local vs global.",
    """Scope decides where a variable can be used. Variables created inside a function are local —
    they exist only while the function runs. Variables created outside functions are global and can
    be read anywhere.""",
    ex=[("""
    message = "global"

    def show():
        message = "local"
        print(message)

    show()
    print(message)""", "local\nglobal", ["The function creates its own local message.", "The global one is untouched."]),
        ("""
    count = 0

    def increase():
        global count
        count += 1

    increase()
    increase()
    print(count)""", "2", ["global lets a function change a global variable.", "Use it sparingly — returning values is usually cleaner."])],
    rules=["Local variables disappear when the function ends.",
           "Reading a global inside a function is fine; assigning to it needs global.",
           "Prefer passing values in and returning results out."],
    mistake=("""
    def f():
        secret = 42

    f()
    print(secret)""", "secret is local to f, so printing it outside raises NameError."),
    q=[("Where can a local variable be used?", ["Anywhere", "Only inside its function", "Only in loops", "Only after the function"], 1, "Local variables live inside the function."),
       ("What is printed?", ["1", "5", "Error", "None"], 1, "The function's x is separate from the global x.", "x = 5\n\ndef f():\n    x = 1\n\nf()\nprint(x)", RUN),
       ("Which keyword lets a function change a global variable?", ["local", "global", "static", "extern"], 1, "global declares the global name."),
       ("What is printed?", ["10", "11", "Error", "None"], 1, "global n lets the function update it.", "n = 10\n\ndef inc():\n    global n\n    n += 1\n\ninc()\nprint(n)", RUN)]),

  S("Docstrings", "Document what your function does.",
    """A docstring is a string written as the first line of a function. It explains what the function
    does, its parameters and what it returns. Tools and editors show it as help.""",
    syntax='''
    def func(x):
        """Short description of what func does."""
        ...''',
    ex=[('''
    def area(r):
        """Return the area of a circle with radius r."""
        return 3.14159 * r * r

    print(area.__doc__)
    print(round(area(2), 2))''', "Return the area of a circle with radius r.\n12.57", ["__doc__ holds the docstring.", "help(area) would also show it."])],
    rules=["Use triple quotes for docstrings.",
           "Put it directly under the def line.",
           "Describe what the function does, not how."],
    q=[("Where does a docstring go?", ["At the end of the file", "As the first statement inside the function", "Before def", "In a comment"], 1, "It's the first line of the body."),
       ("What is printed?", ["Adds two numbers.", "None", "add", "Error"], 0, "__doc__ returns the docstring.", 'def add(a, b):\n    """Adds two numbers."""\n    return a + b\n\nprint(add.__doc__)', RUN),
       ("Which quotes are used for docstrings by convention?", ["Single ''", "Triple \"\"\"", "Backticks", "No quotes"], 1, "Triple double quotes are standard.")]),
]),

# ═══════════════════════════ LEVEL 11 ═══════════════════════════
L("Error Handling", "Catch and handle errors so programs don't crash unexpectedly.", [
  S("Errors & Exceptions", "What happens when something goes wrong.",
    """An exception is an error that happens while a program runs. If it isn't handled, Python stops
    and prints a traceback showing the error type and message.""",
    points=["ZeroDivisionError — dividing by zero", "ValueError — right type, wrong value, e.g. int(\"abc\")",
            "TypeError — wrong type, e.g. \"a\" + 1", "NameError — using a name that doesn't exist",
            "IndexError / KeyError — missing list index / dictionary key"],
    ex=[("""
    print("Before")
    print(10 / 0)
    print("After")""", "Before\nZeroDivisionError: division by zero", ["The error stops the program.", "\"After\" is never printed."])],
    rules=["SyntaxError happens before the program runs; exceptions happen while it runs.",
           "The last line of a traceback tells you the error type and message.",
           "Read error messages carefully — they usually point at the problem."],
    q=[("What does int(\"abc\") raise?", ["TypeError", "ValueError", "NameError", "KeyError"], 1, "The type is right (str) but the value can't be converted."),
       ("What does \"a\" + 1 raise?", ["TypeError", "ValueError", "IndexError", "No error"], 0, "You can't add str and int."),
       ("What happens to the code after an unhandled exception?", ["It still runs", "It doesn't run — the program stops", "It runs twice", "It is skipped then resumed"], 1, "An unhandled exception ends the program."),
       ("Using an undefined variable raises…", ["NameError", "KeyError", "TypeError", "ZeroDivisionError"], 0, "Unknown names raise NameError.")]),

  S("try", "Wrap risky code so errors can be caught.",
    """try marks a block of code that might fail. If an exception happens inside it, Python stops the
    try block immediately and looks for a matching except block instead of crashing.""",
    syntax="""
    try:
        risky_code
    except:
        handle_error""",
    ex=[("""
    try:
        print("Dividing...")
        print(10 / 0)
        print("Not reached")
    except ZeroDivisionError:
        print("Can't divide by zero")
    print("Program continues")""", "Dividing...\nCan't divide by zero\nProgram continues", ["Once the error occurs, the rest of try is skipped.", "The program doesn't crash."])],
    rules=["A try must be followed by at least one except or a finally.",
           "Keep the try block small — only the lines that might fail.",
           "If no error happens, the except block is skipped."],
    q=[("What is printed?", ["A\nB", "A\nC", "C", "A\nB\nC"], 1, "1/0 fails, so B is skipped and except runs.", 'try:\n    print("A")\n    x = 1 / 0\n    print("B")\nexcept ZeroDivisionError:\n    print("C")', RUN),
       ("Can try be used on its own?", ["Yes", "No — it needs except or finally", "Only in functions", "Only with loops"], 1, "try requires a handler or finally."),
       ("If no error occurs in try, what happens to except?", ["It runs anyway", "It's skipped", "It raises an error", "It runs first"], 1, "except only runs when an exception happens.")]),

  S("except", "Handle specific types of errors.",
    """except catches an exception. Name the exception type to catch only that kind of error, and
    use as to get the error object with its message.""",
    syntax="""
    try:
        ...
    except ValueError as e:
        print(e)""",
    ex=[("""
    for text in ["42", "hello"]:
        try:
            print(int(text) * 2)
        except ValueError as e:
            print("Not a number:", e)""", "84\nNot a number: invalid literal for int() with base 10: 'hello'", ["as e stores the exception.", "Printing it shows the message."]),
        ("""
    data = {"a": 1}
    try:
        print(data["b"])
    except (KeyError, IndexError):
        print("Missing item")""", "Missing item", ["A tuple catches several types with one except."])],
    rules=["Catch specific exceptions, not everything.",
           "A bare except: hides real bugs — avoid it.",
           "except Exception catches almost all errors when you truly need it."],
    mistake=("try:\n    x = int(input())\nexcept:\n    pass", "A bare except with pass silently hides every error, including typos. Catch ValueError instead."),
    q=[("What does except ValueError as e give you in e?", ["The line number", "The exception object", "The input value", "True"], 1, "e is the exception, and str(e) is its message."),
       ("What is printed?", ["bad", "Error", "0", "Nothing"], 0, "int(\"x\") raises ValueError, which is caught.", 'try:\n    int("x")\nexcept ValueError:\n    print("bad")', RUN),
       ("How do you catch two exception types in one except?", ["except A or B:", "except (A, B):", "except A, except B:", "except [A, B]:"], 1, "Use a tuple of types."),
       ("Why avoid a bare except:?", ["It's slower", "It hides unexpected bugs", "It's a SyntaxError", "It only catches TypeError"], 1, "It catches everything, including mistakes you'd want to see.")]),

  S("Multiple except Blocks", "Respond differently to different errors.",
    """You can add several except blocks after one try. Python checks them from top to bottom and
    runs the first one that matches the error.""",
    ex=[("""
    def safe_divide(a, b):
        try:
            return a / b
        except ZeroDivisionError:
            return "Error: divide by zero"
        except TypeError:
            return "Error: numbers only"

    print(safe_divide(10, 2))
    print(safe_divide(1, 0))
    print(safe_divide("5", 1))""", "5.0\nError: divide by zero\nError: numbers only", ["Each error type gets its own message."])],
    rules=["Put specific exceptions before general ones like Exception.",
           "Only one except block runs per error.",
           "Unmatched exceptions still crash the program."],
    q=[("How many except blocks run for one error?", ["All matching ones", "Only the first match", "None", "Two"], 1, "Python runs the first matching block only."),
       ("What is printed?", ["zero", "type", "zero\ntype", "Error"], 1, "\"a\" + 1 raises TypeError.", 'try:\n    "a" + 1\nexcept ZeroDivisionError:\n    print("zero")\nexcept TypeError:\n    print("type")', RUN),
       ("Where should except Exception go?", ["First", "Last", "Anywhere", "It can't be used"], 1, "General handlers go after specific ones.")]),

  S("else", "Run code only when no error happened.",
    """An else block after try/except runs only if the try block finished without any exception.
    It's the place for code that should run only on success.""",
    syntax="""
    try:
        ...
    except SomeError:
        ...
    else:
        runs_if_no_error""",
    ex=[("""
    for value in ["8", "x"]:
        try:
            n = int(value)
        except ValueError:
            print(value, "is invalid")
        else:
            print(value, "squared is", n * n)""", "8 squared is 64\nx is invalid", ["else runs for \"8\" because no error happened."])],
    rules=["else must come after all except blocks.",
           "Errors raised inside else are NOT caught by the excepts above it.",
           "Using else keeps the try block focused on the risky line."],
    q=[("When does the else block of a try run?", ["Always", "Only if an exception occurred", "Only if no exception occurred", "Never"], 2, "else is the success path."),
       ("What is printed?", ["ok", "fail", "ok\nfail", "Nothing"], 0, "No error, so else runs.", 'try:\n    x = 1\nexcept ValueError:\n    print("fail")\nelse:\n    print("ok")', RUN),
       ("Where does else go?", ["Before try", "Between try and except", "After all except blocks", "Inside except"], 2, "try → except(s) → else → finally.")]),

  S("finally", "Code that always runs, error or not.",
    """finally runs no matter what — whether the try succeeded, an exception was caught, or even if
    the function returns. It's used for clean-up like closing files or connections.""",
    syntax="""
    try:
        ...
    except SomeError:
        ...
    finally:
        always_runs""",
    ex=[("""
    def test(x):
        try:
            print(10 / x)
        except ZeroDivisionError:
            print("Bad input")
        finally:
            print("Done")

    test(2)
    test(0)""", "5.0\nDone\nBad input\nDone", ["finally runs after success and after an error."])],
    rules=["finally runs even if try contains return.",
           "Use finally for clean-up, not normal logic.",
           "try/finally without except is allowed."],
    q=[("When does finally run?", ["Only on errors", "Only on success", "Always", "Never"], 2, "finally always runs."),
       ("What is printed?", ["A", "A\nB", "B", "Error"], 1, "No error; finally still runs.", 'try:\n    print("A")\nfinally:\n    print("B")', RUN),
       ("What is finally typically used for?", ["Printing results", "Clean-up like closing files", "Raising errors", "Loops"], 1, "It guarantees clean-up happens.")]),

  S("raise", "Signal an error yourself.",
    """raise lets you create an exception on purpose when something is wrong — for example, invalid
    input to your function. The caller can then catch it with try/except.""",
    syntax='raise ValueError("Explain what went wrong")',
    ex=[("""
    def set_age(age):
        if age < 0:
            raise ValueError("Age can't be negative")
        return age

    print(set_age(20))
    try:
        set_age(-5)
    except ValueError as e:
        print("Error:", e)""", "20\nError: Age can't be negative", ["raise stops the function immediately.", "The message travels with the exception."])],
    rules=["Choose a fitting exception type (ValueError, TypeError…).",
           "Always include a clear message.",
           "A bare raise inside except re-raises the current error."],
    q=[("What does raise do?", ["Ignores an error", "Creates (throws) an exception", "Prints a message", "Ends a loop"], 1, "raise throws an exception."),
       ("What is printed?", ["too big", "5", "Error", "Nothing"], 0, "The raised error is caught and its message printed.", 'try:\n    raise ValueError("too big")\nexcept ValueError as e:\n    print(e)', RUN),
       ("Which is a good use of raise?", ["To print output", "When a function receives invalid input", "To exit a loop", "To import a module"], 1, "Raise errors for invalid states.")]),

  S("Custom Exceptions", "Create your own exception types.",
    """You can define your own exception by creating a class that inherits from Exception. Custom
    exceptions make errors in your program clearer and easier to catch precisely.""",
    syntax="""
    class MyError(Exception):
        pass""",
    ex=[("""
    class InsufficientFunds(Exception):
        pass

    def withdraw(balance, amount):
        if amount > balance:
            raise InsufficientFunds(f"Need {amount - balance} more")
        return balance - amount

    try:
        withdraw(100, 150)
    except InsufficientFunds as e:
        print("Failed:", e)""", "Failed: Need 50 more", ["The class just needs to inherit from Exception.", "It's raised and caught like any built-in error."])],
    rules=["Name custom exceptions ending in Error or describing the problem.",
           "Always inherit from Exception (or a subclass of it).",
           "You'll learn more about classes and inheritance in later levels."],
    q=[("What must a custom exception inherit from?", ["object", "Exception", "Error", "str"], 1, "Custom exceptions subclass Exception."),
       ("What is printed?", ["caught", "MyError", "Error", "Nothing"], 0, "The custom error is caught.", 'class MyError(Exception):\n    pass\n\ntry:\n    raise MyError()\nexcept MyError:\n    print("caught")', RUN),
       ("Why create custom exceptions?", ["They run faster", "They make specific problems clearer to catch", "They're required", "To avoid try"], 1, "They describe your program's own error cases.")]),
]),

# ═══════════════════════════ LEVEL 12 ═══════════════════════════
L("Modules", "Reuse code from Python's standard library and from your own files.", [
  S("What is a Module?", "A file of Python code you can reuse.",
    """A module is simply a .py file containing functions, variables and classes. Python comes with
    a huge standard library of modules — math, random, datetime and many more — ready to use.""",
    points=["Modules organise code into separate files", "The standard library is included with Python",
            "Thousands more modules can be installed with pip"],
    key="Don't reinvent the wheel — check if a module already does what you need.",
    ex=[("""
    import math
    print(math.sqrt(16))
    print(math.pi)""", "4.0\n3.141592653589793", ["import loads the math module.", "Use module.name to access what's inside."])],
    rules=["Module names are usually lowercase.",
           "Don't name your own file math.py or random.py — it hides the real module.",
           "dir(module) lists everything a module contains."],
    q=[("What is a module?", ["A type of loop", "A .py file of reusable code", "A variable", "An error"], 1, "Modules are Python files you can import."),
       ("What is printed?", ["3", "3.0", "9", "Error"], 1, "sqrt returns a float.", "import math\nprint(math.sqrt(9))", RUN),
       ("What is the standard library?", ["Modules that come with Python", "A website", "A book", "Your own files"], 0, "It ships with every Python install.")]),

  S("import", "Load a whole module.",
    """The import statement loads a module so you can use it. You then access its contents with a
    dot: module.function().""",
    syntax="import module_name",
    ex=[("""
    import math
    import datetime

    print(math.floor(4.7))
    print(math.ceil(4.2))
    print(datetime.date(2026, 1, 15).year)""", "4\n5\n2026", ["floor rounds down; ceil rounds up.", "Each module keeps its names behind its own prefix."])],
    rules=["Put imports at the top of the file.",
           "A module is only loaded once, even if imported many times.",
           "Calling a module function without the prefix raises NameError."],
    mistake=("import math\nprint(sqrt(25))", "sqrt lives inside math — write math.sqrt(25)."),
    q=[("How do you use pi after import math?", ["pi", "math.pi", "math(pi)", "import.pi"], 1, "Use module.name."),
       ("What is printed?", ["3", "4", "3.7", "Error"], 0, "floor rounds down.", "import math\nprint(math.floor(3.7))", RUN),
       ("Where should imports usually go?", ["At the bottom", "At the top of the file", "Inside loops", "Anywhere randomly"], 1, "Imports go at the top by convention.")]),

  S("from ... import", "Import specific names directly.",
    """from module import name brings specific items into your program so you can use them without
    the module prefix.""",
    syntax="from module import name1, name2",
    ex=[("""
    from math import sqrt, pi
    print(sqrt(49))
    print(round(pi, 3))""", "7.0\n3.142", ["sqrt and pi can be used directly."])],
    rules=["Only the names you list are imported.",
           "Avoid from module import * — it fills your program with unknown names.",
           "If two modules have the same name, the later import wins."],
    q=[("After from math import sqrt, how do you call it?", ["math.sqrt(4)", "sqrt(4)", "import sqrt(4)", "math(sqrt)"], 1, "The name is imported directly."),
       ("What is printed?", ["2.0", "8", "2", "Error"], 0, "sqrt returns a float.", "from math import sqrt\nprint(sqrt(4))", RUN),
       ("Why avoid from module import *?", ["It's slower to type", "It imports unknown names that can clash", "It's a SyntaxError", "It only imports one thing"], 1, "Star imports make it unclear where names come from.")]),

  S("Import Aliases", "Rename modules and names with as.",
    """as gives a module or imported name a shorter or clearer alias. This is common for long module
    names.""",
    syntax="import module as alias\nfrom module import name as alias",
    ex=[("""
    import math as m
    from datetime import date as d
    print(m.factorial(5))
    print(d(2026, 10, 2).month)""", "120\n10", ["m now refers to the math module.", "Popular aliases: import numpy as np, import pandas as pd."])],
    rules=["After aliasing, use the alias — the original name isn't defined.",
           "Stick to well-known aliases so others understand your code.",
           "Aliases are handy to avoid name clashes."],
    q=[("What is printed?", ["24", "4", "Error", "None"], 0, "4! = 24.", "import math as m\nprint(m.factorial(4))", RUN),
       ("After import math as m, does math.pi work?", ["Yes", "No — only m.pi", "Only in functions", "Only once"], 1, "Only the alias is defined."),
       ("What does as do in an import?", ["Deletes the module", "Gives it another name", "Copies it", "Runs it"], 1, "as creates an alias.")]),

  S("The random Module", "Generate random numbers and choices.",
    """random generates pseudo-random values — perfect for games, quizzes and simulations.
    random.seed() makes results repeatable, which is useful for testing.""",
    points=["random.randint(a, b) — whole number from a to b (both included)", "random.choice(seq) — one random item",
            "random.shuffle(list) — shuffle in place", "random.random() — float from 0.0 up to 1.0"],
    ex=[("""
    import random
    random.seed(1)
    print(random.randint(1, 6))
    print(random.choice(["rock", "paper", "scissors"]))
    nums = [1, 2, 3, 4]
    random.shuffle(nums)
    print(nums)""", "2\nscissors\n[3, 4, 2, 1]", ["With seed(1) these results are the same every run.", "Without a seed you'd get different values each time."])],
    rules=["randint includes both ends: randint(1, 6) can return 6.",
           "shuffle changes the list and returns None.",
           "Use the secrets module, not random, for passwords."],
    q=[("Can random.randint(1, 6) return 6?", ["Yes", "No", "Only with seed", "Only once"], 0, "Both ends are included."),
       ("What does random.choice([\"a\", \"b\"]) return?", ["Both items", "One random item", "The index", "A float"], 1, "choice picks one item."),
       ("What does random.seed() do?", ["Deletes randomness", "Makes random results repeatable", "Picks a number", "Imports random"], 1, "The same seed gives the same sequence.")]),

  S("The datetime Module", "Work with dates and times.",
    """datetime lets you create dates, find today's date and do date maths with timedelta.""",
    ex=[("""
    from datetime import date, timedelta
    exam = date(2026, 12, 1)
    start = date(2026, 10, 2)
    print((exam - start).days)
    print(start + timedelta(days=7))
    print(start.strftime("%d %B %Y"))""", "60\n2026-10-09\n02 October 2026", ["Subtracting dates gives a timedelta.", "strftime formats a date as text."])],
    rules=["date.today() gives the current date.",
           "Months and days must be valid — date(2026, 2, 30) raises ValueError.",
           "strftime codes: %d day, %m month, %Y year, %B month name."],
    q=[("What does date(2026, 1, 10) - date(2026, 1, 1) give in .days?", ["9", "10", "1", "Error"], 0, "There are 9 days between them."),
       ("What is printed?", ["2026-01-02", "2026-01-01", "2026-02-01", "Error"], 0, "One day is added.", "from datetime import date, timedelta\nprint(date(2026, 1, 1) + timedelta(days=1))", RUN),
       ("What is timedelta used for?", ["Time zones", "Durations / date maths", "Printing", "Sleeping"], 1, "timedelta represents a length of time.")]),

  S("Creating Your Own Module", "Split your program into files and import them.",
    """Any .py file can be imported as a module. Save functions in one file, then import that file by
    its name (without .py) from another file in the same folder.""",
    ex=[("""
    import helpers
    print(helpers.shout("hi"))
    print(helpers.VERSION)""", "HI!\n1.0", ["helpers.py is in the same folder.", "Its functions and variables are available with the helpers. prefix."],
         {"setup": "open('helpers.py','w').write('VERSION = \"1.0\"\\n\\ndef shout(text):\\n    return text.upper() + \"!\"\\n')"}),
        ("""
    # helpers.py
    VERSION = "1.0"

    def shout(text):
        return text.upper() + "!"

    if __name__ == "__main__":
        print(shout("testing"))""", None, ["This is the content of helpers.py.", "The if __name__ block runs only when the file is run directly, not when it is imported."])],
    rules=["Import by file name without .py: import helpers.",
           "The file must be in the same folder (or on Python's path).",
           "Use if __name__ == \"__main__\": for code that should only run directly."],
    q=[("How do you import a file called tools.py?", ["import tools.py", "import tools", "from tools.py", "include tools"], 1, "Leave off the .py extension."),
       ("When does code under if __name__ == \"__main__\": run?", ["Always", "Only when the file is run directly", "Only when imported", "Never"], 1, "__name__ is \"__main__\" only for the file you run."),
       ("Can any .py file be a module?", ["Yes", "No", "Only standard library files", "Only files named module.py"], 0, "Every Python file can be imported.")]),
]),

# ═══════════════════════════ LEVEL 13 ═══════════════════════════
L("File Handling", "Read from and write to files on your computer.", [
  S("Opening Files", "open() and file modes.",
    """open() connects your program to a file and returns a file object. The mode tells Python what
    you want to do: read, write or append.""",
    points=["\"r\" read (default) — error if the file doesn't exist", "\"w\" write — creates the file or ERASES existing content",
            "\"a\" append — adds to the end", "\"x\" create — error if the file already exists"],
    syntax='file = open("name.txt", "mode")\n...\nfile.close()',
    ex=[("""
    f = open("notes.txt", "w")
    f.write("Hello file")
    f.close()
    f = open("notes.txt", "r")
    print(f.read())
    f.close()""", "Hello file", ["Always close a file when you're done.", "The next sub-levels show a safer way."])],
    rules=["Opening a missing file in \"r\" mode raises FileNotFoundError.",
           "\"w\" wipes the file first — use \"a\" to keep existing content.",
           "Add encoding=\"utf-8\" when working with non-English text."],
    q=[("Which mode erases a file's content when opening it?", ["\"r\"", "\"a\"", "\"w\"", "\"x\""], 2, "\"w\" truncates the file."),
       ("What's the default mode of open()?", ["\"w\"", "\"r\"", "\"a\"", "\"rw\""], 1, "Files open for reading by default."),
       ("What error occurs reading a file that doesn't exist?", ["ValueError", "FileNotFoundError", "KeyError", "TypeError"], 1, "Python can't find the file.")]),

  S("The with Statement", "Open files safely so they close automatically.",
    """with opens a file and automatically closes it when the block ends — even if an error happens.
    It's the recommended way to work with files.""",
    syntax='with open("name.txt", "mode") as f:\n    work_with(f)',
    ex=[("""
    with open("hello.txt", "w") as f:
        f.write("Written safely")

    with open("hello.txt") as f:
        print(f.read())
    print(f.closed)""", "Written safely\nTrue", ["The file closes when the with block ends.", "f.closed confirms it."])],
    rules=["No need to call close() inside with.",
           "Use the file only inside the indented block.",
           "with works with other resources too — you'll meet context managers later."],
    q=[("What does with do for files?", ["Makes them faster", "Closes them automatically", "Deletes them", "Encrypts them"], 1, "The file is closed when the block exits."),
       ("Do you need f.close() inside a with block?", ["Yes", "No", "Only for writing", "Only for reading"], 1, "with handles closing."),
       ("Does with close the file if an error happens?", ["Yes", "No", "Only sometimes", "Only on Windows"], 0, "It's closed even on errors.")]),

  S("Reading Files", "read(), readline() and readlines().",
    """There are several ways to read a file: read() gets everything as one string, readline() gets one
    line, and readlines() gets a list of all lines.""",
    ex=[("""
    with open("fruits.txt") as f:
        content = f.read()
    print(content, end="")
    with open("fruits.txt") as f:
        print(f.readline().strip())
        print(f.readlines())""", "apple\nmango\nkiwi\napple\n['mango\\n', 'kiwi\\n']", ["read() returns the whole text (end=\"\" avoids an extra blank line).", "readline() returns the next line (with its \\n).", "readlines() returns the remaining lines."],
         {"setup": "open('fruits.txt','w').write('apple\\nmango\\nkiwi\\n')"})],
    rules=["Lines keep their \\n — use strip() to remove it.",
           "Once read, the file position moves on: reading again returns ''.",
           "Avoid read() on huge files; loop line by line instead."],
    q=[("What does read() return?", ["A list of lines", "The whole file as one string", "The first line", "The file name"], 1, "read() gives all the text."),
       ("What does readlines() return?", ["A string", "A list of lines", "A number", "A dictionary"], 1, "Each line becomes a list item."),
       ("Why use strip() on lines?", ["To remove the trailing \\n", "To delete the file", "To sort lines", "To count words"], 0, "Lines end with a newline character.")]),

  S("Reading Line by Line", "Loop over a file one line at a time.",
    """A file object can be looped over directly with for. Each iteration gives the next line. This
    is memory-efficient even for very large files.""",
    ex=[("""
    count = 0
    with open("log.txt") as f:
        for line in f:
            line = line.strip()
            if "ERROR" in line:
                print("Found:", line)
            count += 1
    print("Lines:", count)""", "Found: ERROR disk full\nLines: 3", ["Each loop iteration reads one line.", "Combine with if to filter lines."],
         {"setup": "open('log.txt','w').write('INFO start\\nERROR disk full\\nINFO end\\n')"})],
    rules=["for line in f is the most Pythonic way to read lines.",
           "Strip each line before comparing it.",
           "enumerate(f, start=1) gives line numbers."],
    q=[("What does for line in f: give each time?", ["One character", "One line", "The whole file", "One word"], 1, "Files iterate line by line."),
       ("Why is looping line by line good for big files?", ["It's prettier", "It doesn't load the whole file into memory", "It sorts lines", "It compresses the file"], 1, "Only one line is held at a time."),
       ("How can you get line numbers while looping?", ["range(f)", "enumerate(f, start=1)", "f.numbers()", "len(f)"], 1, "enumerate pairs each line with a number.")]),

  S("Writing Files", "Create files and write text with write().",
    """Open a file in \"w\" mode and call write() to put text in it. write() doesn't add a new line
    automatically, so include \\n yourself.""",
    syntax='with open("file.txt", "w") as f:\n    f.write("text\\n")',
    ex=[("""
    names = ["Asha", "Ravi", "Meera"]
    with open("names.txt", "w") as f:
        for n in names:
            f.write(n + "\\n")

    with open("names.txt") as f:
        print(f.read().strip())""", "Asha\nRavi\nMeera", ["Each write adds a name and a newline."]),
        ("""
    with open("out.txt", "w") as f:
        print("Using print", file=f)
    with open("out.txt") as f:
        print(f.read().strip())""", "Using print", ["print(..., file=f) writes to a file and adds \\n for you."])],
    rules=["write() only accepts strings — convert numbers with str().",
           "\"w\" overwrites the existing file every time.",
           "writelines(list) writes several strings at once (no newlines added)."],
    mistake=('with open("n.txt", "w") as f:\n    f.write(42)', "write() needs a string: f.write(str(42))."),
    q=[("Does write() add a newline automatically?", ["Yes", "No", "Only at the end", "Only for numbers"], 1, "Add \\n yourself."),
       ("What happens to existing content when opening with \"w\"?", ["It's kept", "It's erased", "It's moved", "It's appended to"], 1, "\"w\" starts with an empty file."),
       ("What does f.write(5) cause?", ["Writes 5", "TypeError", "Writes nothing", "Writes '5\\n'"], 1, "write() requires a str.")]),

  S("Appending to Files", "Add to the end of a file without erasing it.",
    """Append mode \"a\" opens a file and moves to the end, so new writes are added after the existing
    content. If the file doesn't exist, it's created.""",
    ex=[("""
    with open("diary.txt", "a") as f:
        f.write("Day 2: learned files\\n")

    with open("diary.txt") as f:
        print(f.read().strip())""", "Day 1: started Python\nDay 2: learned files", ["The original line is kept; the new one is added below."],
         {"setup": "open('diary.txt','w').write('Day 1: started Python\\n')"})],
    rules=["Use \"a\" for logs and records you add to over time.",
           "Append mode can't move back to edit earlier lines.",
           "Remember the \\n at the end of each entry."],
    q=[("Which mode adds to the end of a file?", ["\"r\"", "\"w\"", "\"a\"", "\"x\""], 2, "\"a\" is append."),
       ("What happens if the file doesn't exist in \"a\" mode?", ["Error", "It's created", "Nothing", "It asks the user"], 1, "Append creates missing files."),
       ("What is a typical use for append mode?", ["Reading settings", "Adding to a log file", "Deleting data", "Sorting files"], 1, "Logs grow over time.")]),

  S("Handling File Errors", "Deal with missing files and other problems.",
    """File operations can fail — the file may not exist or you may not have permission. Wrap them in
    try/except so your program can respond gracefully.""",
    ex=[("""
    try:
        with open("missing.txt") as f:
            print(f.read())
    except FileNotFoundError:
        print("File not found — creating it")
        with open("missing.txt", "w") as f:
            f.write("new file")""", "File not found — creating it", ["Catch FileNotFoundError specifically."]),
        ("""
    import os
    print(os.path.exists("data.txt"))
    with open("data.txt", "w") as f:
        f.write("x")
    print(os.path.exists("data.txt"))""", "False\nTrue", ["os.path.exists() checks if a file is there."])],
    rules=["FileNotFoundError: the file doesn't exist.",
           "PermissionError: you're not allowed to open it.",
           "IsADirectoryError: you tried to open a folder as a file."],
    q=[("Which exception should you catch for a missing file?", ["KeyError", "FileNotFoundError", "IndexError", "ValueError"], 1, "Opening a missing file raises FileNotFoundError."),
       ("How can you check if a file exists without opening it?", ["os.path.exists(name)", "open(name).exists()", "exists(name)", "file.check()"], 0, "os.path.exists returns True or False."),
       ("What does PermissionError mean?", ["File missing", "Not allowed to access the file", "File too big", "Wrong mode name"], 1, "You lack permission for that file.")]),
]),
]
