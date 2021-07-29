def aplicar_mascara(valor, mascara):
    indice = 0

    valor = str(valor)
    valor_convertido_em_lista = list(valor)

    while '#' in mascara:
        mascara = str(mascara).replace('#', str(valor_convertido_em_lista[indice]), 1)
        indice += 1
    
    return mascara