#!/usr/bin/env python3
"""Brain Games Prog start modul."""
import brain_games.game_engine
import brain_games.games.brain_prog


def main():
    """Run Brain GCD game."""
    brain_games.game_engine.run(brain_games.games.brain_prog)


if __name__ == '__main__':
    main()
