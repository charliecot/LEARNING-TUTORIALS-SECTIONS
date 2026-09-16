# Django Admin Inlines — Complete Reference

Django Admin provides two main types of inline forms:

1. `admin.TabularInline`
2. `admin.StackedInline`

Both are used to display and edit **related model objects inside the Admin page of another model**.

---

# 1. What is an Inline?

Suppose we have:

```python
class Order(models.Model):
    customer = models.CharField(max_length=100)


class OrderItem(models.Model):
    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE
    )
    product = models.CharField(max_length=100)
    quantity = models.PositiveIntegerField()
```

The relationship is:

```text
Order
 │
 ├── OrderItem
 ├── OrderItem
 └── OrderItem
```

Instead of opening:

```text
Order → save
OrderItem → create
OrderItem → create
OrderItem → create
```

an inline allows you to manage the `OrderItem` objects directly from the `Order` Admin page.

---

# 2. The Two Types

## TabularInline

```python
class OrderItemInline(admin.TabularInline):
    model = OrderItem
```

Displays related objects in a **table**.

Example:

```text
Order Items
-------------------------------------------------
Product       Quantity       Price       DELETE
-------------------------------------------------
Shoes         2              50.00       [x]
Shirt         1              30.00       [x]
Bag           3              20.00       [x]
-------------------------------------------------
```

Best when the model has relatively few/simple fields.

---

## StackedInline

```python
class OrderItemInline(admin.StackedInline):
    model = OrderItem
```

Displays each related object as a **vertical block**.

Example:

```text
Order Item #1

Product:  [Shoes       ]
Quantity: [2           ]
Price:    [50.00       ]

--------------------------------

Order Item #2

Product:  [Shirt       ]
Quantity: [1           ]
Price:    [30.00       ]
```

Best when the model has many fields or fields that need more space.

---

# 3. Basic Structure

Both use almost the same configuration.

## Tabular

```python
class OrderItemInline(admin.TabularInline):
    model = OrderItem
```

## Stacked

```python
class OrderItemInline(admin.StackedInline):
    model = OrderItem
```

Then add the inline to the parent `ModelAdmin`:

```python
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    inlines = [OrderItemInline]
```

---

# 4. Complete Basic Example

```python
from django.contrib import admin
from .models import Order, OrderItem


class OrderItemInline(admin.TabularInline):
    model = OrderItem


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    inlines = [OrderItemInline]
```

Now when you open an `Order` in Django Admin, its `OrderItem` objects appear inside the same page.

---

# 5. IMPORTANT: The ForeignKey Relationship

For an inline to work, the child model normally needs a `ForeignKey` to the parent model.

Example:

```python
class Order(models.Model):
    customer = models.CharField(max_length=100)


class OrderItem(models.Model):
    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE
    )
    product = models.CharField(max_length=100)
    quantity = models.PositiveIntegerField()
```

Here:

```python
order = models.ForeignKey(Order, ...)
```

is what connects:

```text
Order
   ↓
OrderItem
```

Django uses this relationship to know which `OrderItem` objects belong to the current `Order`.

---

# 6. model

The most important option.

```python
class OrderItemInline(admin.TabularInline):
    model = OrderItem
```

`model` tells Django which related model should be displayed.

Example:

```python
model = OrderItem
```

means:

> Display `OrderItem` objects inside the parent Admin page.

---

# 7. extra

Controls how many **empty forms** Django displays for creating new objects.

```python
extra = 3
```

Displays 3 empty rows.

Common choice:

```python
extra = 0
```

This means:

> Do not display extra empty rows.

Example:

```python
class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0
```

---

# 8. fields

Controls which fields are displayed and their order.

```python
fields = [
    "product",
    "quantity",
    "price",
]
```

The order here determines the order in the Admin.

Example:

```python
class OrderItemInline(admin.TabularInline):
    model = OrderItem

    fields = [
        "product",
        "quantity",
        "price",
    ]
```

You can also use tuples:

```python
fields = (
    "product",
    "quantity",
    "price",
)
```

---

# 9. exclude

Specifies fields that should NOT be displayed.

```python
exclude = [
    "created_at",
    "updated_at",
]
```

Example:

```python
class OrderItemInline(admin.TabularInline):
    model = OrderItem

    exclude = [
        "created_at",
        "updated_at",
    ]
```

### fields vs exclude

Use `fields` when you want to explicitly say:

> Show these fields.

Use `exclude` when you want to say:

> Show everything except these fields.

Usually you don't need both.

---

# 10. readonly_fields

Makes fields visible but not editable.

```python
readonly_fields = [
    "price",
]
```

Example:

```python
class OrderItemInline(admin.TabularInline):
    model = OrderItem

    readonly_fields = [
        "price",
    ]
```

The user can see the price but cannot edit it.

This is useful for:

```text
created_at
updated_at
price
total
user
```

when those values should be controlled by your application.

---

# 11. can_delete

Controls whether users can delete inline objects.

```python
can_delete = True
```

Default:

```python
can_delete = True
```

Disable deletion:

```python
can_delete = False
```

Example:

```python
class OrderItemInline(admin.TabularInline):
    model = OrderItem

    can_delete = False
```

Now the delete checkbox is not provided.

---

# 12. max_num

Controls the maximum number of inline forms.

```python
max_num = 5
```

This limits the number of forms to 5.

Example:

```python
class OrderItemInline(admin.TabularInline):
    model = OrderItem

    max_num = 5
```

Useful when a parent should have a limited number of related objects.

---

# 13. min_num

Controls the minimum number of inline forms.

```python
min_num = 1
```

This requires at least one inline form.

Example:

```python
class OrderItemInline(admin.TabularInline):
    model = OrderItem

    min_num = 1
```

You can combine:

```python
min_num = 1
max_num = 10
```

Meaning:

```text
Minimum: 1
Maximum: 10
```

---

# 14. ordering

Controls the order of inline objects.

```python
ordering = ["product"]
```

Ascending:

```python
ordering = ["product"]
```

Descending:

```python
ordering = ["-product"]
```

Multiple fields:

```python
ordering = [
    "product",
    "-quantity",
]
```

Example:

```python
class OrderItemInline(admin.TabularInline):
    model = OrderItem

    ordering = ["-created_at"]
```

Newest objects appear first.

---

# 15. fk_name

Normally Django automatically finds the ForeignKey connecting the two models.

But suppose you have:

```python
class OrderItem(models.Model):
    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE,
        related_name="items"
    )

    original_order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE,
        related_name="original_items"
    )
```

There are now **two ForeignKeys to `Order`**.

Django needs to know which one the inline should use.

Use:

```python
fk_name = "order"
```

Example:

```python
class OrderItemInline(admin.TabularInline):
    model = OrderItem
    fk_name = "order"
```

---

# 16. show_change_link

Adds a link to the individual object's Admin change page.

```python
show_change_link = True
```

Example:

```python
class OrderItemInline(admin.TabularInline):
    model = OrderItem

    show_change_link = True
```

This is useful when the inline object has many fields or additional information that isn't displayed in the inline.

---

# 17. classes

Controls CSS classes applied to the inline.

A common example is:

```python
classes = ["collapse"]
```

This makes the inline collapsible.

Example:

```python
class OrderItemInline(admin.TabularInline):
    model = OrderItem

    classes = ["collapse"]
```

The Admin section can then be collapsed/expanded.

---

# 18. verbose_name

Changes the singular name displayed by the Admin.

```python
verbose_name = "Order item"
```

Example:

```python
class OrderItemInline(admin.TabularInline):
    model = OrderItem

    verbose_name = "Product in this order"
```

---

# 19. verbose_name_plural

Changes the plural heading.

```python
verbose_name_plural = "Products in this order"
```

Example:

```python
class OrderItemInline(admin.TabularInline):
    model = OrderItem

    verbose_name_plural = "Products in this order"
```

---

# 20. form

You can provide a custom Django form.

Example:

```python
from django import forms


class OrderItemForm(forms.ModelForm):

    class Meta:
        model = OrderItem
        fields = "__all__"
```

Then:

```python
class OrderItemInline(admin.TabularInline):
    model = OrderItem
    form = OrderItemForm
```

This is useful when you need custom validation or custom form behavior.

---

# 21. formset

You can provide a custom formset.

```python
from django.forms.models import BaseInlineFormSet
```

Example:

```python
class OrderItemFormSet(BaseInlineFormSet):

    def clean(self):
        super().clean()

        # custom validation
```

Then:

```python
class OrderItemInline(admin.TabularInline):
    model = OrderItem
    formset = OrderItemFormSet
```

Use a custom formset when the validation depends on **multiple inline objects together**.

For example:

```text
Order
 ├── Item 1
 ├── Item 2
 └── Item 3
```

You can validate the entire collection of items.

---

# 22. autocomplete_fields

Allows Django Admin to use an autocomplete widget for related fields.

Example:

```python
autocomplete_fields = ["product"]
```

Useful when the related model contains many records.

For example:

```text
Product
---------
1,000 products
10,000 products
100,000 products
```

Instead of displaying a huge dropdown, Admin can provide a search box.

The related `ModelAdmin` also needs appropriate configuration for autocomplete.

---

# 23. raw_id_fields

Instead of a normal select box, Django provides an ID-based lookup widget.

```python
raw_id_fields = ["product"]
```

Useful for very large related tables.

Example:

```python
class OrderItemInline(admin.TabularInline):
    model = OrderItem

    raw_id_fields = ["product"]
```

---

# 24. classes + collapse

A common Admin pattern:

```python
class OrderItemInline(admin.TabularInline):
    model = OrderItem

    classes = ["collapse"]
```

The inline starts collapsed, which keeps a large Admin page cleaner.

---

# 25. TabularInline Complete Example

```python
from django.contrib import admin
from .models import Order, OrderItem


class OrderItemInline(admin.TabularInline):
    model = OrderItem

    extra = 0

    fields = [
        "product",
        "quantity",
        "price",
    ]

    readonly_fields = [
        "price",
    ]

    ordering = [
        "-created_at",
    ]

    show_change_link = True

    can_delete = True

    min_num = 0
    max_num = 20

    classes = ["collapse"]


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    inlines = [
        OrderItemInline,
    ]
```

---

# 26. StackedInline Complete Example

The exact same options can generally be used with `StackedInline`.

```python
from django.contrib import admin
from .models import Order, OrderItem


class OrderItemInline(admin.StackedInline):
    model = OrderItem

    extra = 0

    fields = [
        "product",
        "quantity",
        "price",
    ]

    readonly_fields = [
        "price",
    ]

    ordering = [
        "-created_at",
    ]

    show_change_link = True

    can_delete = True

    min_num = 0
    max_num = 20

    classes = ["collapse"]


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    inlines = [
        OrderItemInline,
    ]
```

The main difference is simply:

```python
admin.TabularInline
```

versus:

```python
admin.StackedInline
```

---

# 27. TabularInline vs StackedInline

| Feature               | TabularInline   | StackedInline    |
| --------------------- | --------------- | ---------------- |
| Layout                | Table           | Vertical blocks  |
| Space used            | Less            | More             |
| Good for many objects | Yes             | Less convenient  |
| Good for many fields  | Less convenient | Yes              |
| Compact               | Yes             | No               |
| Easy to scan          | Yes             | Yes              |
| Main purpose          | Compact editing | Detailed editing |

---

# 28. Simple Example

Imagine:

```python
class Author(models.Model):
    name = models.CharField(max_length=100)


class Book(models.Model):
    author = models.ForeignKey(
        Author,
        on_delete=models.CASCADE
    )
    title = models.CharField(max_length=200)
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )
```

You can create:

```python
class BookInline(admin.TabularInline):
    model = Book
    extra = 1
```

Then:

```python
@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    inlines = [BookInline]
```

The Admin page becomes conceptually:

```text
AUTHOR

Name:
[Charles                         ]


BOOKS

Title              Price
--------------------------
[Python]           [20.00]
[Django]           [30.00]
[React Native]     [25.00]
[                 ] [      ]
```

With `StackedInline`:

```python
class BookInline(admin.StackedInline):
    model = Book
    extra = 1
```

You get:

```text
AUTHOR

Name:
[Charles]


BOOK #1

Title:
[Python]

Price:
[20.00]


BOOK #2

Title:
[Django]

Price:
[30.00]
```

---

# 29. The Most Important Options to Remember

For everyday Django Admin work, remember these first:

```python
class OrderItemInline(admin.TabularInline):
    model = OrderItem

    extra = 0

    fields = [
        "product",
        "quantity",
        "price",
    ]

    readonly_fields = [
        "price",
    ]

    exclude = []

    ordering = ["-created_at"]

    can_delete = True

    min_num = 0

    max_num = 20

    show_change_link = True

    classes = ["collapse"]
```

Then:

```python
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    inlines = [OrderItemInline]
```

---

# 30. Mental Model

Think about an inline like this:

```text
                    PARENT
                      │
                      │ ForeignKey
                      ↓
                   CHILDREN
                      │
          ┌───────────┼───────────┐
          ↓           ↓           ↓
       Child 1     Child 2     Child 3
```

Django Admin lets you edit:

```text
Parent
   +
Children
```

on **one Admin page**.

The two visual choices are:

```text
TabularInline
     ↓
TABLE / ROWS


StackedInline
     ↓
VERTICAL / BLOCKS
```

---

# 31. Quick Template

Use this as your starting template:

```python
class ChildInline(admin.TabularInline):
    model = Child

    extra = 0

    fields = [
        "field1",
        "field2",
        "field3",
    ]

    readonly_fields = [
        "field3",
    ]

    ordering = [
        "-created_at",
    ]

    can_delete = True

    min_num = 0
    max_num = 20

    show_change_link = True

    classes = ["collapse"]
```

Or simply change:

```python
admin.TabularInline
```

to:

```python
admin.StackedInline
```

when you want the vertical layout.

# Key Difference

```python
class MyInline(admin.TabularInline):
    model = MyModel
```

means:

> Show related objects as rows in a table.

```python
class MyInline(admin.StackedInline):
    model = MyModel
```

means:

> Show related objects as separate vertical sections.

Everything else — such as `model`, `extra`, `fields`, `readonly_fields`, `can_delete`, `max_num`, `min_num`, `ordering`, `fk_name`, `form`, `formset`, `show_change_link`, etc. — is configuration for how that inline behaves.
