"""
Mathematics to Python: PEMDAS exercises
Completed version with solutions.
"""


def main():
    # 1. Calculate: 15 + 4 × 6
    print("1.", 15 + 4 * 6)

    # 2. Calculate: (15 + 4) × 6
    print("2.", (15 + 4) * 6)

    # 3. Calculate: (48 - 12) / (3 + 3)
    print("3.", (48 - 12) / (3 + 3))

    # 4. Calculate: 2 to the power of 4, plus 3 to the power of 2
    print("4.", 2**4 + 3**2)

    # 5. Calculate: 100 - 5 × (8 + 2)
    print("5.", 100 - 5 * (8 + 2))

    # 6. Is 12 + 8 equal to 4 × 5?
    print("6.", 12 + 8 == 4 * 5)

    # 7. Is 7 × (3 + 5) greater than 50?
    print("7.", 7 * (3 + 5) > 50)

    # 8. Is 35 + 4 × 6 divisible by 3 without a remainder?
    print("8.", (35 + 4 * 6) % 3 == 0)

    # 9. Calculate: ((18 + 6) × 2) / 4
    print("9.", (18 + 6) * 2 / 4)

    # 10. Is 2 to the power of 3, plus 4 to the power of 2,
    #     equal to 5 × 5?
    print("10.", 2**3 + 4**2 == 5 * 5)


if __name__ == "__main__":
    main()