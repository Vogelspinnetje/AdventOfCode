def AoC_09_2015(datastream: list[list[str]]) -> tuple[int,int]:
    korste_route = float("inf")

    for startpunt in datastream:
        

    return 0, 0

if __name__ == "__main__":
    afstanden = []
    with open("AoC_09_2015.txt", "r") as fh:
        for data in fh:
            data = data.strip()
            data = data.split(" ")
            afstanden.append([data[0], data[2], data[-1]])
    print(afstanden)
    print(AoC_09_2015(afstanden))