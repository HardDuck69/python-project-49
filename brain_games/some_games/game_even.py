from random import randint


def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False


def task():
    question = randint(1, 30)
    if is_even(question):
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return question, correct_answer
