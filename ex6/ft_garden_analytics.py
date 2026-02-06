#!/usr/bin/env python3
"""
Exercise 6: Garden Analytics Platform
"""


class Plant():
    """
    A class representing a plant in the garden.
    """

    def __init__(self, name: str, height: float) -> None:
        """
        Initializes a Plant instance.

        Args:
            height (float): The height of the plant in centimeters.
            name (str): The name of the plant.
        """
        self.__height = height
        self.__name = name

    @property
    def height(self) -> float:
        """Returns the height of the plant."""
        return self.__height

    @height.setter
    def height(self, value: float) -> None:
        """Sets the height of the plant."""
        if value < 0:
            raise ValueError("Height cannot be negative.")
        elif value < self.__height:
            raise ValueError("Height cannot decrease.")
        self.__height = value

    @property
    def name(self) -> str:
        """Returns the name of the plant."""
        return self.__name

    def grow(self, amount: float) -> None:
        """Increases the height of the plant by a specified amount."""
        if amount < 0:
            raise ValueError("Growth amount cannot be negative.")
        elif amount == 0:
            raise ValueError("Growth amount cannot be zero.")
        self.__height += amount
        print(f"{self.__name} grew {amount}cm")

def main_plant() -> None:
    # Create a plant instance
    my_plant = Plant(30.0, "Sunflower")

    # Print the plant's name and height
    print(f"Plant Name: {my_plant.name}")
    print(f"Plant Height: {my_plant.height} cm")

    # Update the plant's height
    my_plant.height = 35.0
    print(f"Updated Plant Height: {my_plant.height} cm")

    # Attempt to set an invalid height (negative)
    try:
        my_plant.height = -5.0
    except ValueError as e:
        print(e)

    # Attempt to set an invalid height (decrease)
    try:
        my_plant.height = 25.0
    except ValueError as e:
        print(e)
    # Grow the plant
    try:
        my_plant.grow(5.0)
    except ValueError as e:
        print(e)
    # Attempt to grow the plant with an invalid amount (negative)
    try:        
        my_plant.grow(-2.0)
    except ValueError as e:
        print(e)
    # Attempt to grow the plant with an invalid amount (zero)
    try:
        my_plant.grow(0.0)
    except ValueError as e:
        print(e)
    # Print the final height of the plant
    print(f"Final Plant Height: {my_plant.height} cm")

class FloweringPlant(Plant):
    """
    A class representing a flowering plant, which is a subclass of Plant.
    """

    def __init__(
            self,
            name: str,
            height: float,
            flower_color: str) -> None:
        """
        Constructor of flowering plants
        Args:
            name(str): name of the flower
            height(float): initial height of the flower in cm
            flower_color(str): color of the flower
        Return: Nothing
        """


        super().__init__(name, height)
        self.flower_color = flower_color

    def bloom(self) -> str:
        """
        Message of blooming
        Return: message of blooming

        Args: None
        Return type: str

        """

        return (f"{self.flower_color} flowers (blooming)")

def main_flowering() -> None:
    # Create a flowering plant instance
    my_flowering_plant = FloweringPlant("Rose", 25.0, "Red")

    # Print the flowering plant's name, height, and flower color
    print(f"Flowering Plant Name: {my_flowering_plant.name}")
    print(f"Flowering Plant Height: {my_flowering_plant.height} cm")
    print(f"Flowering Plant Flower Color: {my_flowering_plant.flower_color}")

    # Call the bloom method and print the result
    print(my_flowering_plant.bloom())

class PrizeFlower(FloweringPlant):


    def __init__(
            self,
            name: str,
            height: float,
            flower_color: str,
            prize_points: int) -> None:
        """
        """
        super().__init__(name, height, flower_color)
        self.prize_points = prize_points

    def get_points(self) -> str:
        """
        """
        return (f"Prize points: {self.prize_points}")


def main() -> None:
    my_prize_flower = PrizeFlower("Rosa", 25, "yellow", 2)
    print(f"name: {my_prize_flower.name}, "
        f"{my_prize_flower.height}cm, "
        f"{my_prize_flower.flower_color}")
    print(my_prize_flower.get_points())

if __name__ == "__main__":
    main()
