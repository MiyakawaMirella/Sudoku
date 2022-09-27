import random

# criar um sudoku
# 3 * 3 | 3 * 3 | 3 * 3
#
# 3 * 3 | 3 * 3 | 3 * 3
#
# 3 * 3 | 3 * 3 | 3 * 3

# declaração de variáveis
quadrado = []
quadradinhos = []
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
controle = 0
controle2 = 3
quadradinho = []

# Separação dos quadradinhos
while q <= (len(quadrado) * 3):
	enderecos = {}

	# separação dos quadradinhos
	for i in range(3):
		if q > 80 and controle2 <= 6:
			q = controle2
			controle2 += 3
		elif q > 80:
			break

		quadradinho.append(quadrado[q])
		Caminho(q, controle, enderecos)
		q += 1
	q += 6
	controle += 1
	if len(quadradinho) == 9:
		listaQuadradinho = []
		for i in range(0, 9):
			listaQuadradinho.append(quadradinho[i])

		quadradinhos.append(listaQuadradinho)
		quadradinho.clear()

	"""if len(quadradinho) == 9:
		for i in range(len(quadradinho)):
			numero = quadradinho[i]
			listaControle = [numero]
	
			# Pega as últimos números
			controleQuadradinho = i - 1
			tamanhoD = i
			if tamanhoD != 0 and tamanhoD <= 8:
				if numero == quadradinho[controleQuadradinho]:
	
					while True:
						num = random.randint(1, 9)
	
						if num in listaControle:
							continue
						else:
							endereco = ""
							enderecos[tamanhoD] = endereco
							enderecos = num
							listaControle.append(num)
							break
				else:
					listaControle.append(numero)
				controleQuadradinho -= 1
			quadradinhos.append(listaControle)
		quadradinho.clear()"""


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
