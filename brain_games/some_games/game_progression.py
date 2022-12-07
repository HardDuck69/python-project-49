from random import randint, choice


RULE = 'What number is missing in the progression?'
LENGHT = 9


def get_game():
    random_number = randint(0, 10)
    step = randint(1, 10)
    progression = []
    for i in range(LENGHT):
        next_step = random_number + step * i
        progression.append(str(next_step))
    secret_index = choice(range(len(progression) - 1))
    correct_answer = progression[secret_index]
    progression[secret_index] = '..'
    question = " ".join(progression)
    return question, correct_answer


if __name__ == '__main__':
    get_game()
