"""Simple snake growth simulation.

This module defines a :class:`Snake` that gains weight when it eats apples.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass
class Snake:
    """Represents a snake with a body length and width.

    Attributes
    ----------
    length : int
        The length of the snake in arbitrary units.
    girth : int
        The girth of the snake. When the snake eats an apple its girth increases.
    """

    length: int
    girth: int

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

    @property
    def description(self) -> str:
        """Return a short description of the snake's current state."""

        return (
            f"The snake is now {self.length} units long and "
            f"{self.girth} units around."
        )


if __name__ == "__main__":
    snake = Snake(length=5, girth=2)
    print("Initial:", snake.description)
    snake.eat_apple(length_gain=2, girth_gain=3)
    print("After eating an apple:", snake.description)
