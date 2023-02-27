import re
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
    tratamento = data[line].replace('    ', ' [#] ')
    tratamento = tratamento.strip().replace('  ', ' ')
    print(tratamento)
    retornoRe = re.findall(r'\[([^\]]+)\]', tratamento)
    newData.append(retornoRe)

colunas = zip(*newData)
matriz = [list(coluna) for coluna in colunas]
print(matriz)

## FINALMENTE CHEGUEI NAS COLUNAS DO DEMONIO
# agora vamos iniciar finalmente

for linha in range(MOVES_SIZE, len(data)):
    match   =   re.match(r'move (\d+) from (\d+) to (\d+)', data[linha])
    move    =   int(match.group(1))
    frm     =   int(match.group(2))
    to      =   int(match.group(3))
    movimentado = 0
    while movimentado < move:
        for col in matriz[frm]:
            if matriz[frm][col] is not '#':
                for col2 in matriz[to]:
                    if matriz[to][col2] is not '#' and matriz[col2-1] is '#':
                        matriz[to][col2].replace('#', matriz[col])
                    else:
                        matriz[col2]
                matriz[col] = '#'