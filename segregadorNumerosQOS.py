
limiteSuperior = 1000
limiteInferior = 1

def somarAlgarismos(numero):    
  textoN = str(numero)
  somaAlgarismos = 0
  for alg in textoN:
    valorAlg = int(alg)
    somaAlgarismos += valorAlg
  return somaAlgarismos

def gerarParesElementos (lista):
  pares = []
  contador = 0
  for elemento1 in lista:
      contador +=1    
      for elemento2 in lista[contador:]:
          par = [elemento1, elemento2]
          pares.append(par)
  return pares


eliminados1 =[]
eliminados2 =[]
eliminados3 =[]
eliminados4 =[]
eliminados5 =[]
eliminados6 =[]
eliminados7 =[]
segredos =[]

for numero in range(limiteInferior, limiteSuperior):
  #primeira pista: o número não é multiplo de 4 
  if numero % 4 == 0 :
    eliminados1.append(numero)
  #segunda pista: o número não é divisivel por 5
  elif numero % 5 == 0 :
    eliminados2.append(numero)
  #terceira pista: o número não é par
  elif numero % 2 == 0 :
    eliminados3.append(numero)
  #quarta pista: o número é multiplo de 3
  elif numero % 3 != 0 :
    eliminados4.append(numero)
  #quinta pista: o número não é divisivel por 9
  elif numero % 9 == 0 :
    eliminados5.append(numero)
  #sexta pista: o resto da divisão por 5 é 2
  elif numero % 5 != 2 :
    eliminados6.append(numero)
  #setima pista: a soma dos algarimos é impar 
  elif somarAlgarismos(numero) % 2 == 0 :
    eliminados7.append(numero)
  #os candidatos a segredo  
  else:
    segredos.append(numero)
    
paresSegredos = gerarParesElementos(segredos)
    
conjuntos = [eliminados1, eliminados2, eliminados3, eliminados4, eliminados5, eliminados6, eliminados7, segredos, paresSegredos]


with open('gruposNumerosQOS.py', mode='w') as repositorio:
  repositorio.write('\nlimiteSuperior = {}'.format(limiteSuperior))
  repositorio.write('\nlimiteInferior = {}\n'.format(limiteInferior))
  repositorio.write('\neliminados1 = {}\n'.format(eliminados1))
  repositorio.write('\neliminados2 = {}\n'.format(eliminados2))
  repositorio.write('\neliminados3 = {}\n'.format(eliminados3))
  repositorio.write('\neliminados4 = {}\n'.format(eliminados4))
  repositorio.write('\neliminados5 = {}\n'.format(eliminados5))
  repositorio.write('\neliminados6 = {}\n'.format(eliminados6))
  repositorio.write('\neliminados7 = {}\n'.format(eliminados7))
  repositorio.write('\nsegredos = {}\n'.format(segredos))
  repositorio.write('\nparesSegredos = {}\n'.format(paresSegredos))
  repositorio.write('\nconjuntos = {}\n'.format(conjuntos))
