import prompt
from brain_games.cli import welcome_user


def round(question, correct_answer):
    print(f"Question: {question}")
    answer = prompt.string('Your answer: ')
    if correct_answer == answer:
        print('Correct!')
        return True
    else:
        print(f"{answer} is wrong answer ;(. \
Correct answer was {correct_answer}")
        return False


def play(game):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    if name:
        print('Hello, {}!'.format(name))
    print(game.Goal)
    count = 0
    while count != 3:
        question, correct_answer = game.task()
        if round(question, correct_answer):
            count += 1
        else:
            print(f"Let's try again, {}!".format(name))
            break
    else:
        print(f'Congratulations, {}!'.format(name))
