def convert_letter_in_value (letter):
    ascii_letter = ord(letter)
    if ascii_letter > 96:
        return ascii_letter - 96
    return ascii_letter - 38

FILE_PATH = input('insira o path do arquivo: ')
with open(FILE_PATH) as file:
    rucksacks = [i for i in file.read().strip().split("\n")]

CONTADOR = 0
val_max = range(0, len(rucksacks), 3)
for i in val_max:
    ARMAZENAR_LETRA = ""
    for letra_um in list(rucksacks[i]):
        for letra_dois in list(rucksacks[i+1]):
            if letra_um == letra_dois:
                for letra_tres in list(rucksacks[i+2]):
                    if letra_tres == letra_um:
                        ARMAZENAR_LETRA = letra_um
                        break
    if len(ARMAZENAR_LETRA) > 0:
        CONTADOR += convert_letter_in_value(ARMAZENAR_LETRA)
print(CONTADOR)
