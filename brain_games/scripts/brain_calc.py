#!/usr/bin/env python3
"""Brain Games Calculator start modul."""
import brain_games.game_engine
import brain_games.games.brain_calc


def main():
    """Run Brain Calc game."""
    brain_games.game_engine.run(brain_games.games.brain_calc)


if __name__ == '__main__':
    main()
