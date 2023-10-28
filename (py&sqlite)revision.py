# %% [markdown]
# ##################################################
# # 1- Markdown
# ##################################################
# 

# %% [markdown]
# <meta charset="utf-8">
# 
# ## headings {#markdown-id}
# 
# ---
# 
# > This is good
# 
# <blockquote>This is good</blockquote>
# 
# ---
# 
# ```
#   print(code)
# ```
# 
# <code>
#   print(code)
# </code>
# 
# ---
# 
# <b>Ahmed</b> <br> **Mohamed** <br> **Bassiouny**
# 
# ---
# 
# <i>Ahmed</i> <br> _Mohamed_ <br> _Bassiouny_
# 
# ---
# 
# Ahmed ~~Mohamed~~ Bassiouny
# 
# ---
# 
# <ol>
# <li>Ahmed</li>
# <li>Mohamed</li>
# <li>Bassiouny</li>
# </ol>
# 
# 1. First item
# 2. Second item
# 3. Third item
# 
# ---
# 
# <ul>
# <li>Ahmed</li>
# <li>Mohamed</li>
# <li>Bassiouny</li>
# </ul>
# 
# - Ahmed
# - Mohamed
# - Bassiouny
# 
# ---
# 
# <a href="https://www.google.com" >Link to Google</a>
# 
# [Section title](#markdown-id)
# 
# ---
# 
# <table>
# <tr>
# <th>Name</th>
# <th>Address</th>
# <th>Salary</th>
# </tr>
# 
# <tr>
# <td>Adam</td>
# <td>Sydney</td>
# <td>5000</td>
# </tr>
# </table>
# 
# <br>
# 
# | Syntax    | Description |
# | --------- | ----------- |
# | Header    | Title       |
# | Paragraph | Text        |
# 
# ---
# 
# ![alt text](files/a.png)
# 
# ---
# 

# %% [markdown]
# ##################################################
# # 2- Comment
# ##################################################
# 

# %%
##comment
# you can use (#) to comment any thing

# %% [markdown]
# ##################################################
# # 3- Data Types
# ##################################################
# 

# %%
##data-types
print(type(10))  # (10,-10,0) int
print(type(10.5))  # (0.5,-5.5,10.0) float
print(type(10 + 4j))  # complex ,complex.real , complex.imag
print(type("+10"))  # ("abc","10","+10") string
print(type(True))  # (true , false , 5>0 , 1=3) string
print(type({"one": 10, "two": 20}))  # dict => Dictionary
print(type([1, "AMB", 3]))  # list(array)
print(type((1, "AMB", 3)))  # tuple
print(type({1, "AMB", 3}))  # set

# List you can add and modify any item
print(type([1, "AMB", 3]))  # list(array)

# Tuples you can not add or delete items
print(type((1, "AMB", 3)))  # tuple

# %% [markdown]
# ##################################################
# # 4- Var
# ##################################################
# 

# %%
# (1)
a = 1
# (2)
a, b, c = 1, 2, 3

# %% [markdown]
# ##################################################
# # 5- Escape Characters
# ##################################################
# 

# %%
## Escape Sequences Characters
# (\b) Back Space
print("Hello\b World")  # => Hell World
# (\n) line feed
print("Hello \n World")  # => Hello (at new line) World
# (\t) Horizontal Tab
print("Hello \t World")  # => Hello  World
# (\r) Carriage Return
print("123456\r****")  # => ****56
# (\) Back slash
print("Hello \\ World")  # => Hello \ World

# %% [markdown]
# ##################################################
# # 6- Concatenation
# ##################################################
# 

# %%
txt1 = "ahmed"
txt2 = "bassiouny"
num1 = 20
num2 = 20

print("\n", "=-" * 20 + "=", "\n")

print(txt1 + " " + txt2, (5 + 10), (num1 * num2))

print("\n", "=-" * 20 + "=", "\n")

# %% [markdown]
# ##################################################
# # 7- Multy line text
# ##################################################
# 

# %%
## Multy line text use => (""" txt """) or (''' txt ''')
txt1 = """ahmed
mohamed
bassiouny
'amb'
"""
print(txt1)

# %% [markdown]
# ##################################################
# # 8- string
# ##################################################
# 

# %% [markdown]
# ### 1- Indexing & Slicing
# 

# %%
txt = "   Ahmed Mohamed Bassiouny   "
print(txt[0])  # =>A
print(txt[-1])  # =>y
print(txt[0:5])  # =>Ahmed (from 0 to 4)
print(txt[:5])  # =>Ahmed (from 0 to 4)
print(txt[14:])  # =>Ahmed (from 14 to end)
print(txt[:])  # =>Ahmed Mohamed Bassiouny (from 0 to end) all text
print(txt[::1])  # =>Ahmed Mohamed Bassiouny (from 0 to end) 1 step
print(txt[::2])  # =>AmdMhmdBsiuy (from 0 to end) 2 step


lst = [1, 2, 3, 4, 5]
print(lst)
lst[::2] = [0, 0, 0]
print(lst)
lst[:3] = [0, 0, 0]
print(lst)

# %% [markdown]
# ### 2- Strings Methods
# 

# %% [markdown]
# - len()
# - strip()
# - title()
# - capitalize()
# - upper() & lower()
# - swapcase()
# - split() & rsplit()
# - splitLines() == split("\n")
# - join()
# - join()
# - zfill()
# - center()
# - rjust() & ljust()
# - count()
# - startswith() & endswith()
# - index()
# - find()
# - expandtabs()
# - is()
# 

# %%
txt = "   Ahmed Mohamed Bassiouny   "

##len()
print(len(txt))  # =>29

##strip()
print(txt.strip())  # =>Ahmed Mohamed Bassiouny len(23) , rstrip() , lstrip()

##title()
b = "I Love 2d graphics and 3g technology and python"
print(b.title())

##capitalize()
c = "i love 2d Graphics and 3g Technology and python"
print(b.capitalize())

##upper() & lower()
a, b = "ahmED", "BASSiounY"
print(a.upper() + " " + b.lower())

##swapcase()
g = "AAAbbb"
print(g.swapcase())

##split() & rsplit()
print(txt.split())  # => ['Ahmed', 'Mohamed', 'Bassiouny']
c = "I-Love-Python-and-PHP-and-MySQL"
print(c.split("-", 3))  # => ['I', 'Love', 'Python', 'and-PHP-and-MySQL']

##splitLines() == split("\n")
txt5 = """ahmed
mohamed
bassiouny"""  # or txt5 = "ahmed\nmohamed\nbassiouny"
print(txt5.splitlines())  # => ['ahmed', 'mohamed', 'bassiouny']

##join()
x = ["Ahmed", "Mohamed", "Bassiouny"]
print(" ".join(x))  # => Ahmed Mohamed Bassiouny

##join()
x = "Ahmed Mohamed Bassiouny"
print(x.replace(" ", "-"))  # => Ahmed-Mohamed-Bassiouny

##zfill()
a, b, c = "1", "11", "111"
print(a.zfill(3) + "\n" + b.zfill(3) + "\n" + c.zfill(3))

##center()
e = "AMB"
print(e.center(9))  # Spaces =>  Osama
print(e.center(9, "#"))  # Hashes =>##Osama##

##rjust() & ljust()
e = "AMB"
print(e.rjust(9))  # Spaces =>      AMB
print(e.ljust(9, "#"))  # Hashes =>AMB######

##count()
f = "i Love Python and PHP Because PHP is Easy"
print(f.count("PHP"))  # => 2
print(f.count("PHP", 0, 20))  # => 0

##startswith() & endswith()
g = "abcd"
print(g.startswith("ab"))  # =>True
print(g.endswith("cd"))  # =>True
print(g.endswith("bc"))  # =>False
print(g.endswith("bc", 1, 3))  # =>True

##index()
h = "abcd"
# print (g.index("z"))     # =>Error
print(g.index("a"))  # =>0
print(g.index("d"))  # =>3
print(g.index("bc"))  # =>1
print(g.index("c", 1, 3))  # =>2

##find()
h = "abcd"
print(g.find("z"))  # =>-1
print(g.find("a"))  # =>0
print(g.find("d"))  # =>3
print(g.find("bc"))  # =>1
print(g.find("c", 1, 3))  # =>2

##expandtabs()
x = "Hello\tWor1d\tI\tLove\tpython"
print(x.expandtabs(6))

##is()
one = "I Love Python And 3G"
two = "I Love Python And 3g"
print(one.istitle())
print(two.istitle())

three = " "
four = ""
print(three.isspace())
print(four.isspace())

five = "i love python"
six = "I Love Python"
print(five.islower())
print(six.islower())

seven = "1osama_elzero"
eight = "OsamaElzero100"
nine = "Osama--Elzero100"

print(seven.isidentifier())
print(eight.isidentifier())
print(nine.isidentifier())

x = "AaaaaBbbbbb"
y = "AaaaaBbbbbb111"
print(x.isalpha())
print(y.isalpha())

u = "AaaaaBbbbbb"
z = "AaaaaBbbbbb111"
print(u.isalnum())
print(z.isalnum())

u = "1010114"
z = "5555"
print(u.isdigit())
print(z.isnumeric())

# %% [markdown]
# ### 3- Formating
# 

# %%
##Formating
x = "Ahmed Mohamed Bassiouny"
y = 10
z = 2.5
v = 25000
# Format version
print(
    "Iam %.5s and my age is %d Iam %s developer and my salary is %.2f"
    % (x, y, "python", z)
)
print(
    "Iam {:.5s} and my age is {} Iam {} developer and my salary is {:.2f}".format(
        x, y, "python", z
    )
)
print(f"Iam {x:.5s} and my age is {y} Iam python developer and my salary is {z}")
# Format money
print("my new salary is {:-,.2f}".format(v))
print("my new salary is {:,d}".format(v))
# reArrange
print("my variables %d %d %d" % (y, z, v))
print("my variables {1:.2f} {0} {2}".format(y, z, v))

# %% [markdown]
# ##################################################
# # 9- dect
# ##################################################
# 

# %%
peoples = {
    "osama": {"HTML": "70%", "CSS": "80%", "JS": "70%"},
    "Ahmed": {"HTML-1": "90%", "CSS-1": "80%", "JS-1": "90%"},
}
peoples

# %%
for person in peoples:
    print(f"{person} skills is :")
    for skill in peoples[person]:
        print(f" --{skill} => {peoples[person][skill]}")

# %% [markdown]
# ### dect.items()
# 

# %%
for person, skills in peoples.items():
    print(f"{person} skills is :")
    for skillNM, skillVL in skills.items():
        print(f"--{skillNM} => {skillVL}")
print(peoples.items())
print(peoples)

# %% [markdown]
# ### nested list
# 

# %%
xx = [["1", "2", "3"], ["4", "5555", "6"], ["7", "8", "9"]]
for x in xx:
    for y in x:
        print(y)
    print("#" * 10)

# %% [markdown]
# ### Nested Dect
# 

# %%
peoples = {
    "Osama": {"Html": "70%", "Css": "80%", "Js": "70%"},
    "Ahmed": {"Html": "90%", "Css": "80%", "Js": "90%"},
    "Sayed": {"Html": "70%", "Css": "60%", "Js": "90%"},
}

print(peoples["Osama"])
print(peoples["Ahmed"])
print(peoples["Sayed"])

print(peoples["Osama"]["Css"])
print(peoples["Ahmed"]["Js"])
print(peoples["Sayed"]["Html"])

print("=-" * 20)

for name in peoples:
    print(f"{name} Skills Is: ")
    for skill in peoples[name]:
        print(f"  - {skill} => {peoples[name][skill]}")

# %% [markdown]
# ##################################################
# # 10- Function
# ##################################################
# 

# %%
def ShowSkills(name, *study, **skills):
    print(f"Hello {name} ")
    print("Your study is : ")
    for std in study:
        print(f"--{std}")
    print("Your skills is : ")
    for skill, skillValue in skills.items():
        print(f"--{skill} => {skillValue}")


study = ["CS", "AI", "ML"]

skills = {"Html": "70%", "Csss": "85%", "Jquery": "95%"}

ShowSkills("Ahmed", "CS", "AI", "ML", Html="70%", Csss="85%", Jquery="95%")
print(" func-2 ".center(20, "#"))
ShowSkills("Ahmed", *study, **skills)

# %%
hello = lambda f, s, l: f"Hello => {f} {s.capitalize():.1s} {l}"
print(hello("Ahmed", "mohamed", "Bassiouny"))
print(type(hello))

# %% [markdown]
# ##################################################
# # 11- files
# ##################################################
# 

# %%
myFile = open("files/test.txt")  # ,r ,w ,a
print(type(myFile))
print(myFile)

# %% [markdown]
# #### read
# 

# %%
## read
myFile = open("files/test.txt", "r")
print(myFile.read(5))
print(myFile.readline())
print(myFile.readlines())

# %% [markdown]
# #### write & append
# 

# %%
## write
myFile = open("files/test.txt", "w")
myFile.write("Ahmed \n")
myFile.write("Ahmed Mohamed Bassiouny \n " * 10)
lst = ["ahmed\n", "ahmed\n", "ahmed\n"]
myFile.writelines(lst)
myFile.close()

## append
myFile = open("files/test.txt", "a")
myFile.write("Ahmed \n")
myFile.write("Ahmed Mohamed Bassiouny \n " * 10)
lst = ["ahmed\n", "ahmed\n", "ahmed\n"]
myFile.writelines(lst)
myFile.close()

# %% [markdown]
# #### tell() & truncate() & seek()
# 

# %%
## tell => tell current index to write
myFile = open("files/test.txt", "a")
myFile.tell()

## truncate => clear file content after given index
myFile = open("files/test.txt", "a")
myFile.truncate(10)
myFile.close()

## seek() => set current index to read
myFile = open("files/test.txt", "r")
myFile.seek(50)
print(myFile.read())
myFile.close()

# %% [markdown]
# ##################################################
# # 12- Built-in-Function
# ##################################################
# 

# %% [markdown]
# ### All()
# 

# %%
items = [1, 2, 3, 4, 5]
if all(item > 0 for item in items):
    print("All items are greater than 0")
else:
    print("Not all items are greater than 0")

# %% [markdown]
# ### any()
# 

# %%
items = [1, 2, 0, 4, 5]
if any(item > 0 for item in items):
    print("one item is greater than 0")
else:
    print("Not any items are greater than 0")

# %% [markdown]
# ### bin() => integet to binary
# 

# %%
bin(10)

# %% [markdown]
# ### id() => id in memory
# 

# %%
w = False
x = 20
y = 21
z = "AMB"
print(id(w))
print(id(x))
print(id(y))
print(id(z))

# %% [markdown]
# ### sum()
# 

# %%
x = [10, 20, 30, 40]
print(sum(x))
print(sum(x, 40))

# %% [markdown]
# ### round()
# 

# %%
print(round(2.6583, 3))

# %% [markdown]
# ### range()
# 

# %%
x = list(range(0, 20, 2))
print(x)

# %% [markdown]
# ### print()
# 

# %%
print("Ahmed Mohamed Bassiouny")
print("Ahmed", "Mohamed", "Bassiouny")
print("Ahmed", "Mohamed", "Bassiouny", sep=" . ")

print("Ahmed", end=" ")
print("Mohamed")
print("Bassiouny")

# %% [markdown]
# ### abs()
# 

# %%
print(abs(12))
print(abs(-12))
print(abs(-12.5))

# %% [markdown]
# ### pow()
# 

# %%
# pow(base, exp, mod)
pow(5, 2)  # => 25
pow(5, 2, 10)  # => 25 % 10 = 5

# %% [markdown]
# ### min() & max()
# 

# %%
nums = [1, 2, 3, 100, -15, 20]
abc = ["a", "b", "c", "z"]

print(min(nums))
print(min("ahmed", "z", "x"))

print(max(abc))
print(
    min(
        3,
        -100,
        -15,
    )
)

# %% [markdown]
# ### slice(str, end, stp)
# 

# %%
x = ["a", "b", "c", "d"]
print(x[0:2])
print(x[slice(0, 3, 2)])

# %% [markdown]
# ### map()
# 

# %%
names = ["ahmed", "mohamed", "bassiouny"]

# 1
# names = list(map(str.upper, names))

# 2
# names = list(map( lambda name: name.upper(), names))

# 3
# def upp(n):
#   return n.upper()
# names = list(map( upp, names))

print(names)

# %% [markdown]
# ### filter()
# 

# %%
names = ["ahmed", "mohamed", "ali"]

names = list(filter((lambda name: name.startswith("a")), names))
print(names)

# %% [markdown]
# ### reduce()
# 

# %%
from functools import reduce


names = ["ahmed", "mohamed", "bassiouny"]

names = reduce((lambda n1, n2: n1 + " " + n2), names)
print(names)

# %% [markdown]
# 

# %% [markdown]
# ### enumerate()
# 

# %%
names = ["ahmed", "mohamed", "bassiouny"]
newNames = enumerate(names, 1)

for key, val in newNames:
    print(f"{key} - {val}")

# %% [markdown]
# ### reversed()
# 

# %%
names = ["ahmed", "mohamed", "bassiouny"]
newNames = reversed(names)

for val in newNames:
    print(f"{val}")

# %% [markdown]
# ### help()
# 

# %%
print(help(print))

# %% [markdown]
# ##################################################
# # 13- Modules
# ##################################################
# 

# %% [markdown]
# ### random
# 

# %%
import random

print(random.random())
print(random.randint(0, 2))
print(random.randrange(0, 10, 2))

from random import randint, randrange

print(randint(0, 2))

from random import randint as rint

print(rint(0, 2))

# %% [markdown]
# ### termcolor & pyfiglet
# 

# %%
import termcolor
import pyfiglet

print(termcolor.colored(pyfiglet.figlet_format("Ahmed Bassiouny"), color="yellow"))
# print(termcolor.colored(pyfiglet.figlet_format("Palastin"), color="yellow"))

# %% [markdown]
# ### pillow => images
# 

# %%
from PIL import Image

# open
img = Image.open("files/ieee.jfif")
# show
img.show()
# crop-1
img2 = img.crop((0, 0, 200, 200))
img2.show()
# crop-1
points = (0, 0, 600, 600)
img3 = img.crop(points)
img3.show()
# mode
img4 = img.convert("L")
img4.show()

# %% [markdown]
# ### timeit
# 

# %%
import timeit


print(timeit.timeit(stmt="random.randint(0, 50)", setup="import random"))

print("=" * 20)

print(timeit.repeat(stmt="random.randint(0, 50)", setup="import random", repeat=5))

# %% [markdown]
# ### string
# 

# %%
import string as str

print(str.digits)
print(str.octdigits)
print(str.hexdigits)

print(str.ascii_lowercase)
print(str.ascii_uppercase)
print(str.ascii_letters)

print(str.whitespace)

print(str.punctuation)

print(str.printable)

# %% [markdown]
# ##################################################
# # 14- Date & Time
# ##################################################
# 

# %% [markdown]
# | Directive           | Example                  |
# | ------------------- | ------------------------ |
# | **Day**             | -----------              |
# | %a                  | Sun, Mon                 |
# | %a                  | Sunday                   |
# | %d                  | 01:31                    |
# | %-d                 | 1:31                     |
# | %w                  | 1:6                      |
# | **Day of the year** | -----------              |
# | %j                  | 001, 002, ..., 366       |
# | %-j                 | 1, 2, ..., 366           |
# | **Month**           | -----------              |
# | %d                  | Jan, Feb, ..., Dec       |
# | %B                  | January, February, ...   |
# | %m                  | 01, 02, ..., 12          |
# | %-m                 | 1, 2, ..., 12            |
# | **Year**            | -----------              |
# | %Y                  | 2013, 2019 ,....         |
# | %y                  | 0, 1, ..., 99            |
# | %-y                 | 00, 01, ..., 99          |
# | **Hour**            | -----------              |
# | %H                  | 00, 01, ..., 23          |
# | %-H                 | 0, 1, ..., 23            |
# | %I                  | 01, 02, ..., 12          |
# | %-I                 | 1, 2, ... 12             |
# | **Minute**          | -----------              |
# | %M                  | 00, 01, ..., 59          |
# | %-M                 | 0, 1, ..., 59            |
# | **Second**          | -----------              |
# | %S                  | 00, 01, ..., 59          |
# | %-S                 | 0, 1, ..., 59            |
# | **Microsecond**     | -----------              |
# | %f                  | 000000 - 999999          |
# | **PM or AM**        | -----------              |
# | %p                  | AM, PM                   |
# | **representation**  | -----------              |
# | %S                  | Mon Sep 30 07:06:05 2013 |
# | %x                  | 09/30/13                 |
# | %X                  | 07:06:05                 |
# 

# %%
import datetime

# Print The Current Date and Time
print(datetime.datetime.now())

# # Print The Current date
# print(datetime.datetime.now().date())
# # Print The Current date Year
# print(datetime.datetime.now().date().year)
# # Print The Current date Month
# print(datetime.datetime.now().month)
# # Print The Current date Day
# print(datetime.datetime.now().day)

# # Print The Current Time
# print(datetime.datetime.now().time())
# # Print The Current Time Hour
# print(datetime.datetime.now().hour)
# # Print The Current Time Minute
# print(datetime.datetime.now().time().minute)
# # Print The Current Time Second
# print(datetime.datetime.now().time().second)

toDay = datetime.datetime.now()

birthDay = datetime.datetime(2003, 5, 22)
print(birthDay.strftime("%j %p %X %x"))

myOld = toDay - birthDay
print(myOld.days / 365.25)

# %% [markdown]
# ##################################################
# # 15- zip()
# ##################################################
# 

# %% [markdown]
# - the zip controled the length from the shortest list of parameters
# 

# %%
listl = [1, 2, 3, 4]
list2 = ["A", "B", "c"]

ultimateList1 = zip(listl, list2)
ultimateList2 = zip(listl, list2)
ultimateList3 = zip(listl, list2)

print(ultimateList1)


print("=" * 20)

## -1
for item in ultimateList1:
    print(item[0], item)

print("=" * 20)

## -2
for key, item in ultimateList2:
    print(f" {key} => {item}")

print("=" * 20)

## -3
print(list(ultimateList3))

# %% [markdown]
# 

# %% [markdown]
# ##################################################
# # 16- Decorators
# ##################################################
# 

# %%
from time import time


def speedTest(func):
    def nested(x):
        start = time()
        print(f"Start Function: {func.__name__}")
        func(x)
        end = time()
        print("End func")
        print(f"Time taken: {end - start}")

    return nested


@speedTest
def looping(x):
    for num in range(1, x):
        print(num)


looping(10)

# %% [markdown]
# ##################################################
# # 17- iterator
# ##################################################
# 

# %% [markdown]
# - iter()
# - next()
# 

# %%
list1 = [1, 2, 3]

for item1 in list1:
    print(item1)

print("=" * 30)

list2 = iter(["a", "b", "c"])
print(next(list2))
print(next(list2))
print(next(list2))
# print(next(list2)) => StopIteration:

print("=" * 30)

list2 = iter("AMB")
print(next(list2))
print(next(list2))
print(next(list2))
# print(next(list2)) => StopIteration:

# %% [markdown]
# ##################################################
# # 18- Generator
# ##################################################
# 

# %%
def myGenerator(x):
    yield x
    x += 1
    yield x
    x += 1
    yield x
    x += 1


gen = myGenerator(8)

print(next(gen))
print(next(gen))
print(next(gen))
# print(next(gen)) => StopIteration

# ********************
print("*" * 20)
# ********************


def my_range(start, end, step=1):
    while start < end:
        yield start
        start += step


# Usage:
for i in my_range(1, 30, 2):
    print(i)

# ********************
print("*" * 20)
# ********************

print(list(my_range(1, 30, 2)))

# %% [markdown]
# ##################################################
# # 19- DocString
# ##################################################
# 

# %%
def sum(
    *args,
) -> int:
    """
    func to sum all args
    """
    total = 0
    for num in args:
        total += num
    return total


print(sum(1, 2, 3, 4, 5))
print("==" * 30)

# all directories
print(dir(sum))
print("==" * 30)

# help
print(help(sum))
print("==" * 30)

# docstring
print(sum.__doc__)

# %% [markdown]
# ##################################################
# # 20- Errors
# ##################################################
# 

# %% [markdown]
# ## raise
# 

# %%
name = "10"

if type(name) != str:
    print("V_Error")
    print("hi1")
else:
    print("Ok1")

if type(name) != str:
    raise ValueError("V_Error")
    print("hi2")
else:
    print("Ok2")

# %% [markdown]
# ## Try & Except
# 

# %%
try:
    print(5 / 0)
    print(int("ahmed"))
    print(var)

except ZeroDivisionError:
    print("zero Division Error")
except ValueError:
    print("Value Error")
except:
    print("Error")
else:
    print("No Error")
finally:
    print("Finally")

# %% [markdown]
# ##################################################
# # 21- Regular Expressions
# ##################################################
# 

# %%
import re

# my_search = re.search(r"[A-Z]{2}", "OOsamaEElzero")
#
# print(my_search)
# print(my_search.span())
# print(my_search.string)
# print(my_search.group())
#
# is_email = re.search(r"[A-z0-9\.]+@[A-z0-9]+\.(com|net)", "Ahmed@AMB.com")
#
# if is_email:
#
#   print("This is A Valid Email")
#
#   print(is_email.span())
#   print(is_email.string)
#   print(is_email.group())
#
# else:
#
#   print("This is Not A Valid Email")

email_input = input("Please Write Your Email: ")

search = re.findall(r"[A-z0-9\.]+@[A-z0-9]+\.com|net", email_input)

empty_list = []

print(search)

if search != []:
    empty_list.append(search)

    print("Email Added")

else:
    print("Invalid Email")

for email in empty_list:
    print(email)

# %% [markdown]
# ## split()
# 

# %%
string_one = "I Love Python Programming Language"

search_one = re.split(r"\s", string_one)
# search_one = re.split(r"\s", string_one, 1)
# => ['I', 'Love Python Programming Language']

print(search_one)

# %% [markdown]
# ## sub()
# 

# %%
my_string = "   I Love Python   "

print(re.sub(r"\s", "-", my_string))
# print(re.sub(r"\s", "-", my_string, 1))
# => I-Love Python

# %% [markdown]
# ##################################################
# # 22- pass
# ##################################################
# 

# %%
for x in [1, 2, 3, 4]:
    pass


def func():
    pass


class student:
    pass


print("hello")

# %% [markdown]
# ##################################################
# # 23- if
# ##################################################
# 

# %% [markdown]
# - if in
# 

# %%
## 1
txt = "Ahmed Mohamed Bassiouny"
name = "Mohamed"
if name in txt:
    print(True)
else:
    print(False)

## 2
nums = [1, 2, 3, 4, 5]
num = 50
if num in nums:
    print(True)
else:
    print(False)

## 3
dect = {"name": "ahmed", "age": 20}
ietm = "name"
if ietm in dect:
    print(True)
else:
    print(False)

# %% [markdown]
# - = if else
# 

# %%
# 1
txt = "Ahmed Mohamed Bassiouny"
name = "Mohameyd"

chek = "yes" if name in txt else "No"
print(chek)


# 2
num = -1

num += 5 if num >= 0 else -5

print(num)

# %% [markdown]
# ##################################################
# # 24- OOP
# ##################################################
# 

# %% [markdown]
# - instance (Attributes & Methods)
# 

# %%
class student:
    def __init__(self, fName, lName, GPA, Level):
        self.fnm = fName
        self.lnm = lName
        self.GPA = GPA
        self.lv = Level

    def get_info(self):
        return f"Hello {self.fnm} {self.lnm} you are in level {self.lv} and your GPA is {self.GPA}  "


# ========================================
print("=" * 20)
# ========================================

student_1 = student("ahmed", "bassiouny", 3.9, 3)

print(student)
print(student_1)

# ========================================
print("=" * 20)
# ========================================

print(student_1.fnm)
print(student_1.get_info())

# %% [markdown]
# - class Attributes
# 

# %%
class std:
    allowed_levels = [1, 2, 3, 4]

    students_num = 0

    def __init__(self, fName, lName, GPA, Level):
        self.fnm = fName
        self.lnm = lName
        self.GPA = GPA
        self.lv = Level
        std.students_num += 1

    def get_info(self):
        return f"""Hello {self.fnm} {self.lnm} 
  you are in level {self.lv if self.lv in std.allowed_levels else "encorrect level" } 
  and your GPA is {self.GPA} 
  your id is {std.students_num}  """
        # pass


# ========================================
print("=" * 20)
# ========================================

student_1 = std("ahmed", "bassiouny", 3.9, 3)
print(student_1.get_info())

student_2 = std("mohamed", "bassiouny", 3.9, 3)
print(student_2.get_info())

student_3 = std("ahmed", "mohamed", 3.9, 0)
print(student_3.get_info())

student_4 = std("bassiouny", "bassiouny", 3.9, 3)
print(student_4.get_info())

# %% [markdown]
# - Class_methods & Static_methods
# 

# %%
class Car:
    def __init__(self, name, model, year, price):
        self.name = name
        self.model = model
        self.year = year
        self.price = price
        Car.num_of_cars += 1

    def get_info(self):
        return f"{self.name} {self.model} {self.year} {self.price}"

    num_of_cars = 0

    @classmethod
    def cars_num(cls):
        return Car.num_of_cars

    @staticmethod
    def our_slogan():
        return "the pest car in the world"


car_1 = Car("Renault", "Logan", 2010, 12000)
car_2 = Car("aaaaa", "ABC", 2019, 40000)
car_3 = Car("tttt", "HMP", 2013, 33250)

print(car_1.get_info())
print(Car.cars_num())
print(Car.our_slogan())

# %% [markdown]
# - Magic Methods
# 

# %%
class lang:
    def __init__(self, name, version, methods):
        self.name = name
        self.version = version
        self.methods = methods

    def __str__(self):
        return f"{self.name} {self.version} ({len(self.methods)} methods)  => {self.methods}"

    def __len__(self):
        return len(self.methods)

    def __eq__(self, other):
        return self.methods == other.methods


lang_1 = lang("Python", "3.10", ["print", "len"])
lang_2 = lang("C++", "7.8", ["stack"])

print(lang_1)
print(lang_2)

print(lang_1 == lang_2)
print(lang_1.__eq__(lang_2))

print(len(lang_1))

# %%
class Employee:
    def __init__(self, name, salary, years):
        self.name = name
        self.salary = salary
        self.years = years
        print(f"Name: {self.name}")
        print(f"Salary: {self.salary}")
        print(f"Years: {self.years}")

    def hello(self):
        print("parent => hello")


emp1 = Employee("Maria", 10000, 2)
print("+" * 20)


class Manager(Employee):
    def __init__(self, name, salary, years, emp_nums):
        self.emp_nums = emp_nums

        # 1
        # Employee.__init__(self, name, salary, years)
        # 2
        super().__init__(name, salary, years)
        print(f"emp_nums: {self.emp_nums}")
        print("Manager")

    def hello(self):
        print(f"parent => hello {self.name}")


mng1 = Manager("ahmed", 1000, 5, 9)
mng1.hello()

# %% [markdown]
# - property Decorator
# 

# %%
class std:
    def __init__(self, fName, lName, GPA):
        self.fnm = fName
        self.lnm = lName
        self.GPA = GPA

    @property
    def get_info(self):
        return f"Hello {self.fnm} {self.lnm} your GPA is {self.GPA} "


# ========================================
print("=" * 20)
# ========================================

student_1 = std("ahmed", "bassiouny", 3.9)
print(student_1.get_info)
# print(student_1.get_info()) # => Error

# %% [markdown]
# - ABCs => Abstract Base Class
# 

# %%
from abc import ABCMeta, abstractmethod


class programming(metaclass=ABCMeta):
    @abstractmethod
    def has_oop(self):
        pass

    def new_func(self):
        pass


class python(programming):
    def has_oop(self):
        return True

    # pass


class c(programming):
    def has_oop(self):
        return False


PL_1 = python()
print(PL_1.has_oop())

# %% [markdown]
# ##################################################
# # 25- Data Base (SQLite)
# ##################################################
# 

# %% [markdown]
# - create table
# 

# %%
# import
import sqlite3

# creat & connect
db = sqlite3.connect("files/students.db")

# cursor
cr = db.cursor()

# create(1) table and fields
# cr.execute("CREATE TABLE students (id INTEGER,name TEXT,age INTEGER,GPA INTEGER)  ")

# create(2) table and fields only if not exists
cr.execute(
    "CREATE  TABLE IF NOT EXISTS students (id INTEGER,name TEXT,age INTEGER,GPA INTEGER)  "
)

# close
# db.close()

# %% [markdown]
# - insert data
# 

# %%
# # insert(1)
# cr.execute("insert into students(id, name, age, GPA) values(1, 'ahmed', 20, 3.9)")
# cr.execute("insert into students(id, name, age, GPA) values(2, 'mohamed', 23, 3.0)")
# cr.execute("insert into students(id, name, age, GPA) values(3, 'nour', 21, 2.5)")

# # insert(2)
# users = [[1, 'ahmed', 20, 3.9], [2, 'mohamed', 23, 3.0], [3, 'nour', 21, 2.5]]
# for user in users :
#   cr.execute("insert into students(id, name, age, GPA) values(?,?,?,?)", user)

# insert(3)
users = [["ahmed", 20, 3.9], ["mohamed", 23, 3.0], ["nour", 21, 2.5]]
for key, user in enumerate(users):
    cr.execute(
        f"insert into students(id, name, age, GPA) values({key + 1},'{user[0]}',{user[1]},{user[2]})"
    )

# commit
db.commit()

# %% [markdown]
# - fetch data
# 

# %%
# fetch execute
# cr.execute("select * from students")
cr.execute("select id, name from students")

# # fetchone()
# print(cr.fetchone())
# print(cr.fetchone())
# print(cr.fetchone()) # return None if empty or fetching all rows

# # fetchall()
# print(cr.fetchall())
# print(cr.fetchall())  # return empty [] if empty or fetching all rows

# # fetchmany()
# print(cr.fetchmany(1))
# print(cr.fetchmany(3))  # return empty [] if empty or fetching all rows

print("=" * 20)
for x, y in cr.fetchall():
    print(x, "=>", y)


# db.close()

# %% [markdown]
# - delete & Update
# 

# %%
# 1- delete

# delete_all
cr.execute("delete from students ")

# delete_some_data
cr.execute("delete from students where id > 2 ")

# 2- update

# update_all
cr.execute("update students set name = 'student' ")

# update_some_data
cr.execute("update students set name = 'std' where id > 2 ")


# show data
cr.execute("select id, name from students")
print("=" * 20)

for x, y in cr.fetchall():
    cr.execute(f"update students set name = 'MR.{y}' where id = {x} ")
    print(x, "=>", y)

db.commit()
# db.close()

# %% [markdown]
# - Example-1
# 

# %%
import sqlite3


def get_all_data():
    try:
        db = sqlite3.connect("students.db")
        cr = db.cursor()
        cr.execute("SELECT * FROM students")
        res = cr.fetchall()

        # way (1) to get data
        for row in res:
            print(f"ID => {row[0]},name => {row[1]},age => {row[2]},GPA => {row[3]}")

        # # way (2) to get data
        # for x, y, w, z in res :
        #   print(f"ID => {x},name => {y},age => {w},GPA => {z}")

    except sqlite3.Error as er:
        print(f"Error : {er}")
        db = None

    finally:
        if db:
            db.close()
            print("data base is closed")


get_all_data()

# %% [markdown]
# - more
# 

# %%
##################################################################
### 1-Setting Up The Cursor to be more secured
cr = db.cursor()

my_tuple = ("Pascal", "65", 4)

# Inserting Data
cr.execute("insert into skills values(?, ?, ?)", my_tuple)

##################################################################
### 2-Fetch Data From Database (order, limit, offset, [<, >, >=, ... ] , not, and, in)
cr.execute("select * from skills order by name limit 3 offset 2")
cr.execute("select * from skills where user_id > 1")
cr.execute("select * from skills where user_id not in(1, 2, 3)")

# %% [markdown]
# - Example-2
# 

# %%
# -----------------------------------------------------
# -- Databases => SQLite => Create Skills App Part 4 --
# -----------------------------------------------------

# Import SQLite Module
import sqlite3

# Create Database And Connect
db = sqlite3.connect("files/app.db")

# Setting Up The Cursor
cr = db.cursor()

cr.execute(
    "CREATE  TABLE IF NOT EXISTS skills (name TEXT, progress INTEGER, user_id INTEGER) "
)


def commit_and_close():
    """Commit Changes and Close Connection To Database"""
    db.commit()  # Save (Commit) Changes
    db.close()  # Close Database
    print("Connection To Database Is Closed")


# My User ID
uid = 1

# Input Big Message
input_message = """
What Do You Want To Do ?
"s" => Show All Skills
"a" => Add New Skill
"d" => Delete A Skill
"u" => Update Skill Progress
"q" => Quit The App
Choose Option:
"""

# Input Option Choose
user_input = input(input_message).strip().lower()

# Command List
commands_list = ["s", "a", "d", "u", "q"]


# Define The Methods
def show_skills():
    cr.execute(f"select * from skills where user_id = '{uid}'")

    results = cr.fetchall()

    print(f"You Have {len(results)} Skills.")

    if len(results) > 0:
        print("Showing Skills With Progress: ")

    for row in results:
        print(f"Skill => {row[0]},", end=" ")

        print(f"Progress => {row[1]}%")

    commit_and_close()


def add_skill():
    sk = input("Write Skill Name: ").strip().capitalize()

    cr.execute(f"select name from skills where name = '{sk}' and user_id = '{uid}'")

    results = cr.fetchone()

    if results == None:  # Theres No Skill With This Name In Database
        prog = input("Write Skill Progress ").strip()

        cr.execute(
            f"insert into skills(name, progress, user_id) values('{sk}', '{prog}', '{uid}')"
        )

    else:  # Theres A Skill With This Name in Database
        print("You Cannot Add It")

    commit_and_close()


def delete_skill():
    sk = input("Write Skill Name: ").strip().capitalize()

    cr.execute(f"delete from skills where name = '{sk}' and user_id = '{uid}'")

    commit_and_close()


def update_skill():
    sk = input("Write Skill Name: ").strip().capitalize()

    prog = input("Write The New Skill Progress ").strip()

    cr.execute(
        f"update skills set progress = '{prog}' where name = '{sk}' and user_id = '{uid}'"
    )

    commit_and_close()


# Check If Command Is Exists
if user_input in commands_list:
    # print(f"Command Found {user_input}")

    if user_input == "s":
        show_skills()

    elif user_input == "a":
        add_skill()

    elif user_input == "d":
        delete_skill()

    elif user_input == "u":
        update_skill()

    else:
        print("App Is Closed.")

        commit_and_close()

else:
    print(f'Sorry This Command "{user_input}" Is Not Found')

