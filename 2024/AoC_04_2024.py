def AoC_04_2024(datastream: list) -> tuple[int, int]:
    antwoord: int = 0

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

    return antwoord,0


if __name__ == "__main__":
    with open("2024/AoC_04_2024.txt", "r") as fh:
        invoer = [list(regels.strip()) for regels in fh]

    print(AoC_04_2024(invoer))