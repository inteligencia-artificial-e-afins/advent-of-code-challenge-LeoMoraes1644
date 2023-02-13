from enum import Enum

# ================ ENUMS ================
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

# ================ FUNÇÕES ================
def elfs_move (valor):
    """
     Nome já diz tudo.
    """
    conversao = {
        "A" : RockPaperScissors.PEDRA,
        "B" : RockPaperScissors.PAPEL,
        "C" : RockPaperScissors.TESOURA
    }
    return conversao.get(valor)

def need_to_win (elf_move):
    if elf_move == RockPaperScissors.PEDRA:
        return RockPaperScissors.PAPEL
    elif elf_move == RockPaperScissors.PAPEL:
        return RockPaperScissors.TESOURA
    else:
        return RockPaperScissors.PEDRA

def need_to_lose (elf_move):
    if elf_move == RockPaperScissors.PEDRA:
        return RockPaperScissors.TESOURA
    elif elf_move == RockPaperScissors.PAPEL:
        return RockPaperScissors.PEDRA
    else:
        return RockPaperScissors.PAPEL
    
def my_move (signal, elf_move):
    """
     Nome já diz tudo.
    """
    conversao = {
        "X" : need_to_lose(elf_move),
        "Y" : elf_move,
        "Z" : need_to_win(elf_move)
    }
    return conversao.get(signal)

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

# ================ MAIN ================

FILE_PATH = input('insira o path do arquivo: ')
with open(FILE_PATH) as file:
    ROUNDS = [i for i in file.read().strip().split("\n")]

SOMADOR_RESULTADOS = 0
for ROUND in ROUNDS:
    MOVE = ROUND.split(" ")
    ELFO = elfs_move(MOVE[0])
    EU = my_move(MOVE[1], ELFO)
    if ELFO == EU:
        SOMADOR_RESULTADOS += draw(EU.value)
    else:
        SOMADOR_RESULTADOS += find_winner(EU, ELFO)

print(SOMADOR_RESULTADOS)