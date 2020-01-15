import RPi.GPIO as GPIO 
import time
import os
from gpiozero import MotionSensor
from picamera import PiCamera
from datetime import datetime

GPIO.setmode(GPIO.BCM) #pins
GPIO.setup(23, GPIO.IN) #pins
camera = PiCamera() #Kamera
i = 0 #variabel

while True:
    def videoname (fileName, fileEnding): #name änder von File
        fileNmb = os.system('ls | wc -l')
        return fileName + str(int(fileNmb) + i) + fileEnding
    
    if GPIO.input(23): #auslösung der Kamera
        i += 1 #Variabel +1
        print("Motion Detected...") #Ausgabe Motion Detected
        duration = 1  # second
        freq = 700  # Hz
        os.system('play --no-show-progress --null --channels 1 synth %s sine %f' % (duration, freq))
        camera.start_recording(videoname('Aufnahme_','.h264')) #started Aufnahme
        time.sleep(7) #7 Sekunden Sleep
        camera.stop_recording() #Kamera stoppt Aufnahme
        time.sleep(8)
        time.sleep(0.1)