import time
import pygame

# Inicializa o mixer do pygame
pygame.mixer.init()

# Carrega o arquivo MP3
pygame.mixer.music.load("a.mp3")

# Reproduz o áudio
pygame.mixer.music.play()

# Gambiarra necessária: o Python precisa continuar executando para o áudio tocar
while pygame.mixer.music.get_busy():
    time.sleep(1)