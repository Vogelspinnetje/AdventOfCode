def increment_password(pw: str) -> str:
    pw_list: list = list(pw)
    position: int = len(pw_list) - 1

    while position >= 0:
        if pw_list[position] == 'z':
            pw_list[position] = 'a'
            position -= 1
        else:
            pw_list[position] = chr(ord(pw_list[position]) + 1)
            break

    return ''.join(pw_list)


def req1(pw: str) -> bool:
    alphabet: str = "abcdefghijklmnopqrstuvwxyz"
    
    for position in range(len(pw)-2):
        window: str = f"{pw[position]}{pw[position+1]}{pw[position+2]}"
        if window in alphabet:
            return True

    return False

def req2(pw: str) -> bool:
    if "i" in pw or "l" in pw or "o" in pw:
        return False
    else:
        return True
    
def req3(pw: str) -> bool:
    doubles: int = 0
    forbidden: str = ""
    
    for position in range(len(pw)-1):
        if pw[position] == pw[position+1] and forbidden != pw[position]:
            doubles += 1
            forbidden = pw[position]
        if doubles >= 2:
            return True
        
    return False


def AoC_11_2015(datastream: list[str]) -> tuple[int, int]:
    antwoord1: str = ""
    antwoord2: list[str] = []
    
    datastream = datastream[0]
    
    while len(antwoord2) < 2:
        if req1(datastream) and req2(datastream) and req3(datastream):
            antwoord2.append(datastream)
            
        datastream = increment_password(datastream)

    antwoord1 = antwoord2[0]
    antwoord2 = antwoord2[1]
    
    return antwoord1,antwoord2

if __name__ == "__main__":
    with open("2015/AoC_11_2015.txt", "r") as fh:
        invoer: list[str] = [regels.strip() for regels in fh]

    print(AoC_11_2015(invoer))