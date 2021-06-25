numeros = list()

while len(numeros) != 3:
    numero = int(input(f'Informe o {len(numeros) + 1}º número: '))
    numeros.append(numero)

primeiro_numero = numeros[0]
segundo_numero = numeros[1]
terceiro_numero = numeros[2]

menor_numero = None
maior_numero = None
numero_do_meio = None

if primeiro_numero < segundo_numero and segundo_numero < terceiro_numero:
    # 1 2 3
    menor_numero = primeiro_numero
    numero_do_meio = segundo_numero
    maior_numero = terceiro_numero

elif primeiro_numero > segundo_numero and primeiro_numero > terceiro_numero:
    # 3 2 1
    maior_numero = primeiro_numero

    if segundo_numero > terceiro_numero:
        numero_do_meio = segundo_numero
        menor_numero = terceiro_numero
    else:
        numero_do_meio = terceiro_numero
        menor_numero = segundo_numero

elif primeiro_numero > segundo_numero and primeiro_numero < terceiro_numero:
    # 2 1 3
    maior_numero = terceiro_numero

    if segundo_numero < terceiro_numero:
    	numero_do_meio = primeiro_numero
    	menor_numero = segundo_numero

print(menor_numero, numero_do_meio, maior_numero)
