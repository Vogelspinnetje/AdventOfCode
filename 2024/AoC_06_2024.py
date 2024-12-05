def AoC_06_2024(datastream: list[str]) -> tuple[int, int]:
    antwoord1: int = 0
    antwoord2: int = 0

    return antwoord1,antwoord2


if __name__ == "__main__":
    with open("2024/AoC_06_2024.txt", "r") as fh:
        invoer: list[str] = [regels.strip() for regels in fh]

    print(AoC_06_2024(invoer))