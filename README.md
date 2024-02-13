##Steam Auto Balance API

Ubuntu 20.04 LTC system is required to run docker

1.Let's update the system:
`sudo apt update`
2.Install additional packages for Docker
`sudo apt install curl software-properties-common ca-certificates apt-transport-https -y`

3.Import the GPG key

`wget -O- https://download.docker.com/linux/ubuntu/gpg | gpg --dearmor | sudo tee /etc/apt/keyrings/docker.gpg > /dev/null`
4. Add the docker repository
`echo "deb [arch=amd64 signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu jammy stable"| sudo tee /etc/apt/sources.list.d/docker.list > /dev/null`
5.Install docker
`sudo apt install docker-ce -y`
6.To run use command `docker-compose up --build`

