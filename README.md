Tofik
=====

Introduction
------------

Tofik is a python script based on Julius LVCSR (large vocabulary continuous speech recognition) decoder software to control Ubuntu. It very simple example how Julius can be set up and useful.

Requirements
------------

python3, julius-voxforge and libnotify-bin packages - which can be installed with usage of following command:
    
    sudo apt-get install python3 julius-voxforge libnotify-bin
    
Usage
-----

You need to have julius installed in the newest version - you can find step by step guide at link below:

http://kamilskowron.pl/en/linux/julius-step-by-step-step-1-instalation/

Clone the repository to your home directory:
    
    git clone https://github.com/Emanuel1989/tofik.git
    
Go to cloned and simply start Julius:

    cd ~/tofik
    padsp julius -C ./python/julian.jconf 2> /dev/null | python3 ./python/tofik.py

Important files
---------------

Julius configuration file:
  
    python/julian.jconf
    
Vocabulary file:
  
    python/mediaplayer.voca
    
Grammar file:

    python/mediaplayer.grammar
    
Vocabulary dictionary(english words dictionary downloaded from - http://www.keithv.com/software/giga/ ):

    python/voca.dic

Important system settings
-------------------------

This is the level that input should be "catched" when listening to music etc.(It shouldn't pass half of scale)
![Valid noices level](http://kamilskowron.pl/music.png "Valid noices level")

And this one is the level that input command should be "catched"(It shoudn't pass over the whole scale but it should be considerebly louder then music and other noices)
![Valid user command level](http://kamilskowron.pl/command.png "Valid user command level")
