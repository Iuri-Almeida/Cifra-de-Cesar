# Projeto César Cipher - Python
# Autor: Iuri Lopes Almeida
# Perfil GitHub: https://github.com/Iuri-Almeida
# Data: 22/05/2020
# Descrição: Esse programa foi escrito na linguagem Python e tem o objetivo
# 			 de cifrar e decifrar textos utilizando a Cifra de César.
# Forma de uso: python cesar-cipher.py

# Importações necessárias.
import string


# Função responsável por cifrar/decifrar a frase do usuário.
def cesarCipher():

	# Apresentação do programa para o usuário.
	print("[INFO] Para decifrar, esse programa transforma o seu texto em uma string única, ou seja, sem nenhum espaço entre as letras das palavras.")

	# Observação para o usuário.
	print("[INFO] Número máximo de rotações é 26!")

	print("")

	# Escolha que o usuário vai fazer sobre cifrar ou decifrar. Caso digite
	# alguma letra em maiúsculo será colocado em minúsculo pela função lower().
	escolha_usuario = input("Você deseja Cifrar ou Decifrar (c/d)? ").lower()

	# Caso tenha espaços, irá tirar todos os espaços da escolha.
	escolha_usuario = escolha_usuario.replace(" ", "")

	# Enquanto a escolha do usuário for diferente de "c" e "d", faça:
	while escolha_usuario != "c" and escolha_usuario != "d":

		# Avise que ele errou na hora de digitar.
		print("[ERROR] Erro no recebimento da escolha!")

		# Peça para entrar outra escolha.
		escolha_usuario = input("Entrada do texto parece conter algum erro. Tente novamente (c/d): ")

		# Caso tenha espaços, irá tirar todos os espaços da escolha.
		escolha_usuario = escolha_usuario.replace(" ", "")

	# Texto que será cifrado/decifrado. Caso digite alguma letra
	# em maiúsculo será colocado em minúsculo pela função lower().
	entrada_texto_usuario = input("Escreva o texto: ").lower()

	# Caso tenha espaços, irá tirar todos os espaços da escolha.
	entrada_texto_usuario = entrada_texto_usuario.replace(" ", "")

	# Enquanto o que o usuário digitou não for um texto, ou seja,
	# contém caracteres diferentes de letras, faça:
	while entrada_texto_usuario.isalpha() == False:

		# Avise que ele errou na hora de digitar.
		print("[ERROR] Erro no recebimento do texto!")

		# Peça para entrar outro texto.
		entrada_texto_usuario = input("Entrada do texto parece conter algum erro. Tente novamente: ")

		# Caso tenha espaços, irá tirar todos os espaços da escolha.
		entrada_texto_usuario = entrada_texto_usuario.replace(" ", "")

	# Retorna o alfabeto de a - z.
	alfabeto = list(string.ascii_lowercase)

	# Array que irá conter cada letra da frase do usuário.
	# Obs.: Não vai conter os espaços.
	frase_usuario = []

	# Para cada i de 0 até o tamanho do array de entrada de texto, faça:
	for i in range(0, len(entrada_texto_usuario)):

		# Se um desses caracteres não for o espaço, faça:
		if entrada_texto_usuario[i] != " ":

			# Conecte esse caracter ao array frase_usuario.
			# Obs.: Esse array contém todos os caracteres de entrada do usuário,
			# 		mas sem o espaço.
			frase_usuario.append(entrada_texto_usuario[i])

		# Se um desses caracteres for o espaço, faça:
		else:

			# Não faça nada e cotinue o loop.
			pass

	# Se a escolha do usuário foi cifrar, faça:
	if escolha_usuario == "c":

		# Número de onde a cifragem será baseada.
		entrada_valor_usuario = input("Informe o número de rotação: ")

	# Se a escolha do usuário foi decifrar, faça:
	if escolha_usuario == "d":

		# Número de onde a cifragem será baseada.
		entrada_valor_usuario = input("Informe o número de rotação (pressione ENTER para listar todas as opções): ")

		# Se a entrada do valor foi vazia, ou seja, apertou o ENTER, faça:
		if entrada_valor_usuario == "":

			# Para cada t de 0 até o tamanho do array que contém o alfabeto, faça:
			for t in range(0, len(alfabeto)):

				# Chama a função que vai listar todas as opções decifradas.
				listaTodasOpcoes(alfabeto, frase_usuario, t)

			# Acaba com a função cesarCipher().
			return

	# Caso tenha espaços, irá tirar todos os espaços da escolha.
	entrada_valor_usuario = entrada_valor_usuario.replace(" ", "")

	# Enquanto o que o usuário digitou não for um número, ou seja,
	# contém caracteres diferentes de números ou valor digitado
	# for maior que 26, faça:
	while entrada_valor_usuario.isdigit() == False or int(entrada_valor_usuario) > 26:

		# Avise que ele errou na hora de digitar.
		print("[ERROR] Erro no recebimento do número!")

		# Peça para entrar outro número.
		entrada_valor_usuario = input("Entrada do número parece conter algum erro (valor máximo aceito = 26 rotações). Tente novamente: ")

		# Caso tenha espaços, irá tirar todos os espaços da escolha.
		entrada_valor_usuario = entrada_valor_usuario.replace(" ", "")

	# Para cada j de 0 até o tamanho do array onde contém a frase que o usúario
	# escreveu, faça:
	for j in range(0, len(frase_usuario)):
		
		# Encontre onde está cada letra da frase do usuário no alfabeto e retorne
		# sua localização.
		num_alfabeto = alfabeto.index(frase_usuario[j])

		# Se a escolha do usuário foi cifrar, faça:
		if escolha_usuario == "c":

			# Some essa localização com o número de rotações que o usuário solicitou.
			num_novo = int(num_alfabeto) + int(entrada_valor_usuario)

		# Se a escolha do usuário foi decifrar, faça:
		if escolha_usuario == "d":
	
			# Subtraia essa localização com o número de rotações que o usuário solicitou.
			num_novo = int(num_alfabeto) - int(entrada_valor_usuario)

		# Enquanto o número que vai identificar qual letra do alfabeto será colocada
		# no lugar da letra que o usuário digitou for maior que 25, faça:
		# Obs.: Isso é para que quando chegue a letra "z", o programa volte para
		# 		o início do alfabeto, no caso a letra "a".
		while num_novo > 25:

			# Faça um loop e volte ao início do array alfabeto.
			num_novo -= 26

		# Mude a letra antiga que foi escrita pelo usuário para a letra cifrada.
		frase_usuario[j] = alfabeto[num_novo]

	print("")

	# Se a escolha do usuário foi cifrar, faça:
	if escolha_usuario == "c":

		# Faz a junção de todas as letras cifradas, formando uma única string.
		monta_texto = "".join(frase_usuario)

		# Separa as letras em strings que contém 5 letras cada.
		monta_texto = [monta_texto[i:i+5] for i in range(0, len(monta_texto), 5)]

		# Faz a junção de tudo, separando com espaço.
		monta_texto = " ".join(monta_texto)

		# Apresente essa string cifrada para o usuário.
		print("Seu texto cifrado é -> " + monta_texto)

	# Se a escolha do usuário foi decifrar, faça:
	if escolha_usuario == "d":

		# Faz a junção de todas as letras decifradas, formando uma única string.
		monta_texto = "".join(frase_usuario)

		# Apresente essa string decifrada para o usuário.
		print("Seu texto decifrado é -> " + monta_texto)


# Função que vai listar todas as opções de rotação que podem ser feitas.
# É para o caso do usuário não souber qual rotação foi feita na mensagem.
def listaTodasOpcoes(alfabeto, frase, valor):

	# Inicia um array vazio toda vez que for chamada.
	# Obs.: Como está dentro de um "for", para cada loop do "for" esse array
	# 		é zerado.
	frase_usuario_nova = []

	# Para cada j entre 0 e o tamanho do array que contém a frase que o usuário
	# digitou, faça:
	for j in range(0, len(frase)):

		# Encontre onde está cada letra da frase do usuário no alfabeto e retorne
		# sua localização.
		num_alfabeto = alfabeto.index(frase[j])

		# Subtraia essa localização com o número de rotações atribuído pelo "for".
		num_novo = int(num_alfabeto) - int(valor)

		# Junte todas essas palavras no array frase_usuario_nova[].
		frase_usuario_nova.append(alfabeto[num_novo])

	# Junte todas as palavras dentro do array frase_usuario_nova[] e transforme em
	# uma string única.
	monta_texto_novo = "".join(frase_usuario_nova)

	print("")

	# Apresente cada uma dessa string decifrada para o usuário, contendo o número
	# da sua rotação.
	print("Seu texto decifrado com " + str(valor) + " rotação(ões) é -> " + monta_texto_novo)


# Função principal que chamará as outras funções.
def main():

	# Chama a função para cifrar/decifrar.
	cesarCipher()


if __name__ == "__main__":
	main()