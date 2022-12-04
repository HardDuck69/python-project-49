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
    name = welcome_user()
    print(game.task)
    count = 0
    while count != 3:
        question, correct_answer = game.task()
        if round(question, correct_answer):
            count += 1
        else:
            print(f"Let's try again, {name}!")
            break
    else:
        print(f'Congratulations, {name}!')