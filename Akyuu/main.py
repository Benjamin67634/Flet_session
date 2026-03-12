import flet as ft

def main(page: ft.Page):
    page.horizontal_alignment = ft.MainAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.title = "Examen Final - Registro de Participantes"
   
    
    page.add(ft.Text(
        text_align=ft.TextAlign.CENTER,
        value="Registro de participantes",
        size=40,
        weight=ft.FontWeight.BOLD,
    ))

    txt_usuario = (ft.TextField(
        label="Nombres",
    ))
    
    txt_contra =(ft.TextField(
        label="Contraseña",
        password=True,
        can_reveal_password=True,
    ))
    
    button_resumen= (ft.Button(
    content="Mostrar Ficha del Participante",
    icon=ft.Icons.SAVE,
    icon_color=ft.Colors.WHITE,
    color=ft.Colors.WHITE,
    bgcolor=ft.Colors.BLUE,
    elevation=5,
    style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=10)),
    ))
    
    page.add(
        ft.Container(
            padding=20,
            bgcolor=ft.Colors.WHITE,
            border=ft.Border.all(3, ft.Colors.OUTLINE),
            #theme_mode=ft.ThemeMode.LIGHT,
            content = ft.Column(
                controls = [
                    txt_usuario,
                    txt_contra,
                    button_resumen,
                ]

            )
        )
        
    )
ft.run(main)