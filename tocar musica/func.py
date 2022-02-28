import pygame
import keyboard as kb
import time
import os


class control:
    def pause(music):
        if kb.is_pressed('altgr + p'):
            pygame.mixer.music.pause()
            print("Musica '" + music.replace('_', ' ') + "' pausada\n")
            time.sleep(1)

    def unpause(music):
        if kb.is_pressed('altgr + u'):
            pygame.mixer.music.unpause()
            tool.clear()
            print('Tocando ' + music.replace('_', ' ') + '\n')
            time.sleep(1)

    def set_volume(music):
        if kb.is_pressed('altgr + v'):
            import pyautogui as gui
            gui.press('delete')
            volume = input('Volume [0.0 a 1.0]:')
            time.sleep(1)
            pygame.mixer.music.set_volume(float(volume))
            tool.clear()
            print('Tocando ' + music.replace('_', ' ') + '\n')


class musica:
    def nome(nome_musica):
        musica = './musicas/{musica}.mp3'.format(musica=nome_musica)
        if os.path.exists(musica):
            pygame.mixer.music.load(musica)

    def loading():
        j = 0
        for i in range(11):
            print('Loading ' + str(j) + '%')
            j += 10
            time.sleep(0.25)
            tool.clear()


class tool:
    def clear():
        import os
        os.system("cls")
