---
id: zMH0dupWakQIQQ8AYJXks
title: Day 2 - Beginner
desc: 'Understanding Data Types and How to Manipulate Strings'
updated: 1640615632295
created: 1640586318523
---

## Overview

### Goals

1. Learn data types and operations
1. Convert data types
1. Print with f-Strings

### Project

- Tip Calculator 💵

## String

### Subscript

- pull out particular element/s from a string using `[x]`
- `x` is an index and always starts at `0` and ends in `length-1`

```py
print("Hello"[0]) # H
print("Hello"[4]) # o
```

### Concatenation

- join a string with other strings using `+`

```py
print(1 + "2") # ERROR
```

## Integer

- whole numbers
- can be separated with underscore `_`

```py
123
123_456_789 # 123456789
```

## Float

- numbers with a decimal point

```py
0.123
3.1416
123_456.789 # 123456.789
```

## Boolean

- logical true or false
- first letter is in uppercase

```py
print(True) # yes, 1
print(False) # no, 0
```

## Type

- check the data type using `type()`

```py
num = 123
type(num) # <class 'int'>
```

## Conversion

- convert data type to another

```py
num = 123
str(num) # '123'
type(str(num)) # <class 'str'>
```

## Operations

```py
3 + 5 # addition: 8
7 - 4 # subtraction: 3
3 * 2 # multiplication: 6
6 / 3 # division: 2.0 (float)
2 ** 3 # power/exponent: 8
```

### PEMDAS(LR)

- order of priority in calculation
- left to right for `* /` and `+ -`

1. `()`
1. `**`
1. `* /` (left to right)
1. `+ -` (left to right)

```py
3 * 3 + 3 / 3 - 3 # 7.0 (float because of /)
3 * (3 + 3) / 3 - 3 # 3.0
```

### Number manipulation

```py
print(8 / 3) # 2.6666666666666665 (float)
print(int(8 / 3)) # 2 (int)
```

### Round

- round off a number (with a specified number of decimals)
- `round(number, decimal_places)`

```py
print(round(8 / 3)) # 3 (int)
print(round(8 / 3, 2)) # 2.67 (float)
```

### Floor division

- get floor value between 2 divided numbers using `//`

```py
print(8 // 3) # 2 (int)
```

### Short forms

- `+=` add to previous value
- `-=` subtract from previous value
- `*=` multiple to previous value
- `/=` divide by previous value

```py
score = 0
score += 1 # 1

result = 4 / 2 # 2
result /= 2 # 1.0
```

## f-String

- formatted string literals
- prefix string with `f` and enclose variable with `{}`
- example: `f"String has {variable}"`

```py
score = 1
print("Your score is " + str(score))

height = 1.8
is_winning = True

print(f"Your score is {score}, your height is {height}, you are winning is {is_winning}")
```

### Format

- float with decimal places `{variable:.2f}`

```py
value = 3 / 6 # 0.5
print(f"Value is {value:.2f}") # 0.50
```
