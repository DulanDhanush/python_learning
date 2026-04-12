import time
import datetime
import pygame

def set_alarm(alarm_time):
    print(f"Alarm set for {alarm_time}")
    sound_file = "paper-plane-by-declan-dp.mp3"

    pygame.mixer.init()

    while True:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        print(current_time, end="\r")

        if current_time >= alarm_time:
            print("\nWAKE UP!")

            pygame.mixer.music.load(sound_file)
            pygame.mixer.music.play()

            while pygame.mixer.music.get_busy():
                time.sleep(1)

            break

        time.sleep(1)

if __name__ == "__main__":
    alarm_time = input("Enter the alarm time (HH:MM:SS): ")
    set_alarm(alarm_time)