from random import randint, choice


Goal = 'What number is missing in the progression?'
Length = 9


def task():
    number = randint(0, 10)
    step = randint(1, 10)
    progression = []
    for i in range(Length):
        next_step = number + step * i
        progression.append(str(next_step))
    secret_index = choice(range(len(progression) - 1))
    correct_answer = progression[secret_index]
    progression[secret_index] = '..'
    question = " ".join(progression)
    return question, correct_answer


if __name__ == '__main__':
    task()
