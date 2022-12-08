import random
import operator
RULE = 'What is the result of the expression?'
OPERATORS = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul
}


def get_game():
    random_number1 = random.randint(1, 30)
    random_number2 = random.randint(1, 30)
    operator_symb = random.choice(list(OPERATORS))
    question = f"{random_number1} {operator_symb} {random_number2}"
    correct_answer = str(
        OPERATORS.get(operator_symb)
        (random_number1, random_number2)
    )
    return question, correct_answer
