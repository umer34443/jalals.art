"""Simple snake growth simulation.

This module defines a :class:`Snake` that gains weight when it eats apples.
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass, field
from typing import Tuple


@dataclass
class Snake:
    """Represents a snake with a body length, width, and color.

    Attributes
    ----------
    length : int
        The length of the snake in arbitrary units.
    girth : int
        The girth of the snake. When the snake eats an apple its girth increases.
    color : str
        The color of the snake, which changes every time it eats an apple.
    """

    length: int
    girth: int
    color: str = "green"
    _color_cycle: Tuple[str, ...] = field(
        default=("green", "yellow", "red", "blue"), init=False, repr=False
    )
    _color_index: int = field(init=False, repr=False)

    def __post_init__(self) -> None:
        """Validate the initial color and set up the cycle index."""

        if self.color not in self._color_cycle:
            allowed_colors = ", ".join(self._color_cycle)
            raise ValueError(
                f"Initial color must be one of {allowed_colors}; got '{self.color}'."
            )

        self._color_index = self._color_cycle.index(self.color)

    def eat_apple(self, *, length_gain: int = 1, girth_gain: int = 1) -> None:
        """Grow the snake after it eats an apple.

        Parameters
        ----------
        length_gain : int, default=1
            How much longer the snake becomes.
        girth_gain : int, default=1
            How much fatter the snake becomes.
        """

        if length_gain < 0 or girth_gain < 0:
            raise ValueError("Growth values must be non-negative")

        self.length += length_gain
        self.girth += girth_gain
        self._advance_color()

    @property
    def description(self) -> str:
        """Return a short description of the snake's current state."""

        return (
            f"The snake is now {self.length} units long, "
            f"{self.girth} units around, and {self.color}."
        )

    def _advance_color(self) -> None:
        """Move the snake's color to the next entry in the cycle."""

        self._color_index = (self._color_index + 1) % len(self._color_cycle)
        self.color = self._color_cycle[self._color_index]


def run_simulation(
    *,
    apples: int,
    length_gain: int,
    girth_gain: int,
) -> None:
    """Execute a simple simulation that feeds the snake a number of apples."""

    snake = Snake(length=5, girth=2)
    print("Initial:", snake.description)

    for apple_number in range(1, apples + 1):
        snake.eat_apple(length_gain=length_gain, girth_gain=girth_gain)
        print(
            f"After apple {apple_number}:",
            snake.description,
        )


def build_arg_parser() -> argparse.ArgumentParser:
    """Create the argument parser for the simulation CLI."""

    parser = argparse.ArgumentParser(
        description="Run a simple snake growth simulation.",
    )
    parser.add_argument(
        "--apples",
        type=int,
        default=2,
        help="How many apples to feed the snake.",
    )
    parser.add_argument(
        "--length-gain",
        type=int,
        default=1,
        help="How much the snake grows in length per apple.",
    )
    parser.add_argument(
        "--girth-gain",
        type=int,
        default=1,
        help="How much the snake grows in girth per apple.",
    )
    return parser


def main() -> None:
    """Parse CLI arguments and run the simulation."""

    parser = build_arg_parser()
    args = parser.parse_args()
    run_simulation(
        apples=args.apples,
        length_gain=args.length_gain,
        girth_gain=args.girth_gain,
    )


if __name__ == "__main__":
    main()
