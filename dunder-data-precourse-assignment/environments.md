# Other Programming Environments

# Using a Text Editor

Interactive programming using the Python REPL is nice to immediately get results together but when building larger programs its likely that you will need a more formidable programming environment such as a text editor. There are [dozens and dozens][13] of text editors. This tutorial covers the popular Sublime Text 3 editor which may be used for any programming language. 

# Installing Sublime Text 3
There are many ways to run and write Python. Python can be written in any text editor, even the basic ones that come preinstalled with all operating systems. Sublime Text 3 is an enhanced text editor that is highly customizable to help make programming in Python easier.

> [Download and install Sublime Text 3][8] and open it.

To enhance the editing experience of sublime specifically for Python we first need to install the package control manager. This is the package control manager for Sublime and has nothing to do with `conda` or `pip`. There are 1000's of third party packages written for Sublime.

> 1. Visit the [Package Control website][9]. All Sublime packages can be found here. 
> 1. Click the `install now` button and follow the instructions to install the package manager.

Now that you have the package manager, you may begin to install packages. We will install the Anaconda Sublime package. This has nothing to do with the Anaconda distribution, it just happens to share the same name. It adds code completion, linting, inline documentation and more. Visit the [Anaconda Sublime package home page][10] for more info.

> 1. To access the package manager, you must first open up the `command palette` with `cmd + shift + P`. It is also found under Tools -> Command Palette.
> 1. In the text box that pops up, begin typing in the word `install`. Click on `Package Control: Install Package`
> 1. A new text box will open up with a huge list of available packages
> 1. Type in 'Anaconda'. It should be the first option damnwidget.github.io/anaconda

# Opening our first Python program
Open up the program `guess_number.py` in Sublime. This is a small game that attempts to guess your number within a few step. Before we play or analyze the game, take a look at the bottom right hand corner of Sublime. You should see some text that reads `Tab Size: 4`. There is nothing inherently wrong with this except that Python's style guide PEP 8 suggests using 4 spaces over tabs. To change the default settings do the following:

> 1. While in `guess_number.py` click on `Sublime Text -> Preferences -> Settings - Syntax Specific`
> 1. This will open up a file titled `Python.sublime_settings`. 
> 1. Append to the end of this JSON file: `"translate_tabs_to_spaces": true`
> 1. This defaults all tabs to spaces for only your Python files. You might need to close and reopen sublime to see the effects take place.

Now lets take a look at the contents of `guess_number.py`. Comments may be made with the hash symbol or between triple quotes. The top of the file has comments with the author's name and purpose. All functions have triple quotes immediately after their definition. These quotes have a special name and purpose. They are called docstrings and magically appear whenever you attempt to get help on this function in the future.

You should also see different lines of text outlined and some gray circles to the left of the line numbers. This indicates that there might be some linting or style issues with the current code. You can customize the appearance of all your downloaded sublime packages. Go the menu Sublime Text -> Preferences -> Package Settings -> Anaconda -> Settings - Default. This is a JSON file that has easy to read documentation.

Let's change one of the settings in this file. 
> 1. Scroll down to around line 286
> 1. Find the line with the `anaconda_linter_mark_style` setting. It should currently be mapped to `outline`.
> 1. Look at the comments above and change the setting to something else
> 1. Go back to the `guess_number.py` file and notice the changes.

## Executing this program
The most straightforward way to execute this program is to do the following:
> 1. Open a terminal
> 1. `cd` into the directory where `guess_number.py` exits
> 1. Run the command `python guess_number.py`
> 1. Play the game a few times 

## Running programs in Sublime
Some programs may be run directly in Sublime. Unfortunately, `guess_number.py` does not work since it takes user input. We will download an additional package later that will allows us to run it. 

For now we will run a different program by using the build system. 

> 1. Open th file `rain.py`. This program may be found at [matplotlib's site][14].
> 1. Go to Tools -> Build to make it rain
> 1. Exit out of program and press `esc` to remove the bottom window.

## Using the Sublime console
Sublime comes with its own Python interpretter that is separate from the one that you downloaded with the Anaconda distribution.

> 1. Go to View -> Show Console
> 1. Type in some basic Python commands

This is not meant for serious development. There is a much better console that you can add to Sublime.

## SublimeREPL Package
We will now download another very useful package called `SublimeREPL`.

> 1. Open the command pallette with `cmd + shift + p`
> 1. Begin typing in `install` and open the `Package Control: Install Package`
> 1. You will see a very long list of available packages
> 1. Type in `SublimeREPL` and install it.
> 1. Open up the command pallette again and type in `SublimeREPL: Python` and press enter
> 1. This runs the REPL directly in Sublime
> 1. Run a few Python commands

### Running `guess_number.py` with SublimeREPL
Remember how I mentioned above that `guess_number.py` does not run well by using `Build`? You can however, run the program with SublimeREPL.

> 1. Go to the `guess_number.py` file
> 1. Go to Tools -> SublimeREPL -> Python - Run Current File 
> 1. This exacat option is also available via the command palette.
> 1. Play the game in the REPL

You may also use the REPL to run code interactively. 
> 1. Start SublimeREPL and run some lines of code

### Sublime resources

+ [Watch this video][11] to get more in-depth tutorial on Sublime packages for Python.
+ Sublime has a [very detailed documentation][15] page where you can learn everything about it.
+ There is also a package called Sublime Tutor you can install and learn through practice.

## IPython
IPython is an enhanced command line REPL with much more functionality than the default one shipped with Python. IPython stands for interactive Python and has grown extremely popular in recent years.

Let's see some of the extra features it provides

> 1. Launch IPython by opening up a terminal and running the command `iPython`
> 1. Enter `?` and press enter. This will give you a quick overview of IPython
> 1. For a more complete reference of its capabilities run `%quickref`

Get help with any object by placing a question mark after it.
```
   import pandas as pd
   pd?
```

Get nice tab completion with `pd.<press tab>`

Run shell commands with `!` like `!ls`

### IPython magic commands
IPython comes equipped with a few dozen [magic commands][18] that conveniently do things that are not so easy using native Python interactively. Take for instance the `%timeit` magic which is the one I most often use. Let's time the difference between adding a one to each element in a list vs adding one to each element of a NumPy array.

```python
In [1]: n = 10000000
In [2]: some_list = list(range(n))
In [3]: import numpy as np
In [4]: some_array = np.arange(n)
In [5]: %timeit [x+1 for x in some_list]
809 ms ± 19.1 ms per loop (mean ± std. dev. of 7 runs, 1 loop each)
In [6]: %timeit some_array + 1
27.9 ms ± 720 µs per loop (mean ± std. dev. of 7 runs, 10 loops each)
```

### IPython resources
+ [IPython documentation][16]
+ [IPython cookbook][17]

## PyCharm
PyCharm is an excellent [IDE][19] (integrated development environment) made specifically for Python. It provides lots of graphical tools to help developers produce code.
There is a free community edition a paid enterprise edition and an education edition with lots of exercises to get you started using it. 

Let's download and install PyCharm Edu
> 1. Visit [PyCharm Edu][20] and download and install.
> 1. A new project title **Introduction to Python** should start up.
> 1. If it does not navigate to file -> new project -> educational
> 1. Before beginning on the 50 exercises you will want to ensure that PyCharm is using a Python 3 interpretter
> 1. Go to Preferences -> Project -> Project Interpreter and choose the Python 3 interpreter than comes with Anaconda
> 1. Complete the exercises by reading the task description and editing the code.
> 1. Press the run button to execute the code and then mark the code as complete.

PyCharm offers a lot more and is excellent for large and complex projects. Watch [this series of YouTube][21] videos to learn more.

## Minimal text editors
Some developers like to keep their hands on the keyboard at all times and prefer minimal text editors like VIM or Emacs. [Visit this page][22] to see a longer list of editors for Python.

## Jupyter Notebook
We have finally arrived at my personal favorite environment for doing data science. Jupyter Notebooks provide a web-based interface to a number of different programming languages. The project was originally titled "iPython notebook" and was specifically built for just iPython as a backend. It turned out that notebooks are a very popular way to develop. To accomodate other languages that project was retitled Jupyter for the languages **JU**lia, **PY**thon and **R**. The Jupyter project now works with over 50 different language "kernels" of which IPython is just one.

The rest of this tutorial will take place in Jupyter Notebooks.

> 1. Open a terminal and run `jupyter notebook`
> 1. Open up the first notebook `0 Jupyter Intro`

[1]: (https://www.meetup.com/Houston-Data-Science/) 
[2]: (https://www.python.org/downloads/)
[3]: https://git-scm.com/downloads
[4]: https://git-scm.com/book/en/v2/Getting-Started-First-Time-Git-Setup
[5]: https://jakevdp.github.io/blog/2016/08/25/conda-myths-and-misconceptions/
[6]: https://www.continuum.io/downloads
[7]: https://prismoskills.appspot.com/lessons/Git/imgs/git_file_stages.png
[8]: https://www.sublimetext.com/
[9]: https://packagecontrol.io/
[10]: http://damnwidget.github.io/anaconda
[11]: https://www.youtube.com/watch?v=xFciV6Ew5r4
[12]: https://en.wikipedia.org/wiki/Read%E2%80%93eval%E2%80%93print_loop
[13]: https://en.wikipedia.org/wiki/Comparison_of_text_editors
[14]: https://matplotlib.org/examples/animation/rain.html
[15]: http://docs.sublimetext.info/en/latest/
[16]: http://ipython.readthedocs.io/en/stable/
[17]: https://github.com/ipython/ipython/wiki?path=Cookbook
[18]: http://ipython.readthedocs.io/en/stable/interactive/tutorial.html#magic-functions
[19]: https://en.wikipedia.org/wiki/Integrated_development_environment
[20]: https://www.jetbrains.com/pycharm-edu/
[21]: https://www.youtube.com/watch?v=BPC-bGdBSM8&list=PLQ176FUIyIUZ1mwB-uImQE-gmkwzjNLjP
[22]: https://wiki.python.org/moin/PythonEditors
