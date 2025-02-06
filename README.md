# Setup The system
I bought a used Nvidia RTX 3090 TI FE 24Gb for $800 then bought my other PC parts from MicroCenter.
My PC has Ryzen 7 CPU and 32 GB of Ram. After assembly I installed Ubuntu 24.04.

On Linux installing compatible Nvidia driver, Cuda, and Pytorch versions is a headache. I had errors with the following apps:
- text-generation-webui (didn't run)
- ollama (didn't use my GPU)
 Here is how I installed and finally made them work. 



## Nvidia driver
NVIDIA-SMI 550.144.03 
sudo dmesg | grep -i nvrm
nvidia-smi -L
```[_{{{CITATION{{{_2{ollama/docs/gpu.md at main - GitHub](https://github.com/ollama/ollama/blob/main/docs/gpu.md)

nvtop (monitor GPU and CPU usage)


# Cuda
nvcc --version
ls -l /usr/local/cuda
ls -l /usr/local/cuda/lib64/libcudart*


# llama.cpp didn't work following the process 
https://erichartford.com/dolphin-25-mixtral-8x7b
instead of cmake . I had to use 
cmake -B build -DGGML_CUDA=ON
cmake --build build --config Release
but server wasn't created in the root directory



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

Check your command The command you have psql -h 172.17.0.2 -U postgres -d sqlpractice needs to have the host be localhost or 127.0.0.1 if you have successfully mapped your docker container's 5432 port to the host. If you are using 172.17.0.2 then it must be the address of the postgress container in your host docker network and you should not use port mapping (instead using host networking which is less common).

load the DVD rental sample database into PostgreSQL:
psql -h 127.0.0.1 -U postgres -d dvdrental -f .\dvdrental.tar



# Cheat Sheet Ollama
$ ollama list
huggingface-cli login

export HUGGINGFACE_TOKEN

# docker

 
n linux, after a suspend/resume cycle, sometimes Ollama will fail to discover your NVIDIA GPU, and fallback to running on the CPU. You can workaround this driver bug by reloading the NVIDIA UVM driver with sudo rmmod nvidia_uvm && sudo modprobe nvidia_uvm

# open-webui
pip install open-webui
open-webui serve --port 8090
myllms



deepseek Janus-pro 7b

Trouble shooting
sudo apt install libtinfo5 didn't work soo I used the following approach:
wget http://archive.ubuntu.com/ubuntu/pool/universe/n/ncurses/libtinfo5_6.3-2ubuntu0.1_amd64.deb
sudo dpkg -i libtinfo5_6.3-2ubuntu0.1_amd64.deb
sudo apt-get install -f