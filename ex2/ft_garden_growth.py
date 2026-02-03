#!/usr/bin/env python3

from typing import List

"""
Exercise 2: Plant Growth Simulator
"""


class Plant:
    """
    A class to represent a plant in the garden.
    """

    def __init__(self, name: str, height: int, age: int, growth_rate: int):
        """
        Allocate memory to create a new Plant instance.

        Args:
            name (str): plant name.
            height (int): plant height in centimeters.
            age (int): plant age in days.
        """
        self.name = name
        self.height = height
        self.age = age
        self.growth_rate = growth_rate  # centimeters per day

    def grow(self, cm: int) -> None:
        """
        Add cm to the plant height.

        Args:
            cm (int): number of centimeters to add to the plant height.
        """

        if cm > 0:
            self.height += cm

    def add_age(self, days: int) -> None:
        """
        Add days to the plant age.

        Args:
            days (int): number of days to add to the plant age.
        """

        if days > 0:
            self.age += days
            self.grow(self.growth_rate * days)

    def get_info(self) -> str:
        """
        Get the plant information as a string.

        Returns:
            str: a string containing the plant's name, height, and age.
        """

        return f"{self.name}: {self.height}cm, {self.age} days old"


def main():

    garden: List[Plant] = []
    rose: Plant = Plant("Rose", 25, 30, 1)
    sunflower: Plant = Plant("Sunflower", 80, 45, 2)
    cactus: Plant = Plant("Cactus", 15, 120, 1)
    garden.extend([rose, sunflower, cactus])
    print("=== Day 1 ===")
    for plant in garden:
        print(plant.get_info())
    for plant in garden:
        plant.add_age(7)
    print("=== Day 7 ===")
    for plant in garden:
        print(plant.get_info())
        print(f"Growth this week: +{plant.growth_rate * 7}cm")


if __name__ == "__main__":
    main()
