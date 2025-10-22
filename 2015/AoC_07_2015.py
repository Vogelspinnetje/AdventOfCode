def extract_data(datastream: list[str]) -> dict:
    instructions: dict = {}
    
    for instruction in datastream:
        splitted = instruction.split(' -> ')
        instructions[splitted[1]] = splitted[0].split(' ')
        
    return instructions

def AoC_07_2015(datastream: list[str]) -> tuple[int, int]:
    antwoord1: int = 0
    antwoord2: int = 0
    
    original_instructions: dict = extract_data(datastream)
    decoded_instructions: dict = {}
    
    def decoding(wire: str):
        if wire.isdigit():
            return int(wire)
        
        if wire not in decoded_instructions.keys():
            if len(original_instructions[wire]) == 1:
                result = decoding(original_instructions[wire][0])
            else:
                operator: str = original_instructions[wire][-2]
                match operator:
                    case "AND":
                        result = decoding(original_instructions[wire][0]) & decoding(original_instructions[wire][2])
                    case "OR":
                        result = decoding(original_instructions[wire][0]) | decoding(original_instructions[wire][2])
                    case "NOT":
                        result = ~decoding(original_instructions[wire][1]) & 0xffff
                    case "LSHIFT":
                        result = decoding(original_instructions[wire][0]) << decoding(original_instructions[wire][2])
                    case "RSHIFT":
                        result = decoding(original_instructions[wire][0]) >> decoding(original_instructions[wire][2])
            decoded_instructions[wire] = result
        return decoded_instructions[wire]
    
    antwoord1: int = decoding("a")
    
    decoded_instructions: dict = {}
    original_instructions["b"] = [str(antwoord1)]
    
    antwoord2: int = decoding("a")
    
    
    return antwoord1,antwoord2

if __name__ == "__main__":
    with open("2015/AoC_07_2015.txt", "r") as fh:
        invoer: list[str] = [regels.strip() for regels in fh]

    print(AoC_07_2015(invoer))