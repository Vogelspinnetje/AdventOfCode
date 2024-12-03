import re

def AoC_12_2015(datastream: list[str]) -> tuple[int, int]:
    antwoord: int = 0

    getallen: list[str] = re.findall(r"-*\d{1,}", datastream)

    for getal in getallen:
        antwoord += int(getal)


    return antwoord,0 


if __name__ == "__main__":
    with open("2015/AoC_12_2015.txt", "r") as fh:
        invoer: list[str] = fh.read().strip()

    print(AoC_12_2015(invoer))