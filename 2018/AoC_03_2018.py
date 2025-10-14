def extract_data(data: list[str]):
    data_new = {}
    
    for items in data:
        splitted_data = items.split(" ")
        start_pos = splitted_data[2].split(",")
        start_pos[1] = start_pos[1][:-1]
        lengte = splitted_data[3].split("x")
        
        data_new[splitted_data[0]] = [[int(start_pos[0]), int(start_pos[0]) + int(lengte[0])], [int(start_pos[1]), int(start_pos[1])+int(lengte[1])]]
        
    return data_new
        

def AoC_03_2018(datastream: list[str]) -> tuple[int, int]:
    antwoord1: int = 0
    antwoord2: int = 0
    
    data_new = extract_data(datastream)
    occupied_positions = {}
    
    for items in data_new:
        for x in range(data_new[items][0][0], data_new[items][0][1]):
            for y in range(data_new[items][1][0], data_new[items][1][1]):
                if (x,y) in occupied_positions.keys():
                    occupied_positions[(x,y)] = 2
                else:
                    occupied_positions[(x,y)] = 1

    antwoord1 = sum([1 for items in occupied_positions if occupied_positions[items] == 2])
    
    for items in data_new:
        correct_claim = True
        for x in range(data_new[items][0][0], data_new[items][0][1]):
            for y in range(data_new[items][1][0], data_new[items][1][1]):
                if occupied_positions[(x,y)] == 2:
                    correct_claim = False
                    
        if correct_claim:
            antwoord2 = int(items[1:])
                
    
    return antwoord1,antwoord2

if __name__ == "__main__":
    with open("2018/AoC_03_2018.txt", "r") as fh:
        invoer: list[str] = [regels.strip() for regels in fh]

    print(AoC_03_2018(invoer))