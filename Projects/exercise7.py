from pygame import mixer
from datetime import datetime
from time import time
def play_music(song,stopper):
    mixer.init()
    mixer.music.load(song)
    mixer.music.play()
    while True:
        quit=input()
        if quit==stopper:
            mixer.music.stop()
            break


def log_on_file(msg):
    with open("myfile.txt","a") as f:
        f.write(f"{msg} {datetime.now()}\n")

if __name__ == '__main__':
    init_water=time()
    init_phy=time()
    init_eye=time()

    water_secs=20
    eye_secs=30
    phy_secs=60
    while True:
        if time() - init_water > water_secs:
            print("Enter drank to stop the music")
            play_music("water.mp3","drank")
            log_on_file("Mihir drank water at")
            init_water=time()
        if time() - init_phy > phy_secs:
            print("Enter donephy to stop the music")
            play_music("gym.mp3","donephy")
            log_on_file("Mihir done exercise at")
            init_phy=time()
        if time() - init_eye > eye_secs:
            print("Enter doney to stop the music")
            play_music("eyes.mp3","doney")
            log_on_file("Mihir relaxed his eyes at")
            init_eye=time()

