#!/usr/bin/env python3
class Plant:
    def __init__(self, name: str, height: float, age: int):
        self.name = name
        self.height = height
        self.current_age = age

    def __str__(self) -> str:
        return (
            f"{self.name}: "
            f"{round(self.height, 1)}cm, "
            f"{self.current_age} days old"
        )

    def grow(self, growth: float) -> None:
        self.height += growth

    def age(self, year: int) -> None:
        self.current_age += year

    def show(self) -> None:
        print(self)


class Flower(Plant):
    def __init__(self, name: str, height: float, age: int, color: str):
        super().__init__(name, height, age)
        self.color = color
        self.is_blooming = False

    def __str__(self) -> str:
        return (
            f"{super().__str__()}\n"
            f" Color: {self.color}\n"
            f" {self._bloom_msg()}"
        )

    def bloom(self) -> None:
        self.is_blooming = True

    def _bloom_msg(self) -> str:
        if not self.is_blooming:
            return f"{self.name} has not bloomed yet"
        else:
            return f"{self.name} is blooming beautifully!"


class Tree(Plant):
    def __init__(
        self, name: str, height: float, age: int, trunk_diameter: float
    ):
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter

    def __str__(self) -> str:
        return (
            f"{super().__str__()}\n"
            f" Trunk diameter: {self.trunk_diameter}cm"
        )

    def produce_shade(self) -> None:
        print(
            f"Tree {self.name} now produces a shade of "
            f"{round(self.height, 1)}cm long and "
            f"{self.trunk_diameter}cm wide."
        )


class Vegetable(Plant):
    def __init__(
        self, name: str, height: float, age: int, harvest_season: str
    ):
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = 0

    def __str__(self) -> str:
        return (
            f"{super().__str__()}\n"
            f" Harvest season: {self.harvest_season}\n"
            f" Nutritional value: {self.nutritional_value}"
        )

    def age(self, year: int) -> None:
        super().age(year)
        self.nutritional_value += year


def main() -> None:
    print("=== Garden Plant Types ===")

    print("=== Flower")
    rose = Flower("Rose", 15.0, 10, "red")
    rose.show()
    print("[asking the rose to bloom]")
    rose.bloom()
    rose.show()
    print("")

    print("=== Tree")
    oak = Tree("Oak", 200.0, 365, 5.0)
    oak.show()
    print("[asking the oak to produce shade]")
    oak.produce_shade()
    print("")

    print("=== Vegetable")
    tomato = Vegetable("Tomato", 5.0, 10, "April")
    tomato.show()
    print("[make tomato grow and age for 20 days]")
    tomato.grow(42)
    tomato.age(20)
    tomato.show()


if __name__ == "__main__":
    main()
