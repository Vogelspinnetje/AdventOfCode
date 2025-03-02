def AoC_01_2015(datastream: str) -> tuple[int, int]:
    verdieping = 0
    karakter_van_kelder = 0

    for x, stappen in enumerate(datastream):
        if stappen == "(":
            verdieping += 1
        else:
            verdieping -= 1

        if verdieping < 0 and karakter_van_kelder == 0:
            karakter_van_kelder = x + 1


    return verdieping, karakter_van_kelder


if __name__ == "__main__":
    with open("AoC_01_2015.txt", "r") as fh:
        instructies = fh.readline().strip()

    print(AoC_01_2015(instructies))
