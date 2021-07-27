#!/usr/bin/env python3
"""Brain Games GCD start modul."""
import brain_games.game_engine
import brain_games.games.brain_gcd


def main():
    """Run Brain GCD game."""
    brain_games.game_engine.run(brain_games.games.brain_gcd)


if __name__ == '__main__':
    main()
