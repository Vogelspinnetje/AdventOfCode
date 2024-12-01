def AoC_15_2023(datastream: list[str]) -> int:
    antwoord = 0

    for sequenties in datastream:
        waarde = 0
        for karakters in sequenties:
            waarde += ord(karakters)
            waarde = waarde * 17
            waarde = waarde % 256
        antwoord += waarde

    return antwoord


if __name__ == "__main__":
    with open("AoC_15_2023.txt","r") as fh:
        invoer = [items.strip().split(",") for items in fh]

    print(AoC_15_2023(invoer[0]))