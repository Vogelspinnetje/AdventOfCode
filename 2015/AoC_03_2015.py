def AoC_03_2015(datastream: str) -> tuple[int, int]:
    directies = {"^": [0,1], ">": [1,0], "v": [0,-1], "<": [-1,0]}

    huizen_in_duo = [[1,1]]
    laatste_bezorging_santa = [[1,1]]
    laatste_bezorging_robo = [[1,1]]
    for x, bezorgingen in enumerate(datastream):
        if x % 2 == 1:
            nieuwe_x = laatste_bezorging_santa[-1][0] + directies[bezorgingen][0]
            nieuwe_y = laatste_bezorging_santa[-1][1] + directies[bezorgingen][1]
            laatste_bezorging_santa.append([nieuwe_x, nieuwe_y])
        else:
            nieuwe_x = laatste_bezorging_robo[-1][0] + directies[bezorgingen][
                0]
            nieuwe_y = laatste_bezorging_robo[-1][1] + directies[bezorgingen][
                1]
            laatste_bezorging_robo.append([nieuwe_x, nieuwe_y])

        if [nieuwe_x, nieuwe_y] in huizen_in_duo:
            continue
        huizen_in_duo.append([nieuwe_x, nieuwe_y])

    huizen = [[1, 1]]
    laatste_bezorging = [[1, 1]]
    for bezorgingen in datastream:
        nieuwe_x = laatste_bezorging[-1][0] + directies[bezorgingen][0]
        nieuwe_y = laatste_bezorging[-1][1] + directies[bezorgingen][1]
        laatste_bezorging.append([nieuwe_x, nieuwe_y])
        if [nieuwe_x, nieuwe_y] in huizen:
            continue
        huizen.append([nieuwe_x, nieuwe_y])

    return len(huizen),len(huizen_in_duo)


if __name__ == "__main__":
    with open("AoC_03_2015.txt", "r") as fh:
        route = fh.read().strip()

    print(AoC_03_2015(route))