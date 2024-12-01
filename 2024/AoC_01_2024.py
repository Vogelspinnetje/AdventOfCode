def AoC_01_2024(datastream1, datastream2) -> tuple[int,int]:
    datastream1.sort()
    datastream2.sort()

    antwoord = 0
    gelijkenis = 0

    for i in range(len(datastream1)):
        antwoord += abs(datastream1[i] - datastream2[i])
        gelijkenis += datastream2.count(datastream1[i]) * datastream1[i]

    return antwoord,gelijkenis

if __name__ == "__main__":
    invoerL = []
    invoerR = []
    with open("AoC_01_2024.txt", "r") as fh:
        for regels in fh:
            invoerL.append(int(regels.split("   ")[0].strip()))
            invoerR.append(int(regels.split("   ")[1].strip()))

    print(AoC_01_2024(invoerL, invoerR))