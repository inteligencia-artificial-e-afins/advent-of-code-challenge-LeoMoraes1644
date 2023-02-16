FILE_PATH = input('insira o path do arquivo: ')
with open(FILE_PATH, encoding='utf-8') as file:
    data = [i for i in file.read().splitlines()]

CRATES_SIZE = 0
MOVES_SIZE  = 0
totalSize = range(len(data))
for i in totalSize:
    if not data[i]:
        CRATES_SIZE = i
        MOVES_SIZE  = i + 2
        break
newData = []
for line in range((CRATES_SIZE - 1)):
    newData.append(data[line].replace('    ', ' ### '))
    print(newData[line].strip().replace('  ', ' '))
# crates = 
# colunas = zip(*crates)
# matriz = [list(coluna) for coluna in colunas]
# print(matriz)
