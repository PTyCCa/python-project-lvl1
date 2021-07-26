#!/usr/bin/env python3
"""Brain Games Even start modul."""
import brain_games.game_engine
import brain_games.games.brain_even


def main():
    """Run Brain Even game."""
    brain_games.game_engine.run(brain_games.games.brain_even)


if __name__ == '__main__':
    main()
