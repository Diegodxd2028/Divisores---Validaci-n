def obtener_divisores(numero):
    divisores = []
    for i in range(1, numero + 1):
        if numero % i == 0:
            divisores.append(i)
    return divisores


def leer_numero_natural():
    while True:
        try:
            entrada = input("Ingrese un número natural: ")
            numero = int(entrada)
            if numero <= 0:
                raise ValueError("El número debe ser un entero positivo.")
            return numero
        except ValueError as ve:
            print(f"Error: {ve}. Inténtelo de nuevo.")


if __name__ == "__main__":
    # Leer número natural
    numero = leer_numero_natural()

    # Calcular y mostrar los divisores
    divisores = obtener_divisores(numero)
    print(f"Los divisores de {numero} son: {divisores}")
