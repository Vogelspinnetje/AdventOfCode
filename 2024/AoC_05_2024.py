def data_verwerken(datastream: list[str]) -> tuple[list[int], list[list[int]]]:
    """
    Functie om de data te verwerken in twee losse lijsten.
    """
    volgorde: list[list[str]] = []
    updates: list[list[str]] = []

    switch_naar_updates: bool = False

    for regels in datastream:
        if regels == "":
            switch_naar_updates = True
        elif switch_naar_updates:
            updates.append(list(map(int, regels.split(","))))
        else:
            gesplitte_waardes = regels.split("|")
            volgorde.append(list((map(int, gesplitte_waardes))))

    return volgorde, updates


def is_gesorteerd(volgorde, update):
    """
    Kijkt of de updatelijst gesoorteerd is aan de hand van de volgorde lijst
    """
    kloppend: bool = True
    for eerst, laatst in volgorde:
        if eerst not in update or laatst not in update:
            continue
        
        if update.index(eerst) > update.index(laatst):
            kloppend = False
            break
        
    return kloppend


def sorteer(volgorde, update):
    """
    Sorteert de update lijst aan de hand van de bepaalde volgorde. Moet in meeste gevallen meerdere keren worden uitgevoerd.
    """
    for eerst, laatst in volgorde:
        if eerst not in update or laatst not in update:
            continue
        
        if update.index(eerst) > update.index(laatst):
            wissel = update[update.index(eerst)]
            update[update.index(eerst)] = update[update.index(laatst)]
            update[update.index(laatst)] = wissel
    return update


def AoC_05_2024(datastream: list[str]) -> tuple[int, int]:
    antwoord1: int = 0
    antwoord2: int = 0

    volgorde: list[list[int]]
    updates: list[list[int]]
    volgorde, updates = data_verwerken(datastream)
    
    for update in updates:
        if is_gesorteerd(volgorde, update):
            antwoord1 += update[len(update) // 2]
        else:
            while not is_gesorteerd(volgorde, update):
                update = sorteer(volgorde, update)
            
            antwoord2 += update[len(update) // 2]
        

    return antwoord1,antwoord2


if __name__ == "__main__":
    with open("2024/AoC_05_2024.txt", "r") as fh:
        invoer: list[str] = [regels.strip() for regels in fh]

    print(AoC_05_2024(invoer))