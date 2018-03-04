#schema sensor DHT11
#http://www.internetdelascosas.cl/wp-content/uploads/2017/05/Raspberry-Pi-DHT11_bb-768x374.png
# source spanish languaje  http://www.internetdelascosas.cl/2017/05/19/raspberry-pi-conectando-un-sensor-de-temperatura-y-humedad-dht11/


sudo apt-get update && upgrade
sudo apt-get install git-core
sudo apt-get install build-essential python-dev

#create directory for proyect
mkdir proyect
cd proyect

#clone proyect
git clone https://github.com/adafruit/Adafruit_Python_DHT.git
cd Adafruit_Python_DHT

#install adafruit
sudo python setup.py install


#clone my script, this script its modified from original -> git clone https://github.com/internetdelascosas/RaspberryPi-DHT11.git
git clone https://github.com/jesusamoros/rasp-ip-temperature-humidity.git

#install mysql dependencies
#don't remenber what is the correct, but whith this dependecies its working
apt-get install pip
pip install mysql-python
pip install MySQL-python
easy_install mysql-python
pip install mysql
pip install mysqlclient


# how to work 
python new_dht_consola.py

#remenber add to crontab 
#example */10 * * * *   /usr/bin/python /root/proyect/new_dht_consola.py  update any 10min.