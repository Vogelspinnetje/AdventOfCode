from datetime import datetime
import re

def extract_datetime(line):
    timestamp = re.findall(r"\d{4}-\d{2}-\d{2} \d{2}:\d{2}", line)
    return datetime.strptime(timestamp[0], "%Y-%m-%d %H:%M")

 
def AoC_04_2018(datastream: list[str]) -> tuple[int, int]:
    antwoord1: int = 0
    antwoord2: int = 0

    sorted_lines = sorted(datastream, key=extract_datetime)

    for line in sorted_lines:
        print(line)

    return antwoord1,antwoord2

if __name__ == "__main__":
    with open("2018/AoC_04_2018.txt", "r") as fh:
        invoer: list[str] = [regels.strip() for regels in fh]

    print(AoC_04_2018(invoer))