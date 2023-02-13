from enum import Enum

class RockPaperScissors(Enum):
    """
     Enum tipos de jogada
    """
    PEDRA = 1
    PAPEL = 2
    TESOURA = 3

class RESULT (Enum):
    """
     Enum dos tipos de resultados
    """
    WIN = 6
    DRAW = 3
    LOSE = 0

def converter_input (valor):
    """
     Nome já diz tudo.
    """
    conversao = {
        "X" : RockPaperScissors.PEDRA,
        "Y" : RockPaperScissors.PAPEL,
        "Z" : RockPaperScissors.TESOURA,
        "A" : RockPaperScissors.PEDRA,
        "B" : RockPaperScissors.PAPEL,
        "C" : RockPaperScissors.TESOURA
    }
    return conversao.get(valor)


def draw(my_move):
    """
     Nome já diz tudo.
    """
    return my_move + RESULT.DRAW.value

def win(my_move):
    """
     Nome já diz tudo.
    """
    return my_move + RESULT.WIN.value

def lose(my_move):
    """
     Nome já diz tudo.
    """
    return my_move + RESULT.LOSE.value

def find_winner (me, elf):
    """
     Nome já diz tudo.
    """
    if (elf == RockPaperScissors.TESOURA and me == RockPaperScissors.PEDRA) or \
   (elf == RockPaperScissors.PAPEL and me == RockPaperScissors.TESOURA) or \
   (elf == RockPaperScissors.PEDRA and me == RockPaperScissors.PAPEL):
        return win(me.value)
    return lose(me.value)

FILE_PATH = input('insira o path do arquivo: ')
with open(FILE_PATH) as file:
    ROUNDS = [i for i in file.read().strip().split("\n")]

SOMADOR_RESULTADOS = 0
for ROUND in ROUNDS:
    MOVE = ROUND.split(" ")
    ELFO = converter_input(MOVE[0])
    EU = converter_input(MOVE[1])
    if ELFO == EU:
        SOMADOR_RESULTADOS += draw(EU.value)
    else:
        SOMADOR_RESULTADOS += find_winner(EU, ELFO)

print(SOMADOR_RESULTADOS)