import flet as ft
import random



def main(page: ft.Page):
    
    page.scroll= "always"
    
    
    def gerarPoemaAleatorio(e):
        
        
        
        
        pass
    
    srcs= [
        "../img (1).jpg",
        "../img (2).jpg",
        "../img (3).jpg",
        "../img (4).jpg",
        "../img (5).jpg",
        "../img (6).jpg",
        "../img (7).jpg",
        
    ]
    
    
    def img():
        random.shuffle(srcs)
        
        return srcs[0]
    
    poema = ft.Text(
        
        
        
        
    )
    
    
    page.add(ft.Stack(
        
        [
            ft.Image(src=img(), fit= 'cover'),
            
            ft.Column(
                [
                    ft.ElevatedButton(
                text= "Gerar Poema",
                on_click= gerarPoemaAleatorio,
                bgcolor= 'Transparent',
                color= '',
                
                
            )
                ]
            )
            
            
        ],
        
        
        
        
        
    ))
    
    



ft.app(target=main)