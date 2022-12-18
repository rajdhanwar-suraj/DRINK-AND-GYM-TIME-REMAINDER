# This program gives a remainder to go to gym and drink water time after 90 and 60 sec regularly.
# This program also write the time to drink water and time to go gym.
from pygame import mixer
from datetime import datetime
from time import time


def musiconloop(file,stopper):
    mixer.init()
    mixer.music.load(file)
    mixer.music.play()
    while True:
        a = input("Enter the stopper : ")
        if a == stopper:
            mixer.music.stop()
            break


def log_now(msg):
    with open("log.txt","a") as f:
        f.write(f"{msg} {datetime.now()}\n")


if __name__ == '__main__':
    init_water = time()
    init_Exercise = time()

    watersec = 60
    Exercisesec = 90


    while True:
        if time() - init_water > watersec:
            print("Time to drink water, Enter 'D' to stop alarm.")
            musiconloop("Drink.mp3","D")
            log_now(f"Drank water at {watersec}")
            init_water = time()


        if time() - init_Exercise > Exercisesec:
            print("Time to go Gym, Enter 'G' to stop alarm.")
            musiconloop("reminder.mp3","G")
            log_now(f"Physical exercise done at {Exercisesec}")
            init_Exercise = time()




