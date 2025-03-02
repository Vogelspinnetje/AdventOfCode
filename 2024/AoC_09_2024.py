import re

def id_toewijzen(datastream: str) -> list[str]:
    id_nummer: int = 0
    id_reeks: list[str] = []
    file: bool = True
    
    for getallen in datastream:
        if file:
            for plekken in range(int(getallen)):
                id_reeks.append(str(id_nummer))
            file = False
            id_nummer += 1
        else:
            for plekken in range(int(getallen)):
                id_reeks.append(".")
            file = True
    
    return id_reeks

def AoC_09_2024(datastream: list[str]) -> tuple[int, int]:
    antwoord1: int = 0
    antwoord2: int = 0
    
    id_reeks = id_toewijzen(datastream)
    
    print(id_reeks)
    
    while not re.fullmatch(r"^[0-9]*\.*$", "".join(id_reeks)):
        for plek, id in enumerate(id_reeks):
            if id != ".":
                continue
            
            if re.fullmatch(r"^[0-9]*\.*$", "".join(id_reeks)):
                print("yo")
                break
            
            wissel_plek = -1
            while id_reeks[wissel_plek] == ".":
                wissel_plek -= 1
               
            id_reeks[plek] = id_reeks[wissel_plek]
            id_reeks[wissel_plek] = "."
    
    print(id_reeks)
    
    for punten, id in enumerate(id_reeks):
        if id != ".":
            print(f"Punten/plek: {punten}\nId: {id}")
            antwoord1 += punten * int(id)
                    
    return antwoord1,antwoord2

if __name__ == "__main__":
    with open("2024/AoC_09_2024.txt", "r") as fh:
        invoer: str = fh.readline()

    print(AoC_09_2024(invoer))