# Dunder Data Pre-course Assignment

This repository contains a pre-course assignment that is intended to get everyone on the same page upon entering the class so we can quickly dive into the material. It will cover...  

1. Bootcamp Objectives
2. Environment setup with Anaconda
4. Intro to Jupyter notebooks
5. Intro to the Python programming language

## Primary Bootcamp Objectives

The primary objective of this bootcamp is to teach you the concepts of data exploration and machine learning using the tools provided by the Python programming language. By the end of the bootcamp, you will have a routine in place that you can trust to begin exploring any dataset. You will be able to apply any filter, transformation, aggregation, or visualization to your data. You will also learn how to combine your results into a report that can be shared. In addition to exploratory data analysis, you will learn how to apply supervised machine learning models using the latest and most up-to-date workflows.

### Learning Objectives

There are many more items that are crucial to the entire learning process.

* Tools vs Concepts
* Minimally sufficient Pandas
* Asking and answering your own questions
* A Workflow for doing data analysis
* Getting help

#### Tools vs Concepts

There is an important distinction that must be made between two major themes throughout the course; tools and concepts. The major tool we will be using is the Pandas library. As programmers, we must obey its syntactical rules in order to complete a data analysis.

The data analysis itself is driven by theoretical and practical concepts such as strategies for filling in missing values or handling of outliers. These concepts are independent of the tool we use and do not change much over time.

In order to implement these concepts in our dataset we must use a particular tool. During this course, you should be aware of this divide between the tools (essentially syntax) and the concepts. Both are necessary in order to produce a valid data analysis.

#### Minimally sufficient Pandas

Pandas is a huge library and can be quite intimidating for those first approaching it. Pandas has (unfortunately) many commands that do the same thing. It is common to see different experts at Pandas all answer the same problem with different syntax.

This course focuses on using a subset of the Pandas library that is the most powerful, explicit, and efficient with the least amount of commands. The goal is not to learn the Pandas library, but to learn how to do data analysis with the help of the Pandas library. "Minimally sufficient Pandas" is a phrase that encapsulates this mindset and will be reinforced throughout the course.

#### Asking and answering your own questions

There are several hundred questions available to be solved within this course. While answering these questions will help reinforce the material, they do not help much when developing a data analysis on your own. You will need to be able to think of your own questions about the dataset you are exploring and answer them programmatically.

There are sections of this course devoted to practicing this skill. It is also an exercise in learning the limits of your knowledge. If you devise a question, and know what the answer should look like, but do not know what commands to issue to reach that final state, then you have a gap in your knowledge. It is important to discover these gaps and ask your question to an expert who can help you solve it.

#### A workflow for doing data analysis

As a beginner, when proceeding through a data analysis, you will not have a standardized workflow. It often helps to have a simple procedure to follow that you can trust to help structure and standardize the workflow. In the beginning of the course, we will cover this simple procedure.

#### Getting Help

This is a short course and you will soon be on your own crafting new data analyses. The skill of helping yourself is extremely important. Throughout the course, we will cover many common ways to get help as well as how to learn by experimenting.

## Course Assumptions

While it helps to have prior programming experience and exposure to elementary statistics, there is no strict pre-requisite knowledge assumed for this course other than a desire to get better at making sense of data. That said, this pre-course will cover quite a lot of material and it is expected that all students come to class with a good understanding of it.

## Pre-Course Assessment

When you have finished this pre-course assignment, please go the [assessment folder](assessment), read the instructions, and take the assessment.

## Setting up the Environment

One of the hurdles beginners face is setting up a programming environment where they can successfully run Python.

# Installing Anaconda with Python 3

Anaconda is the name of a distribution of Python created by a company with the same name (formerly Continuum Analytics). It is currently the most popular distribution of Python for data science and contains all the popular libraries plus some extra software.

* Please download [Anaconda with Python 3][1] now for your operating system
* Select all the defaults during installation

## Reason for Python 3 and not Python 2

Jan 1, 2020 will mark the last day that Python 2 will be officially supported. Python 3 is the present and future and nearly all serious development will use it.

## Testing for Successful Installation

Let's ensure that the Anaconda distribution got installed correctly and that you are indeed running the latest version of Python 3.

## Windows Users

Open up the program **`Anaconda Prompt`**. This program will look very similar to the normal **`Command Prompt`** but will place the destination of the latest Python 3 version at the beginning of the path.

## Mac/Linux Users

Open up a terminal

## All Users

1. Type **`python`** at the prompt
2. Ensure that in the header you see Python version 3.X where X >= 6 
![][2]
3. If you don't see this header with the three arrow **`>>>`** prompts and instead see an error or alternatively have Python 2 run, then we need to troubleshoot here.

## Troubleshooting

### Windows

The error message that you will see is **`'python' is not recognized as an internal or external command...`**

Make sure you are running the **`Anaconda Prompt`** and not the normal **`Command Prompt`**.

If you are in **`Anaconda Prompt`** and still getting this message then see the optional installation below.

### Mac/Linux

The error message you should have received is **`python: command not found`**. The following will still work if you came here because Python 2 ran.

Let's try and find out where Python is installed on your machine.

1. Run the command: **`$ which -a python`**    
![][4]
1. This outputs a list of all the locations where there is an executable file with the name **`python`**. My machine has two Python installations.
1. This location must be contained in something called the **PATH**. The path is a list (separated by colons) containing directories to look through to find executable files.
2. Let's output the path with the command: **`echo $PATH`**
![][5]
1. My path contains the directory (**`/Users/Ted/Anaconda/bin`**) from above so running the command **`python`** works for me.
1. If your path does not have the directory outputted from step 1 then we will need to edit a file called **`.bash_profile`** (or **`.profile`** on some linux machines)
1. Make sure you are in your home directory and run the command: **`nano .bash_profile`**
1. This will open up the file **`.bash_profile`**, which may be empty
2. Add the following line inside of it: **`export PATH="/Users/Ted/anaconda3/bin:$PATH"`** (use your Anaconda directory)
3. Exit (**`ctrl + x`**) and make sure to save
4. You may need to reload the bash profile by executing the command: `source ~/.bash_profile`
5. Close and reopen the terminal and execute: **`echo $PATH`**
6. The path should be updated with the Anaconda directory prepended to the front
7. Again, type in **`python`** and you should be good to go
8. **`.bash_profile`** is itself a file of commands that get executed each time you open a new terminal.

## Optional (Advanced) Installation for Windows Users

It is possible to run Python from the **`Command Prompt`** directly in Windows. If you so desire, [manually configure][3] your **Command Prompt**.

## More on the path (all operating systems)

The path is a list of directories that the computer will search in order, from left to right, to find an executable program with the name you entered on the command line. It is possible to have many executables with the same name but in different folders. The first one found will be the one executed.

### Displaying the path

* Windows: **`path`** or **`set %PATH%`**
* Mac/Linux **`echo $PATH`**

### Finding the location of a program

* Windows: **` where program_name`**
* Mac\Linux: **`which program_name`**

### Editing the path

* Windows: Use the [set (or setx)][6] command or from a [GUI][7]
* Mac\Linux: By editing the **`.bash_profile`** as seen above

# Python vs IPython

**`python`** and **`ipython`** are both executable programs that run Python interactively from the command line. The **`python`** command runs the default interpreter, which comes prepackaged with Python. There is almost no reason to ever run this program. It has been surpassed by **`ipython`** (interactive Python) which you also run from the command line. IPython adds lots of functionality such as syntax highlighting and special commands.

# IPython vs Jupyter Notebook

The Jupyter Notebook is a browser based version of IPython. Instead of being stuck within the confines of the command line, you are given a powerful web application that allows you to intertwine code, text, and images. [See this][8] for more details of the internals.

![][9]

# Jupyter Lab

[Jupyter Lab][11] is yet another interactive browser-based program that allows you to have windows for notebooks, terminals, data previews, and text editors all on one screen.  It is the "next-generation user interface for Project Jupyter".

# Interactive Computing vs Executing a File

### Interactive Computing
Nearly all the work that we will do in class will be done **interactively**, meaning that we will be typing one, or at most a few lines of code into an **input** area and executing it. The result will be displayed in an **output** area.

### Executing a Python File
The other way we can execute Python code is by writing it within a file and then executing the entire contents of that file.

An entire file of Python code can be executed either from the command line. We execute the file by placing the name of the file after the **`python`** command. For instance, if you are in the home directory of this repository, run the following on the command line to play a number guessing game.

**`python scripts/guess_number.py`**

### Interactive Computing for Data Science
Interactive computing is the most popular way to analyze data using Python. You can get instant feedback which will direct how the analysis progresses.

### Writing Code in Files to Build Software
All software has code written in files. This code is executed in its entirety. You cannot add or change code once the file has been executed. Although most tutorials (including this one) will use an interactive environment to do data science, you will eventually need to take your exploratory work from an interactive session and put it in inside of a file.

# Anaconda Navigator vs Command Line

Anaconda comes with a simple GUI-based program called **Anaconda Navigator** to launch Jupyter Notebooks, Labs and a few other programs. This is just a point and click method for doing the same thing on the command line.

# Downloading the material

1. Go to the top of this page and click the green button 'Clone or download'
1. Click "Download ZIP"
1. Go to your downloads folder and unzip the files
1. Create a folder somewhere else in your file system and name it 'Dunder Data Bootcamp'
1. Move those files into this new folder

# Files

 As you can see at the top of this page, there are multiple file types in this repository.

1. The README file that you are reading right now
2. The `.ipynb` files where you will be completing the assignments
3. A few `.py` files that store Python scripts that you will run or edit

# The Actual Assignment!

OK, so you've installed Anaconda, downloaded the material and are ready for your pre-course assignment. To begin learning...

1. Open a terminal
2. `cd` into the directory where this repository is located on your machine
3. Run the command `jupyter notebook`
4. A new browser tab will open up located at `localhost:8888` with a listing of all the files in this repository.
5. Click on `1. Intro Jupyter Notebook.ipynb` and a Jupyter notebook will open that will walk you through the entire assignment.
6. Complete each numbered notebook
7. Check your answers as you go by opening the precourse solutions notebook only AFTER you have attempted the problems on your own
8. It is mandatory that you complete the precourse. Please ask questions about the assignment in slack

# Extra Python Assignment

After completing the assignments in the Jupyter notebooks, it is highly recommended to read and complete the exercises in the book [Think Python 2nd Edition](http://greenteapress.com/wp/think-python-2e/). The book is free to download and covers all the material in the notebooks plus quite a bit more. You can find many of the solutions in [this github repository](https://github.com/AllenDowney/ThinkPython2/tree/master/code).

## Resources

More Python resources are available in the [Resources.md][20] file

[1]: https://www.anaconda.com/download
[2]: images/pythonterminal.png
[3]: https://medium.com/@GalarnykMichael/install-python-on-windows-anaconda-c63c7c3d1444
[4]: images/which_python.png
[5]: images/path_mac.png
[6]: https://stackoverflow.com/questions/9546324/adding-directory-to-path-environment-variable-in-windows
[7]: https://www.computerhope.com/issues/ch000549.htm
[8]: http://jupyter.readthedocs.io/en/latest/architecture/how_jupyter_ipython_work.html
[9]: images/jupyter_internal.png
[10]: images/windows_anaconda_check.png
[11]: http://jupyterlab.readthedocs.io/en/stable/
[20]: https://github.com/tdpetrou/precourse-assignment/blob/master/resources.md
