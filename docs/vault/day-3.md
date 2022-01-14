---
id: hnGiQ8UPD9akby4lRWt2D
title: Day 3 - Beginner
desc: 'Control Flow and Logical Operators'
updated: 1642171301097
created: 1641824164751
---

## Overview

### Goals

1. Conditional statements
2. Logical operators
3. Code blocks
4. Scope

### Project

- Choose Your Own Adventure 👑

## Conditionals

- if condition is true, execute code block

```py
if condition:
    # do this
else:
    # do this
```

```py
water_level = 50

if water_level > 80:
    print("Drain water")
else:
    print("Continue")
```

## Code blocks

- indented code/s

## Comparison operators

- `==` equal
- `!=` not equal
- `>` greater than
- `<` less than
- `>=` greater than or equal
- `<=` less than or equal

## Modulo

- `%` calculates for the remainder after dividing one number by another

```py
8 % 2 # returns 0
9 % 2 # returns 1
```

## Nested conditionals

- nest conditional statements inside another

### nested if/else

```py
if condition:
    if condition:
        # do this
    else:
        # do this
else:
    # do this
```

### if/elif/else

- checks conditions in sequence

```py
if condition1:
    # do A
elif condition2:
    # do B
else:
    # do this
```

## Multiple if statements

```py
if condition1:
    # do A

if condition2:
    # do B

if condition3:
    # do C
```

### Increment value

```py
x = x + 1
x += 1
```

## Logical operators

- `and`
  - TRUE if all conditions are true
  - FALSE if at least one condition is false
- `or`
  - TRUE if at least one condition is true
  - FALSE if all conditions are false

## Multi-block string

- enclosed in triple quotes `'''`

```py
'''
This line is part of a multi-block string.
This line is also part of a multi-block string.
'''
```
