# Función para verificar si la contraseña tiene letras minúsculas
def verificar_minusculas(password):
    return any(letra.islower() for letra in password)

# Función para verificar si la contraseña tiene letras mayúsculas
def verificar_mayusculas(password):
    return any(letra.isupper() for letra in password)

# Función para verificar si la contraseña tiene números
def verificar_numeros(password):
    return any(letra.isdigit() for letra in password)

# Función para verificar si la contraseña tiene más de 8 caracteres
def verificar_longitud(password):
    return len(password) > 8