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
# text-generation-webui
Referring to https://huggingface.co/TheBloke/dolphin-2.6-mistral-7B-GGUF I followed the steps and installed text-generation-webui
To use my powerful PC in the network, I ran the command for port-forwarding 
ssh -L 7860:localhost:7860 user@10.0.0.177
and then http://localhost:7860/


why ollama doesn't use my gpu on linux machine with rtx 3090. The nvcc --version returns 12.8 nvidia-smi returns NVIDIA-SMI 550.144.03             Driver Version: 550.144.03     CUDA Version: 12.4.  How 
# ComfyUI
python main.py --listen 0.0.0.0


# Postgres and PG-Admin
https://medium.com/@marvinjungre/get-postgresql-and-pgadmin-4-up-and-running-with-docker-4a8d81048aea
docker run --name sqlpractice -e POSTGRES_PASSWORD=lohrasp -p 5432:5432 -d postgres
docker run --name pgadmin-container -p 5050:80 -e PGADMIN_DEFAULT_EMAIL=lohraspco@gmail.com -e PGADMIN_DEFAULT_PASSWORD=lohrasp -d dpage/pgadmin4 
docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' sqlpractice

check database
docker exec -it sqlpractice psql -U postgres

## load dvdrental
Approach selected: 
in local 
pg_restore -U postgres -d dvdrentaldb dvdrental.tar

Approach 1
docker cp dvdrental.tar sqlpractice:/var/lib/postgresql/dvdrental.tar
docker exec -i sqlpractice pg_restore -U postgres -d dvdrentaldb -n dvd  /var/lib/postgresql/dvdrental.tar
approach2:
Run the New Container with Volume Mounted: Replace /path/to/local/directory with the path to the directory containing your dvdrental.tar file, and /path/in/container with the desired path inside the container.
docker run -d -p 5432:5432 --name sqlpractice -v /path/to/local/directory:/path/in/container postgres
docker exec -i sqlpractice pg_restore -U postgres -d dvdrentaldb -n dvd < /path/in/container/dvdrental.tar



Check your command The command you have psql -h 172.17.0.2 -U postgres -d sqlpractice needs to have the host be localhost or 127.0.0.1 if you have successfully mapped your docker container's 5432 port to the host. If you are using 172.17.0.2 then it must be the address of the postgress container in your host docker network and you should not use port mapping (instead using host networking which is less common).

load the DVD rental sample database into PostgreSQL:
psql -h 127.0.0.1 -U postgres -d dvdrental -f .\dvdrental.tar




  git config --global user.email "lohraspco@gmail.com"
  git config --global user.name "Matt Najarian"