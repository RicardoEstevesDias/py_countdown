from playsound import playsound
import time
heure_fin = 17
minute_fin = 27
seconde_fin = 00


def actu(result):
    
    heure_actuel = result.tm_hour
    if heure_actuel < 10:
        heure_actuel = (f"0{heure_actuel}")
        
    minute_actuel = result.tm_min
    if minute_actuel < 10:
        minute_actuel = (f"0{minute_actuel}")
        
    seconde_actuel = result.tm_sec
    if seconde_actuel < 10:
        seconde_actuel = (f"0{seconde_actuel}")
        
    temps_actuel = (f"{heure_actuel}:{minute_actuel}:{seconde_actuel}")
    return temps_actuel
    
    
def rest(result):
    
    heure_restant = heure_fin - result.tm_hour
    minute_restant = minute_fin - result.tm_min
    seconde_restant = seconde_fin - result.tm_sec 
    
    if seconde_restant < 0:
        minute_restant -= 1
        seconde_restant += 60
    if seconde_restant < 10:
        seconde_restant = (f"0{seconde_restant}")
        
    if minute_restant < 0:
        heure_restant = "00"
        minute_restant += 60
    if minute_restant < 10:
        minute_restant = (f"0{minute_restant}")
        
    if type(heure_restant) == int and heure_restant < 10:
        heure_restant = (f"0{heure_restant}")
        
    if heure_restant == "00":
        temps_restant = (f"{minute_restant}:{seconde_restant}")
    elif heure_restant == "00" and minute_restant == "00":
        temps_restant = (f"{seconde_restant}")
    else:
        temps_restant = (f"{heure_restant}:{minute_restant}:{seconde_restant}")
        
    return temps_restant


while(True):
    result = time.localtime()
    temps_actuel = actu(result)
    temps_restant = rest(result)
    
    print(f"Heure actuelle = {temps_actuel}")
    print(f"Temps restant = {temps_restant}")
    #print(type(temps_restant))
    
    if temps_restant == "00:00":
        print("Fini")
        playsound('success-fanfare-trumpets-6185.mp3')
        break
    
    time.sleep(1)

