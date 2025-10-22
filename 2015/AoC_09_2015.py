from itertools import permutations
from math import inf

def extract(data: list[str]) -> dict:
    distances: dict = {}
    
    for routes in data:
        splitted: list[str] = routes.split(" ")
        if splitted[0] not in distances.keys():
            distances[splitted[0]] = {} 
        distances[splitted[0]][splitted[2]] = int(splitted[4])
        
        if splitted[2] not in distances.keys():
            distances[splitted[2]] = {}
        distances[splitted[2]][splitted[0]] = int(splitted[4])
        
    return distances

def AoC_09_2015(datastream: list[str]) -> tuple[int, int]:
    antwoord1: int = inf
    antwoord2: int = 0

    distances = extract(datastream)
    
    for route in permutations(distances.keys()):
        length: int = 0
        for city in range(len(route)-1):
            length += distances[route[city]][route[city+1]]
        
        antwoord1 = min(antwoord1, length)
        antwoord2 = max(antwoord2, length)
    
    return antwoord1,antwoord2

if __name__ == "__main__":
    with open("2015/AoC_09_2015.txt", "r") as fh:
        invoer: list[str] = [regels.strip() for regels in fh]

    print(AoC_09_2015(invoer))