import flet as ft
from flet_core import ImageFit

entrenadores = {'entrenador':'123'}
clientes = {'sofia':'123'}

# Funciones adicionales pueden ser importadas aquí
# from funciones import *

def main(page: ft.Page):
    page.title = "Ejemplo de Navegación con Funciones"
    page.window.width = 780  # ancho ventana
    page.window.height = 800  # alto ventana
    page.window.maximizable = False  # maximizar desactivado
    page.padding = 24
    page.margin = 24
    page.bgcolor = ft.colors.TRANSPARENT  # volver transparente el fondo
    page.decoration = ft.BoxDecoration(image=ft.DecorationImage('fondo'))  # asignar imagen de fondo
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER



    # Campos para el formulario
    username_label = ft.Text("Nombre de Usuario",
                             weight=ft.FontWeight.BOLD,
                             size=20,
                             color=ft.colors.PURPLE_500)  # etiquetas

    password_label = ft.Text("Contraseña",
                             weight=ft.FontWeight.BOLD,
                             size=20,
                             font_family='consolas',
                             color=ft.colors.PURPLE_500)  # etiquetas

    # Crear campos de texto e tiquetas
    username_field = ft.TextField(
        autofocus=True,
        hint_text="Ingresa tu nombre de usuario",

    )

    password_field = ft.TextField(
        password=True,
        hint_text="Ingresa tu contraseña"
    )

    #SEPARADOR_________________________________________________________________

    #inicio se sesion

    # Variable para almacenar si el usuario ha iniciado sesión
    logged_in = False

    # Función de inicio de sesión
    def login(e):
        nonlocal logged_in  # Usar la variable externa
        usuario = username_field.value.lower()
        contraseña = password_field.value.lower()

        if usuario in entrenadores and entrenadores[usuario] == contraseña:
            logged_in = True
            inicio()  # Mostrar contenido de la pestaña "Explorar" al iniciar sesión
        elif usuario in clientes and clientes[usuario] == contraseña:
            logged_in =True
            inicio()
        else:
            page.add(ft.Text("Credenciales incorrectas.", color="red"))
            page.update()

    # Botón para iniciar sesión
    login_button = ft.ElevatedButton("Iniciar Sesión", on_click=login)

    # Agregar los elementos a la página
    page.add(username_label,username_field,password_label, password_field, login_button)

    # SEPARADOR____________________________________________________________

    # PESTAÑAS USUARIO

    def inicio():
        page.clean()  # Limpiar contenido anterior
        navegacion()

        column = ft.Column(spacing=100,
                           height=300,
                           scroll=ft.ScrollMode.ALWAYS,
                           expand=True)

        '''for n in range(1, 101):
            column.controls.append(ft.Text(20 * '_' + str(n), size=20, color=ft.colors.BLACK))'''

        logout_button = ft.ElevatedButton("Cerrar Sesión", on_click=lambda e: logout())

        column.controls.append(logout_button)

        page.add(column)
        page.update()

    def rutina():
        page.clean()
        navegacion()

        column = ft.Column(spacing=100,
                           height=300,
                           scroll=ft.ScrollMode.ALWAYS,
                           expand=True)

        page.clean()  # Limpiar contenido anterior
        page.add(ft.Text("Contenido de la pestaña Desplazamiento"))

        logout_button = ft.ElevatedButton("Cerrar Sesión", on_click=lambda e: logout())
        column.controls.append(logout_button)

        page.update()

    def comidas():
        page.clean()
        navegacion()

        column = ft.Column(spacing=100,
                           height=300,
                           scroll=ft.ScrollMode.ALWAYS,
                           expand=True)

        page.clean()  # Limpiar contenido anterior
        page.add(ft.Text("Contenido de la pestaña Marcador"))

        logout_button = ft.ElevatedButton("Cerrar Sesión", on_click=lambda e: logout())
        column.controls.append(logout_button)

        page.update()

    # Definir la función para manejar el cambio de pestañas usuario
    def on_tab_change(e):
        if not logged_in:
            return  # No hacer nada si no está autenticado

        print("Selected tab:", e.control.selected_index)  # Imprimir índice seleccionado

        # Llamar a la función correspondiente según la pestaña seleccionada
        if e.control.selected_index == 0:
            inicio()
        elif e.control.selected_index == 1:
            comidas()
        elif e.control.selected_index == 2:
            pass

    # SEPARADOR________________________________________________________________

    # PESTAÑAS ENTRENADOR

    def ingreso_alumnos():  # POSICION 0
        navegacion()
        nonlocal logged_in
        page.clean()

        column = ft.Column(spacing=10)

        column.controls.append(ft.Text("Registro de Nuevos Usuarios"))

        new_username_field = ft.TextField(label="Nuevo Nombre de Usuario")
        new_password_field = ft.TextField(label="Nueva Contraseña", password=True)

        def register_user(e):

            nuevo_usuario = new_username_field.value
            nueva_contraseña = new_password_field.value

            if nuevo_usuario in clientes:
                column.controls.append(ft.Text("El usuario ya existe.", color="black"))

            else:
                clientes[nuevo_usuario] = nueva_contraseña
                column.controls.append(ft.Text("Usuario registrado exitosamente.", color="black"))

            new_username_field.value = ""
            new_password_field.value = ""
            page.update()

        register_button = ft.ElevatedButton("Registrar Usuario", on_click=register_user)

        column.controls.extend([new_username_field, new_password_field, register_button])

        # Botón para cerrar sesión
        logout_button = ft.ElevatedButton("Cerrar Sesión", on_click=lambda e: logout())

        column.controls.append(logout_button)

        page.add(column)
        page.update()


    def lista_alumnos():

        lista =[]
        for i in clientes:
            lista.append(ft.Text(i))

        columna_alumno=ft.Column(controls=lista)
        page.add(columna_alumno)
        page.update()


    #CERRAR SESION

    def logout():
        nonlocal logged_in
        logged_in = False  # Cambiar el estado a no autenticado
        username_field.value = ""  # Limpiar campos de inicio de sesión
        password_field.value = ""

        # Regresar a la pantalla de inicio de sesión
        page.clean()
        page.add(username_field, password_field, login_button)
        navegacion()

        page.update()


    #SEPARADOR_______________________________

    # Configurar la barra de navegación usuario

    def on_tab_change(e):
        if not logged_in:
            return  # No hacer nada si no está autenticado

        print("Selected tab:", e.control.selected_index)  # Imprimir índice seleccionado

        # Llamar a la función correspondiente según la pestaña seleccionada
        if e.control.selected_index == 0:
            lista_alumnos()
        elif e.control.selected_index == 1:
            comidas()
        elif e.control.selected_index == 2:
            pass


    def navegacion():

        if logged_in:
            page.navigation_bar = ft.CupertinoNavigationBar(
                bgcolor=ft.colors.RED_ACCENT_100,
                inactive_color=ft.colors.WHITE60,
                active_color=ft.colors.WHITE,
                destinations=[
                    ft.NavigationBarDestination(icon=ft.icons.EXPLORE, label="INICIO"),
                    ft.NavigationBarDestination(icon=ft.icons.SPORTS_GYMNASTICS, label="RUTINA"),
                    ft.NavigationBarDestination(icon=ft.icons.LOCAL_RESTAURANT, label="COMIDAS")
                ],
                on_change=on_tab_change
            )

        else:
            page.navigation_bar = None


    # SEPARADOR_______________________________________________________________________

# Ejecutar la aplicación
ft.app(main)
