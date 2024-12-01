def AoC_11_2015(datastream: list[str]) -> str:
    alfabet_list = list("abcdefghijklmnopqrstuvwxyza")
    alfabet = {}
    for items in range(len(alfabet_list)-1):
        alfabet[alfabet_list[items]] = alfabet_list[items+1]

    nieuw_wachtwoord = ""
    requirements = [False, True, False, False]
    aanpas_index = -1

    while not requirements[-1]:
        if datastream[aanpas_index] == "z":
            datastream[aanpas_index] = alfabet[datastream[aanpas_index]]
        else:
            datastream[aanpas_index] = alfabet[datastream[aanpas_index]]

        mogelijk_wachtwoord = "".join(datastream)

        for letters in range(len(alfabet)):
            sequentie = alfabet[letters:letters+3]
            if (len("".join(sequentie)) == 3 and "".join(sequentie) in
                    mogelijk_wachtwoord):
                requirements[0] = True
                break
        for verboden in ["i", "o", "l"]:
            if verboden in mogelijk_wachtwoord:
                requirements[1] = False
                break
        vorige = ""
        aantal_dubbel = 0
        for karakters in datastream:
            if vorige == karakters:
                aantal_dubbel +=1
            if aantal_dubbel == 2:
                requirements[2] = True
                break
            vorige = karakters

        if requirements[:3] == [True, True, True]:
            requirements[-1] = True

    return ""

if __name__ == "__main__":
    with open("AoC_11_2015.txt", "r") as fh:
        invoer = fh.read().strip()

    print(AoC_11_2015(list(invoer)))