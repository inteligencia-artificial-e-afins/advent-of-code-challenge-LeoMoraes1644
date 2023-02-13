FILE_PATH = input('insira o path do arquivo: ')
with open(FILE_PATH) as file:
    calorias = [i for i in file.read().strip().split("\n")]

MAIOR_CALORIA = 0
SOMADOR_CALORIA_ELFO = 0
for caloria in calorias:
    if caloria == '':
        if SOMADOR_CALORIA_ELFO > MAIOR_CALORIA:
            MAIOR_CALORIA = SOMADOR_CALORIA_ELFO
        SOMADOR_CALORIA_ELFO = 0
    else:
        SOMADOR_CALORIA_ELFO += int(caloria)
print("Resposta: ", MAIOR_CALORIA)
