import flet as ft
import teste as t
from teste2 import rimas, assuntos

cor1 = '#1b8bfe'
cor2 = '#2776f7'

Poema = ft.Column([], scroll="auto", expand=True)

def main(page: ft.Page):
    page.bgcolor = '#0c0730'
    page.scroll = "auto"
    page.padding = 20
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.START

    def gerarPoemasCruzados(e):
        Poema.controls.clear()
        a = rimaA.value
        b = rimaB.value
        for i in t.gerarVersosCruzados(a, b):
            Poema.controls.append(ft.Text(value=i, color='white', size=14))
        page.update()

    def gerarpoemaPorRimas(rima, linhas):
        Poema.controls.clear()
        rima = rimaA.value
        linhas = linhas.value
        for i in t.gerarpoemaPorRimas(rima, linhas):
            Poema.controls.append(ft.Text(value=i, color='white', size=14))
        page.update()

    def GerarPoemasAleatorios(e):
        Poema.controls.clear()
        l = int(linhas.value)
        for i in t.gerarpoemaAleatorio(l):
            Poema.controls.append(ft.Text(value=i, color='white', size=14))
        page.update()

    def GerarPoemasPorAssuntos(e):
        Poema.controls.clear()
        a = assunto.value
        l = int(linhas.value)
        if a != "":
            for i in t.gerarpoemaPorAssunto(a, l):
                Poema.controls.append(ft.Text(value=i, color='white', size=14))
        page.update()

    def GerarSonetos(e):
        Poema.controls.clear()
        a = assunto.value
        if a != "":
            for i in t.gerarSoneto(a):
                Poema.controls.append(ft.Text(value=i, color='white', size=14))
        page.update()

    def GerarCruzadosAleatorios(e):
        Poema.controls.clear()
        for i in t.gerarVersosCruzadosAleatorios():
            Poema.controls.append(ft.Text(value=i, color='white', size=14))
        page.update()

    # Inputs
    assunto = ft.Dropdown(
        label="Temas",
        hint_text="Escolha o Assunto da Rima",
        width=300,
        options=[ft.dropdown.Option(str(i)) for i in assuntos],
    )

    rimaA = ft.Dropdown(
        label="Rima A",
        hint_text="Terminação A",
        width=150,
        options=[ft.dropdown.Option(str(i)) for i in rimas],
    )

    rimaB = ft.Dropdown(
        label="Rima B",
        hint_text="Terminação B",
        width=150,
        options=[ft.dropdown.Option(str(i)) for i in rimas],
    )

    linhas = ft.TextField(
        label="Número de linhas",
        width=150,
        value="5",
        keyboard_type="number",
        on_change=lambda e: e.control.update(value="".join(filter(str.isdigit, e.control.value))),
    )

    # Área de entrada
    page.add(
        ft.Container(
            content=ft.ResponsiveRow(
                controls=[assunto, ft.Row(
                    [
                        
                        rimaA, rimaB
                        ],alignment=ft.MainAxisAlignment.CENTER,
                spacing=20,
                run_spacing=10,), linhas],
                alignment=ft.MainAxisAlignment.CENTER,
                spacing=20,
                run_spacing=10,
            ),
            padding=10,
        )
    )

    # Botões (substituímos o Wrap por ResponsiveRow)
    botoes = [
        ft.ElevatedButton(text="Poemas Aleatórios", on_click=GerarPoemasAleatorios, bgcolor='black12',),
        ft.ElevatedButton(text="Poemas por Assunto", on_click=GerarPoemasPorAssuntos, bgcolor='black12',),
        ft.ElevatedButton(text="Sonetos", on_click=GerarSonetos,bgcolor='black12',),
        ft.ElevatedButton(text="Versos Cruzados", on_click=gerarPoemasCruzados, bgcolor='black12',),
        ft.ElevatedButton(text="Cruzados Aleatórios", on_click=GerarCruzadosAleatorios, bgcolor='black12',),
        ft.ElevatedButton(text="Poema com Rimas", on_click=gerarpoemaPorRimas, bgcolor='black12',),
        ft.ElevatedButton(text="Poema Acrostico", bgcolor='black12',),
        ft.ElevatedButton(text="Poema Circular", bgcolor='black12',),
        ft.ElevatedButton(text="Poemas por Estrofes", bgcolor='black12',),
        ft.ElevatedButton(text="Palavras Obrigatórias", bgcolor='black12',),
        ft.ElevatedButton(text="Limite de Palavras",bgcolor='black12',),
        ft.ElevatedButton(text="Soneto Solto", bgcolor='black12',),
    ]
    
    # Área de exibição do poema
    page.add(
        ft.Container(
            content=Poema,
            padding=20,
            bgcolor="#1b1733",
            border_radius=20,
            expand=True,
        )
    )

    page.add(
        ft.Container(
            content=ft.ResponsiveRow(
                controls=botoes,
                alignment=ft.MainAxisAlignment.CENTER,
                spacing=10,
                run_spacing=10,
            ),
            padding=10,
        )
    )



    page.update()

ft.app(target=main)
