from os import rename


def AoC_14_2015(datastream: list[str], seconden) -> tuple[0,0]:
    rendier_stats = []
    wedstrijd_stand = []
    wedstrijd_stand2 = []

    for regels in datastream:
        rendier_stats.append([])
        wedstrijd_stand.append(0)
        wedstrijd_stand2.append(0)
        for woorden in regels.split(" "):
            if woorden.isdigit():
                rendier_stats[-1].append(int(woorden))
        rendier_stats[-1].append(0) #voor aantal gerende secondes
        rendier_stats[-1].append(rendier_stats[-1][2]) #countdown rust

    for i in range(1,seconden+1):
        for rendier_nummer, rendieren in enumerate(rendier_stats):
            if rendieren[4] == 0:
                rendieren[4] = rendieren[2]
                rendieren[3] = 0

            if rendieren[3] >= rendieren[1]:
                rendieren[4] -= 1
                continue

            rendieren[3] += 1
            wedstrijd_stand[rendier_nummer] += rendieren[0]

        hoogste_punt = max(wedstrijd_stand)
        for rendieren in range(len(wedstrijd_stand)):
            if wedstrijd_stand[rendieren] != hoogste_punt:
                continue
            wedstrijd_stand2[rendieren] += 1

    return max(wedstrijd_stand),max(wedstrijd_stand2)

if __name__ == "__main__":
    with open("AoC_14_2015.txt", "r") as fh:
        invoer = [regel for lines in fh if (regel := lines.strip())]

    print(AoC_14_2015(invoer, 2503))