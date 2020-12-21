GroMass: A way to move GROMACSs files across servers and perform Data Cleanup in Bulk
=====================================================================================

![Python](https://img.shields.io/badge/python-3.6-blue.svg)
[![PEP8](https://img.shields.io/badge/code%20style-pep8-orange.svg)](https://www.python.org/dev/peps/pep-0008/)
[![saythanks](https://img.shields.io/badge/GROMACS-5.1-ff69b3.svg)](https://www.computchem.org/)
[![saythanks](https://img.shields.io/badge/Lab-Shen%20Group-ff69b4.svg)](https://www.computchem.org/)

GroMass was started out of a need to not only transport trajectory files across servers for molecular simulations but also
perform routine steps such as `rewrapping` a trajectory on a large collection of files.


Quick Start
===========

First you will need authentication to the cluster or server running the Molecular Dynamics simulation for GROMACS.

First is simple 

1. Register your RSA key with the dedicated server so you don't have to be password prompted when SSH'ing into the server

`GroLogs` class takes 4 arguments

- **target_directory** - target directory where all your log files for this particular experiment will be
- **log_file_name** - the name of the log file. Traditionally, I have everything called as `md_3.log`
- **username** - the username registered on the cluster or particular machine
- **hostname** - the hostname or ip address of the target server that we want to extrapolate information.


Announcements
=============

-   Work has began! Dec 21st


Installation 
============

GroMass is going to be distribute via PyPi and as the content store grows we can expand it to other pieces of software
making it accessible to all regardless of what you use. Alternatively, you could have a glance at the source code and copy/paste
it yourself.

To install the reader 

```

python -m pip install grologs

```

Structure of GroMass
=======================

Currently, the main subpackages are:

- **gromass**: logreader main class. 


Genesis
=======

GroMass was created because I wanted to automate the GROMACS pipeline using python.

- Lead Developer [Suliman Sharif](http://sulstice.github.io/)


* * * * *

External links
==============


