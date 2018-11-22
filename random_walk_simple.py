#! /usr/bin/env python3

import random

random.seed(1986)


def simple_random_walk_1(steps):

    position = 0
    walk = [position]

    for i in range(steps):
        step = random.randint(0, 1)
        if step == 0:
            position -= 1
            walk.append(position)
        else:
            position += 1
            walk.append(position)
    return walk


def simple_random_walk_2(steps):

    position = 0
    walk = [position]

    for i in range(steps):
        step = 1 if random.randint(0, 1) else -1
        position += step
        walk.append(position)
    return walk


def simple_improved_rand_walk(steps):

    import numpy as np

    steps = np.random.randint(0, 2, steps)
    steps = np.where(steps > 0, 1, -1)
    walk = np.cumsum(steps)
    return walk
