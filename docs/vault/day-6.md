---
id: xOyWcjrOcRUBsxZUYPT6x
title: Day 6 - Beginner
desc: 'Python Functions & Karel'
updated: 1643810762521
created: 1643723392137
---

## Overview

### Lessons

1. Code blocks
1. Functions
1. While Loops

### Project

- Karel, The Robot 🤖

## Functions

- code block that does something
- can be called multiple times
- makes code more manageable, reusable and readable

```py
def my_function():
    # do this
    # then do this
    # finally do this

my_function()
```

## While loop

- loop that will continue to run while the condition is true
- infinite loop occurs when condition remains true always, thus not stopping

```py
while condition_is_true:
    # do something repeatedly
```

## References

1. [Reeborg's World](https://reeborg.ca/reeborg.html)

```py
def turn_around():
    turn_left()
    turn_left()

def turn_right():
    turn_left()
    turn_left()
    turn_left()

# draw square
turn_left()
move()
turn_right()
move()
turn_right()
move()
turn_right()
move()
```
