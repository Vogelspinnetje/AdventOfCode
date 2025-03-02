import math

def lcm_multiple(numbers):
    result = numbers[0]
    for num in numbers[1:]:
        result = math.lcm(result, num)
    return result


def verwerk_data(datastream:list[str]) -> tuple[str,dict]:
    richting = datastream[0].strip()
    routes = {}

    for lines in datastream:
        if len(lines) < 17:
            continue

        routes[lines[:3]] = lines[7:-2].split(", ")

    return richting, routes


def deel2(datastream: dict, richting: str, positie: str) -> int:
    richting_positie = 0
    richting_vertaler = {"R": 1, "L": 0}
    stappen = 0

    while positie[-1] != "Z":
        if richting_positie == len(richting):
            richting_positie = 0

        positie = datastream[positie][richting_vertaler[richting[richting_positie]]]
        richting_positie += 1
        stappen += 1
    return stappen


def AoC_08_2023(datastream:list[str]) -> tuple[int,int]:
    richting, route = verwerk_data(datastream)
    positie = "AAA"
    richting_positie = 0
    richting_vertaler = {"R": 1, "L": 0}
    stappen = 0

    while positie != "ZZZ":
        if richting_positie == len(richting):
            richting_positie = 0

        positie = route[positie][richting_vertaler[richting[richting_positie]]]
        richting_positie += 1
        stappen += 1


    posities = []
    stappen_deel2 = []
    for keys in route:
        if keys[-1] == "A":
            posities.append(keys)
            stappen_deel2.append(deel2(route, richting, posities[-1]))

    return stappen, lcm_multiple(stappen_deel2)


if __name__ == "__main__":
    with open("AoC_08_2023.txt", "r") as fh:
        invoer = fh.readlines()

    print(AoC_08_2023(invoer))