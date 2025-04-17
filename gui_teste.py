import flet as ft
import teste as t
from teste2 import rimas,assuntos

cor1 = '#1b8bfe'
cor2 = '#2776f7'

Poema = ft.Column([], scroll= "auto", width= 500,)


#a = (t.gerarpoemaPorAssunto("Amor",5))
#for i in (t.gerarpoemaPorAssunto("Amor",5)):
        #page.add(ft.Text(value= i))


#print("Aqui está o a: ",a)

def main(page: ft.Page):
    page.bgcolor = '#0c0730'
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.scroll = "auto"
    page.window.vertical_alignment =  ft.MainAxisAlignment.CENTER,
    page.window.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    
    def gerarPoemasCruzados(e):
        Poema.controls.clear()
        
        a = rimaA.value
        b = rimaB.value
            
        for i in (t.gerarVersosCruzados(a,b)):
            Poema.controls.append(ft.Text(value= i, color= 'white', offset= (1,1), size= 12))
            page.update()
            
            
    
    def gerarpoemaPorRimas(rima, linhas):
        
        Poema.controls.clear()
        
        rima = rimaA.value
        linhas = linhas.value
            
        for i in (t.gerarpoemaPorRimas(rima,linhas)):
            Poema.controls.append(ft.Text(value= i, color= 'white', offset= (1,1), size= 12))
            page.update()
    
    
    
    
    
    
    def GerarPoemasAleatorios(e):
        Poema.controls.clear()
        
        
        
        l = int(linhas.value)
            
        for i in (t.gerarpoemaAleatorio(l)):
            Poema.controls.append(ft.Text(value= i, color= 'white', offset= (1,1), size= 12))
            page.update()
    
    def GerarPoemasPorAssuntos(e):
        Poema.controls.clear()
        a = assunto.value
        
        l = int(linhas.value)
            
        
        if a != "":
            for i in (t.gerarpoemaPorAssunto(a,l)):
                Poema.controls.append(ft.Text(value= i, color= 'white', offset= (1,1), size= 12))
        page.update()
    
    def GerarSonetos(e):
        Poema.controls.clear()
        a = assunto.value
        if a != "":
            for i in (t.gerarSoneto(a)):
                Poema.controls.append(ft.Text(value= i, color= 'white', offset= (1,1), size= 12))
        page.update()

    
    def GerarCruzadosAleatorios(e):
        Poema.controls.clear()
        for i in (t.gerarVersosCruzadosAleatorios()):
            Poema.controls.append(ft.Text(value= i, color= 'black', offset= (1,1)))
            page.update()
    
    assunto = ft.Dropdown(
        label="Temas",
        width= 300,
        hint_text= "Escolha o Assunto da Rima",
        options=[
        ],
    )
    
    rimaA = ft.Dropdown(
        label="Rimas",
        hint_text= "Escolha a terminação da Rima",
        width= 300,
        options=[

        ],
    
    )
    rimaB = ft.Dropdown(
        label="Rimas",
        hint_text= "Escolha a terminação da Rima",
        width= 300,
        options=[

        ],
    
    )
    
    linhas = ft.TextField(
        label="Número de linhas",
        width=300,
        value="5",
        keyboard_type="number",  # Ensures numeric input on supported devices
        on_change=lambda e: e.control.update(value="".join(filter(str.isdigit, e.control.value)))  # Filters non-digit input
    )
    

    
    for i in rimas:
        
        rimaA.options.append(ft.dropdown.Option(str(i)))
    for i in rimas:
        
        rimaB.options.append(ft.dropdown.Option(str(i)))
    
    for i in assuntos:
        assunto.options.append(ft.dropdown.Option(str(i)))
    
    
    
    page.add(
        ft.Row(
            [
                assunto, rimaA,rimaB,linhas
            ]
        ),
        ft.Container(
            width= page.window.width * 0.5,
            height= page.window.height * 0.9,
            bgcolor= '#1b1733',
            border_radius= 20,
            
            
            #expand= True,
            
            
            content= ft.Stack(
                [   
                    Poema,
                ],
                
                
            )
        ),
        
        ft.Row(
            
            [
                
                ft.ElevatedButton(text= " Gerar Poemas Aleatórios",on_click= GerarPoemasAleatorios, bgcolor= cor2),
                ft.ElevatedButton(text= " Gerar Poemas Por Assuntos",on_click= GerarPoemasPorAssuntos, bgcolor= cor2),
                ft.ElevatedButton(text= " Gerar Sonetos",on_click= GerarSonetos, bgcolor= cor2),
                ft.ElevatedButton(text= " Gerar Poemas Cruzados",on_click= gerarPoemasCruzados, bgcolor= cor2),
                ft.ElevatedButton(text= " Gerar Poemas Cruzados Aleatórios", on_click= GerarCruzadosAleatorios, bgcolor= 'white'),
                ft.ElevatedButton(text= " Gerar PoemaComRimasAlternadas"),
                ft.ElevatedButton(text= " Gerar Poemas PoemaAcrostico"),
                ft.ElevatedButton(text= " PoemaCircular"),
                ft.ElevatedButton(text= " Gerar Poemas Por Estrofes"),
                ft.ElevatedButton(text= " Gerar Poemas ComPalavrasObrigatorias"),
                ft.ElevatedButton(text= " Gerar Poemas ComLimiteDePalavras"),
                ft.ElevatedButton(text= " Gerar Poema PorRimas",on_click= gerarpoemaPorRimas, bgcolor= cor2),
                ft.ElevatedButton(text= " Gerar Poemas SonetoSolto",),
                
                
                
            
            ],
            scroll= "auto",
            height= 100,
            spacing= 10,
        )
    )
    
    
    
    page.update()






ft.app(target= main,)