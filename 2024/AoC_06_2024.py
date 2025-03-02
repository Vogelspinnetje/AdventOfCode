def zoek_startpositie(datastream: list[list[str]]) -> list[int]:
    for y, regels in enumerate(datastream):
        if "^" not in regels:
            continue

        x = regels.index("^")
        return x, y
    
    raise Exception("Geen ^ teken gevonden")


def AoC_06_2024(datastream: list[list[str]]) -> tuple[int, int]:
    antwoord1: int = 0
    antwoord2: int = 0

    x: int
    y: int
    x, y = zoek_startpositie(datastream)
    richting: str = "U" # opties: U=up, R=right, L=left, D=down
    stap_per_richting: dict = {"U": [0,-1], "R": [1,0], "L": [-1,0], "D": [0,1],}

    while 0 <= x < len(datastream[0])-1 and 0 <= y < len(datastream)-1:
        if richting == "U" and datastream[y-1][x] == "#":
            richting = "R"
        elif richting == "R" and datastream[y][x+1] == "#":
            richting = "D"
        elif richting == "D" and datastream[y+1][x] == "#":
            richting = "L"
        elif richting == "L" and datastream[y][x-1] == "#":
            richting = "U"
            
        
        x += stap_per_richting[richting][0]
        y += stap_per_richting[richting][1]

        if datastream[y][x] != "V":
            datastream[y][x] = "V"
            antwoord1 += 1

    return antwoord1,antwoord2


if __name__ == "__main__":
    with open("2024/AoC_06_2024.txt", "r") as fh:
        invoer: list[list[str]] = [list(regels.strip()) for regels in fh]

    print(AoC_06_2024(invoer))