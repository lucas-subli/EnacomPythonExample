# ENACOM python example

This project will present examples for ENACOM's code style for python.
As well as a tutorial on how to configure your environment for the 
first time.

The default IDE is pycharm community edition. Available at:
https://www.jetbrains.com/pycharm/

We do recommend installing it through the
[jetbrains toolbox](https://www.jetbrains.com/toolbox/) to keep it
up to date.

The professional edition is available for free if you are a student and
would like to have the extra features.

The IDE is quite powerful and provides a vast set of features to speed 
up and facilitate python development. Take your time to get to know this
amazing tool that is at your disposal.

Memorizing shortcuts is also very helpful, I recommend using a [cheat 
sheet](https://blog.jetbrains.com/pycharm/files/2010/07/PyCharm_Reference_Card.pdf) while you are a beginner in the tool.

Finally the full action search (ctrl + shift + a) allows you to search 
for any IDE feature and is quite powerful, do not be afraid to 
experiment with it.


## Prerequisites

What things you need to have to be able to run:


* Python 3.6 +
* Pip 3+
* VirtualEnvWrapper is recommended but not mandatory

Disclaimer: This tutorial was made and tested on Ubuntu, if 
you are not using a Linux distribution you should be.
 
If you ignored my warning and want to keep using other Operational 
System we will provide no help or company time for you to configure
your environment, and all of your code must work on linux.

# Setup 

## Installing python 3.6

This quick tutorial is going to show you how to install the latest
Python 3.6.1 in Ubuntu.

Ubuntu comes with both Python 2.7 and Python 3.5 by default.
You can install Python 3.6 along with them by doing following steps:

* Open terminal via Ctrl+Alt+T or searching for “Terminal” from 
app launcher. 
When it opens, run commands:

```bash
$ sudo apt-get update
$ sudo apt-get install python3.6
```

Now you have three Python versions, use python command for version 2.7,
python3 for version 3.5, and/or python3.6 for version 3.6.x.

To verify if it worked type
```bash
python3.6 --version
```
your output should look like:

Python 3.6.2

## Installing pip

The first step is to install pip , a Python package manager.
In the Linux terminal type:

```shell
$ wget https://bootstrap.pypa.io/get-pip.py
$ sudo python get-pip.py
$ sudo python3 get-pip.py
```

## Installing virtualenv and virtualenvwrapper

Using pip , we can install any package in the Python Package Index
quite easily including virtualenv and virtualenvwrapper. 
I’m a fan of Python virtual environments and I encourage you to 
use them for ENACOM projects.

In case you have multiple projects on your machine, using virtual 
environments will allow you to isolate them and install 
different versions of packages. In short, using both virtualenv 
and virtualenvwrapper  allow you to solve the 
“Project X depends on version 1.x, 
but Project Y needs 4.x dilemma.

[The folks over at RealPython may be able to convince you if 
I haven’t, so give this excellent blog post on RealPython a read.](https://realpython.com/blog/python/python-virtual-environments-a-primer/)

Again, let me reiterate that it’s standard practice in the 
Python community to be leveraging virtual environments of some sort, 
so I suggest you do the same:

```shell
$ sudo pip install virtualenv virtualenvwrapper
$ sudo rm -rf ~/.cache/pip get-pip.py
```
Once we have  virtualenv  and  virtualenvwrapper  installed, 
we need to update our ~/.bashrc  file to include the following l
ines at the bottom of the file:


```
export WORKON_HOME=$HOME/.virtualenvs
export VIRTUALENVWRAPPER_PYTHON=/usr/bin/python3
source /usr/local/bin/virtualenvwrapper.sh
```

After editing our ~/.bashrc  file, we need to reload the changes:

```shell
$ source ~/.bashrc
```

Now that we have installed  virtualenv  and virtualenvwrapper, 
the next step is to actually create the Python virtual
environment — we do this using the  mkvirtualenv  command.


With that said, for the following command, ensure you set the --python 
flag to python 3.6 .
```
$ mkvirtualenv enacom --python=python3.6
```

You can name this virtual environment whatever you like 
(and create as many Python virtual environments as you want), 
but for the time being, I would suggest sticking with the enacom name 
as that is what I’ll be using throughout the rest of this tutorial.

If you ever reboot your Ubuntu system; log out and log back in; 
or open up a new terminal, you’ll need to use the workon  
command to re-access your dl4cv  virtual environment. 
An example of the workon command follows:

```
$ workon enacom
```

To validate that you are in the enacom virtual environment, 
simply examine your command line — if you see the text (enacom) 
preceding your prompt, then you are in the enacom virtual environment:


![alt text](https://i.imgur.com/Vg4MC0f.png "Verifying env")

The virtual env can also be configured in your project in pycharm.
When creating a project you can create a new virtual env or select
an existing one: 

![alt text](https://i.imgur.com/9YIwsL9.png "Pycharm create env")

![alt text](https://i.imgur.com/liKv3w6.png "Pycharm select env")



If you want to change the env of an existing project access the all 
search menu in pycharm by pressing ctrl + shift + a
and type in ***Project Interpreter*** and changing for the desired env.

![alt text](https://i.imgur.com/N6JpUPu.png "Pycharm find config")

![alt text](https://i.imgur.com/bsUHv6d.png "Pycharm change env")


And with the environments configured we are ready to write some code

# Definitions

A Python module is simply a Python source file, which can expose classes,
functions and global variables.

When imported from another Python source file, the file name 
is treated as a namespace.

A Python package is simply a directory of Python module(s).

For example, imagine the following directory tree 
in /usr/lib/python/site-packages:

***mypackage/\_\_init\_\_.py*** <-- this is what tells Python to 
treat this directory as a package
***mypackage/mymodule.py***
So then you would do:

```python
import mypackage.mymodule
```

or

```python
from mypackage.mymodule import myclass
```


# Conventions

## Code style 

The default code style is the pycharm one. So if your IDE is 
complaining about something (an underline by default) you should
fix it. Please also keep the spelling
check on and use the features provided in the IDE to suppress warnings
when necessary

Avoid committing code that have warnings or errors, even grammatical 
ones. TODOs are completely acceptable.

## Mandatory comments

Docstrings comments are mandatory

Docstrings documentation is available at 
http://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html

The class / methods should be commented with triple " as soon
as they are declared

To make pycharm accept it, and provide a help interface
when using commented methods press ctrl + shift + a 
and search for python integrated tools and finally change 
DocString format to google

![alt text](https://i.imgur.com/ZUkABiZ.png "Pycharm find Integrated Tool")

![alt text](https://i.imgur.com/mm1Uqmh.png "Pycharm Google Docstring")


## Package and Module Names
Modules should have short, all-lowercase names. Underscores can be used in the module name if it improves readability. Python packages should also have short, all-lowercase names, although the use of underscores is discouraged.

When an extension module written in C or C++ has an accompanying Python module that provides a higher level (e.g. more object oriented) interface, the C/C++ module has a leading underscore (e.g. _socket).

### Class Names
Class names should normally use the CapWords convention.

The naming convention for functions may be used instead in cases where the interface is documented and used primarily as a callable.

Note that there is a separate convention for builtin names: most builtin names are single words (or two words run together), with the CapWords convention used only for exception names and builtin constants.

### Function Names
Function names should be lowercase, with words separated by underscores as necessary to improve readability.

mixedCase is allowed only in contexts where that's already the prevailing style (e.g. threading.py), to retain backwards compatibility.

### Function and method arguments
Always use self for the first argument to instance methods.

Always use cls for the first argument to class methods.

If a function argument's name clashes with a reserved keyword, it is generally better to append a single trailing underscore rather than use an abbreviation or spelling corruption. Thus class_ is better than clss. (Perhaps better is to avoid such clashes by using a synonym.)

### Method Names and Instance Variables
Use the function naming rules: lowercase with words separated by underscores as necessary to improve readability.

Use one leading underscore only for non-public methods and instance variables.

To avoid name clashes with subclasses, use two leading underscores to invoke Python's name mangling rules.

Python mangles these names with the class name: if class Foo has an attribute named __a, it cannot be accessed by Foo.__a. (An insistent user could still gain access by calling Foo._Foo__a.) Generally, double leading underscores should be used only to avoid name conflicts with attributes in classes designed to be subclassed.

Note: there is some controversy about the use of __names (see below).

### Constants
Constants are usually defined on a module level and written in all capital letters with underscores separating words. Examples include MAX_OVERFLOW and TOTAL.


# Tests

Every module should have a folder dedicated to the testing code
of that specific module


Every test file should be prefixed with the word ***test_***


Every single class should have a corresponding test.


We ***recommend*** using TDD (Test Driven Development).


## TDD

TDD, in its most basic terms, is the process of implementing 
code by writing your tests first, seeing them fail, then writing 
the code to make the tests pass. You can then build upon this 
developed code by appropriately altering your test to expect the 
outcome of additional functionality, then writing the code to make 
it pass again.


You can see that TDD is very much a cycle, with your code going 
through as many iterations of tests, writing, and development as 
necessary, until the feature is finished. By implementing these 
tests before you write the code, it brings out a natural tendency 
to think about your problem first. While you start to construct 
your test, you have to think about the way you design your code.
 What will this method return? What if we get an exception here?
  And so on.
  
  
![alt text](https://i.imgur.com/loFXKJ3.jpg "TDD Cycle")



By developing in this way, it means you consider the different 
routes through the code, and cover these with tests as needed. 
This approach allows you to escape the trap that many developers
fall into (myself included): diving into a problem and writing
code exclusively for the first solution you need to handle.


The process can be defined as such:

Write a failing unit test
Make the unit test pass
Refactor
Repeat this process for every feature, as is necessary.

# General Guidelines

## always call numpy np

For fucks sake just do it

## Use is not operator rather than not ... is. While both expressions are functionally identical, the former is more readable and preferred.

Yes:
```python
if foo is not None:
```

No:

```python
if not foo is None:
```


## Derive exceptions from Exception rather than BaseException. Direct inheritance from BaseException is reserved for exceptions where catching them is almost always the wrong thing to do.

Design exception hierarchies based on the distinctions that code catching the exceptions is likely to need, rather than the locations where the exceptions are raised. Aim to answer the question "What went wrong?" programmatically, rather than only stating that "A problem occurred" (see PEP 3151 for an example of this lesson being learned for the builtin exception hierarchy)

Class naming conventions apply here, although you should add the suffix "Error" to your exception classes if the exception is an error. Non-error exceptions that are used for non-local flow control or other forms of signaling need no special suffix.


# Authors

* **Lucas 'Subli' Ferreira** - *Every line so far.* - [lucas.subli@gmail.com](mailto:lucas.subli@gmail.com)


# Extra Material

https://www.python.org/dev/peps/pep-0008/

# License

 **WTFPL**  [(Do What the Fuck You Want To Public License)](https://en.wikipedia.org/wiki/WTFPL)
 
     === Version 2 ===
     The text of the license, written by Sam Hocevar:<ref name="Hocevar, WTFPL, 2.0" />


	 DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE
		Version 2, December 2004
 
	 Copyright (C) 2004 Sam Hocevar <sam@hocevar.net>
 
     Everyone is permitted to copy and distribute verbatim or modified
     copies of this license document, and changing it is allowed as long
     as the name is changed.
 
			DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE
     TERMS AND CONDITIONS FOR COPYING, DISTRIBUTION AND MODIFICATION
 
     0. You just DO WHAT THE FUCK YOU WANT TO.

 