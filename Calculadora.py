import flet as ft
from flet import colors
from decimal import Decimal

buttons = [
    {'valor': 'C', 'cor_fonte': colors.RED, 'cor_fundo': colors.GREY_900}, 
    {'valor': '±', 'cor_fonte': colors.AMBER_100, 'cor_fundo': colors.GREY_900},
    {'valor': '%', 'cor_fonte': colors.AMBER_100, 'cor_fundo': colors.GREY_900},
    {'valor': '/', 'cor_fonte': colors.AMBER_100, 'cor_fundo': colors.GREY_900},
    {'valor': '7', 'cor_fonte': colors.BLUE_GREY_200, 'cor_fundo': colors.GREY_900},
    {'valor': '8', 'cor_fonte': colors.BLUE_GREY_200, 'cor_fundo': colors.GREY_900},
    {'valor': '9', 'cor_fonte': colors.BLUE_GREY_200, 'cor_fundo': colors.GREY_900},
    {'valor': '*', 'cor_fonte': colors.AMBER_100, 'cor_fundo': colors.GREY_900},
    {'valor': '4', 'cor_fonte': colors.BLUE_GREY_200, 'cor_fundo': colors.GREY_900},
    {'valor': '5', 'cor_fonte': colors.BLUE_GREY_200, 'cor_fundo': colors.GREY_900},
    {'valor': '6', 'cor_fonte': colors.BLUE_GREY_200, 'cor_fundo': colors.GREY_900},
    {'valor': '-', 'cor_fonte': colors.AMBER_100, 'cor_fundo': colors.GREY_900},
    {'valor': '1', 'cor_fonte': colors.BLUE_GREY_200, 'cor_fundo': colors.GREY_900},
    {'valor': '2', 'cor_fonte': colors.BLUE_GREY_200, 'cor_fundo': colors.GREY_900},
    {'valor': '3', 'cor_fonte': colors.BLUE_GREY_200, 'cor_fundo': colors.GREY_900},
    {'valor': '+', 'cor_fonte': colors.AMBER_100, 'cor_fundo': colors.GREY_900},
    {'valor': '0', 'cor_fonte': colors.BLUE_GREY_200, 'cor_fundo': colors.GREY_900},
    {'valor': '.', 'cor_fonte': colors.BLUE_GREY_200, 'cor_fundo': colors.GREY_900},
    {'valor': '=', 'cor_fonte': colors.GREY_900, 'cor_fundo': colors.AMBER_100}
]

def main(page: ft.Page):
    page.bgcolor = '#000'
    page.window_resizable = False
    page.window_width = 350
    page.window_height =  550
    page.title = "Calculadora"
    #page.window_always_on_top = True

    result = ft.Text(value = "0", color = colors.WHITE, size = 30)

    def calculate(operador, valor_atual):
        try:
            value = eval(valor_atual)

            if operador == '%':
                value /= 100
            elif operador == '±':
                value = -value
        except:
            return 'Erro'
        casas_decimais = min(abs(Decimal(value).as_tuple().exponent), 5)
        return format(value, f'.{casas_decimais}f')

    def select(e):
        valor_atual = result.value if result.value not in {'0', 'Erro'} else ''
        value = e.control.content.value
        #print("Antes - valor_atual:", valor_atual, "value:", value)
        if value.isdigit():
            value = valor_atual + value
        elif value == 'C':
            value='0'
        else:
            if valor_atual and valor_atual [-1] in ('/', '*', '-', '+', '.'):
                valor_atual = valor_atual [:-1]
            
            value = valor_atual + value

            if value[-1] in ('=', '%', '±'):
                value = calculate(operador=value[-1], valor_atual = valor_atual)
        #print("Depois - valor_atual:", valor_atual, "value:", value)
        result.value = value
        result.update()



    display = ft.Row(
        width = 350,
        height= 80,
        controls = [result],
        alignment = "end",
    )

    button = [ft.Container(
        content=ft.Text(value= button['valor'], color=button['cor_fonte'], size= 30), 
        width= 70, 
        height= 70, 
        bgcolor=button['cor_fundo'], 
        border_radius= 100,
        alignment= ft.alignment.center,
        on_click=select
    ) for button in buttons]

    keyboard = ft.Row(
        width= 350,
        controls= button,
        wrap=True,
        alignment= 'end'

    )


    page.add(display, keyboard)

ft.app(target= main)
