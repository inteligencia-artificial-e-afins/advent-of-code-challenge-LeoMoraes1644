def convert_letter_in_value (letter):
    ascii_letter = ord(letter)
    if ascii_letter > 96:
        return ascii_letter - 96
    return ascii_letter - 38

FILE_PATH = input('insira o path do arquivo: ')
with open(FILE_PATH) as file:
    rucksacks = [i for i in file.read().strip().split("\n")]

contador = 0
for rucksack in rucksacks:
    total_size = len(rucksack)
    primeira_metade = rucksack[0:total_size//2]
    segunda_metade = rucksack[total_size//2:]
    armazenar_letra = ""
    for letra_um in list(primeira_metade):
        print(letra_um)
        for letra_dois in list(segunda_metade):
            if letra_um == letra_dois:
                armazenar_letra = letra_um
    if len(armazenar_letra) > 0:
        contador += convert_letter_in_value(armazenar_letra)
print(contador)
