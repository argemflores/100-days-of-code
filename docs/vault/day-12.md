---
id: picb8gs33gmn9hkfmtuc3ti
title: Day 12 - Beginner
desc: 'Scope & Number Guessing Game'
updated: 1646657509576
created: 1646656567512
---

## Overview

### Lessons

1. Namespaces and scope

### Project

- The Number Guessing Game 🔮

## Local scope

- variables, functions, and other objects are accessible within code block (e.g. functions)

## Global scope

- variables, functions, and other objects are accessible across all the code

```py
# Global scope
player_health = 10

def game():
    def drink_potion():
        # Local scope
        potion_strength = 2
        print(potion_strength)
        print(player_health)

    drink_potion()

# print(potion_strength)
print(player_health)
game()
```

```shell
10
2
10
```

## Block scope does not exist

- variable is still accessible outside a code block where it is defined (e.g. if statement, for loop)

```py
game_level = 3

def create_enemy():
    enemies = ["Skeleton", "Zombie", "Alien"]

    if game_level < 5:
        new_enemy = enemies[0]

    # still accessible
    print(new_enemy)

create_enemy()
```

```shell
Skeleton
```
