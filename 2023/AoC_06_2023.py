def bereken_winsten(datastream: list):
    number_of_ways_total = 1

    for races in range(len(datastream[0])):
        number_of_ways = 0
        for snelheid in range(1, datastream[0][races] + 1):
            afstand = snelheid * (datastream[0][races] - snelheid)
            if afstand > datastream[1][races]:
                number_of_ways += 1

        number_of_ways_total = number_of_ways * number_of_ways_total

    return number_of_ways_total

def AoC_06_2023(datastream: list[str]) -> tuple[int,int]:
    edited_datastream = []
    for lines in datastream:
        waardes = [int(i) for i in lines.strip().split(" ")[1:] if i.strip()]
        edited_datastream.append(waardes)

    edited_datastream2 = [[int("".join([str(i) for i in edited_datastream[0]]))],
                          [int("".join([str(i) for i in edited_datastream[1]]))]]

    return bereken_winsten(edited_datastream),bereken_winsten(edited_datastream2)


if __name__ == "__main__":
    with open("AoC_06_2023.txt", "r") as fh:
        invoer = fh.readlines()

    print(AoC_06_2023(invoer))
