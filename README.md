Introduction to Data Science
====
Welcome to our Introduction to Data Science. I've broken the material up into 7 modules that are inteded to be executed sequentially. I expect that people will come to this material with different backgrounds and different levels of experience, so feel free to skip any of the modules for the material that you're already comfortable with.

There's a table of contents at the bottom of this notebook for those who want to skip ahead and browse what's available here.

Python
-----
Throughout this course we'll be putting together a "data science toolbox", a set of resouces that you'll use to collect, clean, store, explore, visualize, and analyze data. There are several good platforms for doing these tasks, and in this tutorial we'll be using the Python programming language for almost all of them.

Python's major advantages are that

1. it's free
2. it's easy to learn and use
3. there's a Python library that solves almost every problem we'll come up against

Python comes with a core set of libraries, but a number of the data tools we'll need are not included. You could download the libraries for these tools one-by-one, but there are a number of dependencies that make this process a little bit tedious. Instead, I recommend downloading the [Anaconda distribution of Python provided by Continuum Analytics](https://docs.continuum.io/anaconda/install). It comes with almost all of the libraries you'll ever need *and* it takes care of all of the dependency issues that would otherwise make you hate your life.

There aren't many pre-requisites for this course, but basic familiarity of Python is one of them. There are two online tutorials that I recommend:

1. https://docs.python.org/2/tutorial/index.html
2. http://www.codecademy.com/en/tracks/python

The first comes directly from python, and, if you can get through it, is probably the best option. If option one feels a little over your head, the second tutorial from code academy is a little bit easier to get started with. It even allows you to complete all of the exercises right in your browser.

If you have other recommendations for python tutorials, please let me know!

The Command Line
--
One of the great features of python is that it comes with a command line tool that allows you to run python code one line at a time and print the results to your screen (this is not the case with languages like C++ or Java). This is one (of the many) features that makes python so easy to learn.

Getting to the command line will be slightly different depending on whether you're operating system is Mac, Windows, or Linux.

On Mac you'll use the Terminal app. On Windows you'll open the Command Prompt program. If you're using Linux, I'll assume you've already skipped this section. Regardless of whether you'r on Mac, Windows, or Linux, I'll be referring to your command line tool as a "terminal".

IPython and Jupyter Notebooks
--
IPython is an alternative command line tool to the one that comes with python. It's part of the Anaconda python distribution, so if you've installed Anaconda you can open an ipython shell just by typing ipython in your terminal window.

The ipython shell has all of the functionality of the regular python shell, plus several handy extras. The two features that you'll probably find most helpful are tab completion and built in object descriptions [http://ipython.org/ipython-doc/stable/interactive/tutorial.html#tab-completion].

Anaconda also comes with an interactive browser-based editor called Jupyter that combines code execution, plots, and text formatting. It's a great tool for both exploring data, sharing your results, and learning how to use new python tools. Jupyter notebooks are essentially running ipython in your browser so all the features available in ipython are also available in jupyter notebooks. All of the modules for this course are written in jupyter notebooks which allows you to execute all of the examples in your browser and explore the results yourself.


Github
--
All of the modules and supporting material for this course are hosted on github here: [https://github.com/adamhajari/Introduction-to-Data-Science]. If you don't already have one, setup a github account, fork this repo [https://help.github.com/articles/fork-a-repo/], and clone your forked copy of the repo to whatever computers you'll be working from.

Table of Contents
---
- [0.Getting Started](https://github.com/adamhajari/Introduction-to-Data-Science/blob/master/0_Getting_Started.ipynb)
- [1.Python Data Tools](https://github.com/adamhajari/Introduction-to-Data-Science/blob/master/1_Python_Data_Tools.ipynb)
- [2.Data Storage](https://github.com/adamhajari/Introduction-to-Data-Science/blob/master/2_Storing_Data_Module.ipynb)
- [3.Data Collection](https://github.com/adamhajari/Introduction-to-Data-Science/blob/master/3_Data_Collection.ipynb)
- [4.Exploring Data](https://github.com/adamhajari/Introduction-to-Data-Science/blob/master/4_Exploring_Data.ipynb)
- [5.Data Analysis](https://github.com/adamhajari/Introduction-to-Data-Science/blob/master/5_Data_Analysis.ipynb)
- [6.Data Cleaning](https://github.com/adamhajari/Introduction-to-Data-Science/blob/master/6_Data_Cleaning.ipynb)
- [7.Web Apps with Spyre](https://github.com/adamhajari/Introduction-to-Data-Science/blob/master/7_Web_Apps.ipynb)
