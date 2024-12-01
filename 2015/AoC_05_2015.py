def AoC_05_2015(datastream: list[str]) -> tuple[int, int]:
    klinkers = "aeiou"
    stomme_combinaties = ["ab", "cd", "pq", "xy"]
    leuke_strings = 0
    nieuwe_leuke_strings = 0

    for regels in datastream:
        voorwaarden = [False, False, 0]
        voorwaarden_nieuw = [False, False]
        stapel_letters = []
        aantal_klinkers = 0

        for letters in regels:
            #klinkers
            if letters in klinkers:
                aantal_klinkers += 1
                if aantal_klinkers == 3:
                    voorwaarden[0] = True

            #twee letters op rij
            if len(stapel_letters) > 0 and stapel_letters[-1] == letters:
                voorwaarden[1] = True

            #stoute combi's
            if len(stapel_letters) > 0 and stapel_letters[-1] + letters in stomme_combinaties:
                voorwaarden[2] = -1
            ##################################################################################################
            #paartjes
            for items in range(len(stapel_letters) - 2):
                if ("".join(stapel_letters[items:items+2]) == stapel_letters[-1] +
                        letters):
                    print("".join(stapel_letters[items:items+2]))
                    print(stapel_letters[-1] + letters)
                    voorwaarden_nieuw[0] = True

            #paar met een letter er tussen: oMo
            if len(stapel_letters) > 1 and stapel_letters[-2] == letters:
                voorwaarden_nieuw[1] = True

            stapel_letters.append(letters)

        if voorwaarden[0] and voorwaarden[1] and voorwaarden[2] == 0:
            leuke_strings += 1
        if voorwaarden_nieuw[0] and voorwaarden_nieuw[1]:
            print(regels)
            nieuwe_leuke_strings += 1


    return leuke_strings, nieuwe_leuke_strings


if __name__ == "__main__":
    with open("AoC_05_2015.txt", "r") as fh:
        stringetjes = fh.read().strip().split("\n")

    print(AoC_05_2015(stringetjes))
