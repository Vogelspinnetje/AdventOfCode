import hashlib

def AoC_04_2015(datastream: str) -> tuple[int,int]:
    onderzoeks_objecten = ["00000", "000000"]
    getallen = []
    for object in onderzoeks_objecten:
        teller = 0
        while True:
            combined_string = datastream + str(teller)
            hash_object = hashlib.md5(combined_string.encode())
            md5_hash = hash_object.hexdigest()

            if md5_hash.startswith(object):
                getallen.append(teller)
                break

            teller += 1
    return getallen[0], getallen[1]

if __name__ == "__main__":
    puzzle_input = "ckczppom"
    print(AoC_04_2015(puzzle_input))