#!/usr/bin/env python
# coding: utf-8

# # Getting ready with `pytket`
# 

# [Pytket](https://cqcl.github.io/tket/pytket/api/index.html) is a Python toolkit for quantum programming developed by Cambridge Quantum Computing, an extension of their larger TKET toolchain. TKET encompasses the entire toolset of high-performance tools for quantum programming, primarily written in C++. Hence, `pytket` is a Python interface to TKET, a platform-agnostic quantum software development kit (QSDK).
# 
# ## Installation
# 
# First, make sure that a recent version of
# [Python](https://www.python.org/downloads/) is installed on your machine.
# You can check this in a terminal:

# ```python --version```

# I would recommend using either `Python 3.9` or `Python 3.10`.

# ### Jupyter Notebook Installation
# 
# In case you don't have access to Python or a Jupyter Notebook yet, I suggest you install Anaconda.
# 
# #### Step 0: The browser
# Step “zero” consists in installing a modern standard-compliant browser. Either Mozilla Firefox or Google 
# Chrome will work well. Try to avoid MS Explorer.
# 
# #### Step 1: Installation
# The easiest way to install the Jupyter Notebook App is installing a scientific python distribution which 
# also includes scientific python packages. The most common distribution is called Anaconda:<br>
# https://www.anaconda.com/products/distribution 
# 
# Download Anaconda Distribution (a few 100MB), Python 3, 64 bits.<br>
# Install it using the default settings for a single user.
# 
# #### Step 2: open Jupyter Notebook
# Open the application Anaconda. You should see the Anaconda Navigator panel open. Most of this stuff we do 
# not need.  Click on the Jupyter Notebook panel. What will open is a web browser, which is what Jupyter 
# displays on. You should see a file directory displayed. 
# 
# To create a new notebook, click on “New” and select “Python 3”.

# ## Create a virtual environment
# 
# It is usually best to create Python projects in independent environments to avoid potentially conflicting dependencies between different packages. For this hackathon, choose the virtual environment manager you prefer.
# All Python code that follows will be the same in any virtual environment.
# 
# 
# #### When using Anaconda Navigator
# 
# Open the “Anaconda Navigator” and go to “Environments”. Then click on the “create” button on the bottom 
# to make a new TKET environment by typing, for example, the name “tket” . Select the python version 3.9 or 3.10, then click create. 
# 
# Then you can activate the “tket“ environment by slecting "tket" in the "Environments" tab and then clicking on "Home". You should see a Jupyter Notebook pannel. Click on "Install". When the installation is completed, you then click the "Launch" button. You can select your working folder and click on "NEW" to open a new and select “Python 3” to open a working Jupyter notebook.
# 

# ## Install `pytket` and `qiskit`
# 
# Once you opened a new Jupyter notebook, the TKET tool we will use in this hackathon is accessible through the Python package `pytket`. You will thus be able to access all TKET features directly from `pytket` by installing

# `pip install pytket`

# I would recommend you install `pytket-qiskit` at the same time. `pytket-qiskit` integrates `qiskit` into `pytket`,
# an IBM tool that, among other things, provides access to their quantum computers and numerous simulators. Install `qiskit` through

# `pip install pytket-qiskit`

# Now that installation is done, we are ready to implement the first circuit using `pytket`.
