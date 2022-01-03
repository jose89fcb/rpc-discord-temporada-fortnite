from pypresence import Presence
import time
import json
import requests
from colorama import Fore, init
init()

    


client_id = ' '  #Consigue la ID de tu aplicacion en: https://discord.com/developers/applications "APPLICATION ID"
RPC = Presence(client_id,pipe=0) 
RPC.connect() 
response = requests.get("https://jose89fcb.es/diasFortnite/dias.php")
diasFortnite = response.json()['DiasFN']
print(Fore.CYAN + diasFortnite + "\n")

print(Fore.WHITE + "RPC está en " + Fore.GREEN + "LINEA!")
print(Fore.WHITE + "--------")
while True:  # La presencia permanecerá encendida mientras el programa se esté ejecutando.
     
    
    response = requests.get("https://jose89fcb.es/diasFortnite/dias.php")
    diasFortnite = response.json()['DiasFN']
    
    
    fortnite = diasFortnite
    
    
    RPC.update(

    details=fortnite + "!", 
    state="Cada 5 minutos se reinicia",
    small_image="logofn",
    large_image="logofn",
    large_text="Progresso Fortnite",
    small_text="Progresso Fortnite",
    

    buttons = [
        {"label": "twitter", "url": "https://twitter.com/jose89fcb"},
        {"label": "Mi web", "url": "https://jose89fcb.es"},
        



    ],
   
    
    start=time.time())
    print(Fore.CYAN + diasFortnite)
    
   
   

    
    
    time.sleep(300) # Convertimos segundos en minutos, en este caso 5 minutos es 300 segundos
    
   

