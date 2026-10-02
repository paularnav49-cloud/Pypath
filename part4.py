from dsl import S, L

RUN = True

LEVELS = [
# ═══════════════════════════ LEVEL 14 ═══════════════════════════
L("Classes & Objects", "Model real-world things with object-oriented programming.", [
  S("Classes", "A blueprint for creating objects.",
    """A class is a blueprint that describes what data an object holds and what it can do. Think of a
    class as the design of a car, and objects as the actual cars built from it.""",
    syntax="""
    class ClassName:
        body""",
    ex=[("""
    class Dog:
        pass

    print(Dog)
    print(type(Dog))""", "<class '__main__.Dog'>\n<class 'type'>", ["class creates a new type called Dog.", "pass keeps the body empty for now."])],
    rules=["Class names use CapitalisedWords (PascalCase): BankAccount.",
           "A class body is indented like a function body.",
           "Defining a class doesn't create any objects yet."],
    q=[("Which keyword creates a class?", ["def", "class", "object", "new"], 1, "Classes are defined with class."),
       ("What naming style do class names use?", ["snake_case", "PascalCase", "UPPER_CASE", "kebab-case"], 1, "e.g. BankAccount."),
       ("A class is best described as…", ["A loop", "A blueprint for objects", "A list", "A file"], 1, "Objects are built from classes.")]),

  S("Objects", "Create instances of a class.",
    """An object (or instance) is a real thing built from a class. You create one by calling the class
    like a function. Each object is separate from the others.""",
    syntax="my_object = ClassName()",
    ex=[("""
    class Dog:
        pass

    a = Dog()
    b = Dog()
    print(isinstance(a, Dog))
    print(a is b)
    a.name = "Bruno"
    print(a.name)""", "True\nFalse\nBruno", ["a and b are two different Dog objects.", "isinstance checks an object's class."])],
    rules=["Calling ClassName() creates a new object every time.",
           "Objects of the same class are independent.",
           "Everything in Python is an object — even ints and strings."],
    q=[("How do you create an object of class Car?", ["Car", "Car()", "new Car", "class Car()"], 1, "Call the class."),
       ("What is printed?", ["True", "False", "Error", "None"], 1, "Each call creates a new, separate object.", "class A:\n    pass\n\nprint(A() is A())", RUN),
       ("Another word for object is…", ["Instance", "Module", "Loop", "Keyword"], 0, "Objects are instances of a class.")]),

  S("__init__", "Set up a new object with starting values.",
    """__init__ is a special method that runs automatically every time a new object is created. It is
    used to give the object its starting data (attributes).""",
    syntax="""
    class ClassName:
        def __init__(self, value):
            self.value = value""",
    ex=[("""
    class Student:
        def __init__(self, name, grade):
            print("Creating", name)
            self.name = name
            self.grade = grade

    s = Student("Asha", 9)
    print(s.name, s.grade)""", "Creating Asha\nAsha 9", ["Arguments to Student(...) are passed to __init__.", "__init__ runs once per object."])],
    rules=["It's spelled with two underscores on each side.",
           "__init__ must not return a value.",
           "Missing arguments raise TypeError, just like functions."],
    mistake=("class P:\n    def _init_(self, n):\n        self.n = n", "Single underscores: _init_ is just a normal method, so P(5) fails. Use __init__."),
    q=[("When does __init__ run?", ["When the class is defined", "Each time an object is created", "When the program ends", "Only when called manually"], 1, "It's called automatically on creation."),
       ("What is printed?", ["5", "x", "Error", "None"], 0, "__init__ stores 5 in self.x.", "class P:\n    def __init__(self, x):\n        self.x = x\n\nprint(P(5).x)", RUN),
       ("What is __init__ mainly used for?", ["Deleting objects", "Setting initial attributes", "Printing", "Importing"], 1, "It initialises the object.")]),

  S("self", "How an object refers to itself.",
    """self is the first parameter of every method. It refers to the particular object the method is
    working on, so self.name means \"this object's name\". Python passes it automatically.""",
    ex=[("""
    class Counter:
        def __init__(self):
            self.count = 0

        def tick(self):
            self.count += 1

    a = Counter()
    b = Counter()
    a.tick()
    a.tick()
    b.tick()
    print(a.count, b.count)""", "2 1", ["a.tick() passes a as self; b.tick() passes b.", "Each object keeps its own count."])],
    rules=["self must be the first parameter of instance methods.",
           "You don't pass self yourself — obj.method() does it.",
           "Forgetting self. creates a local variable instead of an attribute."],
    mistake=("class C:\n    def set(self, v):\n        value = v", "value is local and vanishes. Write self.value = v to store it on the object."),
    q=[("What does self refer to?", ["The class", "The current object", "The module", "The parent class"], 1, "self is the object the method was called on."),
       ("Do you pass self when calling obj.method()?", ["Yes", "No — Python does it", "Only in __init__", "Only for strings"], 1, "It's passed automatically."),
       ("What is printed?", ["1 1", "2 0", "1 0", "Error"], 2, "Only a's value changed.", "class C:\n    def __init__(self):\n        self.v = 0\n    def up(self):\n        self.v += 1\n\na, b = C(), C()\na.up()\nprint(a.v, b.v)", RUN)]),

  S("Attributes", "Data stored on objects.",
    """Attributes are variables that belong to an object. Read and change them with dot notation:
    object.attribute.""",
    ex=[("""
    class Phone:
        def __init__(self, brand, battery):
            self.brand = brand
            self.battery = battery

    p = Phone("Nokia", 80)
    p.battery -= 30
    print(p.brand, p.battery)
    print(hasattr(p, "brand"), getattr(p, "color", "unknown"))""", "Nokia 50\nTrue unknown", ["Attributes can be changed after creation.", "getattr can return a default for missing attributes."])],
    rules=["Accessing a missing attribute raises AttributeError.",
           "Define all attributes in __init__ so every object has them.",
           "vars(obj) shows an object's attributes as a dict."],
    q=[("How do you read attribute size of object box?", ["box[size]", "box.size", "box->size", "size(box)"], 1, "Use dot notation."),
       ("What error does a missing attribute cause?", ["KeyError", "AttributeError", "NameError", "IndexError"], 1, "Objects raise AttributeError."),
       ("What is printed?", ["10", "15", "5", "Error"], 1, "The attribute is updated to 15.", "class B:\n    def __init__(self):\n        self.n = 10\n\nb = B()\nb.n += 5\nprint(b.n)", RUN)]),

  S("Methods", "Functions that belong to a class.",
    """A method is a function defined inside a class. It describes something an object can do and
    usually works with the object's attributes through self.""",
    ex=[("""
    class BankAccount:
        def __init__(self, owner, balance=0):
            self.owner = owner
            self.balance = balance

        def deposit(self, amount):
            self.balance += amount

        def withdraw(self, amount):
            if amount > self.balance:
                print("Insufficient funds")
            else:
                self.balance -= amount

    acc = BankAccount("Ravi", 100)
    acc.deposit(50)
    acc.withdraw(500)
    print(acc.balance)""", "Insufficient funds\n150", ["Methods change the object's own data.", "Call them with object.method(...)."])],
    rules=["Methods always take self first.",
           "Methods can return values like normal functions.",
           "Methods can call other methods with self.other()."],
    q=[("What is a method?", ["A variable", "A function defined in a class", "A module", "A loop"], 1, "Methods belong to classes."),
       ("What is printed?", ["Hi, Asha", "Hi, name", "Error", "None"], 0, "greet uses the object's name.", 'class P:\n    def __init__(self, name):\n        self.name = name\n    def greet(self):\n        return "Hi, " + self.name\n\nprint(P("Asha").greet())', RUN),
       ("How does one method call another in the same object?", ["other()", "self.other()", "class.other()", "call other"], 1, "Use self.")]),

  S("Class vs Instance Attributes", "Shared data vs per-object data.",
    """Instance attributes (self.x) belong to one object. Class attributes are defined directly in the
    class body and are shared by every object of that class.""",
    ex=[("""
    class Car:
        wheels = 4
        count = 0

        def __init__(self, model):
            self.model = model
            Car.count += 1

    a = Car("Swift")
    b = Car("Creta")
    print(a.wheels, b.wheels)
    print(a.model, b.model)
    print(Car.count)""", "4 4\nSwift Creta\n2", ["wheels and count are shared by all cars.", "model is different for each car."])],
    rules=["Update shared values through the class: Car.count += 1.",
           "Assigning obj.attr = x creates an instance attribute that hides the class one.",
           "Don't use mutable class attributes (like lists) for per-object data."],
    q=[("Where is a class attribute defined?", ["In __init__ with self", "Directly in the class body", "In a function outside", "In a module"], 1, "It's in the class body."),
       ("What is printed?", ["1", "2", "0", "Error"], 1, "Both objects increased the shared counter.", "class A:\n    n = 0\n    def __init__(self):\n        A.n += 1\n\nA()\nA()\nprint(A.n)", RUN),
       ("Instance attributes are…", ["Shared by all objects", "Unique to each object", "Constants", "Only in modules"], 1, "self.x belongs to one object.")]),

  S("__str__ and __repr__", "Control how objects are printed.",
    """By default, printing an object shows something like <__main__.Book object at 0x...>. Define
    __str__ to return a friendly string, and __repr__ for a developer-focused one.""",
    ex=[("""
    class Book:
        def __init__(self, title, pages):
            self.title = title
            self.pages = pages

        def __str__(self):
            return f"{self.title} ({self.pages} pages)"

        def __repr__(self):
            return f"Book({self.title!r}, {self.pages})"

    b = Book("Python 101", 250)
    print(b)
    print([b])""", "Python 101 (250 pages)\n[Book('Python 101', 250)]", ["print uses __str__.", "Lists and the console show __repr__."])],
    rules=["__str__ and __repr__ must return strings.",
           "If only __repr__ exists, print uses it too.",
           "Methods with double underscores are called \"dunder\" (magic) methods."],
    q=[("Which method does print(obj) use?", ["__init__", "__str__", "__print__", "__show__"], 1, "print calls str(obj) → __str__."),
       ("What is printed?", ["Point(1, 2)", "<Point object>", "(1, 2)", "Error"], 2, "__str__ returns \"(1, 2)\".", 'class Point:\n    def __init__(self, x, y):\n        self.x, self.y = x, y\n    def __str__(self):\n        return f"({self.x}, {self.y})"\n\nprint(Point(1, 2))', RUN),
       ("What must __str__ return?", ["A number", "A string", "None", "A list"], 1, "It must return str.")]),
]),

# ═══════════════════════════ LEVEL 15 ═══════════════════════════
L("Inheritance & OOP Principles", "Reuse and extend classes, and apply core OOP ideas.", [
  S("Inheritance", "Create a new class based on an existing one.",
    """Inheritance lets a child class reuse the attributes and methods of a parent class. The child
    can then add its own features. This avoids repeating code.""",
    syntax="""
    class Child(Parent):
        ...""",
    ex=[("""
    class Animal:
        def __init__(self, name):
            self.name = name

        def eat(self):
            print(self.name, "is eating")

    class Dog(Animal):
        def bark(self):
            print(self.name, "says Woof")

    d = Dog("Bruno")
    d.eat()
    d.bark()
    print(isinstance(d, Animal))""", "Bruno is eating\nBruno says Woof\nTrue", ["Dog inherits __init__ and eat from Animal.", "A Dog is also an Animal."])],
    rules=["Put the parent class in brackets after the child's name.",
           "issubclass(Dog, Animal) checks the relationship between classes.",
           "Use inheritance for \"is a\" relationships (a Dog is an Animal)."],
    q=[("How does class Cat inherit from Animal?", ["class Cat -> Animal:", "class Cat(Animal):", "class Cat extends Animal:", "class Animal(Cat):"], 1, "Parent goes in brackets."),
       ("What is printed?", ["hello", "Error", "None", "B"], 0, "B inherits hi() from A.", 'class A:\n    def hi(self):\n        return "hello"\n\nclass B(A):\n    pass\n\nprint(B().hi())', RUN),
       ("Inheritance models which relationship?", ["has a", "is a", "uses a", "none"], 1, "A child \"is a\" kind of parent.")]),

  S("super()", "Call the parent class's methods.",
    """super() gives access to the parent class. It's most often used in __init__ so the parent can set
    up its attributes before the child adds its own.""",
    ex=[("""
    class Person:
        def __init__(self, name):
            self.name = name

    class Student(Person):
        def __init__(self, name, school):
            super().__init__(name)
            self.school = school

    s = Student("Asha", "DPS")
    print(s.name, "-", s.school)""", "Asha - DPS", ["super().__init__(name) runs Person's setup.", "Then Student adds school."])],
    rules=["If a child defines __init__, the parent's __init__ won't run unless you call super().__init__().",
           "Don't pass self to super().__init__().",
           "super() works for any method, not just __init__."],
    q=[("What does super() refer to?", ["The child class", "The parent class", "The object", "The module"], 1, "super() reaches the parent."),
       ("What is printed?", ["1 2", "2 1", "Error", "1"], 0, "super sets a, then b is added.", "class A:\n    def __init__(self, a):\n        self.a = a\n\nclass B(A):\n    def __init__(self, a, b):\n        super().__init__(a)\n        self.b = b\n\nx = B(1, 2)\nprint(x.a, x.b)", RUN),
       ("Why call super().__init__() in a child's __init__?", ["To delete the parent", "So the parent's setup also runs", "It's never needed", "To make it faster"], 1, "Otherwise parent attributes aren't set.")]),

  S("Method Overriding", "Replace a parent's method in the child.",
    """A child class can define a method with the same name as one in the parent. The child's version
    overrides (replaces) the parent's for objects of the child class.""",
    ex=[("""
    class Shape:
        def area(self):
            return 0

        def describe(self):
            return f"Area: {self.area()}"

    class Square(Shape):
        def __init__(self, side):
            self.side = side

        def area(self):
            return self.side ** 2

    print(Shape().describe())
    print(Square(3).describe())""", "Area: 0\nArea: 9", ["Square overrides area().", "describe() automatically uses the right version."])],
    rules=["The overriding method should keep the same parameters.",
           "Use super().method() to extend instead of fully replace.",
           "Python picks the method from the object's own class first."],
    q=[("What is printed?", ["A", "B", "AB", "Error"], 1, "B's speak overrides A's.", 'class A:\n    def speak(self):\n        return "A"\n\nclass B(A):\n    def speak(self):\n        return "B"\n\nprint(B().speak())', RUN),
       ("What is method overriding?", ["Calling a method twice", "Redefining a parent method in a child class", "Deleting a method", "A syntax error"], 1, "The child provides its own version."),
       ("How can an overriding method also run the parent's version?", ["parent.method()", "super().method()", "self.parent()", "It can't"], 1, "super() calls the parent version.")]),

  S("Multiple Inheritance", "Inherit from more than one parent.",
    """A class can inherit from several parents at once. Python searches them left to right using the
    Method Resolution Order (MRO) to decide which method to use.""",
    syntax="class Child(ParentA, ParentB):",
    ex=[("""
    class Flyer:
        def move(self):
            return "flying"

    class Swimmer:
        def move(self):
            return "swimming"

        def dive(self):
            return "diving"

    class Duck(Flyer, Swimmer):
        pass

    d = Duck()
    print(d.move(), d.dive())
    print([c.__name__ for c in Duck.__mro__])""", "flying diving\n['Duck', 'Flyer', 'Swimmer', 'object']", ["Flyer is listed first, so its move() wins.", "__mro__ shows the search order."])],
    rules=["Parent order matters — leftmost first.",
           "Keep multiple inheritance simple; it can get confusing.",
           "Small \"mixin\" classes that add one feature are a common use."],
    q=[("What is printed?", ["A", "B", "Error", "AB"], 0, "A is first in the parent list.", 'class A:\n    def f(self):\n        return "A"\n\nclass B:\n    def f(self):\n        return "B"\n\nclass C(A, B):\n    pass\n\nprint(C().f())', RUN),
       ("What does MRO stand for?", ["Main Run Order", "Method Resolution Order", "Module Return Object", "Multiple Run Option"], 1, "It's the order Python searches classes."),
       ("Can a Python class have two parents?", ["Yes", "No", "Only built-ins", "Only with import"], 0, "Python supports multiple inheritance.")]),

  S("Encapsulation", "Protect an object's internal data.",
    """Encapsulation means keeping data inside an object and controlling access through methods. By
    convention, a leading underscore marks an attribute as internal; two underscores trigger name
    mangling to make it harder to reach from outside.""",
    ex=[("""
    class Account:
        def __init__(self, balance):
            self.__balance = balance

        def deposit(self, amount):
            if amount > 0:
                self.__balance += amount

        def get_balance(self):
            return self.__balance

    a = Account(100)
    a.deposit(50)
    a.deposit(-999)
    print(a.get_balance())
    print(hasattr(a, "__balance"))""", "150\nFalse", ["The negative deposit is rejected by the method.", "__balance can't be reached directly from outside."])],
    rules=["_name: \"internal, please don't touch\" (convention).",
           "__name: name-mangled to _ClassName__name.",
           "Expose data through methods or @property for validation."],
    q=[("What does encapsulation mean?", ["Copying objects", "Hiding internal data and controlling access", "Inheriting classes", "Deleting attributes"], 1, "Data is accessed through controlled methods."),
       ("What does a single leading underscore (_x) signal?", ["A syntax error", "Internal use by convention", "A constant", "A class attribute"], 1, "It's a naming convention."),
       ("What is printed?", ["True", "False", "Error", "None"], 1, "__secret is name-mangled.", 'class S:\n    def __init__(self):\n        self.__secret = 1\n\nprint(hasattr(S(), "__secret"))', RUN)]),

  S("Properties", "Use @property for smart attributes.",
    """@property turns a method into something you access like an attribute. Paired with a setter, it
    lets you validate values whenever they're changed.""",
    ex=[("""
    class Temperature:
        def __init__(self, celsius):
            self.celsius = celsius

        @property
        def fahrenheit(self):
            return self.celsius * 9 / 5 + 32

        @property
        def celsius(self):
            return self._celsius

        @celsius.setter
        def celsius(self, value):
            if value < -273.15:
                raise ValueError("Too cold!")
            self._celsius = value

    t = Temperature(25)
    print(t.fahrenheit)
    t.celsius = 100
    print(t.fahrenheit)""", "77.0\n212.0", ["fahrenheit is calculated, not stored.", "The setter validates every new celsius value."])],
    rules=["Access properties without brackets: t.fahrenheit.",
           "Without a setter, the property is read-only.",
           "Store the real value in an underscore attribute."],
    q=[("How do you access a property called area?", ["obj.area()", "obj.area", "obj[area]", "area(obj)"], 1, "Properties look like attributes."),
       ("What is printed?", ["6", "Error", "None", "area"], 0, "area is computed on access.", "class R:\n    def __init__(self):\n        self.w, self.h = 2, 3\n    @property\n    def area(self):\n        return self.w * self.h\n\nprint(R().area)", RUN),
       ("What is a property setter useful for?", ["Validating new values", "Deleting objects", "Printing", "Importing"], 0, "Setters can check values before storing.")]),

  S("Polymorphism", "One interface, many forms.",
    """Polymorphism means different classes can share the same method name, and code can call that
    method without caring which class the object is. Each object responds in its own way.""",
    ex=[("""
    class Cat:
        def sound(self):
            return "Meow"

    class Cow:
        def sound(self):
            return "Moo"

    class Duck:
        def sound(self):
            return "Quack"

    for animal in [Cat(), Cow(), Duck()]:
        print(animal.sound())""", "Meow\nMoo\nQuack", ["The loop doesn't check the type — it just calls sound()."]),
        ("""
    print(len("hello"), len([1, 2]), len({"a": 1}))""", "5 2 1", ["Built-ins are polymorphic too: len works on many types."])],
    rules=["Python uses \"duck typing\": if it has the method, it can be used.",
           "Polymorphism often works together with inheritance and overriding.",
           "It makes code flexible and easy to extend."],
    q=[("What is polymorphism?", ["Many classes sharing a method name and behaving differently", "Copying a class", "One class with many objects", "A loop"], 0, "Same interface, different behaviour."),
       ("What is printed?", ["1\n2", "2\n1", "Error", "1"], 0, "Each object returns its own value.", "class A:\n    def v(self):\n        return 1\n\nclass B:\n    def v(self):\n        return 2\n\nfor o in [A(), B()]:\n    print(o.v())", RUN),
       ("\"Duck typing\" means…", ["Only ducks can be objects", "If an object has the needed method, it can be used", "Types must be declared", "Classes must inherit from Duck"], 1, "Behaviour matters more than type.")]),
]),

# ═══════════════════════════ LEVEL 16 ═══════════════════════════
L("Functional Tools", "Write compact code with lambdas and Python's built-in helpers.", [
  S("Lambda Functions", "Small anonymous functions in one line.",
    """A lambda is a tiny function written in a single expression, without def or a name. It's used
    for short operations, especially as an argument to other functions.""",
    syntax="lambda parameters: expression",
    ex=[("""
    square = lambda x: x * x
    add = lambda a, b: a + b
    print(square(5))
    print(add(2, 3))
    print((lambda s: s.upper())("hi"))""", "25\n5\nHI", ["The expression's value is returned automatically.", "Lambdas can be called right away."])],
    rules=["A lambda can contain only one expression — no statements or loops.",
           "No return keyword is used.",
           "If it gets complicated, use def instead."],
    q=[("What is printed?", ["6", "9", "3", "Error"], 1, "3 * 3 = 9.", "f = lambda x: x * 3\nprint(f(3))", RUN),
       ("Does a lambda use the return keyword?", ["Yes", "No — the expression is returned", "Only sometimes", "Only with def"], 1, "The result is returned automatically."),
       ("Which is a valid lambda?", ["lambda x: x + 1", "lambda(x): return x", "def lambda x: x", "lambda x => x"], 0, "lambda params: expression.")]),

  S("map()", "Apply a function to every item.",
    """map(function, iterable) applies a function to each item and returns a map object (an iterator)
    of the results. Wrap it in list() to see them.""",
    ex=[("""
    nums = [1, 2, 3, 4]
    print(list(map(lambda n: n * 10, nums)))
    print(list(map(str, nums)))
    print(list(map(int, ["5", "6"])))""", "[10, 20, 30, 40]\n['1', '2', '3', '4']\n[5, 6]", ["Any function works, including built-ins like str and int."])],
    rules=["map returns an iterator, not a list.",
           "It can only be looped over once.",
           "A list comprehension is often more readable."],
    q=[("What is printed?", ["[2, 4, 6]", "[1, 2, 3]", "<map object>", "Error"], 0, "Each item is doubled.", "print(list(map(lambda x: x * 2, [1, 2, 3])))", RUN),
       ("What does map() return?", ["A list", "An iterator (map object)", "A tuple", "A number"], 1, "Wrap in list() to see values."),
       ("What does list(map(int, [\"1\", \"2\"])) give?", ["[\"1\", \"2\"]", "[1, 2]", "3", "Error"], 1, "int is applied to each string.")]),

  S("filter()", "Keep only the items that pass a test.",
    """filter(function, iterable) keeps the items for which the function returns True.""",
    ex=[("""
    nums = [5, 12, 7, 20, 3]
    print(list(filter(lambda n: n > 6, nums)))
    words = ["", "hi", "", "yo"]
    print(list(filter(None, words)))""", "[12, 7, 20]\n['hi', 'yo']", ["Only items where the test is True are kept.", "filter(None, ...) removes falsy values."])],
    rules=["The function must return True or False (or truthy/falsy).",
           "filter returns an iterator.",
           "The original list is not changed."],
    q=[("What is printed?", ["[2, 4]", "[1, 3]", "[1, 2, 3, 4]", "Error"], 0, "Only even numbers pass.", "print(list(filter(lambda x: x % 2 == 0, [1, 2, 3, 4])))", RUN),
       ("What does filter keep?", ["Items where the function returns True", "The first item", "Items where it returns False", "Everything"], 0, "It filters by a condition."),
       ("Does filter change the original list?", ["Yes", "No", "Only if sorted", "Only with None"], 1, "It produces new results.")]),

  S("sorted() with key", "Sort by any rule you choose.",
    """sorted() returns a new sorted list. The key parameter takes a function that decides what to
    sort by, and reverse=True sorts in descending order.""",
    ex=[("""
    words = ["banana", "kiwi", "apple"]
    print(sorted(words))
    print(sorted(words, key=len))
    students = [("Asha", 88), ("Ravi", 95), ("Meera", 72)]
    print(sorted(students, key=lambda s: s[1], reverse=True))""", "['apple', 'banana', 'kiwi']\n['kiwi', 'apple', 'banana']\n[('Ravi', 95), ('Asha', 88), ('Meera', 72)]", ["key=len sorts by length.", "A lambda can pick which part to sort on."])],
    rules=["sorted() returns a new list; list.sort() sorts in place.",
           "key receives each item and returns the value to compare.",
           "max() and min() also accept key."],
    q=[("What is printed?", ["['bb', 'a', 'ccc']", "['a', 'bb', 'ccc']", "['ccc', 'bb', 'a']", "Error"], 1, "Sorted by length.", 'print(sorted(["ccc", "a", "bb"], key=len))', RUN),
       ("What does reverse=True do?", ["Sorts descending", "Reverses strings", "Removes duplicates", "Nothing"], 0, "Largest first."),
       ("What is printed?", ["apple", "fig", "banana", "Error"], 2, "banana is the longest.", 'print(max(["fig", "banana", "apple"], key=len))', RUN)]),

  S("zip()", "Pair up items from several sequences.",
    """zip() combines items from two or more iterables position by position, producing tuples.""",
    ex=[("""
    names = ["Asha", "Ravi", "Meera"]
    scores = [88, 95, 72]
    for name, score in zip(names, scores):
        print(name, score)
    print(dict(zip(names, scores)))""", "Asha 88\nRavi 95\nMeera 72\n{'Asha': 88, 'Ravi': 95, 'Meera': 72}", ["zip pairs the first items, then the second, and so on.", "dict(zip(...)) builds a dictionary."])],
    rules=["zip stops at the shortest iterable.",
           "It returns an iterator.",
           "zip(*pairs) can \"unzip\" a list of pairs."],
    q=[("What is printed?", ["[(1, 'a'), (2, 'b')]", "[1, 2, 'a', 'b']", "{1: 'a'}", "Error"], 0, "Items are paired into tuples.", 'print(list(zip([1, 2], ["a", "b"])))', RUN),
       ("What happens when lists have different lengths?", ["Error", "Stops at the shortest", "Fills with None", "Repeats items"], 1, "Extra items are ignored."),
       ("What does dict(zip(keys, values)) do?", ["Builds a dictionary", "Sorts keys", "Makes a list", "Error"], 0, "Pairs become key-value pairs.")]),

  S("enumerate()", "Loop with both index and value.",
    """enumerate() gives you a counter alongside each item while looping, so you don't need
    range(len(...)).""",
    syntax="for index, item in enumerate(iterable, start=0):",
    ex=[("""
    tasks = ["Learn", "Answer MCQs", "Practice"]
    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task}")
    print(list(enumerate("ab")))""", "1. Learn\n2. Answer MCQs\n3. Practice\n[(0, 'a'), (1, 'b')]", ["start=1 begins counting at 1.", "Default start is 0."])],
    rules=["enumerate yields (index, item) tuples.",
           "Prefer it over range(len(seq)).",
           "start changes only the counter, not which items are used."],
    q=[("What is printed?", ["0 x\n1 y", "1 x\n2 y", "x 0\ny 1", "Error"], 0, "Counting starts at 0.", 'for i, v in enumerate(["x", "y"]):\n    print(i, v)', RUN),
       ("What does start=1 do?", ["Skips the first item", "Starts the counter at 1", "Starts at the second item", "Nothing"], 1, "Only the numbering changes."),
       ("enumerate is a cleaner replacement for…", ["while True", "range(len(seq))", "zip", "map"], 1, "No need to index manually.")]),

  S("any() and all()", "Check conditions across many items.",
    """any() returns True if at least one item is truthy. all() returns True only if every item is
    truthy. They're perfect with generator expressions.""",
    ex=[("""
    scores = [45, 80, 92]
    print(any(s > 90 for s in scores))
    print(all(s >= 40 for s in scores))
    print(all(s >= 50 for s in scores))
    print(any([]), all([]))""", "True\nTrue\nFalse\nFalse True", ["any: at least one passes.", "all: every one passes.", "Empty: any is False, all is True."])],
    rules=["Both stop early once the answer is known.",
           "They work on any iterable.",
           "Combine with generator expressions for readable checks."],
    q=[("What does any([False, True]) return?", ["True", "False", "None", "Error"], 0, "At least one is True."),
       ("What is printed?", ["True", "False", "Error", "None"], 1, "-1 is not positive.", "print(all(n > 0 for n in [3, -1, 5]))", RUN),
       ("What does all([]) return?", ["True", "False", "Error", "None"], 0, "No items fail, so it's True.")]),
]),

# ═══════════════════════════ LEVEL 17 ═══════════════════════════
L("Comprehensions", "Build lists, dictionaries and sets in a single readable line.", [
  S("List Comprehensions", "Create a list from a loop in one line.",
    """A list comprehension builds a new list by applying an expression to each item of an iterable.
    It replaces a for loop with append() in a compact way.""",
    syntax="[expression for item in iterable]",
    ex=[("""
    squares = []
    for n in range(5):
        squares.append(n * n)
    print(squares)

    squares = [n * n for n in range(5)]
    print(squares)
    print([w.upper() for w in ["a", "b"]])""", "[0, 1, 4, 9, 16]\n[0, 1, 4, 9, 16]\n['A', 'B']", ["Both versions give the same list.", "The comprehension is shorter and clearer."])],
    rules=["Square brackets make a list.",
           "The expression comes first, then the for.",
           "Keep comprehensions short — use a loop if it gets complicated."],
    q=[("What is printed?", ["[1, 2, 3]", "[2, 4, 6]", "[1, 4, 9]", "Error"], 1, "Each number is doubled.", "print([x * 2 for x in [1, 2, 3]])", RUN),
       ("Which brackets make a list comprehension?", ["()", "[]", "{}", "<>"], 1, "Square brackets."),
       ("What is printed?", ["[3, 5]", "['a', 'bb']", "[1, 2]", "Error"], 2, "len of each word.", 'print([len(w) for w in ["a", "bb"]])', RUN)]),

  S("Comprehensions with if", "Filter items inside a comprehension.",
    """Add an if at the end to include only items that pass a condition. Use a conditional expression
    (x if cond else y) at the front to change values instead.""",
    syntax="[expr for item in iterable if condition]\n[a if cond else b for item in iterable]",
    ex=[("""
    nums = range(1, 11)
    print([n for n in nums if n % 2 == 0])
    print(["even" if n % 2 == 0 else "odd" for n in range(4)])""", "[2, 4, 6, 8, 10]\n['even', 'odd', 'even', 'odd']", ["A trailing if filters.", "if/else at the front chooses a value for every item."])],
    rules=["Filter if goes at the end; if/else goes before for.",
           "A trailing if can't have an else.",
           "You can use nested for clauses, but keep them readable."],
    q=[("What is printed?", ["[1, 3]", "[2, 4]", "[1, 2, 3, 4]", "Error"], 1, "Only even numbers are kept.", "print([n for n in [1, 2, 3, 4] if n % 2 == 0])", RUN),
       ("What is printed?", ["['big', 'small']", "['small', 'big']", "[5, 1]", "Error"], 1, "1 → small, 5 → big.", 'print(["big" if n > 3 else "small" for n in [1, 5]])', RUN),
       ("Where does a filtering if go?", ["At the start", "After the for clause", "Before the brackets", "It can't be used"], 1, "[x for x in s if cond].")]),

  S("Dictionary Comprehensions", "Build dictionaries in one line.",
    """A dictionary comprehension creates a dict from key: value pairs generated by a loop.""",
    syntax="{key_expr: value_expr for item in iterable}",
    ex=[("""
    squares = {n: n * n for n in range(1, 5)}
    print(squares)
    prices = {"pen": 10, "book": 250, "bag": 900}
    print({k: v for k, v in prices.items() if v > 100})
    print({v: k for k, v in {"a": 1, "b": 2}.items()})""", "{1: 1, 2: 4, 3: 9, 4: 16}\n{'book': 250, 'bag': 900}\n{1: 'a', 2: 'b'}", ["Use key: value inside curly braces.", "Swap keys and values easily."])],
    rules=["Duplicate keys keep the last value.",
           "Loop over .items() to use both keys and values.",
           "Filters with if work the same as in list comprehensions."],
    q=[("What is printed?", ["{1: 2, 2: 4}", "{2: 1, 4: 2}", "[2, 4]", "Error"], 0, "Key n, value n * 2.", "print({n: n * 2 for n in [1, 2]})", RUN),
       ("What separates key and value in a dict comprehension?", [",", ":", "=", "->"], 1, "key: value."),
       ("What is printed?", ["{'a': 1}", "{'b': 5}", "{'a': 1, 'b': 5}", "{}"], 1, "Only values over 2 are kept.", 'd = {"a": 1, "b": 5}\nprint({k: v for k, v in d.items() if v > 2})', RUN)]),

  S("Set Comprehensions", "Build sets of unique values in one line.",
    """A set comprehension uses curly braces without a colon. Like any set, it keeps only unique
    values.""",
    syntax="{expression for item in iterable}",
    ex=[("""
    words = ["apple", "avocado", "banana", "blueberry", "cherry"]
    print(sorted({w[0] for w in words}))
    print({n % 3 for n in range(10)})""", "['a', 'b', 'c']\n{0, 1, 2}", ["Duplicates disappear automatically.", "sorted() is used because sets have no fixed order."])],
    rules=["{x for ...} is a set; {k: v for ...} is a dict.",
           "Sets are unordered.",
           "Great for collecting unique values."],
    q=[("What is printed?", ["{1, 2}", "{1, 1, 2}", "[1, 1, 2]", "Error"], 0, "Duplicates are removed.", "print({x for x in [1, 1, 2]})", RUN),
       ("How is a set comprehension different from a dict comprehension?", ["It uses []", "It has no key: value colon", "It uses ()", "No difference"], 1, "No colon → set."),
       ("What kind of values does a set keep?", ["Ordered", "Unique", "Only numbers", "Only strings"], 1, "Sets store unique items.")]),

  S("Nested Comprehensions", "Use more than one for in a comprehension.",
    """A comprehension can contain several for clauses, read left to right just like nested loops.
    It's useful for flattening lists or building grids.""",
    ex=[("""
    matrix = [[1, 2], [3, 4], [5, 6]]
    flat = [n for row in matrix for n in row]
    print(flat)
    grid = [[r * c for c in range(1, 4)] for r in range(1, 3)]
    print(grid)""", "[1, 2, 3, 4, 5, 6]\n[[1, 2, 3], [2, 4, 6]]", ["Outer loop first, inner loop second.", "A comprehension inside a comprehension builds a 2D list."])],
    rules=["Order of for clauses matches nested loops.",
           "More than two levels gets hard to read — use loops.",
           "Each inner list can be its own comprehension."],
    q=[("What is printed?", ["[1, 2, 3]", "[[1, 2], [3]]", "[1, [2, 3]]", "Error"], 0, "The nested list is flattened.", "print([x for row in [[1, 2], [3]] for x in row])", RUN),
       ("In [x for a in A for x in a], which loop runs outer?", ["for x in a", "for a in A", "Both together", "Neither"], 1, "Read left to right like nested loops."),
       ("When should you switch to normal loops?", ["Never", "When the comprehension becomes hard to read", "Always", "Only for sets"], 1, "Readability comes first.")]),
]),

# ═══════════════════════════ LEVEL 18 ═══════════════════════════
L("Iterators & Generators", "Understand how loops work and produce values lazily.", [
  S("Iterables", "Things you can loop over.",
    """An iterable is any object you can loop over with for: lists, strings, tuples, sets,
    dictionaries, files and range objects. Behind the scenes, for asks the iterable for an iterator.""",
    ex=[("""
    for item in ("a", "b"):
        print(item)
    for ch in "hi":
        print(ch)
    for key in {"x": 1}:
        print(key)""", "a\nb\nh\ni\nx", ["Many different types work with for.", "Looping over a dict gives its keys."])],
    rules=["Numbers are not iterable: for x in 5 raises TypeError.",
           "Functions like list(), sum() and max() accept any iterable.",
           "You can make your own iterables (later in this level)."],
    mistake=("for d in 123:\n    print(d)", "int is not iterable — use str(123) to loop over the digits."),
    q=[("Which is NOT iterable?", ["\"text\"", "[1, 2]", "42", "range(3)"], 2, "Integers can't be looped over."),
       ("What is printed?", ["6", "123", "Error", "3"], 0, "sum works on any iterable.", "print(sum((1, 2, 3)))", RUN),
       ("Looping over a dictionary gives…", ["Values", "Keys", "Pairs", "Indexes"], 1, "Default iteration is over keys.")]),

  S("iter() and next()", "Step through an iterable manually.",
    """iter() turns an iterable into an iterator, and next() gets its next value. When no values are
    left, next() raises StopIteration — which is how for loops know when to stop.""",
    ex=[("""
    it = iter([10, 20, 30])
    print(next(it))
    print(next(it))
    print(next(it))
    print(next(it, "done"))""", "10\n20\n30\ndone", ["Each next() gives the following item.", "A default value avoids StopIteration."])],
    rules=["An iterator remembers its position.",
           "Once exhausted, an iterator stays empty.",
           "for loops call iter() and next() for you."],
    q=[("What does next() return?", ["The first item always", "The next item from an iterator", "The length", "The last item"], 1, "It moves one step forward."),
       ("What is raised when an iterator has no more items?", ["IndexError", "StopIteration", "ValueError", "KeyError"], 1, "StopIteration signals the end."),
       ("What is printed?", ["a b", "a a", "b a", "Error"], 0, "Each next() moves forward.", 'it = iter("ab")\nprint(next(it), next(it))', RUN)]),

  S("Custom Iterators", "Make your own class iterable.",
    """A class becomes an iterator by defining __iter__ (returning self) and __next__ (returning the
    next value or raising StopIteration).""",
    ex=[("""
    class Countdown:
        def __init__(self, start):
            self.current = start

        def __iter__(self):
            return self

        def __next__(self):
            if self.current <= 0:
                raise StopIteration
            value = self.current
            self.current -= 1
            return value

    for n in Countdown(3):
        print(n)""", "3\n2\n1", ["__next__ gives one value per loop step.", "Raising StopIteration ends the loop."])],
    rules=["__iter__ must return an iterator (often self).",
           "__next__ must raise StopIteration at the end.",
           "Generators (next) are usually an easier way to do this."],
    q=[("Which two methods make an iterator?", ["__init__ and __str__", "__iter__ and __next__", "__len__ and __get__", "iter and next"], 1, "These define the iterator protocol."),
       ("What should __next__ do at the end?", ["Return None", "Raise StopIteration", "Return 0", "Print done"], 1, "That's how loops know to stop."),
       ("What does __iter__ usually return in a simple iterator?", ["self", "None", "A list", "0"], 0, "The object itself is the iterator.")]),

  S("Generators", "Functions that produce values one at a time.",
    """A generator function looks like a normal function but uses yield. Calling it returns a
    generator object that produces values lazily — only when asked.""",
    ex=[("""
    def count_up(limit):
        n = 1
        while n <= limit:
            yield n
            n += 1

    gen = count_up(3)
    print(gen)
    for value in gen:
        print(value)""", None, ["Calling count_up(3) doesn't run the body yet.", "The for loop pulls values one by one."]),
        ("""
    def count_up(limit):
        n = 1
        while n <= limit:
            yield n
            n += 1

    print(list(count_up(4)))
    print(sum(count_up(100)))""", "[1, 2, 3, 4]\n5050", ["list() collects all generated values.", "Generators save memory: values aren't stored all at once."])],
    rules=["Any function containing yield is a generator function.",
           "Generators can only be iterated once.",
           "Great for large or infinite sequences."],
    q=[("What makes a function a generator?", ["return", "yield", "lambda", "async"], 1, "Using yield makes it a generator."),
       ("What is printed?", ["[0, 1, 2]", "[1, 2, 3]", "<generator>", "Error"], 0, "The generator yields 0, 1, 2.", "def g():\n    for i in range(3):\n        yield i\n\nprint(list(g()))", RUN),
       ("Why use generators?", ["They're faster to type", "They produce values lazily and save memory", "They sort data", "They replace classes"], 1, "Values are made only when needed.")]),

  S("yield", "Pause a function and hand back a value.",
    """yield sends a value out and pauses the function, remembering exactly where it stopped. The next
    request resumes right after the yield.""",
    ex=[("""
    def steps():
        print("Start")
        yield 1
        print("Middle")
        yield 2
        print("End")

    g = steps()
    print(next(g))
    print(next(g))
    print(next(g, "finished"))""", "Start\n1\nMiddle\n2\nEnd\nfinished", ["Each next() runs until the next yield.", "After the last yield the generator finishes."]),
        ("""
    def nums():
        yield from [1, 2]
        yield 3

    print(list(nums()))""", "[1, 2, 3]", ["yield from yields every item of another iterable."])],
    rules=["return pauses forever; yield pauses temporarily.",
           "Local variables keep their values between yields.",
           "yield from delegates to another iterable or generator."],
    q=[("What does yield do?", ["Ends the function permanently", "Returns a value and pauses the function", "Prints a value", "Raises an error"], 1, "The function can resume later."),
       ("What is printed?", ["A\n1", "1\nA", "A", "1"], 0, "The body runs until the yield.", 'def g():\n    print("A")\n    yield 1\n\nprint(next(g()))', RUN),
       ("What does yield from [1, 2] do?", ["Yields the list once", "Yields 1 then 2", "Returns 2", "Error"], 1, "It yields each item.")]),

  S("Generator Expressions", "Lazy comprehensions with round brackets.",
    """A generator expression looks like a list comprehension but uses round brackets. It produces
    values one at a time instead of building a whole list in memory.""",
    syntax="(expression for item in iterable)",
    ex=[("""
    gen = (n * n for n in range(5))
    print(type(gen).__name__)
    print(list(gen))
    print(sum(n for n in range(1, 101)))
    print(max(len(w) for w in ["hi", "hello"]))""", "generator\n[0, 1, 4, 9, 16]\n5050\n5", ["Round brackets make a generator.", "When it's the only argument, the extra brackets can be dropped."])],
    rules=["Use [] when you need a list; () when you only need to loop once.",
           "Generator expressions can't be indexed: gen[0] fails.",
           "Once consumed, they're empty."],
    q=[("Which creates a generator expression?", ["[x for x in s]", "(x for x in s)", "{x for x in s}", "<x for x in s>"], 1, "Round brackets."),
       ("What is printed?", ["6", "[1, 2, 3]", "Error", "3"], 0, "1 + 2 + 3.", "print(sum(x for x in [1, 2, 3]))", RUN),
       ("What is printed?", ["[1, 2]\n[1, 2]", "[1, 2]\n[]", "[]\n[]", "Error"], 1, "A generator can only be consumed once.", "g = (x for x in [1, 2])\nprint(list(g))\nprint(list(g))", RUN)]),
]),

# ═══════════════════════════ LEVEL 19 ═══════════════════════════
L("Advanced Python", "Decorators, context managers, type hints and other professional tools.", [
  S("Functions as Objects", "Pass functions around like any value.",
    """In Python, functions are objects. You can store them in variables, put them in lists, pass them
    to other functions and return them from functions.""",
    ex=[("""
    def shout(text):
        return text.upper()

    def whisper(text):
        return text.lower()

    def speak(style, message):
        return style(message)

    print(speak(shout, "Hello"))
    print(speak(whisper, "Hello"))
    actions = {"loud": shout, "quiet": whisper}
    print(actions["loud"]("ok"))""", "HELLO\nhello\nOK", ["shout is passed without brackets — the function itself.", "Functions can be stored in dicts."])],
    rules=["func refers to the function; func() calls it.",
           "A function that takes or returns functions is a higher-order function.",
           "This idea powers callbacks, map(), sorted(key=...) and decorators."],
    q=[("What is printed?", ["5", "f", "Error", "None"], 0, "g refers to the same function as f.", "def f():\n    return 5\n\ng = f\nprint(g())", RUN),
       ("What is a higher-order function?", ["A very long function", "A function that takes or returns functions", "A built-in function", "A method"], 1, "It works with other functions."),
       ("What is printed?", ["3", "6", "Error", "apply"], 1, "apply calls double(3).", "def apply(fn, x):\n    return fn(x)\n\ndef double(n):\n    return n * 2\n\nprint(apply(double, 3))", RUN)]),

  S("Closures", "Inner functions that remember values.",
    """A function defined inside another function can use the outer function's variables. When the
    inner function is returned, it remembers those values — this is a closure.""",
    ex=[("""
    def make_multiplier(factor):
        def multiply(n):
            return n * factor
        return multiply

    double = make_multiplier(2)
    triple = make_multiplier(3)
    print(double(5), triple(5))""", "10 15", ["Each returned function remembers its own factor."]),
        ("""
    def counter():
        count = 0
        def increment():
            nonlocal count
            count += 1
            return count
        return increment

    c = counter()
    print(c(), c(), c())""", "1 2 3", ["nonlocal lets the inner function change the outer variable."])],
    rules=["Inner functions can read outer variables freely.",
           "Use nonlocal to modify an outer (non-global) variable.",
           "Closures are the foundation of decorators."],
    q=[("What is printed?", ["5", "15", "10", "Error"], 1, "add10 remembers 10.", "def adder(x):\n    def add(y):\n        return x + y\n    return add\n\nadd10 = adder(10)\nprint(add10(5))", RUN),
       ("Which keyword lets an inner function modify an outer function's variable?", ["global", "nonlocal", "outer", "static"], 1, "nonlocal targets the enclosing function."),
       ("What is a closure?", ["A closed file", "An inner function that remembers outer variables", "The end of a loop", "A class"], 1, "It \"closes over\" the outer values.")]),

  S("Decorators", "Wrap functions to add extra behaviour.",
    """A decorator is a function that takes another function and returns a new function that adds
    behaviour before or after it. The @ syntax applies a decorator neatly.""",
    syntax="""
    @decorator
    def func():
        ...""",
    ex=[("""
    def announce(func):
        def wrapper():
            print("Before")
            func()
            print("After")
        return wrapper

    @announce
    def hello():
        print("Hello!")

    hello()""", "Before\nHello!\nAfter", ["@announce means hello = announce(hello).", "wrapper runs extra code around the original."]),
        ("""
    import functools

    def log_call(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            print(f"Calling {func.__name__}{args}")
            return func(*args, **kwargs)
        return wrapper

    @log_call
    def add(a, b):
        return a + b

    print(add(2, 3))
    print(add.__name__)""", "Calling add(2, 3)\n5\nadd", ["*args, **kwargs pass any arguments through.", "functools.wraps keeps the original name."])],
    rules=["The wrapper must return the original function's result.",
           "Use *args and **kwargs so the decorator works for any function.",
           "Several decorators can be stacked; the closest one applies first."],
    mistake=("def deco(func):\n    def wrapper(*args):\n        func(*args)\n    return wrapper", "The wrapper doesn't return func(*args), so decorated functions always return None."),
    q=[("What does @my_decorator above def f() mean?", ["f = my_decorator(f)", "my_decorator = f", "f is deleted", "f runs twice"], 0, "The decorator replaces f with its result."),
       ("What is printed?", ["*\nhi", "hi\n*", "hi", "*"], 0, "The wrapper prints * first.", 'def star(fn):\n    def w():\n        print("*")\n        fn()\n    return w\n\n@star\ndef hi():\n    print("hi")\n\nhi()', RUN),
       ("Why use *args, **kwargs in a wrapper?", ["Speed", "To accept any arguments the original function takes", "It's required syntax", "To avoid return"], 1, "It makes the decorator general."),
       ("What does functools.wraps do?", ["Speeds up code", "Preserves the original function's name and docstring", "Removes the decorator", "Caches results"], 1, "Metadata is copied to the wrapper.")]),

  S("Context Managers", "Set up and clean up resources with with.",
    """A context manager defines what happens when a with block starts and ends. Files are the
    classic example, but they're used for locks, database connections, timers and more.""",
    ex=[("""
    with open("data.txt", "w") as f:
        f.write("safe")
    print(f.closed)

    try:
        with open("data.txt") as f:
            raise ValueError("oops")
    except ValueError:
        print("Error handled, file closed:", f.closed)""", "True\nError handled, file closed: True", ["Clean-up happens even when an error occurs inside the block."])],
    rules=["with calls __enter__ at the start and __exit__ at the end.",
           "The value after as is what __enter__ returns.",
           "Multiple managers: with open(a) as x, open(b) as y:"],
    q=[("Which methods does a context manager define?", ["__init__ and __del__", "__enter__ and __exit__", "__start__ and __stop__", "open and close"], 1, "These run at the start and end of with."),
       ("Does clean-up run if an error happens inside with?", ["Yes", "No", "Only for files", "Only without except"], 0, "__exit__ always runs."),
       ("What does the as variable hold?", ["The value returned by __enter__", "The error", "The file name", "None"], 0, "__enter__'s return value.")]),

  S("Writing Context Managers", "Create your own with a class or contextlib.",
    """You can build your own context manager as a class with __enter__ and __exit__, or more simply
    with the @contextmanager decorator and a generator that yields once.""",
    ex=[("""
    class Section:
        def __init__(self, name):
            self.name = name

        def __enter__(self):
            print(f"[{self.name} start]")
            return self

        def __exit__(self, exc_type, exc, tb):
            print(f"[{self.name} end]")
            return False

    with Section("Quiz"):
        print("Answering MCQs")""", "[Quiz start]\nAnswering MCQs\n[Quiz end]", ["__exit__ receives error details (None if no error).", "Returning False lets errors propagate."]),
        ("""
    from contextlib import contextmanager

    @contextmanager
    def tag(name):
        print(f"<{name}>")
        yield
        print(f"</{name}>")

    with tag("p"):
        print("Hello")""", "<p>\nHello\n</p>", ["Code before yield = setup; after yield = clean-up."])],
    rules=["__exit__ takes three extra parameters for error info.",
           "With @contextmanager, yield exactly once.",
           "Wrap the yield in try/finally to guarantee clean-up on errors."],
    q=[("With @contextmanager, where does the with block's body run?", ["Before the function", "At the yield", "After return", "Never"], 1, "The block runs while the generator is paused at yield."),
       ("What is printed?", ["in\nbody\nout", "body\nin\nout", "in\nout\nbody", "Error"], 0, "Setup, body, then clean-up.", 'from contextlib import contextmanager\n\n@contextmanager\ndef cm():\n    print("in")\n    yield\n    print("out")\n\nwith cm():\n    print("body")', RUN),
       ("How many parameters (besides self) does __exit__ take?", ["0", "1", "3", "2"], 2, "exc_type, exc_value, traceback.")]),

  S("Type Hints", "Describe the expected types of values.",
    """Type hints label variables, parameters and return values with their expected types. Python
    doesn't enforce them at runtime, but editors and tools like mypy use them to catch bugs.""",
    syntax="def func(param: type) -> return_type:",
    ex=[("""
    def greet(name: str, times: int = 1) -> str:
        return ("Hi " + name + "! ") * times

    scores: list[int] = [90, 85]
    user: dict[str, int] = {"age": 21}
    print(greet("Asha", 2).strip())
    print(greet.__annotations__["return"])""", "Hi Asha! Hi Asha!\n<class 'str'>", ["-> str describes the return type.", "Hints are stored in __annotations__."]),
        ("""
    def double(n: int) -> int:
        return n * 2

    print(double("ab"))""", "abab", ["Hints aren't enforced — Python still runs this.", "A type checker would warn you."])],
    rules=["Hints document intent; they don't convert or check values.",
           "Use X | None (or Optional[X]) for values that may be None.",
           "Built-in generics: list[int], dict[str, float], tuple[int, ...]."],
    q=[("Does Python enforce type hints at runtime?", ["Yes", "No", "Only for int", "Only in classes"], 1, "They are hints for tools and readers."),
       ("How do you hint that a function returns a float?", ["def f() = float:", "def f() -> float:", "def f(): float", "def float f():"], 1, "Use -> after the brackets."),
       ("What does list[str] mean?", ["A string list function", "A list containing strings", "A string of lists", "Error"], 1, "It's a list of str values.")]),

  S("Dataclasses", "Classes for storing data with less code.",
    """The @dataclass decorator automatically writes __init__, __repr__ and __eq__ for you, based on
    type-hinted fields. It's ideal for simple data-holding classes.""",
    ex=[("""
    from dataclasses import dataclass

    @dataclass
    class Lesson:
        title: str
        minutes: int = 10

    a = Lesson("Variables")
    b = Lesson("Variables")
    print(a)
    print(a == b)
    print(Lesson("Loops", 15).minutes)""", "Lesson(title='Variables', minutes=10)\nTrue\n15", ["__init__ and __repr__ were generated automatically.", "== compares the field values."])],
    rules=["Fields need type hints.",
           "Fields with defaults must come after fields without.",
           "@dataclass(frozen=True) makes objects read-only."],
    q=[("What does @dataclass generate automatically?", ["Only __str__", "__init__, __repr__ and __eq__", "Nothing", "Loops"], 1, "Common methods are written for you."),
       ("What is printed?", ["P(x=1)", "<P object>", "1", "Error"], 0, "The generated __repr__ shows fields.", "from dataclasses import dataclass\n\n@dataclass\nclass P:\n    x: int\n\nprint(P(1))", RUN),
       ("What do dataclass fields require?", ["Default values", "Type hints", "self", "Decorators each"], 1, "Fields are declared with annotations.")]),
]),
]
