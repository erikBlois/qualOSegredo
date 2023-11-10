limiteSuperior = 1000
limiteInferior = 1
intervalo = range(limiteInferior, limiteSuperior)

eliminadosPrimeira =[]
eliminadosSegunda =[]
eliminadosTerceira =[]
eliminadosQuarta =[]
eliminadosQuinta =[]
eliminadosSexta =[]
eliminadosSetima =[]

sobreviventes =[]

for numero in intervalo:
  #primeira dica: o número não é multiplo de 4 
  if numero % 4 == 0 :
    eliminadosPrimeira.append(numero)
  #segunda dica: o número não é divisivel por 5
  elif numero % 5 == 0 :
    eliminadosSegunda.append(numero)
  #terceira dica: o número não é par
  elif numero % 2 == 0 :
    eliminadosTerceira.append(numero)
  #quarta dica: o número é multiplo de 3
  elif numero % 3 != 0 :
    eliminadosQuarta.append(numero)
  #quinta dica: o número não é divisivel por 9
  elif numero % 9 == 0 :
    eliminadosQuinta.append(numero)
  #sexta dica: o resto da divisão por 5 é 2
  elif numero % 5 != 2 :
    eliminadosSexta.append(numero)
  #setima dica: a soma dos algarimos é impar 
  else:
    unidade = numero % 10
    dezena = (numero % 100) // 10
    centena = numero // 100
    
    somaAlgarismos = centena + dezena + unidade
    
    if somaAlgarismos % 2 == 0:
      eliminadosSetima.append(numero)
    else:
      sobreviventes.append(numero)
    
Nprimeira = len(eliminadosPrimeira)
Nsegunda = len(eliminadosSegunda)
Nterceira = len(eliminadosTerceira)
Nquarta = len(eliminadosQuarta)
Nquinta = len(eliminadosQuinta)
Nsexta = len(eliminadosSexta)
Nsetima = len(eliminadosSetima)

Nsobrevivente = len(sobreviventes)

#conjuntos = [eliminadosPrimeira, eliminadosSegunda, eliminadosTerceira, eliminadosQuarta, eliminadosQuarta, eliminadosQuinta, eliminadosSexta, eliminadosSetima, sobreviventes]

with open('numerosAgrupadosPorEliminacao.py', mode='w') as repositorio:
  repositorio.write('\neliminadosPrimeira = {}\n'.format(eliminadosPrimeira))
  repositorio.write('\neliminadosSegunda = {}\n'.format(eliminadosSegunda))
  repositorio.write('\neliminadosTerceira = {}\n'.format(eliminadosTerceira))
  repositorio.write('\neliminadosQuarta = {}\n'.format(eliminadosQuarta))
  repositorio.write('\neliminadosQuinta = {}\n'.format(eliminadosQuinta))
  repositorio.write('\neliminadosSexta = {}\n'.format(eliminadosSexta))
  repositorio.write('\neliminadosSetima = {}\n'.format(eliminadosSetima))
  repositorio.write('\nsobreviventes = {}\n'.format(sobreviventes))
  
"""
with open('Relatorio qual o segredo de {} a {}.txt'.format(limiteInferior, limiteSuperior), mode='w') as arquivo:
		arquivo.write("Foram eliminados {} números entre {} e {} com a primeira dica: \nNão é um número multiplo de 4. \nEsses números são: ".format(Nprimeira, limiteInferior, limiteSuperior))
		arquivo.write(str(eliminadosPrimeira))
		
		arquivo.write("\n\nForam eliminados {} números entre {} e {} com a segunda dica: \nNão é um número divisível por 5. \nEsses números são: ".format(Nsegunda, limiteInferior, limiteSuperior))
		arquivo.write(str(eliminadosSegunda))
		
		arquivo.write("\n\nForam eliminados {} números entre {} e {} com a terceira dica: \nNão é um número par. \nEsses números são: ".format(Nterceira, limiteInferior, limiteSuperior))
		arquivo.write(str(eliminadosTerceira))
		
		arquivo.write("\n\nForam eliminados {} números entre {} e {} com a quarta dica: \nÉ um número multiplo de 3. \nEsses números são: ".format(Nquarta, limiteInferior, limiteSuperior))
		arquivo.write(str(eliminadosQuarta))
		
		arquivo.write("\n\nForam eliminados {} números entre {} e {} com a quinta dica: \nNão é um número divisível por 9. \nEsses números são: ".format(Nquinta, limiteInferior, limiteSuperior))
		arquivo.write(str(eliminadosQuinta))
		
		arquivo.write("\n\nForam eliminados {} números entre {} e {} com a sexta dica: \nO resto da divisão por 5 é 2. \nEsses números são:".format(Nsexta, limiteInferior, limiteSuperior))
		arquivo.write(str(eliminadosSexta))
		
		arquivo.write("\n\nForam eliminados {} números entre {} e {} com a sétima dica: \nA soma dos algarismos do número é impar. \nEsses números são: ".format(Nsetima, limiteInferior, limiteSuperior))
		arquivo.write(str(eliminadosSetima))
		
		arquivo.write("\n\nSobraram {} números entre {} e {} depois das sete dicas. \nEsses números são: ".format(Nsobrevivente, limiteInferior, limiteSuperior))
		arquivo.write(str(sobreviventes))
"""
