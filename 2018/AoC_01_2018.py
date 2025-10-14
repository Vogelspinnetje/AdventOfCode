def AoC_01_2018(datastream: list[str]) -> tuple[int, int]:
    antwoord1: int = 0
    antwoord2: int = 0

    for instructions in datastream:
        antwoord1 += int(instructions)
    
    frequency = 0
    seen = set()
    seen.add(frequency)
    
    while antwoord2 == 0:
        for instructions in datastream:
            frequency += int(instructions)
            if frequency in seen:
                antwoord2 = frequency
                break
            seen.add(frequency)
    
    return antwoord1,antwoord2

if __name__ == "__main__":
    with open("2018/AoC_01_2018.txt", "r") as fh:
        invoer: list[str] = [regels.strip() for regels in fh]

    print(AoC_01_2018(invoer))