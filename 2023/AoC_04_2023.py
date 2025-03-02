def AoC_04_2024(datastream:list[list[str]]) -> tuple[int, int]:
    aantal_punten = 0
    kaarten_stapel = [1 for _ in datastream]

    for kaarten in datastream:
        aantal_winnende_kaarten = 0
        huidig_kaartnummer = int(kaarten[0][4:])
        winnende_getallen = kaarten[1].split("|")[0].split(" ")
        winnende_getallen = [int(getal) for getal in winnende_getallen if
                             getal.strip()]
        mijn_getallen = kaarten[1].split("|")[1].split(" ")
        mijn_getallen = [int(getal) for getal in mijn_getallen if
                             getal.strip()]

        for getallen in mijn_getallen:
            if getallen in winnende_getallen:
                aantal_winnende_kaarten += 1
        if aantal_winnende_kaarten > 0:
            aantal_punten += 2 ** (aantal_winnende_kaarten-1)

        for winst in range(aantal_winnende_kaarten):
            kaarten_stapel[winst+huidig_kaartnummer] += 1 * kaarten_stapel[
                huidig_kaartnummer-1]

    return aantal_punten,sum(kaarten_stapel)

if __name__ == "__main__":
    invoer = []
    with open("AoC_04_2023.txt", "r") as fh:
        for regels in fh:
            invoer.append(regels.strip().split(":"))

    print(AoC_04_2024(invoer))