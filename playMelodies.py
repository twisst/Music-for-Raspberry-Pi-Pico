from machine import Pin, PWM
from utime import sleep

buzzer = PWM(Pin(15))   # pin where buzzer is connected

from melodies import *  # import melodies.py
from notes import *     # import notes.py

track = 25      # choose track here (see the list in melodies.py)
volume = 800   # set volume to a value between 0 and 1000


def playtone(frequency):
    buzzer.duty_u16(volume)    
    buzzer.freq(frequency)

def be_quiet():
    buzzer.duty_u16(0)  # turns sound off

def duration(tempo, t):
    
    # calculate the duration of a whole note in milliseconds (60s/tempo)*4 beats
    wholenote = (60000 / tempo) * 4
    
    # calculate the duration of the current note
    # (we need an integer without decimals, hence the // instead of /)
    if t > 0:
      noteDuration = wholenote // t
    elif (t < 0):
      # dotted notes are represented with negative durations
      noteDuration = wholenote // abs(t)
      noteDuration *= 1.5 # increase their duration by a half
    
    return noteDuration

def playsong(mysong):
    
    try:
        
        print(mysong[0]) # print title to the shell 
        tempo = mysong[1]

        # iterate over the notes of the melody. 
        # Remember, the array is twice the number of notes (notes + durations)
        for thisNote in range(2, len(mysong), 2):
            
            noteduration = duration(tempo, int(mysong[thisNote+1]))
            
            if (mysong[thisNote] == "REST"):
                be_quiet()
            else:
                playtone(notes[mysong[thisNote]])
            
            sleep(noteduration*0.9/1000) # we only play the note for 90% of the duration...
            be_quiet()
            sleep(noteduration*0.1/1000) # ... and leave 10% as a pause between notes
    
    except: # make sure the buzzer stops making noise when something goes wrong or when the script is stopped
        
        be_quiet()
        

playsong(melody[track])  # start playing the melody