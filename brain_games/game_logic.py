import prompt


def start_game(game):
    print('Welcome to the Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print(game.RULE)
    count = 0
    while count != 3:
        question, correct_answer = game.get_game()
        print(f'Question: {question}')
        answer = prompt.string('Your answer: ')
        if correct_answer == answer:
                   print('Correct!')
                   count += 1
        else:
                   print(f"'{answer}' is wrong answer ;(. \
Correct answer was '{correct_answer}'")
                   print(f"Let's try again, {name}!")
                   break
    else:
        print(f'Congratulations, {name}!')
