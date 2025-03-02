import re
import json

def AoC_12_2015(datastream: list[str]) -> tuple[int, int]:
    antwoord: int = 0
    antwoord2: int = 0
    getallen: list[str] = re.findall(r"-?\d+", datastream)

    for getal in getallen:
        antwoord += int(getal)

    json_data = str(json.loads(datastream, object_hook=lambda obj: {} if "red" in obj.values() else obj))

    getallen2: list[str] = re.findall(r"-?\d+", json_data)

    for getal in getallen2:
        antwoord2 += int(getal)

    return antwoord, antwoord2


if __name__ == "__main__":
    with open("2015/AoC_12_2015.txt", "r") as fh:
        invoer: list[str] = fh.read().strip()

    print(AoC_12_2015(invoer))