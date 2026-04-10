class Plant:
    name = ""
    height = 0.0
    _age = 0

    def grow(self, growth: float) -> None:
        self.height += growth

    def age(self) -> None:
        self._age += 1

    def show(self) -> None:
        print(f"{self.name}: {round(self.height, 1)}cm, {self._age} days old")


def main() -> None:
    rose = Plant()
    rose.name = "Rose"
    rose.height = 25.0
    rose._age = 30

    initial_height = rose.height
    print("=== Garden Plant Growth ===")
    rose.show()
    for day in range(7):
        print(f"=== Day {day + 1} ===")
        rose.grow(0.8)
        rose.age()
        rose.show()
    total_growth = rose.height - initial_height
    print(f"Growth this week: {round(total_growth, 1)}cm")


if __name__ == "__main__":
    main()
