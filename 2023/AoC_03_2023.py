def zoek_getal(datastream: str, richting: str, positie_teken: int) -> str:
    volgende = ""
    getallenreeks = ""

    while volgende != ".":
        getallenreeks += volgende
        if richting == "l":
            volgende = datastream[positie_teken-len(getallenreeks)-1]
        else:
            volgende = datastream[positie_teken+len(getallenreeks)+1]

    print(datastream, getallenreeks)
    if richting == "l":
        return getallenreeks[::-1]
    return getallenreeks


def omranding(datastream: list[str], regel_nummer: int, karakter_nummer:
int):
    ruimte_links = 0 if karakter_nummer == 0 else 1
    ruimte_rechts = 0 if karakter_nummer == len(datastream[regel_nummer]) -1 else 1
    ruimte_boven = 0 if regel_nummer == 0 else 1
    ruimte_onder = 0 if regel_nummer == len(datastream) -1 else 1

    randenL = datastream[regel_nummer][karakter_nummer-ruimte_links]
    randenR = datastream[regel_nummer][karakter_nummer+ruimte_rechts]
    randenB = datastream[regel_nummer-ruimte_boven][karakter_nummer-ruimte_links:karakter_nummer+ruimte_rechts+1]
    randenO = datastream[regel_nummer+ruimte_onder][karakter_nummer-ruimte_links:karakter_nummer+ruimte_rechts+1]

    getal = []
    if randenL.isdigit():
        getal.append(zoek_getal(datastream[regel_nummer], "l",
                                 karakter_nummer))
    if randenR.isdigit():
        getal.append(zoek_getal(datastream[regel_nummer], "r",
                                 karakter_nummer))

    

    return 0

def AoC_03_2023(datastream: list[str]) -> int:
    goede_onderdelen = 0

    for regel_nummer, regels in enumerate(datastream):
        getallenreeks = ""
        for karakters in range(len(regels)):
            if regels[karakters] == "." or regels[karakters].isdigit():
                continue
            getallen = omranding(datastream, regel_nummer, karakters)

    return goede_onderdelen


if __name__ == "__main__":
    invoer = []
    with open("AoC_03_2023.txt", "r") as fh:
        for lines in fh:
            invoer.append(lines.strip())

    print(AoC_03_2023(invoer))