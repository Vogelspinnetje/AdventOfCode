def AoC_01_2024(datasteam) -> tuple[int,int]:
    return 0,0

if __name__ == "__main__":
    with open("AoC_01_2024.txt", "r") as fh:
        invoer = [regel.strip() for regel in fh]

    print(AoC_01_2024(invoer))