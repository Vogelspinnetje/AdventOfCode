def AoC_02_2018(datastream: list[str]) -> tuple[int, int]:
    antwoord1: int = 0
    antwoord2: str = ""
    twos: int = 0
    threes: int = 0
    
    for ids in datastream:
        letter_count: dict = {}
        two_detected: bool = False
        three_detected: bool = False
        
        for letter in ids:
            if letter in letter_count.keys():
                letter_count[letter] = letter_count[letter] + 1
            else:
                letter_count[letter] = 1
                
        for letters in letter_count:
            if letter_count[letters] == 2:
                two_detected = True
            if letter_count[letters] == 3:
                three_detected = True
        
        twos = twos + 1 if two_detected else twos + 0
        threes = threes + 1 if three_detected else threes + 0
    
    antwoord1 = twos * threes
    
    for ids1 in range(len(datastream)):
        for ids2 in range(ids1+1, len(datastream)):
            word1 = datastream[ids1]
            word2 = datastream[ids2]
            
            print(f"{word1}[{ids1}] VS {word2}[{ids2}]")
            
            possible_answer: list = []
            
            for position in range(len(word1)):
                if word1[position] != word2[position] and len(possible_answer) == 0:
                    possible_answer = list(word1)
                    possible_answer.pop(position)
                elif word1[position] != word2[position] and len(possible_answer) == len(word1)-1:
                    possible_answer = ""
                    break
            
            if len(possible_answer) > 0:
                antwoord2 = "".join(possible_answer)
                break
        if antwoord2 != "":
            break
            
    
    return antwoord1, antwoord2

if __name__ == "__main__":
    with open("2018/AoC_02_2018.txt", "r") as fh:
        invoer: list[str] = [regels.strip() for regels in fh]

    print(AoC_02_2018(invoer))