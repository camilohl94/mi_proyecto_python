def saludar(nombre):
    """
    Función que saluda a una persona.

    Args:
        nombre: El nombre de la persona a la que se saluda.

    Returns:
        Un mensaje de saludo.
    """
    return f"¡Hola, {nombre}!"

def despedirse(nombre):
    """
    Función que se despide de una persona.

    Args:
        nombre: El nombre de la persona a la que se despide.

    Returns:
        Un mensaje de despedida.
    """
    return f"¡Adiós, {nombre}!"


todos=['hacer de comer', 'lavar la ropa','practicar python']

def subir_todo(todos):
    tarea= input('ingresa tu tarea pendiente: ')
    todos.append(tarea)
    return todos

def ver_todos(todos):
    print(todos)
opcion =''
while opcion !='3':
    opcion =input('elija una opcio: \n'
                  '1. agregar tarea \n'
                  '2. ver tareas\n'
                  '3. salir')
    if opcion =='1':
        subir_todo(todos)
    elif opcion == '2':
        ver_todos(todos)
    else:
        print('opcion no valida')


if __name__ == "__main__":
    nombre = input("Ingrese su nombre: ")
    saludo = saludar(nombre)
    print(saludo)
    despedida = despedirse(nombre)
    print(despedida)