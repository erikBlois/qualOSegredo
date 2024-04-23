import gruposNumerosQOS as grupo

Nprimeira = len(grupo.eliminados1)
Nsegunda = len(grupo.eliminados2)
Nterceira = len(grupo.eliminados3)
Nquarta = len(grupo.eliminados4)
Nquinta = len(grupo.eliminados5)
Nsexta = len(grupo.eliminados6)
Nsetima = len(grupo.eliminados7)
Nsegredos = len(grupo.segredos)
Npares = len(grupo.paresSegredos)

with open('Relatorio qual o segredo de {} a {}.txt'.format(grupo.limiteInferior, grupo.limiteSuperior), mode='w') as arquivo:
		arquivo.write("Foram eliminados {} números entre {} e {} com a primeira pista: \nNão é um número multiplo de 4. \nEsses números são: ".format(Nprimeira, grupo.limiteInferior, grupo.limiteSuperior))
		arquivo.write(str(grupo.eliminados1))
		
		arquivo.write("\n\nForam eliminados {} números entre {} e {} com a segunda pista: \nNão é um número divisível por 5. \nEsses números são: ".format(Nsegunda, grupo.limiteInferior, grupo.limiteSuperior))
		arquivo.write(str(grupo.eliminados2))
		
		arquivo.write("\n\nForam eliminados {} números entre {} e {} com a terceira pista: \nNão é um número par. \nEsses números são: ".format(Nterceira, grupo.limiteInferior, grupo.limiteSuperior))
		arquivo.write(str(grupo.eliminados3))
		
		arquivo.write("\n\nForam eliminados {} números entre {} e {} com a quarta pista: \nÉ um número multiplo de 3. \nEsses números são: ".format(Nquarta, grupo.limiteInferior, grupo.limiteSuperior))
		arquivo.write(str(grupo.eliminados4))
		
		arquivo.write("\n\nForam eliminados {} números entre {} e {} com a quinta pista: \nNão é um número divisível por 9. \nEsses números são: ".format(Nquinta, grupo.limiteInferior, grupo.limiteSuperior))
		arquivo.write(str(grupo.eliminados5))
		
		arquivo.write("\n\nForam eliminados {} números entre {} e {} com a sexta pista: \nO resto da divisão por 5 é 2. \nEsses números são:".format(Nsexta, grupo.limiteInferior, grupo.limiteSuperior))
		arquivo.write(str(grupo.eliminados6))
		
		arquivo.write("\n\nForam eliminados {} números entre {} e {} com a sétima pista: \nA soma dos algarismos do número é impar. \nEsses números são: ".format(Nsetima, grupo.limiteInferior, grupo.limiteSuperior))
		arquivo.write(str(grupo.eliminados7))
		
		arquivo.write("\n\nTemos {} candidatos a segredo entre {} e {} depois das sete pistas. \nEsses números são: ".format(Nsegredos, grupo.limiteInferior, grupo.limiteSuperior))
		arquivo.write(str(grupo.segredos))
		
		arquivo.write("\n\nTemos {} pares de candidatos a segredo entre {} e {} depois das sete pistas. \nEsses pares são: ".format(Npares, grupo.limiteInferior, grupo.limiteSuperior))
		arquivo.write(str(grupo.paresSegredos))
