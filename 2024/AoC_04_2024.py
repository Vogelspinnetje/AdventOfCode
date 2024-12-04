import re

def AoC_04_2024(datastream: list) -> tuple[int, int]:
    return 0,0


if __name__ == "__main__":
    with open("AoC_04_2024.txt", "r") as fh:
        invoer = [regels.strip() for regels in fh]

    print(AoC_04_2024(invoer))