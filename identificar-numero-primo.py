def identificarNumeroPrimo(numero):
	if numero == 1:
		return False

	if numero == 2 or numero == 3:
		return True

	if numero % 2 == 0 or numero % 3 == 0:
		return False

	return True