import random

# criar um sudoku
# 3 * 3 | 3 * 3 | 3 * 3
#
# 3 * 3 | 3 * 3 | 3 * 3
#
# 3 * 3 | 3 * 3 | 3 * 3

# declaração de variáveis
quadrado = []
controleQuadradinho = 0


def Caminho(numeroEntrada, controleEndereco, listaEndereco):
	str(numeroEntrada)
	str(controleEndereco)
	listaEndereco[controleEndereco] = numeroEntrada
	int(numeroEntrada)
	int(controleEndereco)


def linhaVerificacao():
	linha = []

	while len(linha) < 9:
		while True:
			numeroRandom = random.randint(1, 9)

			if numeroRandom in linha:
				continue
			else:
				linha.append(numeroRandom)
				quadrado.append(numeroRandom)
				break


while len(quadrado) < (9 * 9):
	# escolhe números aleatórios e verifica se possui número iguais
	linhaVerificacao()


# Separa os números em colunas e verifica se há números iguais --> caso for reinicia o processo
for i in range(0, 9):
	coluna = []
	# número da coluna
	numColuna = i
	enderecos = {}

	# separação dos números e acrescentando na coluna
	s = numColuna
	controle = 0
	while s < (len(quadrado)):
		coluna.append(quadrado[s])

		# guardando os caminhos em um dicionario
		Caminho(s, controle, enderecos)

		s += 9
		controle += 1
	numC = 0
	listaControleC = [coluna[0]]
	# Verifica se um número se repete
	for index in range(len(coluna)):
		numero = coluna[index]

		while numC < len(coluna):
			# Pega as últimos números
			controleColuna = numC - 1

			if 0 <= controleColuna <= 8:
				for x in range(0, 8):
					if len(listaControleC) == 9:
						listaControleC.clear()
					elif controleColuna < 0:
						numC += 1
						break

					if numero == coluna[controleColuna]:
						while True:
							num = random.randint(1, 9)

							if num in listaControleC:
								continue
							else:
								if numC >= 9:
									break
								else:
									quadrado[enderecos[numC]] = num
									listaControleC.append(num)
									numC += 1
								break
					else:
						if numero not in listaControleC:
							listaControleC.append(numero)
						controleColuna -= 1
			elif numC == 0:
				numC += 1
			break

# Verificação por quadradinhos
# Declarando variáveis

q = 0
controleD = 0
controle2 = 3
a = 0
listaQuadradinho = []
enderecosD = {}

# Separação dos quadradinhos
while q <= (len(quadrado) * 3):
	# separação dos quadradinhos
	for i in range(3):
		if q > 80 and controle2 <= 6:
			q = controle2
			controle2 += 3
		elif q > 80:
			break

		listaQuadradinho.append(quadrado[q])
		Caminho(q, controleD, enderecosD)
		q += 1
		controleD += 1

	quadradinho = []
	q += 6
	numD = 0
	macaco = 0

	if len(listaQuadradinho) == 9:
		controle = 0
		for i in range(0, 9):
			quadradinho.append(listaQuadradinho[i])
		listaQuadradinho.clear()

		for index in range(len(quadradinho)):
			listaControle = [quadradinho[0]]

			while numD < len(quadradinho):
				numero = quadradinho[index]
				controleQuadradinho = index - 1

				# Pega as últimos números
				if 0 <= controleQuadradinho <= 8:
					for x in range(0, 8):
						if len(listaControle) == 9:
							listaControle.clear()
							
						elif controleQuadradinho < 0:
							if macaco == 1:
								print(f"{numD} --> númeroD controle menor q 0")
								numD += 1
								macaco = 0
								print(f"{numD} --> númeroD controle menor q 0 - depois")
							else:
								macaco += 1
							break

						if numero == quadradinho[controleQuadradinho]:
							while True:
								num = random.randint(1, 9)

								if num in listaControle:
									continue
								else:
									if numD >= 9:
										break
									else:
										print(f"{numD} --> númeroD troca")
										quadrado[enderecosD[numD]] = num
										listaControle.append(num)
										numD += 1
										print(f"{numD} --> númeroD troca - depois")
									break
						else:
							if numero not in listaControle:
								listaControle.append(numero)
							controleQuadradinho -= 1
				elif numD == 0:
					print(f"{numD} --> númeroD zerinho bolinha")
					numD += 1
					print(f"{numD} --> númeroD zerinho bolinha - depois")
				break

		quadradinho.clear()
		enderecosD.clear()

print()
linhaNova = []
for i in range(len(quadrado)):
	linhaNova.append(quadrado[i])

	if len(linhaNova) % 9 == 0:
		# for i in range(len(linha)):
		#     numero = linha[i]
		#     listaControle = [numero]
		#
		#     # Pega as últimos números
		#     controleLinha = i - 1
		#     tamanhoD = i
		#
		#     if tamanhoD != 0 and tamanhoD <= 8:
		#         if numero == linha[controleLinha]:
		#
		#             while True:
		#                 num = random.randint(1, 9)
		#
		#                 if (num in listaControle) == True:
		#                     continue
		#
		#                 else:
		#                     endereco = ""
		#                     enderecos[tamanhoD] = endereco
		#                     enderecos = num
		#                     listaControle.append(num)
		print(linhaNova)
		linhaNova.clear()
