import gruposNumerosQOS as grupo
from random import randrange
from copy import deepcopy

"""
    decidimos que as 3 ultimas perguntas serão:
    o produto dos algarismos é divisivel por 7 (igual)
    resto da divisão por 15 é 12 (igual)
    resto da divisão por 19 é algum número (diferente)
"""

conjuntos = grupo.conjuntos
copiaConjuntos = deepcopy(conjuntos)
sequenciaEliminacao16 = (4,2,3,2,1,1,1)
sequenciaEliminacao25 = (5,4,5,6,1,1,1)
sequenciaEliminacao36 = (8,6,7,9,1,2,1)

    
def criarNTabuleiros (quantidade, sequenciaEliminacao):
    tabuleiros = []
    for indiceTabuleiro in range(quantidade):
        numerosTabuleiro = []
        for indiceEliminacao in range(len(sequenciaEliminacao)):
            nEliminados = sequenciaEliminacao[indiceEliminacao]
            lista = copiaConjuntos[indiceEliminacao]
            numerosSelecionados = []
            eliminado = 0
            while eliminado < nEliminados:
                if len(lista) > 0:
                    numero = lista.pop(randrange(0,len(lista)))
                    
                else:
                    copiaConjuntos[indiceEliminacao] = deepcopy(conjuntos[indiceEliminacao])
                    lista = copiaConjuntos[indiceEliminacao]
                    numero = lista.pop(randrange(0,len(lista)))
                  
                    
                if numero in numerosSelecionados:
                    pass
                else:
                    numerosSelecionados.append(numero)
                    eliminado += 1
            numerosTabuleiro = numerosTabuleiro + numerosSelecionados
                    
        paresSegredos = copiaConjuntos[-1]
        if len(paresSegredos) > 0:
            par = paresSegredos.pop(randrange(0,len(paresSegredos)))
        else:
            copiaConjuntos[-1] = deepcopy(conjuntos[-1])
            paresSegredos = copiaConjuntos[-1]
            par = possiveisSegredos.pop(randrange(0,len(possiveisSegredos)))
        numerosTabuleiro = numerosTabuleiro + par          
        tabuleiros.append(numerosTabuleiro)
    return tabuleiros


#tabuleiros16 = criarNTabuleiros(8, sequenciaEliminacao16)
#tabuleiros25 = criarNTabuleiros(8, sequenciaEliminacao25)
tabuleiros36 = criarNTabuleiros(91, sequenciaEliminacao36)

with open('tabuleiros.py', mode='w') as repositorio:
#    repositorio.write("\ntabuleiros16 = {}\n".format(tabuleiros16))
#    repositorio.write("\ntabuleiros25 = {}\n".format(tabuleiros25))
    repositorio.write("\ntabuleiros36 = {}\n".format(tabuleiros36))
    
