def calcular_range (elfo_one, elfo_two):
    return int(elfo_one[0]) <= int(elfo_two[0]) <= int(elfo_one[1]) \
        and int(elfo_one[0]) <= int(elfo_two[1]) <= int(elfo_one[1]) \
        or int(elfo_two[0]) <= int(elfo_one[0]) <= int(elfo_two[1]) \
        and int(elfo_two[0]) <= int(elfo_one[1]) <= int(elfo_two[1])

FILE_PATH = input('insira o path do arquivo: ')
with open(FILE_PATH) as file:
    sections = [i for i in file.read().strip().split("\n")]
soma = 0
for section in sections:
    each_one = section.split(",")
    elfo_one = each_one[0].split("-")
    elfo_two = each_one[1].split("-")
    if calcular_range(elfo_one, elfo_two):
        soma += 1
print(soma)