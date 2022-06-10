from Classes.Vector3 import Vector3
from Classes.RectangularCoordinates import RectangularCoordinates


def main():
    print(f"Coordinates test:")
    r = RectangularCoordinates(1)
    print(r)
    r = RectangularCoordinates(1, 2)
    print(r)
    r = RectangularCoordinates(1, 2, 3)
    print(r)
    r = RectangularCoordinates()
    print(r)
    # r = RectangularCoordinates(1, 2, 3, 4)
    # print(r)
    print()

    print(f"Vector test:")
    v = Vector3(1)
    print(v)
    v = Vector3(1, 2)
    print(v)
    v = Vector3(1, 2, 3)
    print(v)
    v = Vector3()
    print(v)
    print()

    a = Vector3(1, 2, 3)
    b = Vector3(4, 5, 6)

    print(a + b)  # (5, 7, 9)
    print(a * b)  # 4 + 10 + 18 = 32
    print(a.length)  # sqrt(1 + 4 + 9) = sqrt(14)
    print(b.length)  # sqrt(16 + 25 + 36) = sqrt(77)
    print(type(b.length))


if __name__ == '__main__':
    main()
