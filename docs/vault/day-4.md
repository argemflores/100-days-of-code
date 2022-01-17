---
id: 19uqvGlDmd0AWIKPHrj8Z
title: Day 4 - Beginner
desc: 'Randomization and Python Lists'
updated: 1642432358314
created: 1642248651908
---

## Overview

### Goals

1. Explore random module
1. Learn about data structures

### Project

- Rock, Paper, Scissors 🖐

## Randomization

- generate random numbers or results
- Python uses Mersenne Twister

```py
import random
```

## Module

- collection of Python codes
- can be imported to other files

```py
import module
```

## Data structure

- storing piece of data

## List

- collection of ordered items

```py
fruits = ['apple', 'banana', 'cherry']

print(fruits[0]) # apple (first item)
print(fruits[-1]) # cherry (last item)
```

### Append items

```py
# add item to the end of the list
fruits.append('peach')
```

### Extend list

```py
# add items to the end of the list
fruits.extend(['mango', 'kiwi])
```

### Errors

- `IndexError`: list index out of range

### Nested lists

- list containing lists

```py
fruits = ['apple', 'banana', 'cherry']
vegetables = ['celery', 'kale']

food = [fruits, vegetables]
```
