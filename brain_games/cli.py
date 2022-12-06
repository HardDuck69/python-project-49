#!/usr/bin/env python3
import prompt


def welcome_user():
    name = prompt.string("Welcome to the Brain Games!\n May I have your name? ")
    print("Hello, {0}!\n".format(name))


if __name__ == '__main__':
    welcome_user()
