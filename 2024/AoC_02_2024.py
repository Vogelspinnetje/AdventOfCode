def check_report(invoer: list[int]) -> bool:
    if sorted(invoer) not in [invoer, invoer[::-1]]:
            return False

    for huidige, volgende in zip(invoer, invoer[1:]):
        if abs(huidige - volgende) <= 0 or abs(huidige - volgende) > 3:
             return False

    return True


def AoC_02_2024(datastream: list[list[int]]) -> tuple[int, int]:
    goede_reports: int = 0
    goede_reports2: int = 0

    for reports in datastream:
        if check_report(reports):
             goede_reports += 1

        for codes in range(len(reports)):
            if check_report(reports[:codes]+reports[codes+1:]):
                goede_reports2 += 1
                break

    return goede_reports, goede_reports2


if __name__ == "__main__":
    invoer: list[list[int]] = []
    with open("2024/AoC_02_2024.txt", "r") as fh:
        for line in fh:
            invoer.append([int(item) for item in line.strip().split(" ")])
    
    print(AoC_02_2024(invoer))