# Python `os` Module Cheat Sheet

The `os` module provides a way to interact with the operating system.

```python
import os
```

---

# Current Working Directory

## Get the current working directory

```python
import os

os.getcwd()
```

**Returns**

```text
C:\Users\Charles\Projects\myproject
```

---

## Change the current working directory

```python
os.chdir("C:\\Projects")
```

---

# Directory Operations

## Create a directory

```python
os.mkdir("images")
```

Creates one directory.

---

## Create nested directories

```python
os.makedirs("media/images/profile")
```

Creates every missing folder.

---

## Remove an empty directory

```python
os.rmdir("images")
```

---

## Remove nested empty directories

```python
os.removedirs("media/images/profile")
```

---

## Rename a directory or file

```python
os.rename("old.txt", "new.txt")
```

---

# File Operations

## Delete a file

```python
os.remove("example.txt")
```

---

## Check if a file exists

```python
os.path.exists("example.txt")
```

Returns

```python
True
```

or

```python
False
```

---

## Get file size

```python
os.path.getsize("example.txt")
```

Returns bytes.

---

## Get last modified time

```python
os.path.getmtime("example.txt")
```

---

## Get creation time

```python
os.path.getctime("example.txt")
```

---

# Listing Files

## List everything

```python
os.listdir()
```

Example

```python
['manage.py', 'core', 'media']
```

---

## List another folder

```python
os.listdir("media")
```

---

# Walking Through Directories

```python
for root, dirs, files in os.walk("."):
    print(root)
    print(dirs)
    print(files)
```

Useful for

* searching files
* backups
* Django media cleanup

---

# Environment Variables

## Read one variable

```python
os.getenv("SECRET_KEY")
```

---

## Read with default

```python
os.getenv("DEBUG", False)
```

---

## Set environment variable

```python
os.environ["DEBUG"] = "True"
```

---

## Access all environment variables

```python
os.environ
```

---

# Paths

## Join paths

```python
os.path.join("media", "images", "cat.jpg")
```

Output

```text
media/images/cat.jpg
```

Windows users do not need to worry about `\` vs `/`.

---

## Absolute path

```python
os.path.abspath("media")
```

---

## Directory name

```python
os.path.dirname(__file__)
```

Very common in Django.

---

## Base filename

```python
os.path.basename("media/image.jpg")
```

Returns

```text
image.jpg
```

---

## Split filename

```python
os.path.split("media/image.jpg")
```

Returns

```python
("media", "image.jpg")
```

---

## Split extension

```python
os.path.splitext("image.jpg")
```

Returns

```python
("image", ".jpg")
```

---

# Path Checks

## Is file?

```python
os.path.isfile("image.jpg")
```

---

## Is directory?

```python
os.path.isdir("media")
```

---

## Is absolute path?

```python
os.path.isabs("media")
```

---

# User Information

## Current user

```python
os.getlogin()
```

---

## User home directory

```python
os.path.expanduser("~")
```

---

# Process Information

## Current process ID

```python
os.getpid()
```

---

## Parent process ID

```python
os.getppid()
```

---

# Execute System Commands

```python
os.system("dir")
```

Linux

```python
os.system("ls")
```

---

# CPU Information

```python
os.cpu_count()
```

Returns

```python
8
```

---

# Random Bytes

```python
os.urandom(16)
```

Useful for

* encryption
* tokens
* security

---

# Common Django Usage

## settings.py

```python
import os

BASE_DIR = os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))
)
```

---

## Upload Path

```python
image_path = os.path.join(
    "media",
    "profile",
    filename
)
```

---

## Environment Variables

```python
SECRET_KEY = os.getenv("SECRET_KEY")

DEBUG = os.getenv("DEBUG")
```

---

# Frequently Used Methods

```python
os.getcwd()
os.chdir()
os.listdir()
os.walk()
os.mkdir()
os.makedirs()
os.rmdir()
os.removedirs()
os.rename()
os.remove()
os.getenv()
os.environ
os.system()
os.cpu_count()
os.getlogin()
os.getpid()
os.getppid()
os.urandom()
```

---

# Frequently Used `os.path` Methods

```python
os.path.exists()
os.path.join()
os.path.abspath()
os.path.dirname()
os.path.basename()
os.path.split()
os.path.splitext()
os.path.isfile()
os.path.isdir()
os.path.isabs()
os.path.getsize()
os.path.getctime()
os.path.getmtime()
os.path.expanduser()
```

---

# Best Practice

For **new Python projects**, prefer using `pathlib` for path manipulation because it's more modern and easier to read.

```python
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

image = BASE_DIR / "media" / "profile" / "cat.jpg"
```

`pathlib` and `os` work well together, and you'll see both used in real Django projects.
