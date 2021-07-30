import pygame.mixer as sound
from time import sleep
sound.init()
sound.music.set_volume(0.7)
sound.music.load("E:\Python\Ring\Over_the_horizon.mp3")
sound.music.play()
while sound.music.get_busy():
    sleep(1)

print(sound.music.get_busy())
sound.music.play()