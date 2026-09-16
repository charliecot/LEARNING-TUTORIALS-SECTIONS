# Django ORM Field Lookups — Complete Reference

## 1. What is a Django Lookup?

A Django lookup tells Django **how to compare a model field with a value**.

Basic structure:

```python
Model.objects.filter(field__lookup=value)
```

Example:

```python
Product.objects.filter(price__gt=100)
```

Read it as:

```text
Product
   ↓
filter
   ↓
price
   ↓
greater than
   ↓
100
```

So:

```python
price__gt=100
```

means:

> Give me products whose price is greater than 100.

---

# 2. The General Syntax

The general syntax is:

```python
field__lookup=value
```

There are **two underscores**:

```text
field
  ↓
__
  ↓
lookup
```

Example:

```python
name__icontains="shoe"
```

Here:

```text
name       → model field
__         → separates field and lookup
icontains  → lookup
"shoe"     → value
```

---

# 3. Important: `__eq` Does NOT Exist as a Normal Django Lookup

If you're coming from another ORM, you may expect:

```python
Product.objects.filter(price__eq=100)
```

Django normally does **not** use `__eq`.

Instead, equality is the default:

```python
Product.objects.filter(price=100)
```

or explicitly:

```python
Product.objects.filter(price__exact=100)
```

These mean the same thing:

```python
price=100
```

and:

```python
price__exact=100
```

So remember:

```text
Django equality
      ↓
field=value

or

field__exact=value
```

---

# 4. `exact`

Exact match.

```python
Product.objects.filter(name__exact="Shoes")
```

Equivalent to:

```python
Product.objects.filter(name="Shoes")
```

Example:

```python
User.objects.filter(username__exact="charles")
```

Means:

> username must exactly match `"charles"`.

---

# 5. `iexact`

Case-insensitive exact match.

```python
Product.objects.filter(name__iexact="shoes")
```

This can match:

```text
Shoes
SHOES
shoes
sHoEs
```

depending on database collation/database behavior.

Difference:

```python
name__exact="shoes"
```

versus:

```python
name__iexact="shoes"
```

---

# 6. `contains`

Checks whether a field contains a string.

```python
Product.objects.filter(name__contains="shoe")
```

Conceptually:

```text
"Running shoe"
       ↑
     shoe
```

Case-sensitive.

---

# 7. `icontains`

Case-insensitive version of `contains`.

```python
Product.objects.filter(name__icontains="shoe")
```

Can match:

```text
Shoe
SHOE
shoe
Running Shoe
running shoes
```

This is one of the **most commonly used lookups**.

---

# 8. `startswith`

Checks whether text starts with a value.

```python
Product.objects.filter(name__startswith="Nike")
```

Matches:

```text
Nike Shoes
Nike Shirt
Nike Air Max
```

Doesn't match:

```text
New Nike Shoes
Adidas Nike
```

---

# 9. `istartswith`

Case-insensitive `startswith`.

```python
Product.objects.filter(
    name__istartswith="nike"
)
```

Matches:

```text
Nike Shoes
NIKE Shoes
nike shoes
```

---

# 10. `endswith`

Checks whether text ends with a value.

```python
Product.objects.filter(name__endswith="shoes")
```

Matches:

```text
Running shoes
Tennis shoes
Nike shoes
```

---

# 11. `iendswith`

Case-insensitive `endswith`.

```python
Product.objects.filter(
    name__iendswith="SHOES"
)
```

---

# 12. `gt`

Greater than.

```python
Product.objects.filter(price__gt=100)
```

Means:

```text
price > 100
```

Example:

```python
Product.objects.filter(stock__gt=0)
```

Means:

> Products with stock greater than zero.

---

# 13. `gte`

Greater than or equal to.

```python
Product.objects.filter(price__gte=100)
```

Means:

```text
price >= 100
```

Includes 100.

---

# 14. `lt`

Less than.

```python
Product.objects.filter(price__lt=100)
```

Means:

```text
price < 100
```

---

# 15. `lte`

Less than or equal to.

```python
Product.objects.filter(price__lte=100)
```

Means:

```text
price <= 100
```

---

# 16. Comparison Lookups Summary

```text
__gt
Greater than

__gte
Greater than or equal

__lt
Less than

__lte
Less than or equal
```

Example:

```python
Product.objects.filter(price__gt=50)
Product.objects.filter(price__gte=50)
Product.objects.filter(price__lt=50)
Product.objects.filter(price__lte=50)
```

Think:

```text
gt   >
gte  >=
lt   <
lte  <=
```

---

# 17. `in`

Checks whether a field is contained in a list of values.

```python
Product.objects.filter(
    category__in=["Shoes", "Shirts", "Bags"]
)
```

Conceptually:

```sql
WHERE category IN (...)
```

Another example:

```python
Product.objects.filter(
    id__in=[1, 3, 7, 10]
)
```

---

# 18. `range`

Checks whether a value falls within a range.

```python
Product.objects.filter(
    price__range=(50, 100)
)
```

Conceptually:

```text
50 <= price <= 100
```

For dates:

```python
Order.objects.filter(
    created_at__range=(start_date, end_date)
)
```

---

# 19. `isnull`

Checks whether a database field is `NULL`.

```python
Product.objects.filter(
    description__isnull=True
)
```

Means:

> Find products whose description is NULL.

Opposite:

```python
Product.objects.filter(
    description__isnull=False
)
```

Means:

> Find products whose description is not NULL.

Important:

```text
isnull=True
       ↓
NULL

isnull=False
       ↓
NOT NULL
```

---

# 20. Date/Time Lookups

Django provides special lookups for dates and times.

Suppose:

```python
created_at = models.DateTimeField()
```

You can do:

```python
Order.objects.filter(
    created_at__year=2026
)
```

---

# 21. `year`

```python
Order.objects.filter(
    created_at__year=2026
)
```

Finds records from the year 2026.

---

# 22. `month`

```python
Order.objects.filter(
    created_at__month=9
)
```

Finds records from September.

---

# 23. `day`

```python
Order.objects.filter(
    created_at__day=15
)
```

Finds records occurring on day 15 of the month.

---

# 24. `week`

```python
Order.objects.filter(
    created_at__week=37
)
```

Filters by ISO week number.

---

# 25. `week_day`

Django's `week_day` lookup uses:

```text
1 = Sunday
2 = Monday
3 = Tuesday
4 = Wednesday
5 = Thursday
6 = Friday
7 = Saturday
```

Example:

```python
Order.objects.filter(
    created_at__week_day=2
)
```

Finds Monday records.

---

# 26. `iso_week_day`

ISO weekday numbering is:

```text
1 = Monday
2 = Tuesday
3 = Wednesday
4 = Thursday
5 = Friday
6 = Saturday
7 = Sunday
```

Example:

```python
Order.objects.filter(
    created_at__iso_week_day=1
)
```

Finds Mondays.

---

# 27. `quarter`

```python
Order.objects.filter(
    created_at__quarter=3
)
```

Means:

> Records created during the third quarter.

Quarters:

```text
Q1 = January - March
Q2 = April - June
Q3 = July - September
Q4 = October - December
```

---

# 28. `time`

Filters the time portion of a `DateTimeField`.

```python
Order.objects.filter(
    created_at__time__gte="09:00"
)
```

---

# 29. `date`

Filters the date portion of a `DateTimeField`.

```python
Order.objects.filter(
    created_at__date="2026-09-15"
)
```

---

# 30. Combining Date Lookups

You can combine transformations and lookups.

Example:

```python
Order.objects.filter(
    created_at__year=2026,
    created_at__month=9
)
```

Meaning:

> Orders from September 2026.

---

# 31. Related Model Lookups

This is extremely important.

Suppose:

```python
class Category(models.Model):
    name = models.CharField(max_length=100)


class Product(models.Model):
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE
    )
    name = models.CharField(max_length=200)
```

You can filter using the related model:

```python
Product.objects.filter(
    category__name="Shoes"
)
```

Notice:

```text
category
   ↓
__
   ↓
name
```

The first `__` means:

> Follow the relationship.

---

# 32. Related Model + Lookup

You can combine relationship traversal with a lookup.

```python
Product.objects.filter(
    category__name__icontains="shoe"
)
```

Break it down:

```text
category
    ↓
__ 
    ↓
name
    ↓
__
    ↓
icontains
    ↓
"shoe"
```

Meaning:

> Find products whose category name contains "shoe", ignoring case.

---

# 33. ForeignKey ID Filtering

You can filter directly by the ForeignKey ID:

```python
Product.objects.filter(
    category_id=5
)
```

Or:

```python
Product.objects.filter(
    category__id=5
)
```

Both can be useful.

---

# 34. Reverse Relationship Lookups

Suppose:

```python
class Category(models.Model):
    name = models.CharField(max_length=100)


class Product(models.Model):
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name="products"
    )
```

You can go from Category to Product:

```python
Category.objects.filter(
    products__name__icontains="shoe"
)
```

Meaning:

> Find categories that have a product whose name contains "shoe".

---

# 35. Many-to-Many Lookups

Suppose:

```python
class Product(models.Model):
    tags = models.ManyToManyField(Tag)
```

You can do:

```python
Product.objects.filter(
    tags__name="Python"
)
```

Or:

```python
Product.objects.filter(
    tags__name__icontains="python"
)
```

---

# 36. Multiple Filters

You can pass multiple conditions to `filter()`.

```python
Product.objects.filter(
    price__gte=50,
    price__lte=100,
)
```

This means:

```text
price >= 50
AND
price <= 100
```

Equivalent conceptually to:

```sql
WHERE price >= 50
AND price <= 100
```

---

# 37. Chaining `filter()`

You can also chain filters:

```python
Product.objects.filter(
    price__gte=50
).filter(
    price__lte=100
)
```

This also represents an AND relationship.

---

# 38. `exclude()`

`exclude()` removes objects matching the condition.

```python
Product.objects.exclude(
    price__lt=50
)
```

Conceptually:

```text
NOT price < 50
```

Another example:

```python
Product.objects.exclude(
    name__icontains="shoe"
)
```

Means:

> Give me products whose name does not contain "shoe".

---

# 39. `Q` Objects

For more complicated conditions, use:

```python
from django.db.models import Q
```

Example:

```python
Product.objects.filter(
    Q(name__icontains="shoe") |
    Q(name__icontains="shirt")
)
```

The `|` means OR.

So:

```text
name contains shoe
OR
name contains shirt
```

---

# 40. `Q` AND

Use `&` for AND.

```python
Product.objects.filter(
    Q(price__gte=50) &
    Q(stock__gt=0)
)
```

Means:

```text
price >= 50
AND
stock > 0
```

---

# 41. `Q` NOT

Use `~` for NOT.

```python
Product.objects.filter(
    ~Q(name__icontains="shoe")
)
```

Means:

> Name does not contain "shoe".

---

# 42. Combining AND and OR

You can create more advanced queries:

```python
Product.objects.filter(
    Q(category__name="Shoes") |
    Q(category__name="Clothing"),
    price__lte=100
)
```

Conceptually:

```text
(
    category = Shoes
    OR
    category = Clothing
)
AND
price <= 100
```

---

# 43. `filter()` vs `get()`

Lookups work with `get()` too:

```python
Product.objects.get(
    id=5
)
```

or:

```python
Product.objects.get(
    name__iexact="shoes"
)
```

But remember:

`get()` expects **exactly one object**.

If zero objects:

```text
DoesNotExist
```

If multiple objects:

```text
MultipleObjectsReturned
```

---

# 44. `filter()` vs `exclude()` vs `get()`

```text
filter()
   ↓
returns QuerySet
can return 0, 1, or many


exclude()
   ↓
returns QuerySet
removes matching objects


get()
   ↓
returns ONE object
must find exactly one
```

---

# 45. `__in` with a QuerySet

You don't have to provide a Python list.

You can provide another QuerySet.

Example:

```python
Product.objects.filter(
    category__in=Category.objects.filter(
        name__icontains="shoe"
    )
)
```

This is useful for more advanced queries.

---

# 46. Filtering Boolean Fields

Suppose:

```python
is_active = models.BooleanField()
```

Use:

```python
Product.objects.filter(
    is_active=True
)
```

or:

```python
Product.objects.filter(
    is_active=False
)
```

No lookup is necessary.

---

# 47. Filtering Decimal Fields

Suppose:

```python
price = models.DecimalField(
    max_digits=10,
    decimal_places=2
)
```

You can use:

```python
Product.objects.filter(price=100)
```

```python
Product.objects.filter(price__gt=100)
```

```python
Product.objects.filter(price__gte=100)
```

```python
Product.objects.filter(price__lt=100)
```

```python
Product.objects.filter(price__lte=100)
```

```python
Product.objects.filter(price__range=(50, 100))
```

---

# 48. Filtering Integer Fields

Suppose:

```python
stock = models.IntegerField()
```

You can do:

```python
Product.objects.filter(stock=10)

Product.objects.filter(stock__gt=10)

Product.objects.filter(stock__gte=10)

Product.objects.filter(stock__lt=10)

Product.objects.filter(stock__lte=10)

Product.objects.filter(stock__in=[0, 5, 10, 20])
```

---

# 49. Filtering CharField

Suppose:

```python
name = models.CharField(max_length=200)
```

Common lookups:

```python
Product.objects.filter(name="Shoes")

Product.objects.filter(name__exact="Shoes")

Product.objects.filter(name__iexact="shoes")

Product.objects.filter(name__contains="Shoe")

Product.objects.filter(name__icontains="shoe")

Product.objects.filter(name__startswith="Nike")

Product.objects.filter(name__istartswith="nike")

Product.objects.filter(name__endswith="Shoes")

Product.objects.filter(name__iendswith="shoes")

Product.objects.filter(name__in=["Shoes", "Shirt"])
```

---

# 50. Filtering NULL vs Empty String

These are NOT necessarily the same:

```text
NULL
""
```

`NULL` means no database value.

Empty string means:

```python
""
```

For NULL:

```python
Product.objects.filter(
    description__isnull=True
)
```

For empty string:

```python
Product.objects.filter(
    description=""
)
```

---

# 51. Case-Sensitive vs Case-Insensitive

A very important pattern:

```text
exact
iexact

contains
icontains

startswith
istartswith

endswith
iendswith
```

The `i` generally means:

```text
case-insensitive
```

So:

```text
exact       → case-sensitive exact
iexact      → case-insensitive exact

contains    → case-sensitive contains
icontains   → case-insensitive contains

startswith  → case-sensitive starts with
istartswith → case-insensitive starts with

endswith    → case-sensitive ends with
iendswith   → case-insensitive ends with
```

---

# 52. Lookup + Relationship + Field

This is one of the most important Django ORM patterns.

Example:

```python
Product.objects.filter(
    category__name__icontains="shoe"
)
```

Structure:

```text
category
   ↓
relationship
   ↓
__
   ↓
name
   ↓
field
   ↓
__
   ↓
icontains
   ↓
lookup
```

You can also do:

```python
Product.objects.filter(
    category__name__startswith="Sho"
)
```

or:

```python
Product.objects.filter(
    category__name__iexact="shoes"
)
```

---

# 53. Traversing Multiple Relationships

Suppose:

```python
Product
   ↓
Category
   ↓
Department
```

You can write:

```python
Product.objects.filter(
    category__department__name="Clothing"
)
```

You can continue traversing relationships using `__`.

---

# 54. Query Lookup Cheat Sheet

## Equality

```python
field=value
field__exact=value
field__iexact=value
```

## Text

```python
field__contains=value
field__icontains=value

field__startswith=value
field__istartswith=value

field__endswith=value
field__iendswith=value
```

## Comparison

```python
field__gt=value
field__gte=value

field__lt=value
field__lte=value
```

## Lists / ranges

```python
field__in=[...]
field__range=(start, end)
```

## NULL

```python
field__isnull=True
field__isnull=False
```

## Date / time

```python
field__year=value
field__month=value
field__day=value
field__week=value
field__week_day=value
field__iso_week_day=value
field__quarter=value

field__date=value
field__time=value
```

---

# 55. The Most Used Lookups

In real Django projects, you will frequently use:

```python
exact
iexact
contains
icontains
startswith
istartswith
endswith
iendswith

gt
gte
lt
lte

in
range
isnull
```

And for relationships:

```python
category__name
category__name__icontains
user__username
user__email
order__id
```

---

# 56. Practical Product Examples

Suppose:

```python
class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )
    stock = models.IntegerField()
    is_active = models.BooleanField(default=True)
```

### Products costing more than 100

```python
Product.objects.filter(
    price__gt=100
)
```

### Products costing at least 100

```python
Product.objects.filter(
    price__gte=100
)
```

### Products costing between 50 and 100

```python
Product.objects.filter(
    price__range=(50, 100)
)
```

### Products containing "shoe"

```python
Product.objects.filter(
    name__icontains="shoe"
)
```

### Products beginning with "Nike"

```python
Product.objects.filter(
    name__istartswith="nike"
)
```

### Products with no stock

```python
Product.objects.filter(
    stock=0
)
```

### Products that are active

```python
Product.objects.filter(
    is_active=True
)
```

### Products with IDs 1, 5 and 10

```python
Product.objects.filter(
    id__in=[1, 5, 10]
)
```

---

# 57. Combining Everything

You can combine multiple lookups:

```python
Product.objects.filter(
    name__icontains="shoe",
    price__gte=50,
    price__lte=200,
    stock__gt=0,
    is_active=True,
)
```

This means:

```text
name contains "shoe"
AND
price >= 50
AND
price <= 200
AND
stock > 0
AND
is_active = True
```

---

# 58. A Real Search Example

Imagine a product search API receives:

```text
search = "shoe"
min_price = 50
max_price = 200
```

You could build:

```python
products = Product.objects.filter(
    name__icontains=search,
    price__gte=min_price,
    price__lte=max_price,
)
```

This is the foundation of many product-filtering APIs.

---

# 59. Dynamic Lookup

Because the lookup is part of the keyword name, Python allows you to construct it dynamically.

```python
lookup = "icontains"

Product.objects.filter(
    **{f"name__{lookup}": "shoe"}
)
```

The generated expression is effectively:

```python
Product.objects.filter(
    name__icontains="shoe"
)
```

This technique becomes useful when building dynamic filtering systems.

---

# 60. Important Distinction: Lookup vs Transform

Django's ORM can have:

```text
field
  ↓
transform
  ↓
lookup
```

For example:

```python
created_at__date__exact="2026-09-15"
```

Here:

```text
created_at
     ↓
date       ← transform
     ↓
exact      ← lookup
```

And:

```python
created_at__year=2026
```

uses a date transform.

You will encounter this more often when working with dates, annotations, and advanced queries.

---

# 61. `filter()` Does Not Execute Immediately

This is an important Django ORM concept.

When you write:

```python
products = Product.objects.filter(
    price__gt=100
)
```

Django creates a **QuerySet**.

The database query is generally evaluated lazily when the QuerySet is actually used.

For example:

```python
products = Product.objects.filter(price__gt=100)

for product in products:
    print(product)
```

The QuerySet is evaluated when needed.

This is called:

> **QuerySet lazy evaluation.**

---

# 62. Seeing the SQL

You can inspect the SQL Django generated:

```python
queryset = Product.objects.filter(
    price__gt=100
)

print(queryset.query)
```

This is extremely useful when learning ORM lookups.

For example:

```python
Product.objects.filter(
    price__gte=100
)
```

can generate SQL conceptually similar to:

```sql
WHERE price >= 100
```

---

# 63. Lookup → SQL Mental Map

Learn this mapping:

```text
Django                         SQL

field=value                   =
field__exact=value            =

field__gt=value               >
field__gte=value              >=
field__lt=value               <
field__lte=value              <=

field__in=[...]               IN (...)

field__range=(a,b)            BETWEEN ...

field__isnull=True             IS NULL

field__contains=value         LIKE ...
field__icontains=value        case-insensitive LIKE ...
field__startswith=value       LIKE 'value%'
field__endswith=value         LIKE '%value'
```

The exact SQL can vary by database backend.

---

# 64. `__` Has Two Major Jobs

The double underscore is extremely important.

## Job 1 — Field lookup

```python
price__gte=100
```

means:

```text
price
  ↓
greater than or equal
```

## Job 2 — Relationship traversal

```python
category__name="Shoes"
```

means:

```text
Product
   ↓
category
   ↓
name
```

You can combine both:

```python
category__name__icontains="shoe"
```

---

# 65. The Pattern You Should Memorize

When you see:

```python
something__something__something=value
```

read from left to right.

Example:

```python
Product.objects.filter(
    category__name__icontains="shoe"
)
```

Read:

```text
Product
   ↓
follow category
   ↓
get name
   ↓
check icontains
   ↓
"shoe"
```

This is the key to understanding Django ORM filters.

---

# 66. Final Cheat Sheet

```python
# EQUALITY
Product.objects.filter(name="Shoes")
Product.objects.filter(name__exact="Shoes")
Product.objects.filter(name__iexact="shoes")


# TEXT
Product.objects.filter(name__contains="Shoe")
Product.objects.filter(name__icontains="shoe")

Product.objects.filter(name__startswith="Nike")
Product.objects.filter(name__istartswith="nike")

Product.objects.filter(name__endswith="Shoes")
Product.objects.filter(name__iendswith="shoes")


# COMPARISON
Product.objects.filter(price__gt=100)
Product.objects.filter(price__gte=100)
Product.objects.filter(price__lt=100)
Product.objects.filter(price__lte=100)


# LIST
Product.objects.filter(id__in=[1, 2, 3])


# RANGE
Product.objects.filter(price__range=(50, 100))


# NULL
Product.objects.filter(description__isnull=True)
Product.objects.filter(description__isnull=False)


# DATE
Order.objects.filter(created_at__year=2026)
Order.objects.filter(created_at__month=9)
Order.objects.filter(created_at__day=15)
Order.objects.filter(created_at__week=37)
Order.objects.filter(created_at__quarter=3)
Order.objects.filter(created_at__date="2026-09-15")
Order.objects.filter(created_at__time__gte="09:00")


# RELATIONSHIP
Product.objects.filter(category__name="Shoes")
Product.objects.filter(category__name__icontains="shoe")
Product.objects.filter(category__id=5)
Product.objects.filter(category_id=5)


# REVERSE RELATIONSHIP
Category.objects.filter(products__name__icontains="shoe")


# MULTIPLE CONDITIONS
Product.objects.filter(
    price__gte=50,
    price__lte=200,
    stock__gt=0,
)


# EXCLUDE
Product.objects.exclude(
    name__icontains="shoe"
)


# OR
from django.db.models import Q

Product.objects.filter(
    Q(name__icontains="shoe") |
    Q(name__icontains="shirt")
)


# AND
Product.objects.filter(
    Q(price__gte=50) &
    Q(stock__gt=0)
)


# NOT
Product.objects.filter(
    ~Q(name__icontains="shoe")
)
```

# The 15 Lookups to Memorize First

If you don't want to memorize everything immediately, start with these:

```text
1.  exact
2.  iexact

3.  contains
4.  icontains

5.  startswith
6.  istartswith

7.  endswith
8.  iendswith

9.  gt
10. gte
11. lt
12. lte

13. in
14. range
15. isnull
```

And remember:

```text
__eq ❌
      ↓
field=value ✅
field__exact=value ✅
```

The most important skill is not memorizing every lookup. It is understanding the pattern:

```python
Model.objects.filter(
    field__lookup=value
)
```

and for relationships:

```python
Model.objects.filter(
    relationship__field__lookup=value
)
```
