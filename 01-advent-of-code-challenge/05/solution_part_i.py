FILE_PATH = input('insira o path do arquivo: ')
with open(FILE_PATH) as file:
    data = [i for i in file.read().strip().split("\n")]
print(data)

CRATES_SIZE = 0
MOVES_SIZE  = 0
EMPTY_CRATE = "   "
totalSize = range(len(data))
for i in totalSize:
    if data[i] == '':
        CRATES_SIZE = i
        MOVES_SIZE = i + 2
        break

# Plano de resolução:
# For -> onde percorro todas o range de 0 até CRATES_SIZE - 1, o que representa os valores a serem armazenados em array
# Dentro desse for, percorrer a string de 4 em 4 caracteres, o motivo é que entre o inicio de uma var até outra são 4 caracteres
# Estando dentro desse loop percorrendo a string dou splice a posição atual + 2, que representa [X] ou vai colocar três espaços no array
# preciso montar essa matriz de maneira vertical, ao invés de linha armazenar em colunas, porque facilitará mais para frente
# dai é só mover baseado nas instruções.
