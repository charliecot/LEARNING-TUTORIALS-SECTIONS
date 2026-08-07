# Python Magic Methods (Dunder Methods) Cheat Sheet

> **Magic methods** (also called **dunder methods**) are special methods whose names begin and end with double underscores (`__`). Python automatically calls them to provide built-in behavior such as printing, comparing, indexing, iterating, and arithmetic.

---

# 1. `__init__()`

### Purpose

Called automatically when a new object is created.

### Syntax

```python
class Person:
    def __init__(self, name):
        self.name = name
```

### Example

```python
person = Person("John")
```

Python automatically does:

```python
Person.__init__(person, "John")
```

### Common Use

* Initialize attributes
* Set default values

---

# 2. `__str__()`

### Purpose

Controls what is displayed when you print an object.

### Example

```python
class Person:
    def __str__(self):
        return self.name
```

```python
print(person)
```

Output

```
John
```

### Django Example

```python
class Course(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
```

---

# 3. `__repr__()`

### Purpose

Official string representation used for debugging.

```python
class Person:
    def __repr__(self):
        return f"Person(name='{self.name}')"
```

Output

```python
Person(name='John')
```

---

# 4. `__len__()`

### Purpose

Makes `len(object)` work.

```python
class Team:

    def __len__(self):
        return len(self.members)
```

```python
len(team)
```

---

# 5. `__iter__()`

### Purpose

Allows an object to be looped over.

```python
class Numbers:

    def __iter__(self):
        return iter([1,2,3])
```

```python
for number in Numbers():
    print(number)
```

---

# 6. `__next__()`

### Purpose

Returns the next item in an iterator.

Usually used together with `__iter__()`.

---

# 7. `__getitem__()`

### Purpose

Allows indexing using `[]`.

```python
class Letters:

    def __getitem__(self,index):
        return ["A","B","C"][index]
```

```python
letters[1]
```

Output

```
B
```

---

# 8. `__setitem__()`

### Purpose

Allows assignment using `[]`.

```python
obj[0] = "Python"
```

---

# 9. `__delitem__()`

### Purpose

Allows deletion using `del`.

```python
del obj[0]
```

---

# 10. `__contains__()`

### Purpose

Makes `in` work.

```python
class Team:

    def __contains__(self,item):
        return item in self.members
```

```python
"John" in team
```

---

# 11. `__call__()`

### Purpose

Makes an object callable like a function.

```python
class Greeting:

    def __call__(self):
        print("Hello")
```

```python
g = Greeting()

g()
```

Output

```
Hello
```

---

# 12. `__eq__()`

### Purpose

Defines equality (`==`).

```python
class Student:

    def __eq__(self,other):
        return self.id == other.id
```

---

# 13. `__ne__()`

### Purpose

Defines inequality (`!=`).

---

# 14. `__lt__()`

### Purpose

Defines less than (`<`).

---

# 15. `__le__()`

### Purpose

Defines less than or equal (`<=`).

---

# 16. `__gt__()`

### Purpose

Defines greater than (`>`).

---

# 17. `__ge__()`

### Purpose

Defines greater than or equal (`>=`).

---

# 18. `__add__()`

### Purpose

Defines `+`.

```python
class Money:

    def __add__(self,other):
        return self.amount + other.amount
```

---

# 19. `__sub__()`

### Purpose

Defines subtraction (`-`).

---

# 20. `__mul__()`

### Purpose

Defines multiplication (`*`).

---

# 21. `__truediv__()`

### Purpose

Defines division (`/`).

---

# 22. `__floordiv__()`

### Purpose

Defines floor division (`//`).

---

# 23. `__mod__()`

### Purpose

Defines modulus (`%`).

---

# 24. `__pow__()`

### Purpose

Defines exponentiation (`**`).

---

# 25. `__bool__()`

### Purpose

Controls the truth value of an object.

```python
class Student:

    def __bool__(self):
        return self.grade >= 50
```

---

# 26. `__hash__()`

### Purpose

Allows an object to be used as a dictionary key or inside a set.

---

# 27. `__enter__()`

### Purpose

Executed when entering a `with` block.

---

# 28. `__exit__()`

### Purpose

Executed when leaving a `with` block.

```python
with open("file.txt") as file:
    pass
```

Python automatically calls:

```python
__enter__()
__exit__()
```

---

# 29. `__new__()`

### Purpose

Creates a new instance before `__init__()` runs.

Rarely overridden.

---

# 30. `__del__()`

### Purpose

Runs when an object is destroyed.

Rarely used.

---

# Django Model Methods (Not Magic Methods)

These are ordinary methods provided by Django that are commonly overridden.

## `save()`

Runs whenever an object is saved.

```python
def save(self,*args,**kwargs):
    super().save(*args,**kwargs)
```

Common uses

* Create slug
* Resize images
* Modify data before saving

---

## `delete()`

Runs before deleting an object.

```python
def delete(self,*args,**kwargs):
    super().delete(*args,**kwargs)
```

---

## `clean()`

Used for model validation.

```python
def clean(self):
    if self.price < 0:
        raise ValidationError("Price cannot be negative")
```

---

## `clean_fields()`

Validates every field.

Usually called internally.

---

## `validate_unique()`

Checks uniqueness constraints.

---

## `full_clean()`

Runs

* `clean_fields()`
* `clean()`
* `validate_unique()`

---

## `get_absolute_url()`

Returns the URL of an object.

```python
def get_absolute_url(self):
    return reverse("course_detail",args=[self.pk])
```

---

# Frequently Used Django Admin Methods

```python
get_queryset()
get_form()
save_model()
delete_model()
save_related()
formfield_for_foreignkey()
formfield_for_manytomany()
has_add_permission()
has_change_permission()
has_delete_permission()
has_view_permission()
```

---

# Frequently Used DRF Methods

```python
create()
update()
validate()
validate_<field>()
to_representation()
get_queryset()
get_serializer_class()
perform_create()
perform_update()
perform_destroy()
```

---

# Frequently Used Form Methods

```python
clean()
clean_<field>()
save()
is_valid()
```

---

# Frequently Used Python Class Methods

```python
@classmethod
def from_string(cls):
```

```python
@staticmethod
def add(a,b):
```

```python
@property
def full_name(self):
```

```python
@property
@setter
```

---

# Summary

## Python Magic Methods

```
__init__()
__str__()
__repr__()
__len__()
__iter__()
__next__()
__getitem__()
__setitem__()
__delitem__()
__contains__()
__call__()
__eq__()
__ne__()
__lt__()
__le__()
__gt__()
__ge__()
__add__()
__sub__()
__mul__()
__truediv__()
__floordiv__()
__mod__()
__pow__()
__bool__()
__hash__()
__enter__()
__exit__()
__new__()
__del__()
```

---

## Django Model Methods

```
save()
delete()
clean()
clean_fields()
validate_unique()
full_clean()
get_absolute_url()
```

---

## Django Admin Methods

```
get_queryset()
get_form()
save_model()
delete_model()
save_related()
formfield_for_foreignkey()
formfield_for_manytomany()
has_add_permission()
has_change_permission()
has_delete_permission()
has_view_permission()
```

---

## Django REST Framework

```
create()
update()
validate()
validate_<field>()
to_representation()
get_queryset()
get_serializer_class()
perform_create()
perform_update()
perform_destroy()
```

---

## Forms

```
clean()
clean_<field>()
save()
is_valid()
```

This covers the most commonly encountered magic methods in Python and the key override methods you'll use regularly in Django, Django Admin, Forms, and Django REST Framework.
