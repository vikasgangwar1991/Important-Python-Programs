#Healthy programmer
#Time : 9 am - 5 pm
#Very Helpful programmer to remind some desired things during job time
#water - water.mp3(3.5 litres - Drank) log
#physical exercise - physical.mp3 (every 45 minutes) Exdone log
#Eyes exercise - eyes.mp3 every 30 minutes eyesdone log

from pygame import mixer
from datetime import datetime
from time import time
def musiconloop(file,stopper):
    mixer.init()
    mixer.music.load(file)
    mixer.music.play()
    while True:
        a=(input())
        if a==stopper:
            mixer.music.stop()
            break
def mylogs(msg):
    with open("logs.txt",'a') as f:
        f.write(f"{msg} {datetime.now()}\n")
if __name__=='__main__':
    # musiconloop("water.wav",3)
    initwater=time()
    initeyes=time()
    initexercise=time()
    watersecs=40*60
    eyessecs=30*60
    exesecs=45*60

    while True:
        if time()-initwater>watersecs:
            print("Water drinking time.Enter drank to stop the alarm")
            musiconloop("water.wav",'drank')
            initwater=time()
            mylogs("Drank water at")
        if time()-initexercise>exesecs:
            print("Physical Exercise time.Enter Exdone to stop the alarm")
            musiconloop("phyexercise.mp3",'Exdone')
            initexercise=time()
            mylogs("Physical exercise done at")
        if time()-initeyes>eyessecs:
            print("Eyes exercise time.Enter eyesdone to stop the alarm")
            musiconloop("eyesexercise.mp3",'eyesdone')
            initeyes=time()
            mylogs("Eyes exercise done at")
