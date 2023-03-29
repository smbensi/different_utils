

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


