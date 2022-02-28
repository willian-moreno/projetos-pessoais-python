import time

import pygame

from func import control, musica, tool

# Lista de musicas
lista_musicas = """
    '0 - Finalizar o código'
    '1 - Black Clover (Opening 3)'
    '2 - Tokyo Revengers'
"""

# Iniciando o pygame
pygame.init()
pygame.mixer.init()

tool.clear()

# Escolhendo uma musica
escolha = str(input('Escolha uma musica' + lista_musicas + '\n:'))
if escolha == '1':
    nome_musica = 'Black_Clover_Open_3'
    musica.nome(nome_musica)
elif escolha == '2':
    nome_musica = 'Tokyo_Revengers'
    musica.nome(nome_musica)
elif escolha == '0':
    print('Programa finalizado')
else:
    print('Nenhuma musica escolhida')

# Tocando a musica
tool.clear()
try:
    musica.loading()
    tool.clear()
    pygame.mixer.music.play()
    pygame.event.wait()
    print('Tocando ' + nome_musica.replace('_', ' ') + '\n')
    while True:
        control.pause(nome_musica)
        control.unpause(nome_musica)
        control.set_volume(nome_musica)
except Exception as ex:
    print('Erro: ' + str(ex))
