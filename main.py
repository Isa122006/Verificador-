from verificador import verificar_minusculas, verificar_mayusculas, verificar_numeros, verificar_longitud

def evaluar_contraseña(password):
    # Inicializa el contador en 0
    contador = 0
    
    # Lista para almacenar los resultados de cada verificación
    verificaciones = []

    # Verificar minúsculas
    if verificar_minusculas(password):
        contador += 25
        verificaciones.append("Minúsculas: ✔")
    else:
        verificaciones.append("Minúsculas: ✘")

    # Verificar mayúsculas
    if verificar_mayusculas(password):
        contador += 25
        verificaciones.append("Mayúsculas: ✔")
    else:
        verificaciones.append("Mayúsculas: ✘")

    # Verificar números
    if verificar_numeros(password):
        contador += 25
        verificaciones.append("Números: ✔")
    else:
        verificaciones.append("Números: ✘")

    # Verificar longitud
    if verificar_longitud(password):
        contador += 25
        verificaciones.append("Longitud (> 8 caracteres): ✔")
    else:
        verificaciones.append("Longitud (> 8 caracteres): ✘")

    # Imprimir el nivel de seguridad y detalles de las verificaciones
    print("Resultados de las verificaciones:")
    for verificacion in verificaciones:
        print(verificacion)

    print(f"Nivel de seguridad de la contraseña: {contador}%")

# Solicitar al usuario ingresar la contraseña
if __name__ == "__main__":
    contraseña = input("Ingresa tu contraseña: ")
    evaluar_contraseña(contraseña)