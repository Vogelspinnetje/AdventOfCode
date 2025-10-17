def verwerk_data(datastream: list[str]) -> tuple[int, list[int]]:
    uitkomst = int(datastream.split(":")[0])
    sommen = datastream.split(": ")[1].split(" ")
    sommen = list(map(int, sommen))
    
    return uitkomst, sommen


def AoC_07_2024(datastream: list[str]) -> tuple[int, int]:
    antwoord1: int = 0
    antwoord2: int = 0
    
    for sommen in datastream:
        uitkomst, getallen = verwerk_data(sommen)
        
        def part1(index, acc):
            if index == len(getallen):
                return acc == uitkomst

            n = getallen[index]

            if part1(index + 1, acc + n):
                return True
            if part1(index + 1, acc * n):
                return True

            return False
            
        if part1(1, getallen[0]):
            antwoord1 += uitkomst
            
        def part2(index, acc):
            if index == len(getallen):
                return acc == uitkomst

            n = getallen[index]

            if part2(index + 1, acc + n):
                return True
            if part2(index + 1, acc * n):
                return True
            if part2(index + 1, int(str(acc)+str(n))):
                return True

            return False
        
        if part2(1, getallen[0]):
            antwoord2 += uitkomst

    return antwoord1,antwoord2

if __name__ == "__main__":
    with open("2024/AoC_07_2024.txt", "r") as fh:
        invoer: list[str] = [regels.strip() for regels in fh]

    print(AoC_07_2024(invoer))