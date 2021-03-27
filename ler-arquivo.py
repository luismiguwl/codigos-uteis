import csv

def obterLista():
	with open('nomeDoArquivo.csv', 'r', encoding = 'utf-8') as file:
		lista = []
		leitor = csv.reader(file)

		for linha in leitor:
			lista.append(linha)
		file.close()

		# remove o cabeçalho
		lista.pop(0);

		return lista

lista = list(obterLista())