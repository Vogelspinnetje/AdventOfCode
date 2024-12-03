import re

def AoC_03_2024(datastream: list) -> tuple[0, 0]:
    antwoord: int = 0
    antwoord2: int = 0

    for regels in datastream:
        sommen: list = re.findall(r"mul\(\d{1,3},\d{1,3}\)", "".join(regels))
        sommen_pos: list = re.finditer(r"mul\(\d{1,3},\d{1,3}\)", "".join(regels))
        deadzone_zoeken: list = re.finditer(r"don\'t\(\).{1,}?do\(\)", regels)
        deadzone: list = [[int(zones.start()), int(zones.end())] for zones in deadzone_zoeken]
        print(deadzone)

        for som, pos in zip(sommen, sommen_pos):
            start_pos: int = int(pos.start())
            mag_rekenen: bool = True

            for zones in deadzone:
                print(f"Controleer zone: {zones} met start_pos: {start_pos}")
                if zones[0] < start_pos < zones[1]:
                    print(f"start_pos {start_pos} valt in zone {zones}")
                    mag_rekenen = False
                    break


            getallen = re.findall(r"\d{1,3}", som)
            antwoord += int(getallen[0]) * int(getallen[1])
            if mag_rekenen:
                antwoord2 += int(getallen[0]) * int(getallen[1])
            break

    return antwoord,antwoord2


if __name__ == "__main__":
    with open("2024/AoC_03_2024.txt", "r") as fh:
        invoer: list[list[str]] = [lines for lines in fh]

    print(AoC_03_2024(invoer))