# Virtual Environments and Packages

Original Documentation [Virtual Environments and Packages](https://docs.python.org/3/tutorial/venv.html)!

### 12.1. Introduction

- It may not be possible for one Python installation to meet the requirements of every application. If application A needs version 1.0 of a particular module but application B needs version 2.0, then the requirements are in conflict and installing either version 1.0 or 2.0 will leave one application unable to run

> The solution for this problem is to create a virtual environment, a self-contained directory tree that contains a Python installation for a particular version of Python, plus a number of additional packages.

### 12.2. Creating Virtual Environments

- The module used to create and manage virtual environments is called venv.

### To create a virtual environment, decide upon a directory where you want to place it, and run the venv module as a script with the directory path:

```
python -m venv tutorial-env
```

- This will create the **tutorial-env** directory if it doesn’t exist, and also create directories inside it containing a copy of the Python interpreter and various supporting files.

- A common directory location for a virtual environment is **.venv**

### On Windows, run:

```
tutorial-env\Scripts\activate
```

### On Unix or MacOS, run:

```
source tutorial-env/bin/activate
```

### Activating the virtual environment will change your shell’s prompt to show what virtual environment you’re using, and modify the environment so that running python will get you that particular version and installation of Python. For example:

```
source ~/envs/tutorial-env/bin/activate
(tutorial-env) $ python
```

- To deactivate a virtual environment, type into the terminal:

```
deactivate
$ python
```

### 12.3. Managing Packages with pip

- You can install, upgrade, and remove packages using a program called pip. By default pip will install packages from [ PyPi ](https://pypi.org/)!. You can browse the Python Package Index by going to it in your web browser.
- pip has a number of subcommands: “install”, “uninstall”, “freeze”, etc. (Consult the Installing Python modules guide for complete documentation for pip.)

- You can install the latest version of a package by specifying a package’s name:

```
(tutorial-env) $ python -m pip install novas
Collecting novas
  Downloading novas-3.1.1.3.tar.gz (136kB)
Installing collected packages: novas
  Running setup.py install for novas
Successfully installed novas-3.1.1.3
```

- If you re-run this command, pip will notice that the requested version is already installed and do nothing. You can supply a different version number to get that version, or you can run python -m pip install --upgrade to upgrade the package to the latest version:

```
(tutorial-env) $ python -m pip install --upgrade requests
Collecting requests
Installing collected packages: requests
  Found existing installation: requests 2.6.0
    Uninstalling requests-2.6.0:
      Successfully uninstalled requests-2.6.0
Successfully installed requests-2.7.0
```

- python -m pip uninstall followed by one or more package names will remove the packages from the virtual environment.

- python -m pip show will display information about a particular package:

```
(tutorial-env) $ python -m pip show requests
---
Metadata-Version: 2.0
Name: requests
Version: 2.7.0
Summary: Python HTTP for Humans.
Home-page: http://python-requests.org
Author: Kenneth Reitz
Author-email: me@kennethreitz.com
License: Apache 2.0
Location: /Users/akuchling/envs/tutorial-env/lib/python3.4/site-packages
Requires:
```

- python -m pip list will display all of the packages installed in the virtual environment

```
(tutorial-env) $ python -m pip list
novas (3.1.1.3)
numpy (1.9.2)
pip (7.0.3)
requests (2.7.0)
setuptools (16.0)
```

- python -m pip freeze will produce a similar list of the installed packages, but the output uses the format that python -m pip install expects. A common convention is to put this list in a requirements.txt file:

```
(tutorial-env) $ python -m pip freeze > requirements.txt
(tutorial-env) $ cat requirements.txt
novas==3.1.1.3
numpy==1.9.2
requests==2.7.0
```
