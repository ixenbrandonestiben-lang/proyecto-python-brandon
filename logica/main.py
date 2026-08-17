import json
import os


# ============================================================
# CONFIGURACIÓN
# ============================================================

NOMBRE_ARCHIVO = "inventario.json"


# ============================================================
# MANEJO DEL ARCHIVO JSON
# ============================================================

def cargar_coleccion():
    """
    Carga los elementos almacenados en inventario.json.
    Si el archivo no existe, devuelve una colección vacía.
    """

    if not os.path.exists(NOMBRE_ARCHIVO):
        return []

    try:
        with open(NOMBRE_ARCHIVO, "r", encoding="utf-8") as archivo:
            datos = json.load(archivo)

            if isinstance(datos, list):
                return datos

            print("Error: el archivo no contiene una colección válida.")
            return []

    except json.JSONDecodeError:
        print("Error: inventario.json tiene un formato incorrecto.")
        return []

    except OSError as error:
        print(f"Error al cargar el archivo: {error}")
        return []


def guardar_coleccion(coleccion):
    """
    Guarda toda la colección en inventario.json.
    """

    try:
        with open(NOMBRE_ARCHIVO, "w", encoding="utf-8") as archivo:
            json.dump(
                coleccion,
                archivo,
                indent=4,
                ensure_ascii=False
            )

        print("\nColección guardada correctamente.")

    except OSError as error:
        print(f"\nError al guardar la colección: {error}")


# ============================================================
# VALIDACIÓN DE DATOS
# ============================================================

def pedir_opcion(mensaje, minimo, maximo):
    """
    Solicita una opción numérica dentro de un rango.
    """

    while True:
        try:
            opcion = int(input(mensaje))

            if minimo <= opcion <= maximo:
                return opcion

            print(
                f"Error: ingrese un número entre "
                f"{minimo} y {maximo}."
            )

        except ValueError:
            print("Error: debe ingresar un número válido.")


def pedir_texto(mensaje):
    """
    Solicita un texto obligatorio.
    """

    while True:
        texto = input(mensaje).strip()

        if texto:
            return texto

        print("Error: este campo no puede estar vacío.")


def pedir_valoracion():
    """
    Solicita una valoración entre 0 y 10.
    """

    while True:
        try:
            valoracion = float(
                input("Ingrese la valoración (0-10): ")
            )

            if 0 <= valoracion <= 10:
                return valoracion

            print("Error: la valoración debe estar entre 0 y 10.")

        except ValueError:
            print("Error: debe ingresar un número válido.")


def obtener_nuevo_id(coleccion):
    """
    Genera automáticamente un nuevo ID.
    """

    if not coleccion:
        return 1

    ids = [
        elemento.get("id", 0)
        for elemento in coleccion
        if isinstance(elemento.get("id", 0), int)
    ]

    if not ids:
        return 1

    return max(ids) + 1


# ============================================================
# MENÚ PRINCIPAL
# ============================================================

def mostrar_menu():
    print("""
===========================================
       ADMINISTRADOR DE COLECCIONES
===========================================
1. Añadir un nuevo elemento
2. Ver todos los elementos
3. Buscar un elemento
4. Editar un elemento
5. Eliminar un elemento
6. Ver elementos por categoría
7. Guardar y cargar colección
8. Salir
===========================================
""")

    return pedir_opcion(
        "Ingrese su opción aquí: ",
        1,
        8
    )


# ============================================================
# MENÚ AÑADIR
# ============================================================

def menu_anadir_nuevo_elemento():
    print("""
===========================================
        AÑADIR UN NUEVO ELEMENTO
===========================================
¿Qué tipo de elemento deseas añadir?

1. Libro
2. Película
3. Música
4. Regresar al menú principal
===========================================
""")

    return pedir_opcion(
        "Seleccione una opción (1-4): ",
        1,
        4
    )


# ============================================================
# MENÚ VER
# ============================================================

def menu_ver_elementos():
    print("""
===========================================
         VER TODOS LOS ELEMENTOS
===========================================
¿Qué categoría deseas ver?

1. Ver todos los libros
2. Ver todas las películas
3. Ver toda la música
4. Regresar al menú principal
===========================================
""")

    return pedir_opcion(
        "Seleccione una opción (1-4): ",
        1,
        4
    )


# ============================================================
# MENÚ BUSCAR
# ============================================================

def menu_buscar_elemento():
    print("""
===========================================
            BUSCAR UN ELEMENTO
===========================================
¿Cómo deseas buscar?

1. Buscar por título
2. Buscar por autor/director/artista
3. Buscar por género
4. Regresar al menú principal
===========================================
""")

    return pedir_opcion(
        "Seleccione una opción (1-4): ",
        1,
        4
    )


# ============================================================
# MENÚ EDITAR
# ============================================================

def menu_editar_elemento():
    print("""
===========================================
            EDITAR UN ELEMENTO
===========================================
¿Qué tipo de cambio deseas realizar?

1. Editar título
2. Editar autor/director/artista
3. Editar género
4. Editar valoración
5. Regresar al menú principal
===========================================
""")

    return pedir_opcion(
        "Seleccione una opción (1-5): ",
        1,
        5
    )


# ============================================================
# MENÚ ELIMINAR
# ============================================================

def menu_eliminar_elemento():
    print("""
===========================================
           ELIMINAR UN ELEMENTO
===========================================
¿Cómo deseas eliminar?

1. Eliminar por título
2. Eliminar por identificador único
3. Regresar al menú principal
===========================================
""")

    return pedir_opcion(
        "Seleccione una opción (1-3): ",
        1,
        3
    )


# ============================================================
# MENÚ CATEGORÍA
# ============================================================

def menu_ver_elementos_por_categoria():
    print("""
===========================================
       VER ELEMENTOS POR CATEGORÍA
===========================================
¿Qué categoría deseas ver?

1. Ver libros
2. Ver películas
3. Ver música
4. Regresar al menú principal
===========================================
""")

    return pedir_opcion(
        "Seleccione una opción (1-4): ",
        1,
        4
    )


# ============================================================
# MENÚ GUARDAR / CARGAR
# ============================================================

def menu_guardar_cargar_coleccion():
    print("""
===========================================
        GUARDAR Y CARGAR COLECCIÓN
===========================================
¿Qué deseas hacer?

1. Guardar la colección actual
2. Cargar una colección guardada
3. Regresar al menú principal
===========================================
""")

    return pedir_opcion(
        "Seleccione una opción (1-3): ",
        1,
        3
    )


# ============================================================
# AÑADIR ELEMENTOS
# ============================================================

def anadir_elemento(coleccion, tipo):
    """
    Añade un libro, película o música.
    """

    print("\n===========================================")
    print(f"            AÑADIR {tipo.upper()}")
    print("===========================================")

    titulo = pedir_texto("Ingrese el título: ")

    autor = pedir_texto(
        "Ingrese el autor/director/artista: "
    )

    genero = pedir_texto(
        "Ingrese el género: "
    )

    valoracion = pedir_valoracion()

    nuevo_elemento = {
        "id": obtener_nuevo_id(coleccion),
        "tipo": tipo,
        "titulo": titulo,
        "autor": autor,
        "genero": genero,
        "valoracion": valoracion
    }

    coleccion.append(nuevo_elemento)

    print("\nElemento añadido correctamente.")
    print(
        f"Identificador asignado: "
        f"{nuevo_elemento['id']}"
    )


# ============================================================
# MOSTRAR ELEMENTOS
# ============================================================

def mostrar_elemento(elemento):
    """
    Muestra la información de un elemento.
    """

    print("-------------------------------------------")
    print(f"ID:          {elemento.get('id', 'N/A')}")
    print(f"Tipo:        {elemento.get('tipo', 'N/A')}")
    print(f"Título:      {elemento.get('titulo', 'N/A')}")
    print(f"Autor:       {elemento.get('autor', 'N/A')}")
    print(f"Género:      {elemento.get('genero', 'N/A')}")
    print(
        f"Valoración:  "
        f"{elemento.get('valoracion', 'N/A')}"
    )


def mostrar_elementos(coleccion, tipo=None):
    """
    Muestra todos los elementos o solamente
    los elementos de una categoría.
    """

    if tipo is None:
        elementos = coleccion
    else:
        elementos = [
            elemento
            for elemento in coleccion
            if elemento.get("tipo", "").lower()
            == tipo.lower()
        ]

    if not elementos:
        print("\nNo existen elementos para mostrar.")
        return

    print("\n===========================================")
    print("              COLECCIÓN")
    print("===========================================")

    for elemento in elementos:
        mostrar_elemento(elemento)

    print("-------------------------------------------")
    print(f"Total de elementos mostrados: {len(elementos)}")


# ============================================================
# BÚSQUEDAS
# ============================================================

def mostrar_resultados_busqueda(resultados):
    if not resultados:
        print("\nNo se encontraron elementos.")
        return

    print(
        f"\nSe encontraron "
        f"{len(resultados)} elemento(s)."
    )

    for elemento in resultados:
        mostrar_elemento(elemento)

    print("-------------------------------------------")


def buscar_por_titulo(coleccion):
    titulo = pedir_texto(
        "Ingrese el título que desea buscar: "
    )

    resultados = [
        elemento
        for elemento in coleccion
        if titulo.lower()
        in elemento.get("titulo", "").lower()
    ]

    mostrar_resultados_busqueda(resultados)


def buscar_por_autor(coleccion):
    autor = pedir_texto(
        "Ingrese el autor/director/artista: "
    )

    resultados = [
        elemento
        for elemento in coleccion
        if autor.lower()
        in elemento.get("autor", "").lower()
    ]

    mostrar_resultados_busqueda(resultados)


def buscar_por_genero(coleccion):
    genero = pedir_texto(
        "Ingrese el género que desea buscar: "
    )

    resultados = [
        elemento
        for elemento in coleccion
        if genero.lower()
        in elemento.get("genero", "").lower()
    ]

    mostrar_resultados_busqueda(resultados)


# ============================================================
# BUSCAR POR ID
# ============================================================

def buscar_por_id(coleccion, identificador):
    """
    Busca un elemento utilizando su ID.
    """

    for elemento in coleccion:
        if elemento.get("id") == identificador:
            return elemento

    return None


# ============================================================
# EDITAR ELEMENTOS
# ============================================================

def seleccionar_elemento_para_editar(coleccion):
    if not coleccion:
        print("\nLa colección está vacía.")
        return None

    try:
        identificador = int(
            input(
                "Ingrese el ID del elemento "
                "que desea editar: "
            )
        )

    except ValueError:
        print("Error: debe ingresar un ID numérico.")
        return None

    elemento = buscar_por_id(
        coleccion,
        identificador
    )

    if elemento is None:
        print(
            "\nNo se encontró ningún elemento "
            "con ese ID."
        )
        return None

    print("\nElemento seleccionado:")
    mostrar_elemento(elemento)

    return elemento


def editar_titulo(coleccion):
    elemento = seleccionar_elemento_para_editar(
        coleccion
    )

    if elemento is None:
        return

    elemento["titulo"] = pedir_texto(
        "Ingrese el nuevo título: "
    )

    print("\nTítulo actualizado correctamente.")


def editar_autor(coleccion):
    elemento = seleccionar_elemento_para_editar(
        coleccion
    )

    if elemento is None:
        return

    elemento["autor"] = pedir_texto(
        "Ingrese el nuevo autor/director/artista: "
    )

    print(
        "\nAutor/director/artista "
        "actualizado correctamente."
    )


def editar_genero(coleccion):
    elemento = seleccionar_elemento_para_editar(
        coleccion
    )

    if elemento is None:
        return

    elemento["genero"] = pedir_texto(
        "Ingrese el nuevo género: "
    )

    print("\nGénero actualizado correctamente.")


def editar_valoracion(coleccion):
    elemento = seleccionar_elemento_para_editar(
        coleccion
    )

    if elemento is None:
        return

    elemento["valoracion"] = pedir_valoracion()

    print(
        "\nValoración actualizada correctamente."
    )


# ============================================================
# ELIMINAR ELEMENTOS
# ============================================================

def confirmar_eliminacion():
    while True:
        respuesta = input(
            "¿Está seguro de eliminarlo? (s/n): "
        ).strip().lower()

        if respuesta in ("s", "n"):
            return respuesta == "s"

        print("Error: responda solamente s o n.")


def eliminar_por_titulo(coleccion):
    titulo = pedir_texto(
        "Ingrese el título que desea eliminar: "
    )

    resultados = [
        elemento
        for elemento in coleccion
        if titulo.lower()
        in elemento.get("titulo", "").lower()
    ]

    if not resultados:
        print(
            "\nNo se encontró ningún elemento "
            "con ese título."
        )
        return

    print("\nElementos encontrados:")

    for elemento in resultados:
        mostrar_elemento(elemento)

    try:
        identificador = int(
            input(
                "\nIngrese el ID del elemento "
                "que desea eliminar: "
            )
        )

    except ValueError:
        print("Error: debe ingresar un ID válido.")
        return

    elemento = buscar_por_id(
        coleccion,
        identificador
    )

    if elemento is None:
        print(
            "\nNo se encontró un elemento "
            "con ese ID."
        )
        return

    if confirmar_eliminacion():
        coleccion.remove(elemento)
        print("\nElemento eliminado correctamente.")
    else:
        print("\nOperación cancelada.")


def eliminar_por_id(coleccion):
    if not coleccion:
        print("\nLa colección está vacía.")
        return

    try:
        identificador = int(
            input(
                "Ingrese el ID del elemento "
                "que desea eliminar: "
            )
        )

    except ValueError:
        print("Error: debe ingresar un ID válido.")
        return

    elemento = buscar_por_id(
        coleccion,
        identificador
    )

    if elemento is None:
        print(
            "\nNo se encontró ningún elemento "
            "con ese ID."
        )
        return

    print("\nElemento seleccionado:")
    mostrar_elemento(elemento)

    if confirmar_eliminacion():
        coleccion.remove(elemento)
        print("\nElemento eliminado correctamente.")
    else:
        print("\nOperación cancelada.")


# ============================================================
# PROGRAMA PRINCIPAL
# ============================================================

def ejecutar_programa():

    coleccion = cargar_coleccion()

    print("\n===========================================")
    print("     ADMINISTRADOR DE COLECCIONES")
    print("===========================================")
    print(
        f"Elementos cargados: {len(coleccion)}"
    )

    while True:

        opcion = mostrar_menu()

        # ----------------------------------------------------
        # OPCIÓN 1: AÑADIR
        # ----------------------------------------------------

        if opcion == 1:

            sub_opcion = menu_anadir_nuevo_elemento()

            if sub_opcion == 1:

                anadir_elemento(
                    coleccion,
                    "Libro"
                )

            elif sub_opcion == 2:

                anadir_elemento(
                    coleccion,
                    "Película"
                )

            elif sub_opcion == 3:

                anadir_elemento(
                    coleccion,
                    "Música"
                )

            elif sub_opcion == 4:

                print(
                    "\nVolviendo al menú principal."
                )

        # ----------------------------------------------------
        # OPCIÓN 2: VER ELEMENTOS
        # ----------------------------------------------------

        elif opcion == 2:

            sub_opcion = menu_ver_elementos()

            if sub_opcion == 1:

                mostrar_elementos(
                    coleccion,
                    "Libro"
                )

            elif sub_opcion == 2:

                mostrar_elementos(
                    coleccion,
                    "Película"
                )

            elif sub_opcion == 3:

                mostrar_elementos(
                    coleccion,
                    "Música"
                )

            elif sub_opcion == 4:

                print(
                    "\nVolviendo al menú principal."
                )

        # ----------------------------------------------------
        # OPCIÓN 3: BUSCAR
        # ----------------------------------------------------

        elif opcion == 3:

            sub_opcion = menu_buscar_elemento()

            if sub_opcion == 1:

                buscar_por_titulo(
                    coleccion
                )

            elif sub_opcion == 2:

                buscar_por_autor(
                    coleccion
                )

            elif sub_opcion == 3:

                buscar_por_genero(
                    coleccion
                )

            elif sub_opcion == 4:

                print(
                    "\nVolviendo al menú principal."
                )

        # ----------------------------------------------------
        # OPCIÓN 4: EDITAR
        # ----------------------------------------------------

        elif opcion == 4:

            sub_opcion = menu_editar_elemento()

            if sub_opcion == 1:

                editar_titulo(
                    coleccion
                )

            elif sub_opcion == 2:

                editar_autor(
                    coleccion
                )

            elif sub_opcion == 3:

                editar_genero(
                    coleccion
                )

            elif sub_opcion == 4:

                editar_valoracion(
                    coleccion
                )

            elif sub_opcion == 5:

                print(
                    "\nVolviendo al menú principal."
                )

        # ----------------------------------------------------
        # OPCIÓN 5: ELIMINAR
        # ----------------------------------------------------

        elif opcion == 5:

            sub_opcion = menu_eliminar_elemento()

            if sub_opcion == 1:

                eliminar_por_titulo(
                    coleccion
                )

            elif sub_opcion == 2:

                eliminar_por_id(
                    coleccion
                )

            elif sub_opcion == 3:

                print(
                    "\nVolviendo al menú principal."
                )

        # ----------------------------------------------------
        # OPCIÓN 6: CATEGORÍAS
        # ----------------------------------------------------

        elif opcion == 6:

            sub_opcion = (
                menu_ver_elementos_por_categoria()
            )

            if sub_opcion == 1:

                mostrar_elementos(
                    coleccion,
                    "Libro"
                )

            elif sub_opcion == 2:

                mostrar_elementos(
                    coleccion,
                    "Película"
                )

            elif sub_opcion == 3:

                mostrar_elementos(
                    coleccion,
                    "Música"
                )

            elif sub_opcion == 4:

                print(
                    "\nVolviendo al menú principal."
                )

        # ----------------------------------------------------
        # OPCIÓN 7: GUARDAR / CARGAR
        # ----------------------------------------------------

        elif opcion == 7:

            sub_opcion = (
                menu_guardar_cargar_coleccion()
            )

            if sub_opcion == 1:

                guardar_coleccion(
                    coleccion
                )

            elif sub_opcion == 2:

                coleccion = cargar_coleccion()

                print(
                    "\nColección cargada correctamente."
                )

                print(
                    f"Elementos cargados: "
                    f"{len(coleccion)}"
                )

            elif sub_opcion == 3:

                print(
                    "\nVolviendo al menú principal."
                )

        # ----------------------------------------------------
        # OPCIÓN 8: SALIR
        # ----------------------------------------------------

        elif opcion == 8:

            print("\n===========================================")
            print("         FINALIZANDO EL PROGRAMA")
            print("===========================================")

            guardar_coleccion(
                coleccion
            )

            print("Saliendo del programa...")
            print("Vuelve pronto.")

            break


# ============================================================
# INICIO
# ============================================================

if __name__ == "__main__":
    ejecutar_programa()