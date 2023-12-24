
# General

## On-premises software

abreviated to **on-prem** is installed and runs on computers on the premises of the person or organization using the software, rather than a remote facility such as server farm or cloud.
off-premises software is commonly called "software as a service"(SaaS) or "cloud computing"

## Happy path

In the context of software or onformation modeling, a **happy path** is a default scenario featuring no exceptional or error conditions.
Happy path testing can show that a system meets its functional requirements but it doesn't guarantee a graceful handling or error conditions or aid in finding hidden bugs.

# Design Pattern

## Singleton


# Linux

## PATH

it's an environment variable specifying a set of directories where executable programs are located.
On Unix-like OS the `$PATH` variable is specified as a list of one or more directory names separated by a colon `:` char.
The `/bin`, `/usr/bin`, and `/usr/local/bin` are typically included in most users' `$PATH`
When a command name is specified by a user on an exec call is made from a program, the system searches through `$PATH` examining each directory from left to right in the list, looking for a filename that matches the command name. Once found, the program is executed as a child process of the command shell or program that issued the command

# VS code

## interpreter

if you want to add an interpreter you can run in python `sys.executable` and paste the response
in select interpreter if its' not in the list


# Python

## Virtual environment

- Create a new venv

> python3 -m venv venv --prompt <name_for_the_prompt>

- Activate it

> source venv/bin/activate

## src layout vs flat layout

The "flat layout" refers to organising a project's files in a folder or repository, such that the various configuration files and import packages are all in the top-level directory
.
├── README.md
├── noxfile.py
├── pyproject.toml
├── setup.py
├── awesome_package/
│   ├── __init__.py
│   └── module.py
└── tools/
    ├── generate_awesomeness.py
    └── decrease_world_suck.py

The "src layout" deviates from the flat layout by moving the code that is intended to be importable. (i.e `import awesome_package`, also known as import packages) into a subdirectory. This subdirectory is typically named `src/` hence "src layout":

.
├── README.md
├── noxfile.py
├── pyproject.toml
├── setup.py
├── src/
│    └── awesome_package/
│       ├── __init__.py
│       └── module.py
└── tools/
    ├── generate_awesomeness.py
    └── decrease_world_suck.py


Here's a breakdown of the important behaviour differences between the src layout and the flat layout:

* The src layout requires installation of the project to be able to run its code,  and the flat layout does not.
This means that the src layout involves an additional step in the dev workflow of a project (typically, an editable installation)

* The src layout helps prevent accidental usage of the in-development copy of the code.


## Development mode ("Editable Installs)

- Tofacilitate exploration and experimanetation, `setuptools` allows users to instruc the Python interpreter and its import machinery to load the code under development directly form the project folder without having to copy the files to a different location in the disk. This means that changes in the Python source code can immediately take place without requiring a new installation

> pip instll --editable .