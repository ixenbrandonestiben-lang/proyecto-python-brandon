from inventario import *

def mostrar_menu():
    menu = """    ===========================================
         Administrador de colecciones
    ==========================================
    1. Añadir un nuevo elemento
    2. Ver Todos los Elementos
    3. Buscar un Elemento
    4. Editar un Elemento
    5. Eliminar un Elemento
    6. Ver Elementos por Categoría
    7. Guardar y Cargar Colección
    8. Salir
    ===========================================
    elecciona una opcion (1-8):
    """
    print (menu)
    opc = int(input("Ingrese su opcion aqui: "))
    return opc
  
def menu_añadir_nuevo_elemento():
    menu = """    ===========================================
        Añadir un Nuevo Elemento
    ===========================================
    ¿Qué tipo de elemento deseas añadir?
    1. Libro
    2. Película
    3. Música
    4. Regresar al Menú Principal
    ===========================================
    Selecciona una opción (1-4): """
    print(menu)
    opc = int(input("Ingrese su opcion aqui: "))
    return opc  
                            
def menu_ver_elementos():
    menu ="""    ===========================================
        Ver Todos los Elementos
    ===========================================
    ¿Qué categoría deseas ver?
    1. Ver Todos los Libros
    2. Ver Todas las Películas
    3. Ver Toda la Música
    4. Regresar al Menú Principal
    ===========================================
    Selecciona una opción (1-4):"""
    print(menu)
    opc = int(input("Ingrese su opcion aqui: "))
    return opc

def mune_buscar_elemento():
    menu = """===========================================
    Buscar un Elemento
    ===========================================
    ¿Cómo deseas buscar?
    1. Buscar por Título
    2. Buscar por Autor/Director/Artista
    3. Buscar por Género
    4. Regresar al Menú Principal
    ===========================================
    Selecciona una opción (1-4): """
    print(menu)
    opc = int(input("Ingrese su opcion aqui: "))
    return opc

def menu_editar_elemento():
    menu="""===========================================
    Editar un Elemento
    ===========================================
    ¿Qué tipo de cambio deseas realizar?
    1. Editar Título
    2. Editar Autor/Director/Artista
    3. Editar Género
    4. Editar Valoración
    5. Regresar al Menú Principal
    ===========================================
    Selecciona una opción (1-5):"""
    print(menu)
    opc = int(input("Ingrese su opcion aqui: "))
    return opc

def menu_eliminar_elemento():
    menu ="""===========================================
    Eliminar un Elemento
    ===========================================
    ¿Cómo deseas eliminar?
    1. Eliminar por Título
    2. Eliminar por Identificador Único
    3. Regresar al Menú Principal
    ===========================================
    Selecciona una opción (1-3):"""
    print(menu)
    opc = int(input("Ingrese su opcion aqui: "))
    return opc

def menu_ver_elementos_por_categoria():
    menu ="""===========================================
    Ver Elementos por Categoría
    ===========================================
    ¿Qué categoría deseas ver?
    1. Ver Libros
    2. Ver Películas
    3. Ver Música
    4. Regresar al Menú Principal
    ===========================================
    Selecciona una opción (1-4):"""
    print(menu)
    opc = int(input("Ingrese su opcion aqui: "))
    return opc

def menu_guardar_cargar_coeccion():
    menu = """===========================================
    Guardar y Cargar Colección
    ===========================================
    ¿Qué deseas hacer?
    1. Guardar la Colección Actual
    2. Cargar una Colección Guardada
    3. Regresar al Menú Principal
    ===========================================
    Selecciona una opción (1-3):"""
    print(menu)
    opc = int(input("Ingrese su opcion aqui: "))
    return opc

nombre_Archivo = "Libreria.json" 

while True:
    opc = mostrar_menu()
    if opc ==1 :
        menu_añadir_nuevo_elemento()
        if opc == 1:
            Añadir(nombre_Archivo)
        elif opc ==2:
            agregar(nombre_Archivo)
        elif opc == 3:
            agregar(nombre_Archivo)
        elif opc == 4:
            print("volviendo al menu principal")
    elif opc == 2:
        menu_ver_elementos()
    elif opc == 3:
        mune_buscar_elemento()
    elif opc == 4:
        menu_editar_elemento
    elif opc == 5:
        menu_eliminar_elemento()
    elif opc == 6:
        menu_ver_elementos_por_categoria
    elif opc == 7:
        menu_guardar_cargar_coeccion()
    elif opc == 8:
        print("finalizando el proceso. \n saliendo del programa \n vuelve pronto  ")
        break
    else:
        print("error, esta mal en algo!!!")
    