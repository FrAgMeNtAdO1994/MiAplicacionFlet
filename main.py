import flet as ft
from flet_core import ImageFit
from datetime import datetime
import time
import mysql.connector


contador_respuestas = 1
entrenadores = {'entrenador':'123','entrenador2':'123'}
clientes = {'mario':'123'}
rutinas = {}
m = 0
ciclo_marcacion = 0
lista_marcaciones = []
usuario_actual =''
comidas_dic ={}
Preguntas_variable = {}
respuestas_dic ={}


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
    '''page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER'''
    txt_time = ft.Text(value="Hora actual: ", size=24)

    # conexion base de datos local
    db = mysql.connector.connect(
        user='**',
        password='***',
        host='****',
        port='**',
        database='**'

    )
    print(db)



    # Campos para el formulario y etiquetas

     #inicio sesion

    username_label = ft.Container(content=ft.Text("Nombre de Usuario",
                             weight=ft.FontWeight.BOLD,
                             size=20,
                             color=ft.colors.WHITE70,
                             font_family='consolas'),
                                  border=ft.border.all(2,ft.colors.WHITE70),
                                  bgcolor=ft.colors.BROWN_900,
                                  border_radius=30,
                                  padding=5,
                                  margin=10)

    password_label = ft.Container(content=ft.Text("Contraseña",
                             weight=ft.FontWeight.BOLD,
                             size=20,
                             color=ft.colors.WHITE70,
                             font_family='consolas'),
                                  border=ft.border.all(2,ft.colors.WHITE70),
                                  bgcolor=ft.colors.BROWN_900,
                                  border_radius=30,
                                  padding=5,
                                  margin=10)

    # Crear campos de texto e tiquetas
    username_field = ft.TextField(
        autofocus=True,
        hint_text="Ingresa tu nombre de usuario")
    contenedor_username = ft.Container(content=username_field,border_radius=6, border=ft.border.all(2,ft.colors.GREY_600))


    password_field = ft.TextField(
        password=True,
        hint_text="Ingresa tu contraseña")
    contenedor_password = ft.Container(content=password_field,border_radius=6, border=ft.border.all(2,ft.colors.GREY_600))


    #SEPARADOR_________________________________________________________________

    #inicio se sesion

    # Variable para almacenar si el usuario ha iniciado sesión


    # SEPARADOR____________________________________________________________

    # PESTAÑAS USUARIO

    def inicio():
        global usuario_actual
        page.clean()  # Limpiar contenido anterior
        page.bgcolor = ft.colors.TRANSPARENT
        page.decoration = ft.BoxDecoration(image=ft.DecorationImage('fondo1.jpg'))
        navegacion_usuario()

        column = ft.Column(spacing=100,
                           height=300,
                           scroll=ft.ScrollMode.ALWAYS,
                           expand=True)



        mensaje_123=ft.Text(usuario_actual)

        column.controls.append(logout_button)

        page.add(column)
        page.update()

    def rutina_asignada():
        global usuario_actual
        global rutinas
        page.clean()
        navegacion_usuario()

        mensaje_1 = ft.Text(f'{usuario_actual.upper()}, Tu Rutina es: ',size=20,font_family='consolas', color=ft.colors.WHITE70,weight=ft.FontWeight.BOLD)

        row5 = ft.Row(controls=[mensaje_1],alignment=ft.MainAxisAlignment.CENTER)
        column5 = ft.Column(controls=[row5])

        row_espacios_rutinas = ft.Row(controls=[ft.Container(width=0, height=40)])
        column_espacio_rutinas = ft.Column(controls=[row_espacios_rutinas])




        def comprobacion_rutina():
            if usuario_actual in rutinas:
                page.clean()
                seleccion_rutina = rutinas[usuario_actual]

                mostrar_rutina = ft.Container(content=ft.Text(seleccion_rutina),
                                              border=ft.border.all(2,ft.colors.RED),
                                              width=450, height=500
                                              )
                row6 = ft.Row(controls=[mostrar_rutina],alignment=ft.MainAxisAlignment.CENTER)
                column6 = ft.Column(controls=[row6])

                page.add(column6,column_boton_volver)
                page.update()

            else:
                page.clean()
                no_rutina = ft.Container(content=ft.Text('Usuario no posee Rutina',weight=ft.FontWeight.BOLD),
                                         border=ft.border.all(2,ft.colors.RED),
                                         width=450,height=500
                                         )
                row7 = ft.Row(controls=[no_rutina],alignment=ft.MainAxisAlignment.CENTER)
                column7= ft.Column(controls=[row7])

                page.add(column_CierreSesion,column_espacio_rutinas,column5,column7,column_boton_volver)
                page.update()

        volver_button = ft.ElevatedButton('Volver', on_click=lambda _: rutina_asignada())
        row_boton_volver = ft.Row(controls=[volver_button], alignment=ft.MainAxisAlignment.CENTER)
        column_boton_volver = ft.Column(controls=[row_boton_volver])

        boton_verificar = ft.ElevatedButton('Verificar', on_click=lambda e: comprobacion_rutina())
        row_boton_verificar = ft.Row(controls=[boton_verificar],alignment=ft.MainAxisAlignment.CENTER)
        column_boton_verificar = ft.Column(controls=[row_boton_verificar])

        page.add(column_CierreSesion,column_espacio_rutinas,column5,column_boton_verificar)

    def comidas_asignadas():
        global usuario_actual
        global comidas_dic
        page.clean()
        navegacion_usuario()

        mensaje_1 = ft.Text(f'{usuario_actual.upper()}, Tus comidas son:', size=20,font_family='consolas', weight=ft.FontWeight.BOLD, color=ft.colors.WHITE70)
        row8 = ft.Row(controls=[mensaje_1], alignment=ft.MainAxisAlignment.CENTER)
        column8 = ft.Column(controls=[row8])

        def comprobar():
            if usuario_actual in comidas_dic:
                page.clean()
                navegacion_usuario()

                revision_comidas = ft.Container(content=ft.Text(comidas_dic[usuario_actual],weight=ft.FontWeight.BOLD),
                                                border=ft.border.all(2,ft.colors.RED),
                                                width=450,height=500)
                row9 = ft.Row(controls=[revision_comidas],alignment=ft.MainAxisAlignment.CENTER)
                column9 = ft.Column(controls=[row9])


                page.add(column_CierreSesion,column_espacio_comidas,column8,column9,column_BotonVolver_comidas)
                page.update()

            else:
                page.clean()

                mensaje_2 = ft.Container(content=ft.Text('Usuario no posee Comidas Asignadas',weight=ft.FontWeight.BOLD),
                                         border=ft.border.all(2,ft.colors.RED),
                                         width=450,height=500)
                row10 = ft.Row(controls=[mensaje_2],alignment=ft.MainAxisAlignment.CENTER)
                column10 = ft.Column(controls=[row10])

                page.add(column_espacio_comidas,column8,column10,column_BotonVolver_comidas)
                page.update()

        boton_volver = ft.ElevatedButton('Volver', on_click= lambda _:comidas_asignadas())
        row_BotonVolver_comidas = ft.Row(controls=[boton_volver], alignment=ft.MainAxisAlignment.CENTER)
        column_BotonVolver_comidas = ft.Column(controls=[row_BotonVolver_comidas])

        boton_verificar = ft.ElevatedButton('Verificar', on_click=lambda e:comprobar())
        row_boton_VerificacionComida = ft.Row(controls=[boton_verificar], alignment=ft.MainAxisAlignment.CENTER)
        column_boton_VerificacionComida = ft.Column(controls=[row_boton_VerificacionComida])

        row_espacio_comidas = ft.Row(controls=[ft.Container(width=0,height=45)])
        column_espacio_comidas = ft.Column(controls=[row_espacio_comidas])

        page.add(column_CierreSesion,column_espacio_comidas,column8,column_boton_VerificacionComida)

    def preguntas_respuestas():
        global respuestas_dic
        global Preguntas_variable
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
                etiqueta_5 = ft.Text('Ingresa la pregunta - Sera respondida en un maximo de 24Hrs')
                recuadro_pregunta = ft.TextField(autofocus=True,multiline=True)
                boton_enviar_pregunta = ft.ElevatedButton('Enviar', on_click=lambda _: guardado_pregunta())
                page.add(mensaje_7,etiqueta_5,recuadro_pregunta,boton_enviar_pregunta,boton_volver1)

            def guardado_pregunta():
                page.clean()
                if clave_seleccionada not in Preguntas_variable:
                    Preguntas_variable[clave_seleccionada] = []
                Preguntas_variable[clave_seleccionada].append(f'Usuario {usuario_actual.upper()} pregunta: {recuadro_pregunta.value.lower()}')
                '''Preguntas_variable[clave_seleccionada].append(recuadro_pregunta.value.lower())'''
                print(Preguntas_variable)
                preguntas_respuestas()

        def administrador_respuestas():
            global contador_respuestas
            page.clean()
            if not respuestas_dic.get(usuario_actual):
                mensaje_de_comparacion = ft.Text('No tienes respuestas')
                page.add(mensaje_de_comparacion,boton_volver1)
                contador_respuestas = 1

            else:
                for r in respuestas_dic:
                    if r == usuario_actual:
                        respuestass = respuestas_dic[r]
                        print(respuestass)
                        for rr in respuestass:
                            contador = ft.Text(f'Respuesta Numero {contador_respuestas}',size=20, color=ft.colors.WHITE70)
                            respuesta_enventana = ft.Text(f'{usuario_actual.upper()}, La respuesta a tu pregunta es: \n{rr}')
                            boton_MarcadoLeido = ft.ElevatedButton('Marcar como Leido', on_click=lambda _:marcar_leido(rr))
                            page.add(contador,respuesta_enventana,boton_MarcadoLeido,boton_volver1)

                            time.sleep(1000000)

        def marcar_leido(elemento):
            global contador_respuestas
            page.clean()
            if usuario_actual in respuestas_dic:
                if elemento in respuestas_dic[usuario_actual]:
                    respuestas_dic[usuario_actual].remove(elemento)
                    contador_respuestas += 1
                    print(respuestas_dic)
                    administrador_respuestas()
                    page.update()



        boton_preguntas_respondidas = ft.ElevatedButton('RESPUESTAS', on_click=lambda _:administrador_respuestas())
        boton_seleccion = ft.ElevatedButton('Seleccionar', on_click=lambda e: seleccion_final())
        boton_volver1 = ft.ElevatedButton('Volver', on_click=lambda _: preguntas_respuestas())
        page.add(selected_option_text, mostrar_profesores, boton_seleccion,boton_preguntas_respondidas)
        page.update()

    def perfil():
        page.clean()
        navegacion_usuario()
        etiqueta_perfil1= ft.Text(usuario_actual,size=15,color=ft.colors.WHITE70)



    # SEPARADOR________________________________________________________________

    # PESTAÑAS ENTRENADOR

    def ingreso_alumnos():  # POSICION 0
        page.clean()
        navegacion_entrenador()
        nonlocal logged_in

        # creacion de la etiqueta color y diseño y asignacion en columna

        container_label_ingreso = ft.Container(content=ft.Text('Ingreso de nuevos usuarios',
                                                               weight=ft.FontWeight.BOLD,
                                                               size=20,
                                                               font_family='consolas',
                                                               color=ft.colors.WHITE70),
                                               border=ft.border.all(2, color=ft.colors.WHITE70),
                                               bgcolor=ft.colors.BROWN_900,
                                               border_radius=30,
                                               padding=5,
                                               margin=10,
                                               )
        row_container_label = ft.Row(controls=[container_label_ingreso], alignment=ft.MainAxisAlignment.CENTER)
        colum_container_label = ft.Column(controls=[row_container_label])

        # columna espaciado

        row_espacio_N_User = ft.Row(controls=[ft.Container(width=0, height=50)])
        colum_espacio_N_User = ft.Column(controls=[row_espacio_N_User])

        row_espacio_pequeño = ft.Row(controls=[ft.Container(width=0, height=30)])
        colum_espacio_pequeño = ft.Column(controls=[row_espacio_pequeño])

        # ingreso de los datos y creacion de columnas y contenedores

        nuevo_usuario = ft.TextField(label="Nuevo Nombre de Usuario")
        nuevo_usuario_container = ft.Container(content=nuevo_usuario, border_radius=6,
                                               border=ft.border.all(2, color=ft.colors.WHITE70))
        column21 = ft.Column(controls=[nuevo_usuario_container])

        nueva_contraseña = ft.TextField(label="Nueva Contraseña", password=True)
        nueva_contraseña_container = ft.Container(content=nueva_contraseña, border_radius=6,
                                                  border=ft.border.all(2, ft.colors.WHITE70))
        column22 = ft.Column(controls=[nueva_contraseña_container])

        def register_user(e):
            cursor = db.cursor()
            verificacion = 0
            usuario = nuevo_usuario.value
            contraseña = nueva_contraseña.value
            query = 'select nombre from usuarios'
            cursor.execute(query)
            resultado = cursor.fetchall()

            if usuario == '' and contraseña == '':
                print('no completo los campos')
                page.add(ft.Text('Complete los campos Obligatorios'))
                page.update()
                return

            elif usuario != '' and contraseña != '':

                for user in resultado:
                    if usuario == user[0]:
                        print('Usuario ya existe')
                        mensaje_error = 'Usuario ya existe'
                        page.add(ft.Text(mensaje_error, color="white"))
                        nuevo_usuario.value = ''
                        nueva_contraseña.value = ''
                        page.update()
                        return


                    else:
                        verificacion = 1

                if verificacion == 1:
                    query = 'insert into usuarios(nombre,contraseña) VALUE(%s,%s)'
                    cursor.execute(query, (usuario, contraseña))
                    db.commit()
                    nuevo_usuario.value = ''
                    nueva_contraseña.value = ''
                    mensaje_ingreso = 'Usuario ingresado'
                    page.add(ft.Text(mensaje_ingreso, color="white"))
                    print('Usuario ingresado')



        register_button = ft.ElevatedButton("Registrar Usuario", on_click=register_user)

        # agregar elementos a la pagina
        # boton de cierre de sesion corresponde al del menu en general por lo cual es el mismo para todas las funciones

        page.add(column_CierreSesion, colum_espacio_N_User, colum_container_label, colum_espacio_pequeño, column21,
                 column22,
                 register_button)
        page.update()

    def lista_alumnos():
        page.clean()
        page.bgcolor = ft.colors.TRANSPARENT
        page.decoration = ft.BoxDecoration(image=ft.DecorationImage('fondo1.jpg'))
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
        global usuario_actual
        cursor = db.cursor()
        page.clean()
        navegacion_entrenador()
        print(usuario_actual)

        def comprobacion():
            page.clean()
            navegacion_entrenador()
            page.update()
            query = 'select nombre from estado_marcacion'
            cursor.execute(query)
            resultados = cursor.fetchall()
            print(resultados)


            #estado
            for user in resultados:
                print('entro al for')
                if usuario_actual==user[0]:
                    query = 'select estado from estado_marcacion where nombre = %s'
                    cursor.execute(query,(usuario_actual,))
                    resultado = cursor.fetchall()
                    print(f'el estado del usuario {usuario_actual}, es {resultado}')
                    print('encontro el estado')
                    analisis(resultado) #PASA A LA FUNCION DE ANALISIS COMO YA ENCONTRO lo necesario
                    break  #fin del for ya que encontro al usuario



                else:
                      print('buscando estado del usuario ') #vuelve al for para que siga buscando al usuario

        def analisis(resultado):
            print('resien entra a todo lo que contiene la pestaña marcacion ya que lo anterior solo es interno')
            for estado in resultado:
                if estado[0] == 0:
                   page.clean()
                   print('marcando entrada')
                   page.add(column32,column30) #agrega los botones para marcar entrada,boton configurado para ejecutar funcion entrada
                   page.update() #ver si pestañea si no desactivar
                   break


        def entrada():
            page.clean()
            navegacion_entrenador()
            query = 'update estado_marcacion set estado = 1 where nombre = %s'
            cursor.execute(query,(usuario_actual,))
            cursor.fetchall()
            db.commit()
            print('primera parte cambio de estado tabla estado marcacion ')
            time.sleep(2)
            query = 'insert into marcacion_entrada(nombre,hora_ingreso) values(%s,now())'
            cursor.execute(query,(usuario_actual,))
            cursor.fetchall()
            db.commit()
            print('segunda parte lista insertar en tabla marcacion entrada')
            time.sleep(2)
            query = 'select hora_ingreso from marcacion_entrada where nombre = %s'
            cursor.execute(query,(usuario_actual,))
            resultado=cursor.fetchall()
            print(f'{resultado}, funciono CTM')



        #boton marcacion entrada
        boton_marcacion_entrada = ft.ElevatedButton('Entrada', on_click=lambda _: entrada())
        row30= ft.Row(controls=[boton_marcacion_entrada], alignment=ft.MainAxisAlignment.CENTER)
        column30 = ft.Column(controls=[row30])

        '''#boton Maracion salida
        boton_marcacion_salida = ft.ElevatedButton('Salida', on_click=lambda _: salida())
        row31 = ft.Row(controls=[boton_marcacion_salida], alignment=ft.MainAxisAlignment.CENTER)
        column31 = ft.Column(controls=[row31])'''

        #mensaje
        mensaje_marcacion = ft.Container(content=ft.Text('RELOJ CONTROL - MARCACION',
                                                               weight=ft.FontWeight.BOLD,
                                                               size=20,
                                                               font_family='consolas',
                                                               color=ft.colors.WHITE70),
                                               border=ft.border.all(2, color=ft.colors.WHITE70),
                                               bgcolor=ft.colors.BROWN_900,
                                               border_radius=30,
                                               padding=5,
                                               margin=10,
                                               )
        row32 = ft.Row(controls=[mensaje_marcacion],alignment=ft.MainAxisAlignment.CENTER)
        column32 = ft.Column(controls=[row32])

        comprobacion()
        '''page.update()'''




        '''global ciclo_marcacion
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
            ciclo_marcacion = 0'''

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

                    if n_c in comidas_dic:
                        mostrar = comidas_dic[n_c]
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

    def preguntas_respuestas_entrenador():
        borrar = ''
        global usuario_actual
        global Preguntas_variable
        page.clean()
        navegacion_entrenador()
        etiqueta_preguntas = ft.Text('Responder Preguntas', size=20, font_family='consolas', color=ft.colors.WHITE70)

        def verificacion_preguntas():
            page.clean()
            if not Preguntas_variable.get(usuario_actual): #asi es como se compara si es que no tiene nada el dic
                mensaje_sin_preguntas = ft.Text('No tienes preguntas por responder')
                page.add(mensaje_sin_preguntas,boton_volver_2)

            else:
                for n in Preguntas_variable:
                    if n == usuario_actual:
                        preguntasss = Preguntas_variable[n]
                        print(preguntasss)
                        for i in preguntasss:
                            preguntas_enventana = ft.Text(i)
                            etiqueta_responder_nombre_usuario = ft.Text('Ingrese el nombre del Usuario')
                            respuesta_nombre_usuario = ft.TextField(autofocus=True)
                            etiqueta_responder_pregunta = ft.Text('Responda la pregunta')
                            respuesta_recuadro = ft.TextField(autofocus=True, multiline=True)
                            boton_responder = ft.ElevatedButton('Responder', on_click=lambda _: borrado_pregunta(i,respuesta_nombre_usuario.value.lower(),respuesta_recuadro.value.lower()))
                            page.add(preguntas_enventana,
                                     etiqueta_responder_nombre_usuario,
                                     respuesta_nombre_usuario,
                                     etiqueta_responder_pregunta,
                                     respuesta_recuadro,
                                     boton_responder)
                            page.update()

                            time.sleep(100000)


        def borrado_pregunta(elemento,user,responder):
            page.clean()
            if user not in respuestas_dic:
                respuestas_dic[user]=[responder]
            else:
                respuestas_dic[user].append(responder)

            if usuario_actual in Preguntas_variable:
                if elemento in Preguntas_variable[usuario_actual]:
                    Preguntas_variable[usuario_actual].remove(elemento)
            print(Preguntas_variable)
            print(respuestas_dic)
            preguntas_respuestas_entrenador()

        boton_volver_2 = ft.ElevatedButton('Volver', on_click=lambda _:preguntas_respuestas_entrenador())
        boton_verificar_preguntas = ft.ElevatedButton('Verificar preguntas', on_click=lambda _:verificacion_preguntas())
        page.add(etiqueta_preguntas,boton_verificar_preguntas)
        page.update()

    #SEPARADOR______________________________________________

    #CERRAR SESION

    def logout():
        nonlocal logged_in
        logged_in = False  # Cambiar el estado a no autenticado
        username_field.value = ""  # Limpiar campos de inicio de sesión
        password_field.value = ""

        # Regresar a la pantalla de inicio de sesión
        page.clean()
        page.add(column_espacio,column1,column2,column3,column4,column_InicioSesion)
        navegacion_usuario()
        navegacion_entrenador()

        page.update()

    #INICIO SESION

    logged_in = False

    def login():
        global usuario_actual
        nonlocal logged_in  # Usar la variable externa
        usuario = username_field.value.lower()
        contraseña = password_field.value.lower()

        def inicio_usuario_base():
            control = 0
            cursor = db.cursor()
            global usuario_actual
            nonlocal logged_in
            query = 'SELECT nombre,contraseña from usuarios'
            cursor.execute(query)
            resultado = cursor.fetchall()

            for user, contra in resultado:
                control += 0
                if user == usuario and contra == contraseña:

                    logged_in = True
                    usuario_actual = usuario
                    print('inicio sesion correcto como usuario')
                    inicio()
                    return



                else:
                    print('revisando usuarios\n')
                    control += 1

            if control > 0:
                print(control)
                time.sleep(2)
                inicio_entrenador_base()

        def inicio_entrenador_base():
            cursor = db.cursor()
            nonlocal logged_in
            global usuario_actual
            query = 'SELECT nombre,contraseña from entrenador'
            cursor.execute(query)
            resultado = cursor.fetchall()

            for user, contra in resultado:

                if user == usuario and contra == contraseña:
                    logged_in = True
                    usuario_actual = usuario
                    print('ingreso como entrenador')
                    lista_alumnos()  # Mostrar contenido de la pestaña "Explorar" al iniciar sesión
                    return


                else:
                    print('revisando usuarios de entrenadores\n')

            print('No Match')
            username_field.value = ''
            password_field.value = ''
            page.add(ft.Text("Credenciales incorrectas.", color="red"))
            page.update()

        inicio_usuario_base()

    #SEPARADOR_______________________________

    #Barra navegacion USUARIO

    def on_tab_change(e):
        if not logged_in:
            return  # No hacer nada si no está autenticado

        print("Selected tab:", e.control.selected_index)  # Imprimir índice seleccionado

        # Llamar a la función correspondiente según la pestaña seleccionada
        if e.control.selected_index == 0:
            page.bgcolor = ft.colors.TRANSPARENT
            page.decoration = ft.BoxDecoration(image=ft.DecorationImage('fondo1.jpg'))

            inicio()
        elif e.control.selected_index == 1:
            page.bgcolor = ft.colors.TRANSPARENT
            page.decoration = ft.BoxDecoration(image=ft.DecorationImage('fondo2.jpg'))
            rutina_asignada()

        elif e.control.selected_index == 2:
            page.bgcolor = ft.colors.TRANSPARENT
            page.decoration = ft.BoxDecoration(image=ft.DecorationImage('fondo5.jpg'))
            comidas_asignadas()

        elif e.control.selected_index == 3:
            page.bgcolor = ft.colors.TRANSPARENT
            page.decoration = ft.BoxDecoration(image=ft.DecorationImage('fondo4.jpg'))
            preguntas_respuestas()
        elif e.control.selected_index==4:
            page.bgcolor = ft.colors.TRANSPARENT
            page.decoration = ft.BoxDecoration(image=ft.DecorationImage('fondo5.jpg'))


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
                    ft.NavigationBarDestination(icon=ft.icons.QUESTION_ANSWER_ROUNDED, label='Preguntas y Respuestas'),
                    ft.NavigationBarDestination(icon=ft.icons.PERSON, label='Perfil')

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

            page.bgcolor = ft.colors.TRANSPARENT
            page.decoration = ft.BoxDecoration(image=ft.DecorationImage('fondo1.jpg'))
            lista_alumnos()

        elif e.control.selected_index == 1:

            page.bgcolor = ft.colors.TRANSPARENT
            page.decoration = ft.BoxDecoration(image=ft.DecorationImage('fondo2.jpg'))
            ingreso_alumnos()

        elif e.control.selected_index == 2:

            page.bgcolor = ft.colors.TRANSPARENT
            page.decoration = ft.BoxDecoration(image=ft.DecorationImage('fondo5.jpg'))
            agregar_rutinas()

        elif e.control.selected_index ==3:

            page.bgcolor = ft.colors.TRANSPARENT
            page.decoration = ft.BoxDecoration(image=ft.DecorationImage('fondo4.jpg'))
            marcacion()

        elif e.control.selected_index==4:

            page.bgcolor = ft.colors.TRANSPARENT
            page.decoration = ft.BoxDecoration(image=ft.DecorationImage('fondo5.jpg'))
            agregar_comidad()

        elif e.control.selected_index ==5:

            page.bgcolor = ft.colors.TRANSPARENT
            page.decoration = ft.BoxDecoration(image=ft.DecorationImage('fondo6.jpg'))
            preguntas_respuestas_entrenador()



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
                    ft.NavigationBarDestination(icon=ft.icons.FOOD_BANK, label='+Comidas'),
                    ft.NavigationBarDestination(icon=ft.icons.QUESTION_MARK, label='Preguntas y respuestas')


                ],
                on_change=barra_entrenador
            )

        else:
            page.navigation_bar = None



    #boton cerrar sesion para todas las funciones
    logout_button = ft.ElevatedButton("Cerrar Sesión", on_click=lambda _: logout())

    # Botón para iniciar sesión
    login_button = ft.ElevatedButton("Iniciar Sesión", on_click=lambda _:login(), bgcolor=ft.colors.RED_400)

    row_boton_InicioSesion = ft.Row(controls=[login_button], alignment=ft.MainAxisAlignment.CENTER)
    column_InicioSesion = ft.Column(controls=[row_boton_InicioSesion])

    row_boton_CierreSesion = ft.Row(controls=[logout_button],alignment=ft.MainAxisAlignment.END)
    column_CierreSesion = ft.Column(controls=[row_boton_CierreSesion])

    # Agregar los elementos a la página
    row_espacios = ft.Row(controls=[ft.Container(width=0,height=200)])
    column_espacio = ft.Column(controls=[row_espacios])

    row = ft.Row(controls=[username_label,ft.Container(width=0, height=0)],alignment=ft.MainAxisAlignment.CENTER)
    column1 = ft.Column(controls=[row])

    row1 = ft.Row(controls=[contenedor_username],alignment=ft.MainAxisAlignment.CENTER)
    column2 = ft.Column(controls=[row1])

    row2 = ft.Row(controls=[password_label],alignment=ft.MainAxisAlignment.CENTER)
    column3 = ft.Column(controls=[row2])

    row3 = ft.Row(controls=[contenedor_password],alignment=ft.MainAxisAlignment.CENTER)
    column4 = ft.Column(controls=[row3])





    page.add(column_espacio,column1,column2,column3,column4,column_InicioSesion)
# Ejecutar la aplicación
ft.app(main)
