#!/usr/bin/env python3
class Plant:
    class _Stats:
        def __init__(self) -> None:
            self.grow = 0
            self.age = 0
            self.show = 0

    def __init__(self, name: str, height: float, age: int):
        self.name = name or "Unknown plant"
        self.height = height
        self.current_age = age
        self.stats = self._Stats()

    def __str__(self) -> str:
        return (
            f"{self.name}: "
            f"{round(self.height, 1)}cm, "
            f"{self.current_age} days old"
        )

    def grow(self, growth: float) -> None:
        self.height += growth
        self.stats.grow += 1

    def age(self, year: int) -> None:
        self.current_age += year
        self.stats.age += 1

    def show(self) -> None:
        print(self)
        self.stats.show += 1

    @classmethod
    def anonymous(cls) -> "Plant":
        return cls("", 0.0, 0)

    @staticmethod
    def is_older_than_a_year(age: int) -> None:
        print(f"Is {age} days more than a year? -> {age > 365}")


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
    class _Stats(Plant._Stats):
        def __init__(self) -> None:
            super().__init__()
            self.produce_shade = 0

    def __init__(
        self, name: str, height: float, age: int, trunk_diameter: float
    ):
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter
        self.stats: Tree._Stats = self._Stats()

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
        self.stats.produce_shade += 1


class Seed(Flower):
    def __init__(self, name: str, height: float, age: int, color: str) -> None:
        super().__init__(name, height, age, color)
        self.seed_count = 0

    def __str__(self) -> str:
        return f"{super().__str__()}\n" f" Seeds: {self.seed_count}"

    def bloom(self) -> None:
        super().bloom()
        self.seed_count = 42


def display_stats(plant: Plant | Tree) -> None:
    stats = plant.stats
    print(f"Stats: {stats.grow} grow, {stats.age} age, {stats.show} show")
    if isinstance(plant, Tree):
        tree_stats = plant.stats
        print(f" {tree_stats.produce_shade} shade")


def main() -> None:
    print("=== Garden statistics ===")

    print("=== Check year-old")
    Plant.is_older_than_a_year(30)
    Plant.is_older_than_a_year(400)
    print("")

    print("=== Flower")
    rose = Flower("Rose", 15.0, 10, "red")
    rose.show()
    print("[statistics for Rose]")
    display_stats(rose)
    print("[asking the rose to grow and bloom]")
    rose.grow(8)
    rose.bloom()
    rose.show()
    print("[statistics for Rose]")
    display_stats(rose)
    print("")

    print("=== Tree")
    oak = Tree("Oak", 200.0, 365, 5.0)
    oak.show()
    print("[statistics for Oak]")
    display_stats(oak)
    print("[asking the oak to produce shade]")
    oak.produce_shade()
    print("[statistics for Oak]")
    display_stats(oak)
    print("")

    print("=== Seed")
    sunflower = Seed("Sunflower", 80.0, 45, "yellow")
    sunflower.show()
    print("[make sunflower grow, age and bloom]")
    sunflower.grow(30)
    sunflower.age(20)
    sunflower.bloom()
    sunflower.show()
    print("[statistics for Sunflower]")
    display_stats(sunflower)
    print("")

    print("=== Anonymous")
    unknown = Plant.anonymous()
    unknown.show()
    print("[statistics for Unknown plant]")
    display_stats(unknown)


if __name__ == "__main__":
    main()
