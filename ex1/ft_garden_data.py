#!/usr/bin/env python3

from typing import List

"""
Exercise 1: Garden Data Organizer
"""


class Plant:
    """
    A class to represent a plant in the garden.
    """
    def __init__(self, name: str, hight: int, age: int):
        """
        Allocate memory to create a new Plant instance.

        Args:
            name (str): plant name.
            height (int): plant height in centimeters.
            age (int): plant age in days.
        """
        self.name = name
        self.height = hight
        self.age = age


def main():
    """
    Main function to create and display plant data.
    """

    garden: List[Plant] = []
    rose: Plant = Plant("Rose", 25, 30)
    sunflower: Plant = Plant("Sunflower", 80, 45)
    cactus: Plant = Plant("Cactus", 15, 120)
    garden.extend([rose, sunflower, cactus])
    print("=== Gardden Plant Registry ===")
    for plant in garden:
        print(f"{plant.name}: {plant.height}cm, {plant.age} days old")


if __name__ == "__main__":
    main()
