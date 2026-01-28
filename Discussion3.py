import math

class Rectangle():
    def __init__(self, width, height):
        self.width = width
        self.height = height


    def __str__(self):
        return f"A rectangle with width {self.width} and height {self.height}"


    def area_calculator(self):
        return self.width * self.height


    def __eq__(self, other):
        if isinstance(other, Rectangle):
            return self.width == other.width and self.height == other.height
        return False


def main():
    r1 = Rectangle(10, 10)
    # call the __str__ method
    print("r1:", r1)
    # call the area_calculator method
    print("Area:", r1.area_calculator())


    r2 = Rectangle(10, 15)
    print("r2:", r2)
    print("Area:", r2.area_calculator())
    # call the __eq__ method
    print("Equal: r1 == r2?", r1 == r2)
    print()

    r3 = Rectangle(10, 15)
    print("r3:", r3)
    print("Area:", r3.area_calculator())
    print("Equal: r2 == r3?", r2 == r3)

if __name__ == "__main__":
    main()