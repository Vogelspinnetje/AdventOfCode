def AoC_01_2023(datastream: list[str]) -> tuple[int,int]:
    totaal_waarde1 = 0
    totaal_waarde2 = 0
    getallen_conversie = {"zero": "0", "one": "1", "two": "2", "three": "3", "four":
        "4", "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9"}
    for lines in datastream:
        waardes_in_line = []
        waardes_in_line2 = []
        karakter_ensemble = []
        for karakters in lines:
            if karakters.isdigit():
                waardes_in_line.append(karakters)
                waardes_in_line2.append(karakters)
                continue
            karakter_ensemble.append(karakters)
            for getallen in getallen_conversie:
                if getallen in "".join(karakter_ensemble):
                    waardes_in_line2.append(getallen_conversie[getallen])
                    karakter_ensemble = [karakter_ensemble[-1]]

        totaal_waarde1 += int(waardes_in_line[0]+waardes_in_line[-1])
        totaal_waarde2 += int(waardes_in_line2[0]+waardes_in_line2[-1])

    return totaal_waarde1, totaal_waarde2

if __name__ == "__main__":
    with open("AoC_01_2023.txt", "r") as fh:
        invoer = fh.readlines()

    print(AoC_01_2023(invoer))