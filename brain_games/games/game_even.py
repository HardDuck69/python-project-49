from random import randint

RULE = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False


def get_game():
    random_number = randint(1, 30)
    if is_even(random_number):
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return random_number, correct_answer
