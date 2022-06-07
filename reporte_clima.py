import requests
API_KEY = 'key'
BASE_URL = 'https://api.openweathermap.org/data/2.5/weather'
requests_url = f'{BASE_URL}?appid={API_KEY}&q=mar del plata&units=metric&lang=es'
response = requests.get(requests_url)

if response.status_code == 200:
    data = response.json()
    clima = data['weather'][0]['description']
    temp = data['main']['temp']
    sensacion = data['main']['feels_like']
    humedad = data['main']['humidity']
    nubosidad = data['clouds']['all']
    viento = data['wind']['speed']

else:
    print('Error')

import smtplib
import ssl
from email.message import EmailMessage

asunto = 'Reporte de clima para hoy:'
remitente = 'user@gmail.com'
destinatario = 'user@gmail.com'
pw = "password"
mensaje = EmailMessage()
mensaje['From'] = remitente
mensaje['To'] = destinatario
mensaje['Subjet'] = asunto

#Html con el reporte
html = f"""
<html>
    <head><h2>{asunto}</h2></head>
    <body>
        <p>Buen dia!</p>
        <p>Estado de clima: {clima}.</p>
        <p>Temperatura: {temp}C°.<p/>
        <p>Humedad: {humedad}%.</p>
        <p>Sensación termica: {sensacion}C°.</p>
        <p>Viento: {viento} km/h.</p|>
        <p>Nubosidad:{nubosidad}%.</p>
        <h3>Buena jornada!</h3>
    </body>
</html>
"""
mensaje.add_alternative(html,subtype="html")
context = ssl.create_default_context()

print('Enviando..')

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as server:
    server.login(remitente, pw)
    server.sendmail(remitente,destinatario,mensaje.as_string())
    server.quit()
print('Enviado!')
