import requests
import smtplib, ssl
from bs4 import BeautifulSoup
import yagmail
import time
#aqui ingresa en las primeras comillas tu correo y en las segundas tu contraseña para desde aqui se envien los correos
yagmail.register('testingproyects06@gmail.com', 'escuelacorreo01')

#esta es la funcion principal del programa
def saveInfo():
    numero = 0
    while(numero <= 10):
        infoTotal = []
        informacion = []
        datos = requests.get('https://coinmarketcap.com/es/currencies/bitcoin/')
        soup = BeautifulSoup(datos.content, 'html.parser')
        nombre = [soup.find('h1').text]
        precio = [soup.find(class_='cmc-details-panel-price__price').text]
        for i in nombre:
            for j in precio:
                informacion += nombre
                informacion += precio
        datosE = requests.get('https://coinmarketcap.com/es/currencies/ethereum/')
        soupE = BeautifulSoup(datosE.content, 'html.parser')
        nombreE = [soupE.find('h1').text]
        precioE = [soupE.find(class_='cmc-details-panel-price__price').text]
        for i in nombreE:
            for j in precioE:
                informacion += nombreE
                informacion += precioE
        datosBE = requests.get('https://coinmarketcap.com/es/currencies/bitcoin-cash/')
        soupBE = BeautifulSoup(datosBE.content, 'html.parser')
        nombreBE = [soupBE.find('h1').text]
        precioBE = [soupBE.find(class_='cmc-details-panel-price__price').text]
        for i in nombreE:
            for j in precioBE:
                informacion += nombreBE
                informacion += precioBE
        infoTotal  = infoTotal +  [informacion]

        receiver = "" ,#aqui ingresa el correo del destinatario// here put your email
        body = "hola, estos son los precios de las 3 cryptomonedas actualmente",  infoTotal
        yag = yagmail.SMTP("testingproyects06@gmail.com")
        yag.send(
            to=receiver,
            subject="test con precios de cryptomonedas",
            contents = body
        )
        numero = numero + 1
        time.sleep(15)

saveInfo()






