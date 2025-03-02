def AoC_02_2023(datastream: list[str]) -> tuple[int,int]:
    aantal_cubes = {"red": 12, "green": 13, "blue": 14}
    goede_ids = 0
    power_minimum_cubes = 0

    for potjes in datastream:
        fout_potje = False
        game_id = int(potjes.split(":")[0][5:])
        alle_hints = potjes.split(":")[1][1:].split("; ")
        minimum_cubes = {"red": 0, "green": 0, "blue": 0}

        for trekkingen in alle_hints:
            kubussen = trekkingen.split(", ")

            for kubus in kubussen:
                aantal_vs_kleur = kubus.split(" ")
                if aantal_cubes[aantal_vs_kleur[1]] < int(aantal_vs_kleur[0]):
                    fout_potje = True
                minimum_cubes[aantal_vs_kleur[1]] = max(minimum_cubes[
                                                            aantal_vs_kleur[
                                                                1]],
                                                        int(aantal_vs_kleur[
                                                                0]))

        power_minimum_cubes += (minimum_cubes["blue"] * minimum_cubes["red"]
                                * minimum_cubes["green"])

        if not fout_potje:
            goede_ids += game_id

    return goede_ids, power_minimum_cubes

if __name__ == "__main__":
    invoer = []
    with open("AoC_02_2023.txt", "r") as fh:
        for lines in fh:
            invoer.append(lines.strip())

    print(AoC_02_2023(invoer))