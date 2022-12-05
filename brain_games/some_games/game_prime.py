from random import randit


Goal = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def prime(num):
    if num == 1:
        return False
    for i in range(2, (number // 2 + 1)):
        if num % i == 0:
            return False
    return True

