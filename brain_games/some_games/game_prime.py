from random import randint


def prime(num):
    if num == 1:
        return False
    for i in range(2, (num // 2 + 1)):
        if num % i == 0:
            return False
    return True


def task():
    question = randint(1, 100)
    if prime(question):
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return question, correct_answer
