import re

def AoC_03_2024(datastream: list) -> tuple[0, 0]:
    antwoord: int = 0
    antwoord2: int = 0

    stoppen: bool = False

    for regels in datastream:
        sommen: list = re.findall(r"mul\(\d{1,3},\d{1,3}\)|don\'t\(\)|do\(\)", "".join(regels))
        for som in sommen:
            if som == "don\'t()":
                print("---"*20)
                stoppen = True
                continue
            
            elif som == "do()":
                print("***"*20)
                stoppen = False
                continue
            
            
            getallen: list[str] = re.findall(r"\d{1,3}", som)
            antwoord += int(getallen[0]) * int(getallen[1])
            
            if not stoppen:
                antwoord2 += int(getallen[0]) * int(getallen[1])

    return antwoord, antwoord2


if __name__ == "__main__":
    with open("2024/AoC_03_2024.txt", "r") as fh:
        invoer: list[list[str]] = [lines for lines in fh]

    print(AoC_03_2024(invoer))