import flet as ft
from flet_core import ImageFit
from datetime import datetime

entrenadores = {'entrenador':'123','entrenador2':'123'}
clientes = {'mario':'123'}
rutinas = {}
m = 0
ciclo_marcacion = 0
lista_marcaciones = []
usuario_actual =''
comidas_dic ={}

# Funciones adicionales pueden ser importadas aquí
# from funciones import *

def main(page: ft.Page):
    page.title = "Ejemplo de Navegación con Funciones"
    page.window.width = 780  # ancho ventana
    page.window.height = 800  # alto ventana
    page.window.maximizable = False  # maximizar desactivado
    page.padding = 24
    page.margin = 24
    page.bgcolor = ft.colors.BLACK  # volver transparente el fondo
    '''page.decoration = ft.BoxDecoration(image=ft.DecorationImage('fondo'))'''  # asignar imagen de fondo
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    txt_time = ft.Text(value="Hora actual: ", size=24)



    # Campos para el formulario y etiquetas

     #inicio sesion
    username_label = ft.Text("Nombre de Usuario",
                             weight=ft.FontWeight.BOLD,
                             size=20,
                             color=ft.colors.WHITE70)  # etiquetas

    password_label = ft.Text("Contraseña",
                             weight=ft.FontWeight.BOLD,
                             size=20,
                             font_family='consolas',
                             color=ft.colors.WHITE70)  # etiquetas

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
        global usuario_actual
        nonlocal logged_in  # Usar la variable externa
        usuario = username_field.value.lower()
        contraseña = password_field.value.lower()

        if usuario in entrenadores and entrenadores[usuario] == contraseña:
            logged_in = True
            lista_alumnos()  # Mostrar contenido de la pestaña "Explorar" al iniciar sesión
            usuario_actual = usuario

        elif usuario in clientes and clientes[usuario] == contraseña:
            logged_in =True
            usuario_actual = usuario
            inicio()
        else:
            page.add(ft.Text("Credenciales incorrectas.", color="red"))
            page.update()

    # Botón para iniciar sesión
    login_button = ft.ElevatedButton("Iniciar Sesión", on_click=login, bgcolor=ft.colors.RED_400)


    # Agregar los elementos a la página
    page.add(username_label,username_field,password_label, password_field, login_button)

    # SEPARADOR____________________________________________________________

    # PESTAÑAS USUARIO

    def inicio():
        global usuario_actual
        page.clean()  # Limpiar contenido anterior
        navegacion_usuario()

        column = ft.Column(spacing=100,
                           height=300,
                           scroll=ft.ScrollMode.ALWAYS,
                           expand=True)


        logout_button = ft.ElevatedButton("Cerrar Sesión", on_click=lambda e: logout())
        mensaje_123=ft.Text(usuario_actual)

        column.controls.append(logout_button)

        page.add(column)
        page.update()

    def rutina_asignada():
        global usuario_actual
        global rutinas
        page.clean()
        navegacion_usuario()

        mensaje_1 = ft.Text(f'{usuario_actual.upper()}, Tu Rutina es: ')


        def comprobacion_rutina():
            if usuario_actual in rutinas:
                page.clean()
                seleccion_rutina = rutinas[usuario_actual]
                mostrar_rutina = ft.Text(seleccion_rutina)
                page.add(mensaje_1,mostrar_rutina,volver_button)
                page.update()



            else:
                page.clean()
                no_rutina = ft.Text('Usuario no posee Rutina')
                page.add(mensaje_1,no_rutina,volver_button)
                page.update()

        volver_button = ft.ElevatedButton('Volver', on_click=lambda _: rutina_asignada())
        boton_verificar = ft.ElevatedButton('Verificar', on_click=lambda e: comprobacion_rutina())
        page.add(mensaje_1,boton_verificar)

    def comidas_asignadas():
        global usuario_actual
        global comidas_dic
        page.clean()
        navegacion_usuario()
        mensaje_1 = ft.Text(f'{usuario_actual.upper()}, Tus comidas son:')

        def comprobar():
            if usuario_actual in comidas_dic:
                page.clean()
                navegacion_usuario()
                revision_comidas = ft.Text(comidas_dic[usuario_actual])
                page.add(mensaje_1,revision_comidas,boton_volver)
                page.update()

            else:
                page.clean()
                mensaje_2 = ft.Text('Usuario no posee Comidas Asignadas')
                page.add(mensaje_1,mensaje_2,boton_volver)
                page.update()

        boton_volver = ft.ElevatedButton('Volver', on_click= lambda _:comidas_asignadas())
        boton_verificar = ft.ElevatedButton('Verificar', on_click=lambda e:comprobar())
        page.add(mensaje_1,boton_verificar)


    def preguntas_respuestas():
        page.clean()
        navegacion_usuario()
        page.title = "Menú Desplegable desde Diccionario"
        global entrenadores
        selected_option_text = ft.Text('Escoge una opcion')

        mostrar_profesores = ft.Dropdown(
            label="Selecciona un profesor",
            options=[
                ft.dropdown.Option(key) for key in entrenadores
            ])

        def seleccion_final():
            page.clean()
            navegacion_usuario()
            clave_seleccionada = mostrar_profesores.value

            if clave_seleccionada:
                mensaje_7 = ft.Text(f'seleccionaste a: {clave_seleccionada}')
                page.add(mensaje_7, boton_volver1)
                page.update()

        boton_seleccion = ft.ElevatedButton('Seleccionar', on_click=lambda e: seleccion_final())
        boton_volver1 = ft.ElevatedButton('Volver', on_click=lambda _: preguntas_respuestas())
        page.add(selected_option_text, mostrar_profesores, boton_seleccion)

    # SEPARADOR________________________________________________________________

    # PESTAÑAS ENTRENADOR

    def ingreso_alumnos():  # POSICION 0
        page.clean()
        navegacion_entrenador()
        nonlocal logged_in


        column = ft.Column(spacing=10)

        column.controls.append(ft.Text("Registro de Nuevos Usuarios"))

        new_username_field = ft.TextField(label="Nuevo Nombre de Usuario")
        new_password_field = ft.TextField(label="Nueva Contraseña", password=True)

        def register_user(e):
            nuevo_usuario = new_username_field.value
            nueva_contraseña = new_password_field.value

            if nuevo_usuario == '' and nueva_contraseña == '':
                column.controls.append(ft.Text("Por favor, completa ambos campos.", color="red"))
                page.update()  # Actualiza la página para mostrar el mensaje
                return  # Salir de la función si los campos están vacíos

            if nuevo_usuario in clientes:
                column.controls.append(ft.Text("El usuario ya existe.", color="white"))

            else:
                clientes[nuevo_usuario] = nueva_contraseña
                column.controls.append(ft.Text("Usuario registrado exitosamente.", color="white"))

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
        page.clean()
        navegacion_entrenador()
        lista =[]
        for i in clientes:
            lista.append(ft.Text(i))

        columna_alumno=ft.Column(controls=lista)
        etiqueta1 = ft.Text('Listado Alumnos',weight=ft.FontWeight.BOLD,size=30,color=ft.colors.WHITE70)
        logout_button = ft.ElevatedButton("Cerrar Sesión", on_click=lambda e: logout())
        page.add(etiqueta1,columna_alumno,logout_button)

        page.update()

    def agregar_rutinas():
        page.clean()
        navegacion_entrenador()
        rutina_clientes = ft.TextField(autofocus=True,hint_text='Ingresa el nombre de Cliente')


        def verificacion_usuario():
            r_c = rutina_clientes.value.lower()
            if r_c in clientes:
                if r_c not in rutinas:
                    page.clean()
                    ingreso_label = ft.Text(f'ingresa una rutina para:  {r_c.upper()}',weight=ft.FontWeight.BOLD,
                                            size=20,
                                            font_family='consolas',
                                            color=ft.colors.WHITE)

                    rutina_field= ft.TextField(autofocus=True, multiline=True)
                    page.add(ingreso_label,rutina_field)

                    boton_ingreso_rutina = ft.ElevatedButton('Ingresar rutina', on_click=lambda e: guardar(r_c, rutina_field.value))
                    page.add(boton_ingreso_rutina,boton_retroceso)

                else:
                    page.clean()
                    mensaje = ft.Text('El usuario ya tiene rutina')

                    # Asegúrate de que rutinas[r_c] existe antes de acceder
                    if r_c in rutinas:
                        mostrar = rutinas[r_c]# Accede directamente al valor
                        columna_rutina = ft.Column(
                            controls=[ft.Text(mostrar)])  # Asegúrate de que sea una lista de controles
                        page.add(columna_rutina, mensaje, boton_retroceso)
                    else:
                        page.add(ft.Text("No se encontró rutina para el usuario."), boton_retroceso)


            else:
                page.clean()
                mensaje = ft.Text('Usuario No encontrado')
                page.add(mensaje,boton_retroceso)

        def guardar(r_c,rutina):
            page.clean()
            rutinas[r_c]= rutina
            mensaje_final = ft.Text('Rutina guardada existosamente')
            print(rutinas)
            page.add(mensaje_final, boton_retroceso)

        etiqueta2 = ft.Text('Ingresar Rutinas', weight=ft.FontWeight.BOLD,size=30,color=ft.colors.WHITE70)
        boton_retroceso = ft.ElevatedButton('Volver',on_click=lambda e: agregar_rutinas())
        boton_buscar=ft.ElevatedButton('Buscar', on_click=lambda e: verificacion_usuario() )
        page.add(etiqueta2,rutina_clientes,boton_buscar)
        page.update()

    def marcacion():
        global ciclo_marcacion
        global m
        page.clean()
        navegacion_entrenador()
        texto_mensaje = ft.Text('Marcar Entrada y Salida',size=20, color=ft.colors.WHITE70)

        def final_marcacion():
            global m
            if m == 0:
                page.clean()
                text = ft.Text('Marcacion Efectuada')
                timer_clock = datetime.now().strftime('%H:%M:%S')
                reloj_clock = ft.Text(f' Hora de marcacion entrada: {timer_clock}')
                m=1
                lista_marcaciones.append(f'{usuario_actual} {timer_clock}')
                print(f'{lista_marcaciones}')
                page.add(text,reloj_clock,boton_marcacion_volver)
                page.update()

            elif m == 1:
                page.clean()
                text = ft.Text('Marcacion Efectuada')
                timer_clock = datetime.now().strftime('%H:%M:%S')
                reloj_clock = ft.Text(f' Hora de marcacion salida: {timer_clock}')
                m = 0
                lista_marcaciones.append(f'{usuario_actual} {timer_clock}')
                print(f'{lista_marcaciones}')
                page.add(text, reloj_clock,boton_marcacion_volver)
                page.update()

        boton_marcacion_entrada = ft.ElevatedButton('Entrada', on_click=lambda _: final_marcacion())
        boton_marcacion_salida = ft.ElevatedButton('Salida', on_click=lambda _: final_marcacion())
        boton_marcacion_volver = ft.ElevatedButton('Volver', on_click=lambda _: marcacion())

        if ciclo_marcacion ==0:
            page.add(texto_mensaje, boton_marcacion_entrada)
            ciclo_marcacion =1
        else:
            page.add(texto_mensaje,boton_marcacion_salida)
            ciclo_marcacion = 0

    def agregar_comidad():
        page.clean()
        navegacion_entrenador()
        ingresar_nombre_cliente = ft.TextField(autofocus=True, hint_text='ingresa nombre del cliente')
        page.update()

        def agregar():
            n_c = ingresar_nombre_cliente.value.lower()
            if n_c in clientes:
                if n_c not in comidas_dic:
                    page.clean()
                    ingreso_label = ft.Text(f'ingresa las comidas de:  {n_c.upper()}', weight=ft.FontWeight.BOLD,
                                            size=20,
                                            font_family='consolas',
                                            color=ft.colors.WHITE)
                    ingresar = ft.TextField(autofocus=True, hint_text='#ingresa las comidas', multiline=True)

                    page.add(ingreso_label,ingresar)

                    boton_ingreso = ft.ElevatedButton('Ingreso', on_click=lambda e: guardar_comida(n_c,ingresar.value.lower()))
                    page.add(boton_ingreso,boton_volver)
                    page.update()

                else:
                    page.clean()
                    mensaje = ft.Text('El Usuario ya contiene las comidas')

                    if n_c in comidas:
                        mostrar = comidas[n_c]
                        columna_comida = ft.Column(controls=[ft.Text(mostrar)])
                        page.add(columna_comida,boton_volver)
                        page.update()


            else:
                page.clean()
                mensaje = ft.Text('cliente no registrado')
                page.add(mensaje,boton_volver)
                page.update()

        def guardar_comida(n_c,comidass):
            page.clean()
            comidas_dic[n_c] = comidass
            mensaje_final_comida = ft.Text('Se agrego la pauta alimenticia')
            print(comidas_dic)
            page.add(mensaje_final_comida,boton_volver)
            page.update()


        boton_volver = ft.ElevatedButton('Volver', on_click=lambda e: agregar_comidad())
        boton_search = ft.ElevatedButton('Buscar', on_click=lambda _: agregar())
        page.add(ingresar_nombre_cliente, boton_search)


    #CERRAR SESION

    def logout():
        nonlocal logged_in
        logged_in = False  # Cambiar el estado a no autenticado
        username_field.value = ""  # Limpiar campos de inicio de sesión
        password_field.value = ""

        # Regresar a la pantalla de inicio de sesión
        page.clean()
        page.add(username_field, password_field, login_button)
        navegacion_usuario()
        navegacion_entrenador()

        page.update()


    #SEPARADOR_______________________________

    # Definir la función para manejar el cambio de pestañas usuario
    def on_tab_change(e):
        if not logged_in:
            return  # No hacer nada si no está autenticado

        print("Selected tab:", e.control.selected_index)  # Imprimir índice seleccionado

        # Llamar a la función correspondiente según la pestaña seleccionada
        if e.control.selected_index == 0:
            inicio()
        elif e.control.selected_index == 1:
            rutina_asignada()
        elif e.control.selected_index == 2:
            comidas_asignadas()
        elif e.control.selected_index == 3:
            preguntas_respuestas()
        elif e.control.selected_index==4:
            pass

    # Configurar la barra de navegación usuario
    def navegacion_usuario():

        if logged_in:
            page.navigation_bar = ft.CupertinoNavigationBar(
                bgcolor=ft.colors.RED_500,
                inactive_color=ft.colors.WHITE60,
                active_color=ft.colors.WHITE,
                destinations=[
                    ft.NavigationBarDestination(icon=ft.icons.EXPLORE, label="INICIO"),
                    ft.NavigationBarDestination(icon=ft.icons.SPORTS_GYMNASTICS, label="Rutina Asignada"),
                    ft.NavigationBarDestination(icon=ft.icons.RESTAURANT, label="Comidas Asignadas"),
                    ft.NavigationBarDestination(icon=ft.icons.RESTAURANT, label='Preguntas y Respuestas'),
                    ft.NavigationBarDestination(icon=ft.icons.SPORTS, label='Rutina Asignada')
                ],
                on_change=on_tab_change
            )

        else:
            page.navigation_bar = None

    # SEPARADOR_______________________________________________________________________


    #barra navegacion ENTRENADOR

    def barra_entrenador(e):
        if not logged_in:
            return  # No hacer nada si no está autenticado

        print("Selected tab:", e.control.selected_index)  # Imprimir índice seleccionado

        # Llamar a la función correspondiente según la pestaña seleccionada
        if e.control.selected_index == 0:
            lista_alumnos()
        elif e.control.selected_index == 1:
            ingreso_alumnos()
        elif e.control.selected_index == 2:
            agregar_rutinas()
        elif e.control.selected_index ==3:
            marcacion()
        elif e.control.selected_index==4:
            agregar_comidad()


    def navegacion_entrenador():

        if logged_in:
            page.navigation_bar = ft.CupertinoNavigationBar(
                bgcolor=ft.colors.RED_500,
                inactive_color=ft.colors.WHITE60,
                active_color=ft.colors.WHITE,
                destinations=[
                    ft.NavigationBarDestination(icon=ft.icons.PERSON, label="Alumnos"),
                    ft.NavigationBarDestination(icon=ft.icons.ADD_PHOTO_ALTERNATE, label="+Usuarios"),
                    ft.NavigationBarDestination(icon=ft.icons.LOCAL_RESTAURANT, label="Rutinas"),
                    ft.NavigationBarDestination(icon=ft.icons.TIMER, label='Horario'),
                    ft.NavigationBarDestination(icon=ft.icons.FOOD_BANK, label='+Comidas')

                ],
                on_change=barra_entrenador
            )

        else:
            page.navigation_bar = None

# Ejecutar la aplicación
ft.app(main)
