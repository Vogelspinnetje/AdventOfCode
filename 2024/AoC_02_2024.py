def AoC_02_2024(datastream: list[list[int]]) -> tuple[int, int]:
    foute_reports: int = 0

    for reports in datastream:
        oplopend: bool = True if reports[0] < reports[-1] else False
        for positie, code in enumerate(reports):
            if positie == 0:
                continue
            
            verschil: int = abs(code - reports[positie-1])
            if oplopend and code < reports[positie-1]:
                foute_reports += 1
                break
            
            if not oplopend and code > reports[positie-1]:
                foute_reports += 1
                break

            if verschil == 0 or verschil > 3:
                foute_reports += 1
                break
    
    goede_reports: int = len(datastream) - foute_reports

    return goede_reports, 0


if __name__ == "__main__":
    invoer: list[list[int]] = []
    with open("2024/AoC_02_2024.txt", "r") as fh:
        for line in fh:
            invoer.append([int(item) for item in line.strip().split(" ")])
    
    print(AoC_02_2024(invoer))