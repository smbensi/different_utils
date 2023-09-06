

# 1.PATHLIB

[Arjan code](https://www.youtube.com/watch?v=UcKkmwaRbsQ)

- path are objects 
- > from pathlib import Path
- > current directory : `Path.cwd()` \
      home directory  `Path.home()` \
      if the path exists : `path.exists()` \
      create a path:  `Path("/usr/bin/local")` or `Path("/usr") / "bin" / "local"` \
      read a file : `path.read_text()` \
      get the full path : `path.resolve()` \
      print the parent: `path.parent` (default relative) if you want the parent you need the path as full path : `path.resolve()` \
      Name of the local folder: `path.name` \
      Stem of the file: `path.stem`
      suffix : `path.suffix`
      file or folder? : `path.is_dir()`  or `path.is_file()` \
      new_file : `Path.cwd() / "new_file.txt"`  ; `new_file.touch()` ; `new_file.write_text("Hello")` \
      new directory : `new_dir.mkdir()`  \
      Change to new directory : `chdir(new_dir)`


# OOP
- [general article on RealPython](https://realpython.com/python-classes/#toc) You can learn about different topics related to OOP in Python like:\
      - **@property**: to make an attribute like method based  and also protect the attribute changing\
      - attributes are in a dictionary  or can save memory using __slots__ (and avoiud attributes adding)\
      - different types of methods or attributes: instance (self), class (cls and @classmethod), static (@staticmethod not using attributes of the class)\
      - special types of classes like **dataclasses** (for dataholder) and **enum** (for constants) \
      - inheritance/multi-inheritance using super() and its alternatives like **composition** (has-a) and **delegation** (can-do) \
      - **ABC classes** to create a uniform API , contains only @abstractmethod \
      - **polymorphism**: the childs class contain the same interface to not be dependent of the type \

## Interface

- [Implementing interface in Python](https://realpython.com/python-interface/#toc) : We learned about building interface : \
      - formal and informal interface\
      - **Informal**: You can use subclass but if you don't implement one of the abstract method there is no error and the MRO continues to say that you are a subclass\
      - You can use **metaclass** that defines 2 dunder methods *__isinstancecheck__(cls,instance)* and *__subclasscheck__(cls,subclass)* that checks that there are the attributes of the parentclass and when creating the abstract class you need to inherit from the metaclass in that way:\
      class InformalParserInterface(metaclass=ParserMeta)\
      if now you create a new class that have the methods have the base abstract class define in **hasattr** of the Metaclass so it's called a **virtual base class**
      \
      \
      -**Formal**: to create formal interface you can use the **abc** built-in package and in the metaclass you define the abstract class in that way:\
      > class FormalParserInterface(metaclass=abc.ABCMeta)\
      and inside you define a function *__subclasshook__(cls,subclass)* with the decorator @classmethod\
      - You can use *register()* to define that the class is a subclass but it's a little bit tricky\
      - lastly, if you want to enforce the subclass to define a method you can define the abstract method with the decorator **@abc.abstractmethod** and in the subclass you get an error if one of these methods is not implemented

## JSON 
- [REAL PYTHON](https://realpython.com/python-json/)
- nice way to encode and decode not basic types
- run a python script interactively with 
>python -i script.py
