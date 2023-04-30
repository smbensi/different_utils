

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