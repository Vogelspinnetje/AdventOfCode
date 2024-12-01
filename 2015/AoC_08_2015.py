def AoC_08_2015(datasream:list[str]) -> tuple[int, int]:
    ruw_counter = 0
    interpreteerde_counter = 0
    extra_lang = 0

    for items in datasream:
        ruw_counter += len(items)
        interpreteerde_counter += len(eval(items))

        extra_lang_transform = items.replace('\\', '\\\\')
        extra_lang_transform = extra_lang_transform.replace('"', '\\"')
        extra_lang += len(f'"{extra_lang_transform}"')
        print(extra_lang_transform)

    return ruw_counter - interpreteerde_counter, extra_lang - ruw_counter

if __name__ == "__main__":
    with open("AoC_08_2015.txt", "r")as fh:
        invoer = fh.read().split("\n")

    print(AoC_08_2015(invoer))