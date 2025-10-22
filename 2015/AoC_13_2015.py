from itertools import permutations
from math import inf

def extract(data: list[str]) -> dict:
    relations: dict = {}
    
    for scores in data:
        splitted: list[str] = scores.split(" ")
        happines_points: int = int(splitted[3])
        if splitted[2] == "lose":
            happines_points = -happines_points
        
        if splitted[0] not in relations.keys():
            relations[splitted[0]] = {}
            
        relations[splitted[0]][splitted[-1][:-1]] = happines_points
    
    return relations


def calculate_relation(relations:dict) -> int:
    ans: int = -inf
    
    for path in permutations(relations.keys()):
        total_points: int = 0
        for person in range(len(path)):
            if person < len(path)-1:
                total_points += relations[path[person]][path[person+1]]
            else:
                total_points += relations[path[person]][path[0]]
                
            if person > 0:
                total_points += relations[path[person]][path[person-1]]
            else:
                total_points += relations[path[person]][path[-1]]


        ans = max(ans, total_points)
        
    return ans

def AoC_13_2015(datastream: list[str]) -> tuple[int, int]:
    antwoord1: int = 0
    antwoord2: int = 0

    relations = extract(datastream)
    antwoord1 = calculate_relation(relations)
    
    relations["you"] = {}
    
    for person in relations.keys():
        relations[person]["you"] = 0
        relations["you"][person] = 0
        
    antwoord2 = calculate_relation(relations)
        
    return antwoord1,antwoord2

if __name__ == "__main__":
    with open("2015/AoC_13_2015.txt", "r") as fh:
        invoer: list[str] = [regels.strip() for regels in fh]

    print(AoC_13_2015(invoer))