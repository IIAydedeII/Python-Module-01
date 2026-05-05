#!/usr/bin/env python3
class Plant:
    name = ""
    height = 0.0
    current_age = 0

    def grow(self, growth: float) -> None:
        self.height += growth

    def age(self, day: int) -> None:
        self.current_age += day

    def show(self) -> None:
        print(
            f"{self.name}:",
            f"{round(self.height, 1)}cm,",
            f"{self.current_age} days old",
        )


def main() -> None:
    rose = Plant()
    rose.name = "Rose"
    rose.height = 25.0
    rose.current_age = 30

    initial_height = rose.height
    print("=== Garden Plant Growth ===")
    rose.show()
    for day in range(7):
        print(f"=== Day {day + 1} ===")
        rose.grow(0.8)
        rose.age(1)
        rose.show()
    total_growth = rose.height - initial_height
    print(f"Growth this week: {round(total_growth, 1)}cm")


if __name__ == "__main__":
    main()
