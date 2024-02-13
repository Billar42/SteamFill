# Steam Auto Balance API DIGISELLER

Ubuntu 20.04 LTC system is required to run docker
## Steps

* Let's update the system: `sudo apt update`
* Install additional packages for Docker `sudo apt install curl software-properties-common ca-certificates apt-transport-https -y`
* Import the GPG key `wget -O- https://download.docker.com/linux/ubuntu/gpg | gpg --dearmor | sudo tee /etc/apt/keyrings/docker.gpg > /dev/null`
* Add the docker repository `echo "deb [arch=amd64 signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu jammy stable"| sudo tee /etc/apt/sources.list.d/docker.list > /dev/null`
* Install docker `sudo apt install docker-ce -y`
* * Open `config.py` and change digiseller_token your shop
* To run use command `docker-compose up --build`
* To down docker use command `docker-compose down`
![image](https://github.com/Billar42/SteamFill/assets/75508060/f3257e5a-9413-409b-84ae-9112d122967a)
