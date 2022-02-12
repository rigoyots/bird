# Bird

### Authors
---
* Emilee Hatch
* Trent Black
* Francis Gomez
* Joseph Devincenzi
* Ashley Dahlberg

### Emails
---
* hemileecm@byui.edu
* trentblack@byui.edu
* rigoyots@gmail.com
* dev15010@byui.edu 
* dah20006@byui.edu

### Overview
---
Bird 

### Gameplay
---
Bird is played according to the following rules.

* Players can move up using the space bar key on the keyboard
* If the player collides with a pipe they lose the game.

### Project Structure 
---
The project files and folders are organized as follows:
```
root (Bird)                    (project root folder)
+-- INSIDE THE GAME FOLDER --+
  +-- Game Folder              (source code for game)
    +-- Audio Folder           (source code for Audio)
      +-- audio.py             (sound class)
    +-- Bird Folder            (source code for player)
      +-- bird.py              (player class)
    +-- Picture Folder         (source code for pictures)
      +-- pictures.py          (picture class)
  +-- Pipe folder              (source code for pipes)
    +-- pipe.py                (pipe class)
  +-- Score folder             (source code for Score)
    +-- score.py               (pipe class)
  
+-- OUTSIDE THE GAME FOLDER --+ 
  +-- .gitignore      
  +-- downpipe.png             (image)
  +-- flap.wav                 (sound)
  +-- flappy1.png              (image)
  +-- flappy3.png              (image)         
  +-- main.py                  (entry point for program)
  +-- over.wav                 (sound)
  +-- pipe.png                 (image)
  +-- README.md                (general info)
  +-- test.py                  (test file)
  +-- tests.py                 (bird test file)
```

### Required Technologies
---
* Python 3.8.0
* Raylib Python CFFI 3.7