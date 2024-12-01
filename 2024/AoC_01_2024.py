def AoC_01_2024(datastreamL: list[int], datastreamR: list[int]) -> tuple[int,int]:
    datastreamL.sort()
    datastreamR.sort()

    antwoord1: int = 0
    antwoord2: int = 0

    for i in range(len(datastreamL)):
        antwoord1 += abs(datastreamL[i] - datastreamR[i])
        antwoord2 += datastreamR.count(datastreamL[i]) * datastreamL[i]

    return antwoord1, antwoord2

if __name__ == "__main__":
    invoerL: list[int] = []
    invoerR: list[int] = []

    with open("AoC_01_2024.txt", "r") as fh:
        for regels in fh:
            invoerL.append(int(regels.split("   ")[0].strip()))
            invoerR.append(int(regels.split("   ")[1].strip()))

    print(AoC_01_2024(invoerL, invoerR))