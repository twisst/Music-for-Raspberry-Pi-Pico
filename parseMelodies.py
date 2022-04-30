# made this script to scrape the melodies from the Arduino files in https://github.com/robsoncouto/arduino-songs

import os
import re

# melody = ['0', 'credits: ']
melody = ['0']
melodystarted = False
creditsrolling = True

directory = './'

num = 0

def comment_remover(text):
    # source: https://stackoverflow.com/questions/241327/remove-c-and-c-comments-using-python
    def replacer(match):
        s = match.group(0)
        if s.startswith('/'):
            return " " # note: a space and not an empty string
        else:
            return s
    pattern = re.compile(
        r'//.*?$|/\*.*?\*/|\'(?:\\.|[^\\\'])*\'|"(?:\\.|[^\\"])*"',
        re.DOTALL | re.MULTILINE
    )
    return re.sub(pattern, replacer, text)



print("melody = []")
print("notes = []")

# iterate over the Arduino scripts with melodies in them
for root, dirs, files in os.walk(directory):
    for filename in files:
        if filename.endswith(".ino"):
            script = os.path.join(root, filename)  # i.e. 'nevergonnagiveyouup/nevergonnagiveyouup.ino'
            s = open(script, 'r')
            
            for x in s:
                
                # get tempo
                if ("int tempo" in x):
                    melody[0] = int(re.findall(r"\d+", x)[0])
                
                # mark the beginning of the melody
                if ("int melody" in x):
                    melodystarted = True
                    continue
                
                if (melodystarted == True):
                    
                    # add notes and durations
                    if "NOTE_" in x or "REST" in x:
                        m = comment_remover(x)
                        m = re.split(r"[,\s\n]+", m)
                        m = list(filter(None, m))
                        for note in m:
                            melody.append(note)
                        creditsrolling = False # make sure we don't save any more lines that are not part of the melody 
                        continue
                    
                    if ("};" in x): # melody ended
                        melodystarted = False
                        break
                    
                    # add credits (unless we're past those)
                    if creditsrolling == False:
                        continue
                    else:
                        credits = x.strip(" /\n")
                        print("# " + credits)
                    
            s.close() 

            print("notes = ", end='')
            print(melody)
            print("melody.append(notes)")
            
            # reset
            melody = ['0']
            melodystarted = False
            creditsrolling = True
            