def AoC_06_2015(datastream: list[list[str]]) -> tuple[int,int]:
    grid = [[0]*1000 for _ in range(1000)]

    for instructie in datastream:
        actie = "".join(instructie[0].split(" ")[:-2])
        coordinaten_begin = instructie[0].split(" ")[-2]
        coordinaten_eind = instructie[1]
        start_x, start_y = map(int, coordinaten_begin.split(','))
        end_x, end_y = map(int, coordinaten_eind.split(','))
        for x in range(start_x, end_x + 1):
            for y in range(start_y, end_y + 1):
                if actie == "turnon":
                    grid[x][y] += 1
                elif actie == "turnoff":
                    grid[x][y] = max(0, grid[x][y] - 1)
                elif actie == "toggle":
                    grid[x][y] += 2

    return 0,sum([sum(row) for row in grid])

if __name__ == "__main__":
    with open("AoC_06_2015.txt", "r") as fh:
        instructies = []
        for regels in fh.readlines():
            instructies.append(regels.split("through"))
            instructies[-1][-1] = instructies[-1][-1].strip()

    print(AoC_06_2015(instructies))