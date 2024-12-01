def AoC_02_2015(datastream: list[list[int]]) -> tuple[int, int]:
    totale_pakpapier = 0
    totale_lint = 0

    for pakjes in datastream:
        l,b,h = pakjes
        pakpapier = (2*l*b) + (2*b*h) + (2*l*h) + min(l*b, l*h, b*h)
        totale_pakpapier += pakpapier
        afmetingen_gesorteerd = sorted(pakjes)
        totale_lint += (2*afmetingen_gesorteerd[0]) + (
                2*afmetingen_gesorteerd[1]) + (l*b*h)

    return totale_pakpapier, totale_lint


if __name__ == "__main__":
    verlanglijstje = []
    with open("AoC_02_2015.txt", "r") as fh:
        for cadeautjes in fh.read().split("\n"):
            waardes = cadeautjes.split("x")
            waardes = [int(i) for i in waardes]
            verlanglijstje.append(waardes)

    print(AoC_02_2015(verlanglijstje))