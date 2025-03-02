def AoC_10_2015(datastream: str) -> tuple[int, int]:
    antwoord1 = ""
    for iteraties in range(50):
        if iteraties == 40:
            antwoord1 = len(datastream)
        nieuw = ""
        counter = 0
        datastream += "-"
        for cijfers in range(len(datastream)):
            counter += 1
            if datastream[cijfers] == "-":
                break
            if datastream[cijfers+1] == datastream[cijfers]:
                continue
            else:
                nieuw += str(counter) + datastream[cijfers]
                counter = 0
        datastream = nieuw

    return antwoord1, len(datastream)


if __name__ == "__main__":
    with open("AoC_10_2015.txt", "r") as fh:
        invoer = fh.read().strip()

    print(AoC_10_2015(invoer))
