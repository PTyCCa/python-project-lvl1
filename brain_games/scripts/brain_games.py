#!/usr/bin/env python3
"""Main  game modul."""

from brain_games.cli import welcome_user


def greet():
    """Make invitation welcome string."""
    print('Welcome to the Brain Games!')
    welcome_user()


def main():
    """Game start invitation."""
    greet()


if __name__ == '__main__':
    main()
