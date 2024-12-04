def AoC_04_2024(datastream: list[list[str]]) -> tuple[int, int]:
    antwoord: int = 0
    antwoord2: int = 0

    # Deel 1
    for y, rij in enumerate(datastream):
        for x, kolom in enumerate(rij):
            if kolom != "X":
                continue

            # Horizontaal
            if x <= len(rij) - 4 and rij[x+1] == "M" and rij[x+2] == "A" and rij[x+3] == "S":
                antwoord += 1
            if x >= 3 and rij[x-1] == "M" and rij[x-2] == "A" and rij[x-3] == "S":
                antwoord += 1

            # Verticaal
            if y <= len(datastream) - 4 and datastream[y+1][x] == "M" and datastream[y+2][x] == "A" and datastream[y+3][x] == "S":
                antwoord += 1
            if y >= 3 and datastream[y-1][x] == "M" and datastream[y-2][x] == "A" and datastream[y-3][x] == "S":
                antwoord += 1
            
            # Diagonaal
            if x >= 3 and y >= 3 and datastream[y-1][x-1] == "M" and datastream[y-2][x-2] == "A" and datastream[y-3][x-3] == "S":
                antwoord += 1
            if x <= len(rij) - 4 and y >= 3 and datastream[y-1][x+1] == "M" and datastream[y-2][x+2] == "A" and datastream[y-3][x+3] == "S":
                antwoord += 1
            if x <= len(rij) - 4 and y <= len(datastream) - 4 and datastream[y+1][x+1] == "M" and datastream[y+2][x+2] == "A" and datastream[y+3][x+3] == "S":
                antwoord += 1
            if x >= 3 and y <= len(datastream) - 4 and datastream[y+1][x-1] == "M" and datastream[y+2][x-2] == "A" and datastream[y+3][x-3] == "S":
                antwoord += 1

    # Deel 2
    for y, rij in enumerate(datastream):
        x_mas: dict = {"M": "S", "S": "M", "X": "_", "A": "_"}

        for x, kolom in enumerate(rij):
            if kolom != "A":
                continue

            if  1 <= x <= len(rij) - 2 and 1 <= y <= len(datastream) -2 and x_mas[datastream[y-1][x-1]] == datastream[y+1][x+1] and x_mas[datastream[y+1][x-1]] == datastream[y-1][x+1]:
                antwoord2 += 1

    return antwoord, antwoord2


if __name__ == "__main__":
    with open("2024/AoC_04_2024.txt", "r") as fh:
        invoer: list[list[str]] = [list(regels.strip()) for regels in fh]

    print(AoC_04_2024(invoer))