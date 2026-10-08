import time
import random

wait = random.randint(1, 4)
farkas_some = ["IG: bazsaa1340, Facebook: Balázs Farkas, TikTok: Bazsa1340, Snapchat: Elvileg feltörve"]

#betöltés, üdvözlés

print("Üdv a büdikalkulátorban! Kérlek várj egy kicsit, amíg betölt az oldal...")

print("Akarsz dumcsizni? Tudom, hogy van barátod, de semmi olyant nem akarok.... ")

#készenléti státusz bekérése

readyon = input("Ha igen, akkor írd be, hogy igen és nyomj entert! ")

if readyon.lower() == "igen":
    i = int(input("Hány éves vagy? "))
    time.sleep(wait)

    if i < 12:
        print("Sajnos most még túl fiatal vagy. Próbálkozz később. ")
    elif i >= 12 and i < 14:
        print("Waooo, te pont illesz a kis büdihez. Keresd instán. IG: bazsaa1340 ")
    elif i >= 14 and i <= 15:
        print("Sajnos most már túl öreg vagy. GAME OVER....")
elif readyon.lower() == "nem":
    farkassome_input = input("Ha szeretnéd, hogy megmutassuk neked a kis büdi elérhetőségeit, akkor nyomj entert! ")

    if farkassome_input == "":
        print("Köszönjük, hogy érdeklődtél! A kis büdi elérhetőségei a következők: ")
        time.sleep(2)
        print(farkas_some)
    else:
        print("Rendben, köszönjük, hogy érdeklődtél! ")
