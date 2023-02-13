# vou reaproveitar a solução 1 para a pt 2
FILE_PATH = input('insira o path do arquivo: ')
with open(FILE_PATH) as file:
    calorias = [i for i in file.read().strip().split("\n")]

MAIOR_CALORIA = 0
SEGUNDA_MAIOR_CALORIA = 0
TERCEIRA_MAIOR_CALORIA = 0
SOMADOR_CALORIA_ELFO = 0
for caloria in calorias:
    if caloria == '':
        if SOMADOR_CALORIA_ELFO > TERCEIRA_MAIOR_CALORIA:
            if SOMADOR_CALORIA_ELFO > SEGUNDA_MAIOR_CALORIA:
                if SOMADOR_CALORIA_ELFO > MAIOR_CALORIA:
                    TERCEIRA_MAIOR_CALORIA = SEGUNDA_MAIOR_CALORIA
                    SEGUNDA_MAIOR_CALORIA = MAIOR_CALORIA
                    MAIOR_CALORIA = SOMADOR_CALORIA_ELFO
                else:
                    TERCEIRA_MAIOR_CALORIA = SEGUNDA_MAIOR_CALORIA
                    SEGUNDA_MAIOR_CALORIA = SOMADOR_CALORIA_ELFO
            else:
                TERCEIRA_MAIOR_CALORIA = SOMADOR_CALORIA_ELFO
        SOMADOR_CALORIA_ELFO = 0
    else:
        SOMADOR_CALORIA_ELFO += int(caloria)
TOTAL = MAIOR_CALORIA + SEGUNDA_MAIOR_CALORIA + TERCEIRA_MAIOR_CALORIA

print("1º ", MAIOR_CALORIA, "\n2º ", SEGUNDA_MAIOR_CALORIA, "\n3º ", TERCEIRA_MAIOR_CALORIA)

print("Soma total das calorias: ", TOTAL)
