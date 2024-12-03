import re

def AoC_03_2024(datastream: list) -> tuple[0, 0]:
    antwoord: int = 0

    for regels in datastream:
        sommen: list = re.findall(r"mul\(\d{1,3},\d{1,3}\)", "".join(regels))

        for som in sommen:
            getallen = re.findall(r"\d{1,3}", som)
            antwoord += int(getallen[0]) * int(getallen[1])

    return antwoord,0


if __name__ == "__main__":
    with open("2024/AoC_03_2024.txt", "r") as fh:
        invoer: list[list[str]] = [lines for lines in fh]

    print(AoC_03_2024(invoer))