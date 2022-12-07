#!/usr/bin/env python3


from brain_games.game_logic import start_game
from brain_games.some_games import game_even


def main():
    start_game(game_even)


if __name__ == '__main__':
    main()
