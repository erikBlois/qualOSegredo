"""
    decidimos que as 3 ultimas perguntas serão:
    soma dos algarismos igual a 15 ou 21 (igual)
    resto da divisão por 15 é 12 (igual)
    resto da divisão por 13 é algum número (diferente)
"""
from random import randrange
import numerosAgrupadosPorEliminacao as nape 

# nos sobreviventes às 7 primeiras perguntas temos números cujos algarigarismos somam 15 e 21 então teremos dois tipos de tabuleiros, os com os ultimos candidatos somando 15 e outro somando 21 
somaAlg15 = []
somaAlg21 = []

#nesse laço de repetição separo os sobreviventes entre os que a soma dos algarismos é 15 ou 21
for numero in nape.sobreviventes:    
    unidade = numero % 10
    dezena = (numero % 100) // 10
    centena = numero // 100
    
    somaAlgarismos = centena + dezena + unidade
    if somaAlgarismos == 15:
        somaAlg15.append(numero)
    elif somaAlgarismos == 21:
        somaAlg21.append(numero)

paresSegredos15 = []
paresSegredos21 = []

#nos laços de repetição seguintes estou montando todos os pares de segredo possíveis para colocar nos tabuleiros mais adiante
contador = 0
for segredo1 in somaAlg15:
    contador +=1    
    for segredo2 in somaAlg15[contador:]:
        par = [segredo1, segredo2]
        paresSegredos15.append(par)

contador = 0
for segredo1 in somaAlg21:
    contador +=1    
    for segredo2 in somaAlg21[contador:]:
        par = [segredo1, segredo2]
        paresSegredos21.append(par)

'''
essa é uma tabela da quantidade de eliminados por questão 
                    4x4 5x5 6x6
eliminadosPrimeira   4   5   8
eliminadosSegunda    2   4   6
eliminadosTerceira   3   5   7
eliminadosQuarta     2   6   9
eliminadosQuinta     1   1   1
eliminadosSexta      1   1   2
eliminadosSetima     1   1   1
                     14  23  34 + 2 possiveis segredos
'''
#essa é a referencia da sequencia de números eliminados baseado na tabela anterior, a primeira tupla é referente aos 4x4 a segunda aos 5x5 e a terceira aos 6x6 
sequenciasEliminacao = ((4,2,3,2,1,1,1),(5,4,5,6,1,1,1),(8,6,7,9,1,2,1))

#aqui estou começando a organizar os tabuleiros, a primeira lista é referente aos 4x4 a segunda aos 5x5 e a terceira aos 6x6
tabuleiros15 = [[],[],[]]
tabuleiros21 = [[],[],[]]

#aqui estou organizando as listas de onde vamos tirar os números dos tabuleiros
EPri = nape.eliminadosPrimeira.copy()
ESeg = nape.eliminadosSegunda.copy()
ETer = nape.eliminadosTerceira.copy()
EQua = nape.eliminadosQuarta.copy()
EQui = nape.eliminadosQuinta.copy()
ESex = nape.eliminadosSexta.copy()
ESet = nape.eliminadosSetima.copy()
pares15 = paresSegredos15.copy()
pares21 = paresSegredos21.copy()


#nos próximos laços de repetição estou dividindo os pares de sobreviventes entre os tipos de tabuleiro (4x4,5x5,6x6)
for par in pares15:
    if pares15.index(par) % 3 == 0:
        tabuleiros15[0].append(par)
    elif pares15.index(par) % 2 == 0:
        tabuleiros15[1].append(par)
    else:
        tabuleiros15[2].append(par)
        
for par in pares21:
    if pares21.index(par) % 3 == 0:
        tabuleiros21[0].append(par)
    elif pares21.index(par) % 2 == 0:
        tabuleiros21[1].append(par)
    else:
        tabuleiros21[2].append(par)           
    
# aqui começo a montagem dos tabuleiros de senhas que soma dos algarismos é 15, o laço externo é fererente aos tipos de tabuleiro (4x4,5x5,6x6)
for tipoTabuleiro in tabuleiros15:
    #no laço seguinte estou montando cada um dos tabuleiros 
    for par in tipoTabuleiro:
        
        #essa lista será usada para adicionar os números que serão eliminados para cada uma das 7 perguntas
        adicionadosTabuleiro = []
        
        #aqui pego o número de vezes que o próximo laço será repetido de acordo com o número de elimidados por perguntas determinado anteriormente
        nEPri = sequenciasEliminacao[tabuleiros15.index(tipoTabuleiro)][0]
        
        while nEPri > 0:
            #caso os números de eliminados na primeira tenham acabado pegamos uma nova copia da lista
            if len(EPri) == 0: 
                EPri = nape.eliminadosPrimeira.copy()
            
            #tentamos pegar um número aleatóriamente da lista de eliminados, quando tem apenas um sobrando dá erro
            try:
                numero = EPri.pop(randrange(len(EPri)))
                                        
            #quando da erro pegamos o unico que sobrou
            except:
                numero = EPri.pop()
                                
            nEPri -= 1
            
            #nesse laço de repetição verificamos se pegamos ou não um número que já estava para ser adicionado no caso de termos pego uma nova copia da lista de eliminados, por conta da aleatoriedade
            for elemento in adicionadosTabuleiro:
                    if numero == elemento:
                        adicionadosTabuleiro = []
                        nEPri = sequenciasEliminacao[tabuleiros15.index(tipoTabuleiro)][0] - 1
            
            #depois de vericar a repetição e resetar ou não o laço adicionamos o novo número, como estamos adicionando o número antes do fim desse ciclo do laço coloquei o - 1 na linha anterior para evitar um número de eliminados maior que o desejado. 
            adicionadosTabuleiro.append(numero)
        
        #depois do laço juntamos os números sorteados ao par de segredos que se tornará o tabuleiro em si
        par += adicionadosTabuleiro
        
        adicionadosTabuleiro = []
        
        #aqui é o mesmo processo do laço de repetição anterior, mas para os eliminados na segunda pergunta
        nESeg = sequenciasEliminacao[tabuleiros15.index(tipoTabuleiro)][1]
        
        while nESeg > 0:
            if len(ESeg) == 0:
                ESeg = nape.eliminadosSegunda.copy()

            try:
                numero = ESeg.pop(randrange(len(ESeg)))
                
            except:
                numero = ESeg.pop()
                
            nESeg -= 1
            
            for elemento in adicionadosTabuleiro:
                    if numero == elemento:
                        adicionadosTabuleiro = []
                        nESeg = sequenciasEliminacao[tabuleiros15.index(tipoTabuleiro)][1] - 1
                        
            adicionadosTabuleiro.append(numero)
            
        par += adicionadosTabuleiro
            
        adicionadosTabuleiro = []
        #aqui é o mesmo processo do laço de repetição anterior, mas para os eliminados na terceira pergunta
        nETer = sequenciasEliminacao[tabuleiros15.index(tipoTabuleiro)][2]
        while nETer > 0:
            if len(ETer) == 0:
                ETer = nape.eliminadosTerceira.copy()
    
            try:
                numero = ETer.pop(randrange(len(ETer)))
                
            except:
                numero = ETer.pop()
                
            nETer -= 1
            
            for elemento in adicionadosTabuleiro:
                    if numero == elemento:
                        adicionadosTabuleiro = []
                        nETer = sequenciasEliminacao[tabuleiros15.index(tipoTabuleiro)][2] - 1
            
            adicionadosTabuleiro.append(numero)
            
        par += adicionadosTabuleiro
            
        adicionadosTabuleiro = []        
        #aqui é o mesmo processo do laço de repetição anterior, mas para os eliminados na quarta pergunta
        nEQua = sequenciasEliminacao[tabuleiros15.index(tipoTabuleiro)][3]
        while nEQua > 0:
            if len(EQua) == 0:
                EQua = nape.eliminadosQuarta.copy()
            
            try:
                numero = EQua.pop(randrange(len(EQua)))                   
                
            except:
                numero = EQua.pop()
                
            nEQua -= 1
            
            for elemento in adicionadosTabuleiro:
                    if numero == elemento:
                        adicionadosTabuleiro = []
                        nEQua = sequenciasEliminacao[tabuleiros15.index(tipoTabuleiro)][3] - 1
                        
            adicionadosTabuleiro.append(numero)
            
        par += adicionadosTabuleiro
            
        adicionadosTabuleiro = []    
        #aqui é o mesmo processo do laço de repetição anterior, mas para os eliminados na quinta pergunta
        nEQui = sequenciasEliminacao[tabuleiros15.index(tipoTabuleiro)][4]
        while nEQui > 0:    
            if len(EQui) == 0:
                EQui = nape.eliminadosQuinta.copy()
                                
            try:
                numero = EQui.pop(randrange(len(EQui)))
                
            except:
                numero = EQui.pop()
                
            nEQui -= 1
            
            for elemento in adicionadosTabuleiro:
                    if numero == elemento:
                        adicionadosTabuleiro = []
                        nEQui = sequenciasEliminacao[tabuleiros15.index(tipoTabuleiro)][4] - 1
                        
            adicionadosTabuleiro.append(numero)
            
        par += adicionadosTabuleiro
        
        adicionadosTabuleiro = []
            
        #aqui é o mesmo processo do laço de repetição anterior, mas para os eliminados na sexta pergunta
        nESex = sequenciasEliminacao[tabuleiros15.index(tipoTabuleiro)][5]
        while nESex > 0:
            if len(ESex) == 0:
                ESex = nape.eliminadosSexta.copy()
            
            try:
                numero = ESex.pop(randrange(len(ESex)))
                
            except:
                numero = ESex.pop()
                
            nESex -= 1
            
            for elemento in adicionadosTabuleiro:
                    if numero == elemento:
                        adicionadosTabuleiro = []
                        nESex = sequenciasEliminacao[tabuleiros15.index(tipoTabuleiro)][5] - 1
            
            adicionadosTabuleiro.append(numero)
            
        par += adicionadosTabuleiro
        
        adicionadosTabuleiro = []
        #aqui é o mesmo processo do laço de repetição anterior, mas para os eliminados na setima pergunta    
        nESet = sequenciasEliminacao[tabuleiros15.index(tipoTabuleiro)][6]
        while nESet > 0:
            if len(ESet) == 0:
                ESet = nape.eliminadosSetima.copy()
                
            try:
                numero = ESet.pop(randrange(len(ESet)))
                
            except:
                numero = ESet.pop()
                
            nESet -= 1
            
            for elemento in adicionadosTabuleiro:
                    if numero == elemento:
                        adicionadosTabuleiro = []
                        nESet = sequenciasEliminacao[tabuleiros15.index(tipoTabuleiro)][6] - 1
                        
            adicionadosTabuleiro.append(numero)
            
        par += adicionadosTabuleiro
            


#aqui repetimos o processo para montar os tabuleiros com senhas que os algarismos somam 21
for tipoTabuleiro in tabuleiros21:
    for par in tipoTabuleiro:
        
        #essa lista será usada para adicionar os números que serão eliminados para cada uma das 7 perguntas
        adicionadosTabuleiro = []
        
        #aqui pego o número de vezes que o próximo laço será repetido de acordo com o número de elimidados por perguntas determinado anteriormente
        nEPri = sequenciasEliminacao[tabuleiros21.index(tipoTabuleiro)][0]
        
        while nEPri > 0:
            #caso os números de eliminados na primeira tenham acabado pegamos uma nova copia da lista
            if len(EPri) == 0: 
                EPri = nape.eliminadosPrimeira.copy()
            
            #tentamos pegar um número aleatóriamente da lista de eliminados, quando tem apenas um sobrando dá erro
            try:
                numero = EPri.pop(randrange(len(EPri)))
                                        
            #quando da erro pegamos o unico que sobrou
            except:
                numero = EPri.pop()
                                
            nEPri -= 1
            
            #nesse laço de repetição verificamos se pegamos ou não um número que já estava para ser adicionado no caso de termos pego uma nova copia da lista de eliminados, por conta da aleatoriedade
            for elemento in adicionadosTabuleiro:
                    if numero == elemento:
                        adicionadosTabuleiro = []
                        nEPri = sequenciasEliminacao[tabuleiros21.index(tipoTabuleiro)][0] - 1
            
            #depois de vericar a repetição e resetar ou não o laço adicionamos o novo número, como estamos adicionando o número antes do fim desse ciclo do laço coloquei o - 1 na linha anterior para evitar um número de eliminados maior que o desejado. 
            adicionadosTabuleiro.append(numero)
        
        #depois do laço juntamos os números sorteados ao par de segredos que se tornará o tabuleiro em si
        par += adicionadosTabuleiro
        
        adicionadosTabuleiro = []
        
        #aqui é o mesmo processo do laço de repetição anterior, mas para os eliminados na segunda pergunta
        nESeg = sequenciasEliminacao[tabuleiros21.index(tipoTabuleiro)][1]
        
        while nESeg > 0:
            if len(ESeg) == 0:
                ESeg = nape.eliminadosSegunda.copy()

            try:
                numero = ESeg.pop(randrange(len(ESeg)))
                
            except:
                numero = ESeg.pop()
                
            nESeg -= 1
            
            for elemento in adicionadosTabuleiro:
                    if numero == elemento:
                        adicionadosTabuleiro = []
                        nESeg = sequenciasEliminacao[tabuleiros21.index(tipoTabuleiro)][1] - 1
                        
            adicionadosTabuleiro.append(numero)
            
        par += adicionadosTabuleiro
            
        adicionadosTabuleiro = []
        #aqui é o mesmo processo do laço de repetição anterior, mas para os eliminados na terceira pergunta
        nETer = sequenciasEliminacao[tabuleiros21.index(tipoTabuleiro)][2]
        while nETer > 0:
            if len(ETer) == 0:
                ETer = nape.eliminadosTerceira.copy()
    
            try:
                numero = ETer.pop(randrange(len(ETer)))
                
            except:
                numero = ETer.pop()
                
            nETer -= 1
            
            for elemento in adicionadosTabuleiro:
                    if numero == elemento:
                        adicionadosTabuleiro = []
                        nETer = sequenciasEliminacao[tabuleiros21.index(tipoTabuleiro)][2] - 1
            
            adicionadosTabuleiro.append(numero)
            
        par += adicionadosTabuleiro
            
        adicionadosTabuleiro = []        
        #aqui é o mesmo processo do laço de repetição anterior, mas para os eliminados na quarta pergunta
        nEQua = sequenciasEliminacao[tabuleiros21.index(tipoTabuleiro)][3]
        while nEQua > 0:
            if len(EQua) == 0:
                EQua = nape.eliminadosQuarta.copy()
            
            try:
                numero = EQua.pop(randrange(len(EQua)))                   
                
            except:
                numero = EQua.pop()
                
            nEQua -= 1
            
            for elemento in adicionadosTabuleiro:
                    if numero == elemento:
                        adicionadosTabuleiro = []
                        nEQua = sequenciasEliminacao[tabuleiros21.index(tipoTabuleiro)][3] - 1
                        
            adicionadosTabuleiro.append(numero)
            
        par += adicionadosTabuleiro
            
        adicionadosTabuleiro = []    
        #aqui é o mesmo processo do laço de repetição anterior, mas para os eliminados na quinta pergunta
        nEQui = sequenciasEliminacao[tabuleiros21.index(tipoTabuleiro)][4]
        while nEQui > 0:    
            if len(EQui) == 0:
                EQui = nape.eliminadosQuinta.copy()
                                
            try:
                numero = EQui.pop(randrange(len(EQui)))
                
            except:
                numero = EQui.pop()
                
            nEQui -= 1
            
            for elemento in adicionadosTabuleiro:
                    if numero == elemento:
                        adicionadosTabuleiro = []
                        nEQui = sequenciasEliminacao[tabuleiros21.index(tipoTabuleiro)][4] - 1
                        
            adicionadosTabuleiro.append(numero)
            
        par += adicionadosTabuleiro
        
        adicionadosTabuleiro = []
            
        #aqui é o mesmo processo do laço de repetição anterior, mas para os eliminados na sexta pergunta
        nESex = sequenciasEliminacao[tabuleiros21.index(tipoTabuleiro)][5]
        while nESex > 0:
            if len(ESex) == 0:
                ESex = nape.eliminadosSexta.copy()
            
            try:
                numero = ESex.pop(randrange(len(ESex)))
                
            except:
                numero = ESex.pop()
                
            nESex -= 1
            
            for elemento in adicionadosTabuleiro:
                    if numero == elemento:
                        adicionadosTabuleiro = []
                        nESex = sequenciasEliminacao[tabuleiros21.index(tipoTabuleiro)][5] - 1
            
            adicionadosTabuleiro.append(numero)
            
        par += adicionadosTabuleiro
        
        adicionadosTabuleiro = []
        #aqui é o mesmo processo do laço de repetição anterior, mas para os eliminados na setima pergunta    
        nESet = sequenciasEliminacao[tabuleiros21.index(tipoTabuleiro)][6]
        while nESet > 0:
            if len(ESet) == 0:
                ESet = nape.eliminadosSetima.copy()
                
            try:
                numero = ESet.pop(randrange(len(ESet)))
                
            except:
                numero = ESet.pop()
                
            nESet -= 1
            
            for elemento in adicionadosTabuleiro:
                    if numero == elemento:
                        adicionadosTabuleiro = []
                        nESet = sequenciasEliminacao[tabuleiros21.index(tipoTabuleiro)][6] - 1
                        
            adicionadosTabuleiro.append(numero)
            
        par += adicionadosTabuleiro
            


quantidadeTabuleiros = len(paresSegredos15)+len(paresSegredos21)

with open('tabuleiros.py', mode='w') as repositorio:

    repositorio.write('#tabuleiros cujos candidatos a segredo têm algarismos que somam 15\n')
    for tipo in tabuleiros15:
        if len(tipo[0]) == 16:
            repositorio.write('\ntabuleiros15_4x4 = {}\n'.format(tipo))
        elif len(tipo[0]) == 25:
            repositorio.write('\ntabuleiros15_5x5 = {}\n'.format(tipo))
        else:
            repositorio.write('\ntabuleiros15_6x6 = {}\n'.format(tipo))
    
    repositorio.write('\n#tabuleiros cujos candidatos a segredo têm algarismos que somam 21\n')
    for tipo in tabuleiros21:
        if len(tipo[0]) == 16:
            repositorio.write('\ntabuleiros21_4x4 = {}\n'.format(tipo))
        elif len(tipo[0]) == 25:
            repositorio.write('\ntabuleiros21_5x5 = {}\n'.format(tipo))
        else:
            repositorio.write('\ntabuleiros21_6x6 = {}\n'.format(tipo))
            
