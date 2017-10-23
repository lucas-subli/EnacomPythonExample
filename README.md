# ENACOM python example


Examples for ENACOM's code style for python.
### Prerequisites

What things you need to have to be able to run:


* Python 3.6 +
* VirtualEnvWrapper is recommended but not mandatory

## Definitions

A Python module is simply a Python source file, which can expose classes, functions and global variables.

When imported from another Python source file, the file name is treated as a namespace.

A Python package is simply a directory of Python module(s).

For example, imagine the following directory tree in /usr/lib/python/site-packages:

mypackage/__init__.py <-- this is what tells Python to treat this directory as a package
mypackage/mymodule.py
So then you would do:

import mypackage.mymodule
or

from mypackage.mymodule import myclass

## Conventions

# The class / methods should be commented with triple " as soon as they are declared

# The default code style is the pycharm one

# Docstrings documentation is available at http://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html

To make pycharm accept it press ctrl + shift + a and search for python integrated tools and finally change DocString format to google

# Prefix test files with test_

### Package and Module Names
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


## Guidelines

### always call numpy np

For fucks sake just do it

### Use is not operator rather than not ... is. While both expressions are functionally identical, the former is more readable and preferred.

Yes:

if foo is not None:
No:

if not foo is None:


### Derive exceptions from Exception rather than BaseException. Direct inheritance from BaseException is reserved for exceptions where catching them is almost always the wrong thing to do.

Design exception hierarchies based on the distinctions that code catching the exceptions is likely to need, rather than the locations where the exceptions are raised. Aim to answer the question "What went wrong?" programmatically, rather than only stating that "A problem occurred" (see PEP 3151 for an example of this lesson being learned for the builtin exception hierarchy)

Class naming conventions apply here, although you should add the suffix "Error" to your exception classes if the exception is an error. Non-error exceptions that are used for non-local flow control or other forms of signaling need no special suffix.


## Authors

* **Lucas 'Subli' Ferreira** - *Every line so far.* - [lucas.subli@gmail.com](mailto:lucas.subli@gmail.com)


## Extra Material

https://www.python.org/dev/peps/pep-0008/

## License

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

 