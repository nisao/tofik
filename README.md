Tofik
=====

Introduction
------------

Tofik is a python script based on Julius LVCSR (large vocabulary continuous speech recognition) decoder software to control Ubuntu. It very simple example how Julius can be set up and useful.

Requirements
------------

python3 and julius-voxforge packages - which can be installed with usage of following command:
    
    sudo apt-get install python3 python3-gi julius-voxforge
    
Usage
-----

You need to have julius installed in the newest version - you can find step by step guide at link below:

    http://kamilskowron.pl/en/linux/julius-step-by-step-step-1-instalation/

Clone the repository to your home directory:
    
    git clone https://github.com/Emanuel1989/tofik.git
    
Go to cloned and simply start Julius:

    cd ~/tofik
    padsp julius -C ./python/julian.jconf | python3 ./python/tofik.py

Important files
---------------

Julius configuration file:
  
    python/julian.jconf
    
Vocabulary file:
  
    python/mediaplayer.voca
    
Grammar file:

    python/mediaplayer.grammar
    
Vocabulary dictionary(english words dictionary downloaded from - http://www.keithv.com/software/giga/):

    python/voca.dic
