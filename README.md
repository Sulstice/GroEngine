GroEngine: A way to move GROMACSs files across servers and perform Data Cleanup in Bulk
=====================================================================================

![Python](https://img.shields.io/badge/python-3.6-blue.svg)
[![PEP8](https://img.shields.io/badge/code%20style-pep8-orange.svg)](https://www.python.org/dev/peps/pep-0008/)
[![saythanks](https://img.shields.io/badge/GROMACS-5.1-ff69b3.svg)](https://www.computchem.org/)
[![saythanks](https://img.shields.io/badge/Lab-Shen%20Group-ff69b4.svg)](https://www.computchem.org/)

GroEngine was developed as a free tool for me to perform GROMACS operations in bulk and I can walk away from my computer and go eat lunch rather than re-running the same command over the course of tons of simulations.


Announcements
=============

-   Work has began! Dec 21st


Quick Start 
===========

For the **rewrap_trajectories** function to work please make sure you have an *index.ndx* file as well as the topology file. 

```

engine = GroEngine('directories_of_interest', 'trajectory_name', 'user', 'host')
engine.transfer_files('target_directory')
engine.rewrap_trajectories('target_directory')
    
```
    
Installation 
============

GroEngine is going to be distribute via PyPi and as the content store grows we can expand it to other pieces of software
making it accessible to all regardless of what you use. Alternatively, you could have a glance at the source code and copy/paste
it yourself.

This is still going to be determined and give it some time as I work out the kinks with this library.

Structure of Engine
=======================


Genesis
=======

GroEngine was created because I wanted to automate the GROMACS pipeline using python.

- Lead Developer [Suliman Sharif](http://sulstice.github.io/)


* * * * *

External links
==============


