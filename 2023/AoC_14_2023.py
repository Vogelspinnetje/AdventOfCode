def AoC_14_2023(datastream: list[list[str]]) -> tuple[0, 0]:
    antwoord1 = 0

    for rijen in range(1, len(datastream)):
        for plekken in range(len(datastream[rijen])):
            if datastream[rijen][plekken] == "O":
                for rolrijen in range(rijen-1, -1, -1):
                    if datastream[rolrijen][plekken] != ".":
                        break
                    datastream[rolrijen+1][plekken] = "."
                    datastream[rolrijen][plekken] = "O"

    for rij_nummers, rijen in enumerate(datastream):
        antwoord1 += rijen.count("O") * (len(datastream)-rij_nummers)


    return antwoord1,0


if __name__ == "__main__":
    invoer = []
    with open("AoC_14_2023.txt", "r") as fh:
        for lines in fh:
            invoer.append(list(lines.strip()))

    print(AoC_14_2023(invoer))