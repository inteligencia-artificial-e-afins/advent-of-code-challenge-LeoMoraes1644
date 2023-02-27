def packing (data):
    for i in range(len(data) - 4):
        aux = data[i:i+4]
        if len(set(aux)) == len(aux):
            return i
    return -1

FILE_PATH = input('insira o path do arquivo: ')
with open(FILE_PATH) as file:
    packs = file.read().strip()

print(packing(packs) + 4)
