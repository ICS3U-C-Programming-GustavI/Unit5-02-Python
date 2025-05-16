#!/usr/bin/env python3
# Created by: Gustav I
# Created on: May 12, 2025
# This calculates the area of a triangle.


def calc_area(base, height):
    area = 0.5 * base * height
    print(f"\nThe area of the triangle is {area:.2f} cm²")


def main():
    try:
        base = float(input("Enter the base of the triangle (cm): "))
        height = float(input("Enter the height of the triangle (cm): "))

        if base <= 0 or height <= 0:
            print("Error: Base and height must be positive numbers.")
        else:
            calc_area(base, height)
    except ValueError:
        print("Error: Invalid input. Please enter a numeric value.")


# Run the main function
main()
