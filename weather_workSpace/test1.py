import os
import RPi.GPIO as GPIO
import time



GPIO.setmode(GPIO.BCM)

GPIO.setup(27, GPIO.IN)
#GPIO.setup(23, GPIO.OUT)



while True:
    
    #GPIO.output(23,GPIO.LOW)
    #GPIO.output(23,GPIO.HIGH)
    #time.sleep(1)
    #GPIO.output(23,GPIO.LOW)
    if  GPIO.input(27)== GPIO.HIGH :
        os.system("aplay -Dhw:1,0 speaker.wav")
        #os.system("rm record_test.wav")
        os.system("arecord  -c 2 -r 16000 -f S16_LE -Dhw:1,0 -d 5 record_test.wav")
        os.system("rm record_test1.wav")
        os.system("ffmpeg -i record_test.wav -acodec pcm_s16le -ac 1 -ar 16000 record_test1.wav")
        os.system("python3 asr.py")
        os.system("python3 weather.py")
        os.system("python3 tts.py")
        os.system("rm output1.wav")
        os.system("ffmpeg -i output.mp3 -acodec pcm_s16le -ac 2 -ar 16000 output1.wav")
        os.system("aplay -Dhw:1,0 output1.wav")
        time.sleep(30)
    time.sleep(1)
GPIO.cleanup()        

       


