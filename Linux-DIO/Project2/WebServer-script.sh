#!/bin/bash


echo "Atualizando o sistema"

apt-get update && apt-get upgrade -y

echo "Instalando o Apache e o Unzip"

apt-get install apache2 -y

apt-get install unzip -y


echo "Copiando os arquivos do repositorio para a pasta do Apache"

cd /tmp

wget https://github.com/denilsonbonatti/linux-site-dio/archive/refs/heads/main.zip

unzip main.zip

cd linux-site-dio-main

cp -R * /var/www/html/








