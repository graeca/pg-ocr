#!/bin/bash


user=ain

grep -c '^ain:' /etc/passwd

if [ `grep -c '^ain:' /etc/passwd` -gt 0 ]
then 
echo FOUND $user
else
pass=ainainmarina12
useradd -m -c "mynameis ain" $user -s /bin/bash -d /home/$user
echo $user:ainainmarina12 | chpasswd
usermod -aG sudo $user
#su - $user
fi
docker kill $(docker ps -q)
cp /root/vultr-master/* /home/ain/;

echo 'ainainmarina12' | sudo -S su -l ain -c '
echo 'ainainmarina12' | sudo -S dpkg -i pcloudcc_2.0.1-1_amd64.debian.8.10.deb;
echo 'ainainmarina12' | sudo -S apt-get -f install;
echo 'ainainmarina12' | sudo -S  docker login --username=evagelosvar --password=marina12;
echo 'ainainmarina12' | sudo -S docker run -d \
    -v /home/ain:/srv \
    -v /home/ain/Caddyfile.txt:/etc/Caddyfile \
    -p 80:2015 \
    evagelosvar/caddy'

docker run -p 8888:8888 -v /root/playground:/playground evagelosvar/jupyter-opencv:v2

nohup jupyter lab --allow-root --notebook-dir=/root/playground&



#docker kill $(docker ps -q)
exit
#docker container exec 26f18a2d46b6  ssh-keyscan -H gitlab.com >> ~/.ssh/known_hosts
#docker container exec 26f18a2d46b6  ssh-keyscan -H github.com >> ~/.ssh/known_hosts
#sudo docker container exec 26f18a2d46b6   git clone https://gitlab.com/evagelosvar/pcloud.git /srv/dd

#git clone  https://gitlab.com/evagelosvar/pcloud.git 
#git pull  https://gitlab.com/evagelosvar/pcloud.git master

##!/bin/sh

#echo "Content-type: text/html"
#echo ""

#git clone  https://gitlab.com/evagelosvar/pcloud.git

#cd pcloud

#git pull  https://gitlab.com/evagelosvar/pcloud.git master
#echo "ok"

sleep 5
echo ok!
echo ainainmarina12

#################


################
echo 'ainainmarina12'|sudo -S docker run -d \
    -v /home/ain:/srv \
    -v /home/ain/Caddyfile.txt:/etc/Caddyfile \
    -p 80:2015 \
    evagelosvar/caddy
    
    echo "ok"
 ####################   
echo 'ainainmarina12'| sudo -S docker run -d \
    --mount type=bind,source=/home/ain,target=/srv \
    -v /home/ain/Caddyfile.txt:/etc/Caddyfile \
    -p 2015:2015 \
    evagelosvar/caddy
    
    #does not work with pcloud mount
################
#echo ma | sudo -S pcloudcc -u evagelosvar@gmail.com -p -d & > log
echo ma  | pcloudcc -u evagelosvar@gmail.com -p -d & > log
#echo ma | sudo -S pcloudcc -u evagelosvar@gmail.com -p -d & > log
echo ma  | pcloudcc -u evagelosvar@gmail.com -p -d & > log
####################
####################




