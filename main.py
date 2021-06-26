# Tela principal, nela terá o primeiro menú para escolha do game.

import pygame
import PySimpleGUI as gui
import emoji

welcome = '''
Esse é um Mini-Game feito totalmente me python, espero que gostem.
'''


layout = [
    [gui.Text('Olá!!\n{}'.format(emoji.emojize(':fogos_de_artifício:', language = 'pt')*6))],
    [gui.Text('{}'.format(welcome))],
    [gui.Input()],
    [gui.Button('Escolha seu jogo.')]
]
window = gui.Window('Mini-Game',layout)
event,values = window.read()



