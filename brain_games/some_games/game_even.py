#!/usr/bin/env python3
from random import randint
import prompt

Goal = 'Answer "yes" if the number is even, otherwise answer "no".'
print(Goal)

def is_even(question):
    if question % 2 == 0:
        return 'yes'
    else:
        return 'no'


def task():
    question = random.randint(1, 30)
    correct_answer = str(is_even(question))
    return question, correct_answer

Congr = prompt.string('Congratulations, ')
print("Congr, {0}!\n".format(name))
