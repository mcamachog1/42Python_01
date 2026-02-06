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


def test_plant() -> None:
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
    # Attempt to grow the plant with an invalid amount (negative)    try:
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
        """

        super().__init__(name, height)
        self.flower_color = flower_color

    def bloom(self) -> str:
        """
        Return blooming message
        """

        return (f"{self.flower_color} flowers (blooming)")


def test_flowering() -> None:
    # Create a flowering plant instance
    my_flowering_plant = FloweringPlant("Rose", 25.0, "Red")

    # Print the flowering plant's name, height, and flower color
    print(f"Flowering Plant Name: {my_flowering_plant.name}")
    print(f"Flowering Plant Height: {my_flowering_plant.height} cm")
    print(f"Flowering Plant Flower Color: {my_flowering_plant.flower_color}")

    # Call the bloom method and print the result
    print(my_flowering_plant.bloom())


class PrizeFlower(FloweringPlant):
    """
    A class representing a Prize Flower.
    """

    def __init__(
            self,
            name: str,
            height: float,
            flower_color: str,
            prize_points: int) -> None:
        """
        A class representing a prize flower,
        which is a subclass of FloweringPlant.
        """
        super().__init__(name, height, flower_color)
        self.prize_points = prize_points

    def get_points(self) -> str:
        """
        Return a message with prize points of the flower
        """
        return (f"Prize points: {self.prize_points}")


def test_prize_flower() -> None:
    my_prize_flower = PrizeFlower("Rosa", 25, "yellow", 2)
    print(
        f"name: {my_prize_flower.name}, "
        f"{my_prize_flower.height}cm, "
        f"{my_prize_flower.flower_color}")
    print(my_prize_flower.get_points())


class GardenManager():
    """
    A class representing a garden manager.
    """

    total_gardens: int = 0
    all_gardens: list['GardenManager'] = []


    def __init__(self, garden_name: str) -> None:
        """
        Initializes a GardenManager instance.

        Args:
            garden_name (str): The name of the garden.
            plants (list[Plant]): The list of plants in the garden.
        """
        self.garden_name: str = garden_name
        self.plants: list[Plant] = []
        GardenManager.total_gardens += 1
        GardenManager.all_gardens.append(self)

    @classmethod
    def get_total_gardens(cls) -> int:
        """Returns the total number of gardens managed."""
        return cls.total_gardens

    @staticmethod
    def validate_height(height: float) -> bool:
        """Validates if the height is a positive number."""
        return height > 0

    @classmethod
    def create_garden_network(cls) -> int:
        """Returns a message indicating that the garden is being managed."""
        return len(cls.all_gardens)

    def add_plant(self, plant: Plant) -> None:
        """Adds a plant to the garden."""
        self.plants.append(plant)
        print(f"Added {plant.name} to the garden {self.garden_name}.")

    class GardenStats():
        """
        A nested class representing garden statistics.
        """
        @staticmethod
        def generate_report(manager: 'GardenManager') -> None:
            """
            Prints a message displaying the garden statistics.
            Args:
                manager (GardenManager): The garden manager
                for which to generate the report.
            """
            for garden in manager.all_gardens:
                print(
                    f"Garden: {garden.garden_name}, "
                    f"Number of Plants: {len(garden.plants)}")



def test_garden_manager() -> None:
    manager1 = GardenManager("Alice")
    manager2 = GardenManager("Bob")

    plant1 = Plant("Sunflower", 30)
    plant2 = FloweringPlant("Rose", 25.0, "Red")
    plant3 = PrizeFlower("Rosa", 25, "yellow", 2)

    manager1.add_plant(plant1)
    manager1.add_plant(plant2)
    manager2.add_plant(plant3)

    GardenManager.GardenStats.generate_report(manager1)
    GardenManager.GardenStats.generate_report(manager2)



if __name__ == "__main__":
    # test_plant()
    # test_flowering()
    # test_prize_flower()
    test_garden_manager()
