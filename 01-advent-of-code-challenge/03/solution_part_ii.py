def convert_letter_in_value (letter):
    ascii_letter = ord(letter)
    if ascii_letter > 96:
        return ascii_letter - 96
    return ascii_letter - 38

FILE_PATH = input('insira o path do arquivo: ')
with open(FILE_PATH) as file:
    rucksacks = [i for i in file.read().strip().split("\n")]

contador = 0
val_max = len(rucksacks)
for index, rucksack in enumerate(rucksacks):
    total_size = len(rucksack)
    armazenar_letra = ""
    for letra_um in list(rucksack):
        if (index+1) > val_max or (index+2) > val_max:
            break
        for letra_dois in list(rucksacks[index+1]):
            if letra_um == letra_dois:
                for letra_tres in list(rucksacks[index+2]):
                    if letra_tres == letra_um:
                        armazenar_letra = letra_um
                        break
    if len(armazenar_letra) > 0:
        contador += convert_letter_in_value(armazenar_letra)
print(contador)
