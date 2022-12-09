from math import gcd
import random

RULE = 'Find the greatest common divisor of given numbers.'


def get_game():
    random_number1 = random.randint(1, 100)
    random_number2 = random.randint(1, 100)
    question = f"{random_number1} {random_number2}"
    correct_answer = str(gcd(random_number1, random_number2))
    return question, correct_answer
