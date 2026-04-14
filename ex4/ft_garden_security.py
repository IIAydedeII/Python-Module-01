class Plant:
    def __init__(self, name: str, height: float, age: int):
        self.name = name
        self._height = 0.0
        self._age = 0

        if not self._is_negative(height, "height"):
            self._height = height
        if not self._is_negative(age, "age"):
            self._age = age

        print(f"Plant created: {self}")

    def __str__(self) -> str:
        return f"{self.name}: {round(self._height, 1)}cm, {self._age} days old"

    def get_height(self) -> float:
        return self._height

    def set_height(self, height: float) -> None:
        if self._is_negative(height, "height"):
            print("Height update rejected")
        else:
            self._height = height
            print(f"Height updated: {round(self._height)}cm")

    def get_age(self) -> int:
        return self._age

    def set_age(self, age: int) -> None:
        if self._is_negative(age, "age"):
            print("Age update rejected")
        else:
            self._age = age
            print(f"Age updated: {self._age} days")

    def _is_negative(self, value: int | float, field_name: str) -> bool:
        if value < 0:
            print(f"{self.name}: Error, {field_name} can't be negative")
            return True
        return False


def main() -> None:
    print("=== Garden Security System ===")

    plant = Plant("Rose", 15.0, 10)
    print("")
    plant.set_height(25)
    plant.set_age(30)
    print("")
    plant.set_height(-5)
    plant.set_age(-10)
    print("")
    print(f"Current state: {plant}")


if __name__ == "__main__":
    main()
