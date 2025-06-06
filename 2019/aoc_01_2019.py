def AoC_01_2019(datastream: list[str]) -> tuple[int, int]:
    antwoord1: int = 0
    antwoord2: int = 0
    
    for masses in datastream:
        antwoord1 += int(int(masses) / 3) - 2
        berekening: int = int(int(masses) / 3) - 2
        while berekening > 0:
            antwoord2 += berekening
            berekening: int = int(berekening / 3) - 2

    return antwoord1,antwoord2

if __name__ == "__main__":
    with open("2019/AoC_01_2019.txt", "r") as fh:
        invoer: list[str] = [regels.strip() for regels in fh]

    print(AoC_01_2019(invoer))