#12/09/21
#Corey Klevan
#Ian Sharp
#Motion sensing with music
import RPi.GPIO as GPIO
import time
import vlc

sensor = 4
GPIO.setmode(GPIO.BCM)
GPIO.setup(sensor, GPIO.IN, GPIO.PUD_DOWN)

previous_state = False
current_state = False
p = vlc.MediaPlayer()
   
curr_time = time.time()
is_playing = False
while True:
    if time.time() - curr_time >= 8 and is_playing:
        p.stop()
        # Stops the music
        p.release()
        # Clears the media Player
        is_playing = False
        curr_time = time.time()
        # Resetting the current time variable after 8 sec pass after it starts playing
    time.sleep(0.1)
    previous_state = current_state
    current_state = GPIO.input(sensor)
    if current_state != previous_state and not is_playing:
        new_state = "HIGH" if current_state else "LOW"
        print("Motion detected")
        curr_time = time.time()
        # Resseting the current time variable whenever motion is detected
        p = vlc.MediaPlayer()
        time.sleep(0.2)
        media = vlc.Media("/home/pi/Shboom.mp3")
        p.set_media(media)
        p.play()
        # Starts the music
        is_playing = True
