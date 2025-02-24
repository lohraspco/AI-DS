# Setup The system
I bought a used Nvidia RTX 3090 TI FE 24Gb for $800 then bought my other PC parts from MicroCenter.
My PC has Ryzen 7 CPU and 32 GB of Ram. 


I had many issues with Ubuntu and Ollama, Text-Generation-WebUI, .... so I switched to Widnows os. However I put the linux s After assembly I installed Ubuntu 24.04.


1- install graphics card and Cuda toolkit
2- install Ollama from the [official website](https://ollama.com/download/windows). Set the environment path, and restart VSCode (if you are using it)

3- set up git
- run this command in cmd ```ssh-keygen -t ed25519 -C "your_email@example.com" ```
- add public key to github
-  `git clone git@github.com:lohraspco/AI-DS.git`






A note on my Graphic Cards 
Installed official drivers from Nvidia site. I had issues with resolution (1080 instead of 4k), I tried a lot of things and even I installed a fresh copy of Windows again which didn't work. Finally I changed the cables and it fixed. I had used the problematic cables with my laptop and they didn't have issue. 
I use Integrated Graphics Devices (IGD) and my RTX 3090 Ti (PEG) to connect to monitors. 




  git config --global user.email "lohraspco@gmail.com"
  git config --global user.name "Matt Najarian"