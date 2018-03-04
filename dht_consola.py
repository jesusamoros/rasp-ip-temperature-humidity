#!/usr/bin/python
#! /usr/bin/env python

# Script ORIGINAL -> Web          : http://internetdelascosas.cl/
 
# Importa las librerias necesarias 
import sys
import time
import Adafruit_DHT
import MySQLdb
import socket
import os, time, sys, smtplib
from time import gmtime, strftime
t = strftime("%X", gmtime())
a = os.popen("curl -s http://icanhazip.com").read()
print "Mi IP: ",a + t
hostname = socket.gethostname()
print hostname
conn = MySQLdb.connect(host= "tecnoactivity.es",
                  user="iotroot",
                  passwd="Ay5x5e^8",
                  db="tecnoactivity_es_iot")
x = conn.cursor()
sensor = Adafruit_DHT.DHT11

# Configuracion del puerto GPIO al cual esta conectado  (GPIO 23)
pin = 23

# Intenta ejecutar las siguientes instrucciones, si falla va a la instruccion except
try:	

		# Obtiene la humedad y la temperatura desde el sensor 
		humedad, temperatura = Adafruit_DHT.read_retry(sensor, pin)
		# Imprime en la consola las variables temperatura y humedad con un decimal
		print('Temperatura={0:0.1f}*  Humedad={1:0.1f}%'.format(temperatura, humedad))
		conn = MySQLdb.connect(host= "tecnoactivity.es",
                  user="iotroot",
                  passwd="Ay5x5e^8",
                  db="tecnoactivity_es_iot")
		x = conn.cursor()
		try:
		   x.execute("""INSERT INTO datosIOT (ip,host,temperatura,humedad) VALUES (%s,%s,%s,%s)""",(a,hostname,temperatura,humedad))
		   conn.commit()
		except:
		   conn.rollback()
		conn.close()
		print('debug ejecute')

# Se ejecuta en caso de que falle alguna instruccion dentro del try
except Exception,e:
	# Imprime en pantalla el error e
	print str(e)
