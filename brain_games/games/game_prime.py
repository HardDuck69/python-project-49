from random import randint

RULE = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def prime(num):
    if num == 1:
        return False
    for i in range(2, (num // 2 + 1)):
        if num % i == 0:
            return False
    return True


def get_game():
    random_number = randint(1, 100)
    if prime(random_number):
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return random_number, correct_answer
