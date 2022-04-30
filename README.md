# Songs for playing on Raspberry Pi Pico


Songs to play with a buzzer connected to a Raspberry Pi Pico.

I run a small electronics workshop at an art academy. I have decided to gradually switch over from the Arduino Uno to the Raspberry Pi Pico as the go-to board in my workshop.

Connecting a buzzer to a microcontroller is a fun first project. After making the first beeping sounds it's fun to also make  so porting Robson's list to Micropython made sense. This version is also a good example of the advantages of the Pico over the Arduino Uno. With the Arduino, each melody had to be a single file to fit on the Uno's limited flash memory of 32k bytes and we had to upload those files every time we wanted to change.
The complete list of 41 melodies easily fits on the 2 Megabyte memory of the Pico. 


## Usage

These scripts run on Micropython. Save them to the Pico (with the Thonny editor for instance).

If you want to compare the code with the original score, I try to group the notes in a measure as one line of ccode and the staves as groups of lines. However, in some cases notes will be tied together among measures or be dotted and this rule is broken.

## Hardware

Just connect an piezo to the board and you are good to go. Pin 11 is used in every sketch because some piezo speakers can be connected between it and the close GND pin without any wiring. You can use basically any pin, as long  as they can be used as digital pins (pins A6 and A7 of the Arduino Nano and mini are analog only). Just remember to assign the pin number to the `buzzer` variable. 

![alt tag](hardware.png)

There are two kinds of piezo buzzers: active and passive. The active one that plays a specific pitch when powevered and is not good for this purpose. The passive kind functions like a speaker, reproducing the pitch you apply to it. You can test the piezo speaker with the "blink" example, the good piezo speaker will just click, while the other kind will play a pitch every other second.  

## List of tunes

 0. Game of Thrones
 1. Greensleeves
 2. Silent Night
 3. Pacman
 4. Ode an die Freude, Beethoven's Symphony No. 9 
 5. Mii Channel theme
 6. Wiegenlied (Brahms' Lullaby)
 7. Minuet in G - Petzold
 8. Badinerie - Johann Sebastian Bach
 9. Für Elise - Ludwig van Beethoven
10. Cantina Band (Star wars)
11. Song of storms (The Legend of Zelda, Ocarina of Time)
12. The Lion Sleeps Tonight
13. Theme A from Tetris (Korobeiniki)
14. Happy Birthday
15. The Lick
16. Canon in D - Pachelbel
17. Darth Vader theme (Star Wars)
18. Nokia Ringtone
19. At Doom's Gate
20. Pink Panther theme
21. Hedwig's theme (Harry Potter)
22. Jigglypuff's Song (Pokémon)
23. We Wish You a Merry Christmas
24. Keyboard cat
25. Star Trek intro
26. Gren Hill Zone (Sonic the Hedgehog)
27. The Legend of Zelda theme
28. Baby Elephant Walk
29. Bloody Tears (Castlevania II)
30. Star Wars theme
31. O Pulo da Gaita (Auto da Compadecida)
32. Vampire Killer (Castlevania)
33. Never Gonna Give You Up - Rick Astley
34. Take on me - A-ha
35. Prince Igor - Polovtsian Dances, Borodin
36. Zelda's Lullaby - The Legend of Zelda, Ocarina of Time
37. Super Mario Bros theme, by Koji Kondo
38. Asa branca - Luiz Gonzaga
39. The Godfather theme
40. Professor Layton's theme

## Source

This is a port of Robson Couto's list of songs for Arduino: https://github.com/robsoncouto/arduino-songs
The sources he used are mentioned in melodies.py.
The sounds are all monophonic; if you want