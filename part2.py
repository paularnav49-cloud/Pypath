from dsl import S, L

RUN = True

LEVELS = [
# ═══════════════════════════ LEVEL 6 ═══════════════════════════
L("Strings", "Work with text: indexing, slicing, methods and formatting.", [
  S("String Indexing", "Get a single character by its position.",
    """Every character in a string has a position number called an index. Indexes start at 0 for the
    first character. Negative indexes count from the end: -1 is the last character.""",
    syntax="text[index]",
    ex=[("""
    word = "Python"
    print(word[0])
    print(word[3])
    print(word[-1])
    print(word[-2])""", "P\nh\nn\no", ["word[0] is the first character.", "word[-1] is the last character."])],
    rules=["The first index is 0, not 1.",
           "Using an index that doesn't exist raises IndexError.",
           "The last index is always len(text) - 1."],
    mistake=('word = "cat"\nprint(word[3])', "\"cat\" has indexes 0, 1, 2 only, so word[3] raises IndexError: string index out of range."),
    q=[("What is \"hello\"[1]?", ["h", "e", "l", "o"], 1, "Indexes start at 0, so index 1 is the second character."),
       ("What is printed?", ["P", "n", "o", "Error"], 1, "-1 is the last character.", 'print("Python"[-1])', RUN),
       ("What is the index of the first character?", ["1", "0", "-1", "Depends on the string"], 1, "Python counts from 0."),
       ("What does \"abc\"[5] cause?", ["Returns ''", "IndexError", "Returns c", "Returns None"], 1, "The index is out of range.")]),

  S("String Slicing", "Take a part of a string with [start:stop:step].",
    """Slicing extracts a section of a string. You give a start index and a stop index; the stop
    position is not included. Leave either out to go from the beginning or to the end.""",
    syntax="text[start:stop]\ntext[start:stop:step]",
    syn=["start is included, stop is excluded.", "Omit start to begin at 0, omit stop to go to the end.", "step skips characters; -1 reverses."],
    ex=[("""
    s = "Programming"
    print(s[0:3])
    print(s[3:7])
    print(s[:4])
    print(s[7:])""", "Pro\ngram\nProg\nming", ["s[0:3] takes indexes 0, 1 and 2."]),
        ("""
    s = "abcdef"
    print(s[::2])
    print(s[::-1])
    print(s[-3:])""", "ace\nfedcba\ndef", ["[::2] takes every second character.", "[::-1] reverses a string.", "[-3:] gives the last 3 characters."])],
    rules=["Slicing never raises IndexError — out-of-range values are trimmed.",
           "The result is a new string; the original is unchanged.",
           "s[:] makes a full copy."],
    q=[("What is \"Python\"[0:2]?", ["Py", "Pyt", "P", "yt"], 0, "Index 0 and 1 are included; 2 is excluded."),
       ("What is printed?", ["olleh", "hello", "h", "Error"], 0, "[::-1] reverses the string.", 'print("hello"[::-1])', RUN),
       ("What is printed?", ["code", "cod", "ode", "de"], 2, "[1:] starts at index 1 and goes to the end.", 'print("code"[1:])', RUN),
       ("Is the stop index included in a slice?", ["Yes", "No", "Only for negative numbers", "Only with a step"], 1, "The slice stops just before it.")]),

  S("len()", "Count how many characters (or items) there are.",
    """len() returns the length of a string — the number of characters it contains, including spaces
    and punctuation. It also works with lists, tuples, sets and dictionaries.""",
    syntax="len(value)",
    ex=[("""
    print(len("cat"))
    print(len("hello world"))
    print(len(""))
    name = "Asha"
    print(name[len(name) - 1])""", "3\n11\n0\na", ["Spaces count as characters.", "An empty string has length 0.", "len(name) - 1 is the last index."])],
    rules=["len() counts characters, not words.",
           "len() of a number is a TypeError: len(123) fails.",
           "Use len() with input to check e.g. password length."],
    q=[("What is len(\"hi there\")?", ["7", "8", "2", "6"], 1, "h-i-space-t-h-e-r-e is 8 characters."),
       ("What is printed?", ["0", "1", "None", "Error"], 0, "An empty string has no characters.", 'print(len(""))', RUN),
       ("What does len(42) do?", ["Returns 2", "Returns 42", "TypeError", "Returns 1"], 2, "Integers have no length."),
       ("What is the last index of a string s?", ["len(s)", "len(s) - 1", "len(s) + 1", "-0"], 1, "Indexes start at 0, so the last is one less than the length.")]),

  S("Changing Case", "upper(), lower(), title() and capitalize().",
    """String methods are functions that belong to strings. You call them with a dot. Case methods
    return a new string with the letters changed.""",
    syntax="text.upper()\ntext.lower()\ntext.title()\ntext.capitalize()",
    ex=[("""
    s = "hello PYTHON world"
    print(s.upper())
    print(s.lower())
    print(s.title())
    print(s.capitalize())""", "HELLO PYTHON WORLD\nhello python world\nHello Python World\nHello python world", ["title() capitalises each word.", "capitalize() capitalises only the first letter."]),
        ("""
    answer = "YeS"
    if answer.lower() == "yes":
        print("Confirmed")""", "Confirmed", ["Lowercasing makes comparisons ignore case."])],
    rules=["Strings are immutable: methods return a NEW string.",
           "s.upper() alone does nothing visible — store or print the result.",
           "Remember the brackets: s.upper not s.upper()."],
    mistake=('name = "ravi"\nname.upper()\nprint(name)', "This still prints ravi. Write name = name.upper()."),
    q=[("What is \"Hi\".upper()?", ["hi", "HI", "Hi", "hI"], 1, "upper() makes every letter uppercase."),
       ("What is printed?", ["Good Morning", "Good morning", "GOOD MORNING", "good morning"], 0, "title() capitalises each word.", 'print("good morning".title())', RUN),
       ("Why does name stay lowercase after name.upper()?", ["upper() is broken", "Methods return a new string", "name is a number", "It doesn't"], 1, "You must store the result."),
       ("How do you compare answers ignoring case?", ["answer == \"YES\"", "answer.lower() == \"yes\"", "answer.case() == \"yes\"", "lower(answer) = \"yes\""], 1, "Lowercase both sides before comparing.")]),

  S("strip()", "Remove unwanted spaces from the ends of a string.",
    """strip() removes whitespace (spaces, tabs, newlines) from both ends of a string. lstrip()
    removes it only on the left and rstrip() only on the right.""",
    syntax="text.strip()\ntext.strip(characters)",
    ex=[("""
    raw = "   hello   "
    print("[" + raw.strip() + "]")
    print("[" + raw.lstrip() + "]")
    print("[" + raw.rstrip() + "]")""", "[hello]\n[hello   ]\n[   hello]", ["The brackets make the remaining spaces visible."]),
        ("""
    print("---title---".strip("-"))
    print("  a b  ".strip())""", "title\na b", ["You can choose which characters to strip.", "Spaces in the middle are kept."])],
    rules=["strip() only affects the ends, never the middle.",
           "Use input().strip() to clean what users type.",
           "Like all string methods, strip() returns a new string."],
    q=[("What is \"  hi  \".strip()?", ["hi", "  hi", "hi  ", " hi "], 0, "Spaces on both ends are removed."),
       ("Does strip() remove spaces in the middle?", ["Yes", "No", "Only one", "Only tabs"], 1, "It only trims the ends."),
       ("What is printed?", ["[x  ]", "[  x]", "[x]", "[  x  ]"], 0, "lstrip() only trims the left side.", 'print("[" + "  x  ".lstrip() + "]")', RUN)]),

  S("find() and replace()", "Search inside a string and swap text.",
    """find() returns the index where some text first appears, or -1 if it isn't found. replace()
    returns a new string with every occurrence of some text swapped for something else.""",
    syntax="text.find(sub)\ntext.replace(old, new)",
    ex=[("""
    s = "I love tea, tea is great"
    print(s.find("tea"))
    print(s.find("coffee"))
    print(s.replace("tea", "coffee"))
    print(s.count("tea"))""", "7\n-1\nI love coffee, coffee is great\n2", ["find() returns the first index.", "-1 means not found.", "replace() changes every match.", "count() tells you how many matches."])],
    rules=["find() returns -1 when nothing is found (index() raises ValueError instead).",
           "replace(old, new, 1) replaces only the first match.",
           "Searching is case-sensitive."],
    q=[("What does \"banana\".find(\"n\") return?", ["1", "2", "3", "-1"], 1, "The first n is at index 2."),
       ("What does find() return if text isn't found?", ["0", "None", "-1", "Error"], 2, "-1 signals not found."),
       ("What is printed?", ["a-b-c", "a b c", "abc", "a-b c"], 0, "Every space is replaced.", 'print("a b c".replace(" ", "-"))', RUN),
       ("Is find() case-sensitive?", ["Yes", "No", "Only for numbers", "Only at the start"], 0, "\"A\" and \"a\" are different characters.")]),

  S("split() and join()", "Break a string into a list and glue a list back together.",
    """split() cuts a string into a list of pieces. By default it splits on whitespace. join() does
    the opposite: it joins a list of strings using the string it's called on as the glue.""",
    syntax='text.split(separator)\n"glue".join(list_of_strings)',
    ex=[("""
    sentence = "learn python step by step"
    words = sentence.split()
    print(words)
    print(len(words))""", "['learn', 'python', 'step', 'by', 'step']\n5", ["split() with no argument splits on spaces."]),
        ("""
    data = "red,green,blue"
    colours = data.split(",")
    print(colours)
    print(" | ".join(colours))
    print("".join(["a", "b", "c"]))""", "['red', 'green', 'blue']\nred | green | blue\nabc", ["split(\",\") splits on commas.", "join() puts the glue between items."])],
    rules=["join() is called on the separator: \", \".join(items), not items.join(\", \").",
           "join() only works if every item is a string.",
           "split() returns a list; the original string is unchanged."],
    mistake=('print(", ".join([1, 2, 3]))', "join needs strings. Convert first: \", \".join(str(n) for n in [1, 2, 3])."),
    q=[("What does \"a b c\".split() return?", ["\"abc\"", "['a', 'b', 'c']", "['a b c']", "('a', 'b', 'c')"], 1, "split() returns a list of words."),
       ("What is printed?", ["x-y-z", "xyz", "['x', 'y', 'z']", "x y z"], 0, "\"-\" is placed between the items.", 'print("-".join(["x", "y", "z"]))', RUN),
       ("Which is correct?", ["[\"a\", \"b\"].join(\",\")", "\",\".join([\"a\", \"b\"])", "join(\",\", [\"a\"])", "\",\".split([\"a\"])"], 1, "join is a method of the separator string."),
       ("What is printed?", ["['1', '2', '3']", "[1, 2, 3]", "1 2 3", "123"], 0, "split returns strings.", 'print("1,2,3".split(","))', RUN)]),

  S("f-Strings", "Put variables and expressions straight into text.",
    """An f-string is a string with an f before the opening quote. Anything inside { } is evaluated
    and inserted into the text. It's the cleanest way to build messages.""",
    syntax='f"Text {variable} more text {expression}"',
    ex=[("""
    name = "Meera"
    level = 3
    print(f"{name} is on level {level}")
    print(f"Next level: {level + 1}")""", "Meera is on level 3\nNext level: 4", ["Variables are inserted directly.", "You can put expressions inside { }."]),
        ("""
    price = 49.5
    print(f"Price: {price:.2f}")
    n = 7
    print(f"{n:03}")""", "Price: 49.50\n007", [":.2f shows 2 decimal places.", ":03 pads with zeros to 3 digits."])],
    rules=["Don't forget the f before the quote, or the braces print literally.",
           "No need for str() — f-strings convert values automatically.",
           "Use {{ and }} to show a literal brace."],
    mistake=('x = 5\nprint("{x} apples")', "Without the f prefix this prints {x} apples. Write f\"{x} apples\"."),
    q=[("What is printed?", ["{x} apples", "x apples", "5 apples", "f5 apples"], 2, "In an f-string, {x} is replaced with its value.", 'x = 5\nprint(f"{x} apples")', RUN),
       ("What is printed?", ["3.14159", "3.14", "3.1", "3"], 1, ":.2f rounds to 2 decimals.", 'pi = 3.14159\nprint(f"{pi:.2f}")', RUN),
       ("What makes a string an f-string?", ["An f before the quote", "Using { }", "Using %", "Ending with f"], 0, "The f prefix enables formatting."),
       ("Can you put expressions in { }?", ["No, only variables", "Yes, like {a + b}", "Only numbers", "Only strings"], 1, "Any expression can go inside the braces.")]),

  S("Escape Characters", "Special characters like new lines, tabs and quotes inside strings.",
    """A backslash \\ starts an escape sequence — a way to write characters that are hard to type
    directly, like a new line or a quote inside quotes.""",
    points=["\\n new line", "\\t tab", "\\\\ a single backslash", "\\\" or \\' a quote inside the string"],
    ex=[("""
    print("Line 1\\nLine 2")
    print("Name:\\tAsha")
    print("She said \\"hi\\"")
    print("C:\\\\Users")""", "Line 1\nLine 2\nName:\tAsha\nShe said \"hi\"\nC:\\Users", ["\\n starts a new line.", "\\t inserts a tab.", "\\\" puts a quote inside double quotes."]),
        ("""
    path = r"C:\\new\\files"
    print(path)""", "C:\\new\\files", ["An r before the quotes makes a raw string — backslashes are kept as they are."])],
    rules=["Windows paths often need raw strings or double backslashes.",
           "len(\"\\n\") is 1 — an escape sequence is one character.",
           "You can mix quote types instead of escaping: 'He said \"hi\"'."],
    q=[("What does \\n do?", ["Prints n", "Starts a new line", "Adds a tab", "Ends the program"], 1, "\\n is the newline character."),
       ("What does print(\"a\\tb\") show?", ["a\\tb", "a and b separated by a tab", "ab", "a\\b"], 1, "\\t is a tab character."),
       ("What is len(\"\\n\")?", ["2", "1", "0", "3"], 1, "An escape sequence counts as a single character."),
       ("What does r\"...\" create?", ["A reversed string", "A raw string where backslashes stay as-is", "A random string", "A regex"], 1, "Raw strings don't process escapes.")]),
]),

# ═══════════════════════════ LEVEL 7 ═══════════════════════════
L("Lists", "Store many values in order and change them whenever you like.", [
  S("Creating Lists", "Make a list of values with square brackets.",
    """A list is an ordered collection of items written inside square brackets [ ] and separated by
    commas. Lists can hold any type — even a mix of types — and can grow or shrink.""",
    syntax="my_list = [item1, item2, item3]",
    ex=[("""
    fruits = ["apple", "mango", "kiwi"]
    numbers = [3, 1, 4, 1, 5]
    mixed = ["Asha", 21, True]
    empty = []
    print(fruits)
    print(len(numbers))
    print(mixed)
    print(empty)""", "['apple', 'mango', 'kiwi']\n5\n['Asha', 21, True]\n[]", ["Lists keep items in the order you wrote them.", "Duplicates are allowed.", "len() counts items."]),
        ("""
    letters = list("abc")
    nums = list(range(4))
    print(letters)
    print(nums)""", "['a', 'b', 'c']\n[0, 1, 2, 3]", ["list() builds a list from any sequence."])],
    rules=["Lists are mutable: you can change them after creating them.",
           "Lists can contain other lists.",
           "Use [] for an empty list."],
    q=[("Which creates a list?", ["(1, 2, 3)", "{1, 2, 3}", "[1, 2, 3]", "<1, 2, 3>"], 2, "Square brackets create a list."),
       ("What is printed?", ["3", "4", "2", "Error"], 1, "There are four items.", "print(len([5, 6, 7, 8]))", RUN),
       ("Can a list hold different types?", ["No", "Yes", "Only numbers and strings", "Only if empty"], 1, "Lists can mix any types."),
       ("Are duplicate items allowed in a list?", ["Yes", "No", "Only numbers", "Only once"], 0, "Lists can contain the same value many times.")]),

  S("Accessing List Items", "Read items with indexes and slices.",
    """List items have indexes just like string characters: the first item is at index 0 and -1 is
    the last. Slicing works the same way too.""",
    syntax="my_list[index]\nmy_list[start:stop]",
    ex=[("""
    days = ["Mon", "Tue", "Wed", "Thu", "Fri"]
    print(days[0])
    print(days[-1])
    print(days[1:3])
    print(days[:2])""", "Mon\nFri\n['Tue', 'Wed']\n['Mon', 'Tue']", ["Slicing a list returns a new list."]),
        ("""
    grid = [[1, 2], [3, 4]]
    print(grid[1])
    print(grid[1][0])""", "[3, 4]\n3", ["grid[1] is the inner list.", "grid[1][0] is the first item of it."])],
    rules=["An index past the end raises IndexError.",
           "Slices never raise IndexError.",
           "Use in to check if an item exists before looking it up."],
    q=[("What is [\"a\", \"b\", \"c\"][1]?", ["a", "b", "c", "Error"], 1, "Index 1 is the second item."),
       ("What is printed?", ["[20, 30]", "[10, 20]", "[20, 30, 40]", "[30, 40]"], 0, "Index 1 up to (not including) 3.", "nums = [10, 20, 30, 40]\nprint(nums[1:3])", RUN),
       ("What is printed?", ["4", "3", "[3, 4]", "2"], 0, "grid[1] is [3, 4], then index 1 is 4.", "grid = [[1, 2], [3, 4]]\nprint(grid[1][1])", RUN)]),

  S("Changing List Items", "Replace items by assigning to an index.",
    """Because lists are mutable, you can change an item by assigning a new value to its index. You
    can even replace a whole slice at once.""",
    syntax="my_list[index] = new_value",
    ex=[("""
    colours = ["red", "green", "blue"]
    colours[1] = "yellow"
    print(colours)
    colours[-1] = "black"
    print(colours)""", "['red', 'yellow', 'blue']\n['red', 'yellow', 'black']", ["Assigning to an index replaces that item."]),
        ("""
    a = [1, 2, 3]
    b = a
    b[0] = 99
    print(a)
    c = a.copy()
    c[0] = 0
    print(a)""", "[99, 2, 3]\n[99, 2, 3]", ["b = a doesn't copy — both names share one list.", "Use .copy() to get an independent list."])],
    rules=["You can't assign to an index that doesn't exist yet (IndexError) — use append() instead.",
           "Strings can't be changed like this; lists can.",
           "Assigning one list variable to another shares the same list."],
    mistake=("nums = [1, 2]\nnums[2] = 3", "Index 2 doesn't exist yet. Use nums.append(3)."),
    q=[("What is printed?", ["[1, 2, 3]", "[9, 2, 3]", "[1, 9, 3]", "Error"], 2, "Index 1 is replaced with 9.", "x = [1, 2, 3]\nx[1] = 9\nprint(x)", RUN),
       ("What is printed?", ["[1, 2]", "[5, 2]", "Error", "[1, 5]"], 1, "b and a are the same list.", "a = [1, 2]\nb = a\nb[0] = 5\nprint(a)", RUN),
       ("How do you get an independent copy of a list?", ["b = a", "b = a.copy()", "b == a", "b = list"], 1, ".copy() creates a new list.")]),

  S("append() and insert()", "Add new items to a list.",
    """append() adds one item to the end of a list. insert() adds an item at a specific position.
    extend() adds every item from another list.""",
    syntax="my_list.append(item)\nmy_list.insert(index, item)\nmy_list.extend(other_list)",
    ex=[("""
    cart = ["pen"]
    cart.append("book")
    cart.insert(0, "bag")
    print(cart)
    cart.extend(["ink", "tape"])
    print(cart)""", "['bag', 'pen', 'book']\n['bag', 'pen', 'book', 'ink', 'tape']", ["append() adds to the end.", "insert(0, ...) adds at the front.", "extend() adds several items."]),
        ("""
    squares = []
    for n in range(1, 5):
        squares.append(n * n)
    print(squares)""", "[1, 4, 9, 16]", ["Building a list in a loop with append() is very common."])],
    rules=["append() changes the list and returns None — don't write x = x.append(1).",
           "append([1, 2]) adds ONE item (a list); extend([1, 2]) adds two items.",
           "insert() shifts later items to the right."],
    mistake=("nums = [1]\nnums = nums.append(2)\nprint(nums)", "append() returns None, so nums becomes None. Just call nums.append(2)."),
    q=[("Where does append() add an item?", ["At the start", "At the end", "In the middle", "In sorted order"], 1, "append() always adds to the end."),
       ("What is printed?", ["[1, 2, 3]", "[0, 1, 2]", "[1, 0, 2]", "[0, 1, 2, 3]"], 1, "insert(0, 0) places 0 at the front.", "x = [1, 2]\nx.insert(0, 0)\nprint(x)", RUN),
       ("What is printed?", ["[1, 2, 3]", "[1, [2, 3]]", "[1, 2, [3]]", "Error"], 1, "append adds the whole list as one item.", "x = [1]\nx.append([2, 3])\nprint(x)", RUN),
       ("What does append() return?", ["The new list", "None", "The added item", "The length"], 1, "It modifies the list in place and returns None.")]),

  S("remove() and pop()", "Take items out of a list.",
    """remove() deletes the first item with a given value. pop() removes an item by index and gives
    it back to you (the last item if no index is given). del removes by index too, and clear()
    empties the list.""",
    syntax="my_list.remove(value)\nmy_list.pop(index)\ndel my_list[index]\nmy_list.clear()",
    ex=[("""
    pets = ["cat", "dog", "fish", "dog"]
    pets.remove("dog")
    print(pets)
    last = pets.pop()
    print(last, pets)
    first = pets.pop(0)
    print(first, pets)""", "['cat', 'fish', 'dog']\ndog ['cat', 'fish']\ncat ['fish']", ["remove() deletes only the first matching value.", "pop() returns the removed item."]),
        ("""
    nums = [10, 20, 30]
    del nums[1]
    print(nums)
    nums.clear()
    print(nums)""", "[10, 30]\n[]", ["del removes by index.", "clear() removes everything."])],
    rules=["remove() raises ValueError if the value isn't in the list.",
           "pop() on an empty list raises IndexError.",
           "Use pop() when you need the removed value."],
    q=[("What does pop() with no index remove?", ["The first item", "The last item", "A random item", "Every item"], 1, "pop() defaults to the last item."),
       ("What is printed?", ["[1, 3, 2]", "[1, 2, 3]", "[3, 2]", "[1, 3]"], 0, "Only the first 2 is removed.", "x = [1, 2, 3, 2]\nx.remove(2)\nprint(x)", RUN),
       ("What happens with [1, 2].remove(5)?", ["Nothing", "ValueError", "Removes the last item", "Returns -1"], 1, "remove() fails if the value isn't present."),
       ("What is printed?", ["c", "a", "['a', 'b']", "b"], 0, "pop() returns the removed last item.", 'x = ["a", "b", "c"]\nprint(x.pop())', RUN)]),

  S("Sorting Lists", "Put items in order with sort() and sorted().",
    """sort() arranges a list in place (it changes the list). sorted() returns a new sorted list and
    leaves the original alone. Both accept reverse=True for descending order.""",
    syntax="my_list.sort()\nnew_list = sorted(my_list)\nmy_list.sort(reverse=True)",
    ex=[("""
    scores = [42, 7, 19, 88]
    scores.sort()
    print(scores)
    scores.sort(reverse=True)
    print(scores)""", "[7, 19, 42, 88]\n[88, 42, 19, 7]", ["sort() changes the list itself."]),
        ("""
    names = ["zoe", "Amit", "bea"]
    print(sorted(names))
    print(sorted(names, key=str.lower))
    print(names)
    nums = [3, 1, 2]
    nums.reverse()
    print(nums)""", "['Amit', 'bea', 'zoe']\n['Amit', 'bea', 'zoe']\n['zoe', 'Amit', 'bea']\n[2, 1, 3]", ["sorted() returns a new list; names is unchanged.", "key=str.lower sorts ignoring case.", "reverse() flips the order without sorting."])],
    rules=["sort() returns None — don't assign its result.",
           "Uppercase letters sort before lowercase ones by default.",
           "You can't sort a list that mixes numbers and strings."],
    q=[("What's the difference between sort() and sorted()?", ["No difference", "sort() changes the list; sorted() returns a new one", "sorted() changes the list", "sort() only works on strings"], 1, "sort() is in-place; sorted() makes a copy."),
       ("What is printed?", ["[3, 2, 1]", "[1, 2, 3]", "[2, 3, 1]", "None"], 0, "reverse=True sorts high to low.", "x = [2, 3, 1]\nx.sort(reverse=True)\nprint(x)", RUN),
       ("What is printed?", ["[1, 2, 3]", "None", "[3, 1, 2]", "Error"], 1, "sort() returns None.", "x = [3, 1, 2]\nprint(x.sort())", RUN)]),

  S("Looping Through Lists", "Visit every item with for, enumerate() and indexes.",
    """The simplest way to process every item is a for loop over the list. When you also need the
    position, use enumerate(), which gives you the index and the item together.""",
    ex=[("""
    marks = [70, 85, 90]
    total = 0
    for m in marks:
        total += m
    print("Total:", total)
    print("Average:", total / len(marks))""", "Total: 245\nAverage: 81.66666666666667", ["Loop through, keep a running total."]),
        ("""
    tasks = ["code", "test", "ship"]
    for i, task in enumerate(tasks, start=1):
        print(i, task)""", "1 code\n2 test\n3 ship", ["enumerate() gives (index, item) pairs.", "start=1 numbers from 1."])],
    rules=["Don't add or remove items from a list while looping over it — loop over a copy instead.",
           "sum(), max() and min() are quick shortcuts for common loops.",
           "Prefer for item in list over for i in range(len(list))."],
    q=[("What does enumerate() give you?", ["Only items", "Only indexes", "Index and item pairs", "The list length"], 2, "enumerate yields (index, item)."),
       ("What is printed?", ["6", "123", "[1, 2, 3]", "3"], 0, "The loop adds 1 + 2 + 3.", "t = 0\nfor n in [1, 2, 3]:\n    t += n\nprint(t)", RUN),
       ("What is printed?", ["0 a\n1 b", "1 a\n2 b", "a\nb", "a 0\nb 1"], 0, "enumerate starts at 0 by default.", 'for i, x in enumerate(["a", "b"]):\n    print(i, x)', RUN)]),

  S("List Functions", "Handy built-ins: sum(), max(), min(), count() and index().",
    """Python has built-in functions for common list jobs, so you don't always need a loop.""",
    points=["sum(list) adds all numbers", "max(list) and min(list) find the largest and smallest",
            "list.count(x) counts occurrences of x", "list.index(x) finds the position of x"],
    ex=[("""
    temps = [31, 28, 35, 28, 30]
    print(sum(temps))
    print(max(temps), min(temps))
    print(temps.count(28))
    print(temps.index(35))""", "152\n35 28\n2\n2", ["index() returns the FIRST position of the value."])],
    rules=["sum() only works with numbers.",
           "max() and min() on an empty list raise ValueError.",
           "index() raises ValueError if the item is missing — check with in first."],
    q=[("What is sum([2, 4, 6])?", ["246", "12", "6", "3"], 1, "2 + 4 + 6 = 12."),
       ("What is printed?", ["9", "1", "3", "0"], 0, "max returns the largest value.", "print(max([4, 9, 1]))", RUN),
       ("What is printed?", ["1", "2", "3", "0"], 2, "There are three 'a' items.", 'print(["a", "b", "a", "a"].count("a"))', RUN)]),
]),

# ═══════════════════════════ LEVEL 8 ═══════════════════════════
L("Tuples & Sets", "Fixed collections with tuples and unique-item collections with sets.", [
  S("Tuples", "Ordered collections that can't be changed.",
    """A tuple is like a list, but immutable: once created, its items can't be changed, added or
    removed. Tuples use round brackets ( ). Use them for data that should stay fixed, like
    coordinates or dates.""",
    syntax="point = (x, y)\nsingle = (item,)",
    ex=[("""
    point = (4, 7)
    rgb = (255, 128, 0)
    print(point[0])
    print(rgb[-1])
    print(len(rgb))
    print(rgb[0:2])""", "4\n0\n3\n(255, 128)", ["Indexing and slicing work like lists."]),
        ("""
    one = (5,)
    not_tuple = (5)
    print(type(one))
    print(type(not_tuple))""", "<class 'tuple'>\n<class 'int'>", ["A one-item tuple needs a trailing comma."])],
    rules=["Assigning to a tuple item raises TypeError.",
           "Tuples are slightly faster than lists and can be dictionary keys.",
           "Use count() and index() — the only two tuple methods."],
    mistake=("t = (1, 2, 3)\nt[0] = 10", "Tuples are immutable: TypeError: 'tuple' object does not support item assignment."),
    q=[("Which creates a tuple?", ["[1, 2]", "(1, 2)", "{1, 2}", "<1, 2>"], 1, "Round brackets with commas make a tuple."),
       ("What happens with t[0] = 5 on a tuple?", ["It works", "TypeError", "It adds a new item", "Nothing"], 1, "Tuples can't be changed."),
       ("What is printed?", ["<class 'int'>", "<class 'tuple'>", "<class 'list'>", "Error"], 1, "The comma makes it a tuple.", "print(type((7,)))", RUN),
       ("When is a tuple a good choice?", ["For data that must not change", "When you need to append often", "For unique items only", "Never"], 0, "Tuples protect fixed data.")]),

  S("Tuple Unpacking", "Assign the items of a tuple to several variables at once.",
    """Unpacking takes the items of a tuple (or list) and stores them in separate variables in one
    step. It also gives Python a neat way to swap variables.""",
    syntax="a, b, c = my_tuple",
    ex=[("""
    person = ("Asha", 21, "Pune")
    name, age, city = person
    print(name)
    print(city)""", "Asha\nPune", ["Each variable gets the item in the same position."]),
        ("""
    a, b = 1, 2
    a, b = b, a
    print(a, b)
    first, *rest = [10, 20, 30, 40]
    print(first, rest)""", "2 1\n10 [20, 30, 40]", ["Swapping in one line.", "*rest collects the remaining items into a list."])],
    rules=["The number of variables must match the number of items (unless you use *).",
           "Functions often return tuples that you unpack.",
           "Use _ for a value you don't need: name, _ = pair."],
    q=[("What is printed?", ["1", "2", "3", "(1, 2, 3)"], 1, "y gets the second item.", "x, y, z = (1, 2, 3)\nprint(y)", RUN),
       ("What happens with a, b = (1, 2, 3)?", ["a=1, b=2", "ValueError: too many values to unpack", "b gets (2, 3)", "Works fine"], 1, "The counts don't match."),
       ("What is printed?", ["5 9", "9 5", "5 5", "9 9"], 1, "a, b = b, a swaps the values.", "a, b = 5, 9\na, b = b, a\nprint(a, b)", RUN)]),

  S("Sets", "Unordered collections of unique items.",
    """A set stores items with no duplicates and no particular order. Sets use curly braces { } and
    are great for removing duplicates and checking membership quickly.""",
    syntax="my_set = {item1, item2}\nempty = set()",
    ex=[("""
    tags = {"python", "code", "python", "fun"}
    print(len(tags))
    print("code" in tags)
    nums = [1, 2, 2, 3, 3, 3]
    print(sorted(set(nums)))""", "3\nTrue\n[1, 2, 3]", ["Duplicates are dropped automatically.", "set(list) removes duplicates from a list."])],
    rules=["{} creates an empty dictionary, not a set — use set().",
           "Sets have no indexes: my_set[0] is a TypeError.",
           "Set items must be immutable (no lists inside sets)."],
    mistake=("empty = {}\nprint(type(empty))", "This prints <class 'dict'>. Use set() for an empty set."),
    q=[("What is len({1, 1, 2})?", ["3", "2", "1", "Error"], 1, "Sets keep only unique values."),
       ("How do you create an empty set?", ["{}", "set()", "[]", "()"], 1, "{} is an empty dictionary."),
       ("Can you access a set item by index?", ["Yes", "No", "Only the first", "Only negative indexes"], 1, "Sets are unordered, so they have no indexes."),
       ("What is printed?", ["[3, 1, 3]", "[1, 3]", "[3, 1]", "{1, 3}"], 1, "set() removes the duplicate, sorted() orders it.", "print(sorted(set([3, 1, 3])))", RUN)]),

  S("Adding & Removing Set Items", "add(), update(), remove() and discard().",
    """Sets are mutable, so you can add and remove items. add() adds one item, update() adds many.
    remove() deletes an item (error if missing) while discard() deletes it silently.""",
    syntax="s.add(item)\ns.update(iterable)\ns.remove(item)\ns.discard(item)",
    ex=[("""
    seen = {"a", "b"}
    seen.add("c")
    seen.add("a")
    print(sorted(seen))
    seen.update(["d", "e"])
    print(len(seen))
    seen.discard("z")
    seen.remove("a")
    print(sorted(seen))""", "['a', 'b', 'c']\n5\n['b', 'c', 'd', 'e']", ["Adding an existing item changes nothing.", "discard() on a missing item doesn't fail."])],
    rules=["remove() raises KeyError if the item is missing; discard() doesn't.",
           "Sets don't keep order, so print sorted(s) for predictable output.",
           "pop() removes an arbitrary item."],
    q=[("Which method silently ignores a missing item?", ["remove()", "discard()", "pop()", "delete()"], 1, "discard() never raises an error for missing items."),
       ("What is printed?", ["2", "3", "4", "Error"], 0, "1 is already in the set.", "s = {1, 2}\ns.add(1)\nprint(len(s))", RUN),
       ("What does update() do?", ["Adds several items", "Replaces the set", "Sorts the set", "Removes items"], 0, "update() adds every item from an iterable.")]),

  S("Set Operations", "Union, intersection and difference.",
    """Sets support maths-style operations that compare two groups of items.""",
    points=["a | b  union — items in either set", "a & b  intersection — items in both",
            "a - b  difference — items in a but not b", "a ^ b  symmetric difference — items in exactly one"],
    ex=[("""
    python_fans = {"Asha", "Ravi", "Meera"}
    java_fans = {"Ravi", "John"}
    print(sorted(python_fans | java_fans))
    print(sorted(python_fans & java_fans))
    print(sorted(python_fans - java_fans))
    print(sorted(python_fans ^ java_fans))""", "['Asha', 'John', 'Meera', 'Ravi']\n['Ravi']\n['Asha', 'Meera']\n['Asha', 'John', 'Meera']", ["Ravi likes both, so he's in the intersection."]),
        ("""
    a = {1, 2}
    b = {1, 2, 3}
    print(a.issubset(b))
    print(a.union({9}) == {1, 2, 9})""", "True\nTrue", ["Every operator also has a method name, like union() and issubset()."])],
    rules=["Order of a - b matters: b - a is different.",
           "These operators create new sets; the originals are unchanged.",
           "Use sets to find common or missing items quickly."],
    q=[("What does a & b give?", ["Items in either", "Items in both", "Items only in a", "All items twice"], 1, "& is intersection."),
       ("What is printed?", ["[1, 2, 3]", "[2]", "[1, 3]", "[1]"], 1, "Only 2 is in both.", "print(sorted({1, 2} & {2, 3}))", RUN),
       ("What is printed?", ["[3]", "[1]", "[1, 2, 3]", "[2]"], 1, "1 is in the first set but not the second.", "print(sorted({1, 2} - {2, 3}))", RUN),
       ("Which operator is union?", ["&", "|", "-", "^"], 1, "| combines both sets.")]),
]),

# ═══════════════════════════ LEVEL 9 ═══════════════════════════
L("Dictionaries", "Store data as key–value pairs and look values up by name.", [
  S("Creating Dictionaries", "Key–value pairs inside curly braces.",
    """A dictionary (dict) stores pairs: each key maps to a value. Instead of looking things up by
    position, you look them up by key — like finding a word in a real dictionary.""",
    syntax='my_dict = {"key": value, "key2": value2}',
    ex=[("""
    student = {"name": "Asha", "age": 21, "city": "Pune"}
    print(student)
    print(len(student))
    empty = {}
    print(empty)""", "{'name': 'Asha', 'age': 21, 'city': 'Pune'}\n3\n{}", ["Each key is followed by a colon and its value.", "len() counts the pairs."]),
        ("""
    prices = dict(tea=10, coffee=25)
    print(prices)""", "{'tea': 10, 'coffee': 25}", ["dict() is another way to create a dictionary."])],
    rules=["Keys must be unique — a repeated key overwrites the earlier one.",
           "Keys must be immutable (strings, numbers, tuples), values can be anything.",
           "Dictionaries keep the order items were added (Python 3.7+)."],
    q=[("What does a dictionary store?", ["Only values", "Key–value pairs", "Sorted numbers", "Unique items only"], 1, "Each key maps to a value."),
       ("What is printed?", ["2", "4", "1", "Error"], 0, "There are two key–value pairs.", 'print(len({"a": 1, "b": 2}))', RUN),
       ("What is printed?", ["{'a': 1}", "{'a': 2}", "{'a': 1, 'a': 2}", "Error"], 1, "A repeated key keeps the last value.", 'print({"a": 1, "a": 2})', RUN),
       ("Which can't be a dictionary key?", ["\"name\"", "42", "(1, 2)", "[1, 2]"], 3, "Lists are mutable, so they can't be keys.")]),

  S("Accessing Values", "Look up a value by its key.",
    """Use square brackets with a key to get its value. If the key doesn't exist, Python raises a
    KeyError, so check with in first when you're not sure.""",
    syntax="value = my_dict[key]",
    ex=[("""
    capitals = {"India": "New Delhi", "Japan": "Tokyo"}
    print(capitals["Japan"])
    print("France" in capitals)
    if "India" in capitals:
        print(capitals["India"])""", "Tokyo\nFalse\nNew Delhi", ["Lookup is by key, not by position.", "in checks keys."])],
    rules=["Dictionaries have no numeric indexes: d[0] looks for the KEY 0.",
           "Missing keys raise KeyError.",
           "Keys are case-sensitive: \"name\" and \"Name\" differ."],
    mistake=('d = {"a": 1}\nprint(d["b"])', "\"b\" isn't a key, so this raises KeyError: 'b'. Use \"b\" in d or d.get(\"b\")."),
    q=[("What is printed?", ["x", "10", "Error", "None"], 1, "The value for key \"x\" is 10.", 'd = {"x": 10}\nprint(d["x"])', RUN),
       ("What happens when you access a missing key with [ ]?", ["Returns None", "KeyError", "Returns 0", "Adds the key"], 1, "Square-bracket lookup fails for missing keys."),
       ("What does \"a\" in my_dict check?", ["Values", "Keys", "Both", "Length"], 1, "in checks keys.")]),

  S("get()", "Safely look up a key with a default value.",
    """get() returns the value for a key, or None (or a default you choose) if the key is missing.
    It never raises KeyError.""",
    syntax="my_dict.get(key)\nmy_dict.get(key, default)",
    ex=[("""
    stock = {"apples": 5, "pears": 0}
    print(stock.get("apples"))
    print(stock.get("kiwis"))
    print(stock.get("kiwis", 0))""", "5\nNone\n0", ["Missing keys return None by default.", "The second argument is the fallback."]),
        ("""
    text = "banana"
    counts = {}
    for ch in text:
        counts[ch] = counts.get(ch, 0) + 1
    print(counts)""", "{'b': 1, 'a': 3, 'n': 2}", ["A classic pattern for counting things."])],
    rules=["get() doesn't add the key to the dictionary.",
           "Use [ ] when a missing key is a real error, get() when it's normal.",
           "The default can be any value: get(k, [])."],
    q=[("What does d.get(\"z\") return if \"z\" is missing?", ["KeyError", "None", "0", "\"z\""], 1, "get() returns None for missing keys."),
       ("What is printed?", ["None", "0", "-1", "Error"], 2, "-1 is the chosen default.", 'd = {}\nprint(d.get("k", -1))', RUN),
       ("Does get() add a missing key?", ["Yes", "No", "Only with a default", "Only for strings"], 1, "It only reads; the dictionary is unchanged.")]),

  S("Adding & Updating Items", "Store new pairs or change existing values.",
    """Assigning to a key adds it if it's new or replaces its value if it already exists. update()
    merges another dictionary in.""",
    syntax="my_dict[key] = value\nmy_dict.update(other_dict)",
    ex=[("""
    user = {"name": "Ravi"}
    user["age"] = 30
    user["name"] = "Ravi K"
    print(user)
    user.update({"city": "Delhi", "age": 31})
    print(user)""", "{'name': 'Ravi K', 'age': 30}\n{'name': 'Ravi K', 'age': 31, 'city': 'Delhi'}", ["New key → added. Existing key → value replaced.", "update() adds and replaces in one go."])],
    rules=["The same syntax both adds and updates — be careful with spelling.",
           "setdefault(k, v) adds k only if it's missing.",
           "a | b merges two dicts into a new one (Python 3.9+)."],
    q=[("What does d[\"new\"] = 1 do if \"new\" isn't a key?", ["KeyError", "Adds the pair", "Nothing", "Replaces the dict"], 1, "Assigning to a new key adds it."),
       ("What is printed?", ["{'a': 1}", "{'a': 2}", "{'a': 1, 'a': 2}", "Error"], 1, "The existing value is replaced.", 'd = {"a": 1}\nd["a"] = 2\nprint(d)', RUN),
       ("What is printed?", ["{'a': 1}", "{'b': 2}", "{'a': 1, 'b': 2}", "Error"], 2, "update() merges the new pair.", 'd = {"a": 1}\nd.update({"b": 2})\nprint(d)', RUN)]),

  S("Removing Items", "pop(), del, popitem() and clear().",
    """You can remove pairs from a dictionary in several ways. pop(key) removes a key and returns
    its value; del removes a key; popitem() removes the most recently added pair; clear() empties
    everything.""",
    syntax="my_dict.pop(key)\ndel my_dict[key]\nmy_dict.popitem()\nmy_dict.clear()",
    ex=[("""
    menu = {"tea": 10, "coffee": 25, "juice": 40}
    price = menu.pop("coffee")
    print(price, menu)
    del menu["tea"]
    print(menu)
    print(menu.pop("cake", "not found"))""", "25 {'tea': 10, 'juice': 40}\n{'juice': 40}\nnot found", ["pop() returns the removed value.", "A default stops pop() from raising KeyError."])],
    rules=["del and pop() raise KeyError for missing keys (unless pop has a default).",
           "Don't remove keys while looping over the same dictionary.",
           "clear() leaves an empty dictionary {}."],
    q=[("What does pop(key) return?", ["The key", "The removed value", "The new dict", "None"], 1, "pop gives back the value it removed."),
       ("What is printed?", ["{'b': 2}", "{'a': 1}", "{}", "Error"], 0, "del removes key a.", 'd = {"a": 1, "b": 2}\ndel d["a"]\nprint(d)', RUN),
       ("What is printed?", ["None", "KeyError", "0", "{}"], 2, "The default 0 is returned for the missing key.", 'd = {}\nprint(d.pop("x", 0))', RUN)]),

  S("keys(), values() and items()", "Get all keys, all values, or key–value pairs.",
    """Dictionaries have three methods for viewing their contents: keys(), values() and items().
    items() gives pairs you can unpack into two variables.""",
    syntax="my_dict.keys()\nmy_dict.values()\nmy_dict.items()",
    ex=[("""
    scores = {"Asha": 90, "Ravi": 75}
    print(list(scores.keys()))
    print(list(scores.values()))
    print(list(scores.items()))
    print(sum(scores.values()))""", "['Asha', 'Ravi']\n[90, 75]\n[('Asha', 90), ('Ravi', 75)]\n165", ["Wrap in list() to see the contents.", "values() is handy with sum() and max()."])],
    rules=["These return live 'views' that update when the dict changes.",
           "items() returns (key, value) tuples.",
           "Convert to list() if you need indexing."],
    q=[("What does items() return?", ["Only keys", "Only values", "Key–value pairs", "The length"], 2, "items() yields (key, value) pairs."),
       ("What is printed?", ["['a', 'b']", "[1, 2]", "[('a', 1), ('b', 2)]", "3"], 1, "values() gives the values.", 'print(list({"a": 1, "b": 2}.values()))', RUN),
       ("What is printed?", ["3", "['x', 'y']", "xy", "2"], 0, "1 + 2 = 3.", 'print(sum({"x": 1, "y": 2}.values()))', RUN)]),

  S("Looping Through Dictionaries", "Visit every key and value with for.",
    """Looping over a dictionary directly gives you its keys. Use items() to get each key and value
    together — the most common pattern.""",
    ex=[("""
    ages = {"Asha": 21, "Ravi": 30}
    for name in ages:
        print(name)
    for name, age in ages.items():
        print(f"{name} is {age}")""", "Asha\nRavi\nAsha is 21\nRavi is 30", ["Looping a dict gives keys.", "items() unpacks into two variables."]),
        ("""
    stock = {"pen": 0, "book": 4, "bag": 0}
    for item, qty in stock.items():
        if qty == 0:
            print("Restock", item)""", "Restock pen\nRestock bag", ["Combine loops and conditions to process data."])],
    rules=["Items come out in insertion order.",
           "Use sorted(d) to loop over keys alphabetically.",
           "Don't add or delete keys during the loop — loop over list(d) if you must."],
    q=[("What does for k in my_dict: loop over?", ["Values", "Keys", "Pairs", "Indexes"], 1, "Iterating a dict gives its keys."),
       ("What is printed?", ["a 1\nb 2", "a\nb", "1\n2", "('a', 1)\n('b', 2)"], 0, "items() gives key and value.", 'for k, v in {"a": 1, "b": 2}.items():\n    print(k, v)', RUN),
       ("How do you loop over keys in alphabetical order?", ["for k in d.sort():", "for k in sorted(d):", "for k in d.alpha():", "for k in d[::-1]:"], 1, "sorted(d) returns the keys in order.")]),

  S("Nested Dictionaries", "Dictionaries and lists inside dictionaries.",
    """Values can be anything — including lists and other dictionaries. Nesting lets you model
    real-world data like users, products or settings.""",
    ex=[("""
    users = {
        "u1": {"name": "Asha", "skills": ["python", "sql"]},
        "u2": {"name": "Ravi", "skills": ["java"]},
    }
    print(users["u1"]["name"])
    print(users["u1"]["skills"][1])
    users["u2"]["skills"].append("python")
    print(users["u2"]["skills"])""", "Asha\nsql\n['java', 'python']", ["Chain lookups from the outside in.", "Inner lists can be changed in place."])],
    rules=["Read nested access left to right: users → \"u1\" → \"skills\" → index 1.",
           "Use get() at each level if a key might be missing.",
           "Data like this is exactly what JSON looks like."],
    q=[("What is printed?", ["1", "2", "{'b': 2}", "Error"], 1, "d[\"a\"] is {\"b\": 2}, then [\"b\"] is 2.", 'd = {"a": {"b": 2}}\nprint(d["a"]["b"])', RUN),
       ("What is printed?", ["Mumbai", "Pune", "['Pune', 'Mumbai']", "Error"], 0, "Index 1 of the list.", 'p = {"cities": ["Pune", "Mumbai"]}\nprint(p["cities"][1])', RUN),
       ("Can dictionary values be lists or dicts?", ["No", "Yes", "Only lists", "Only strings"], 1, "Values can be any type.")]),
]),
]
