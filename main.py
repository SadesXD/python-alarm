import time
import pyttsx3
import os

def bukan(set):
    str(set)

def cls():
    os.system('cls')

# seconds converter function
def ms(t):
    if type(t) != "str":
        bukan(t)
    a1 = len(t) - 1
    a2 = len(t)
    angka = t[0:a1]
    if type(angka) != int:
        try:
            int(angka)
        except:
            print("[!] time is not defined")
    opsi = t[a1:a2].lower()
    if opsi == "m":
        angka = t[0:a1]
        if type(angka) != int:
            try:
                angka = int(angka)
            except:
                print("[!] time is not defined")
        return angka * 60
    elif opsi == "s":
        angkas = t[0:a1]
        if type(angkas) != int:
            try:
                angkas = int(angkas)
            except:
                print("[!] time is not defined")
        return angkas
    elif opsi == "h":
        angkad = t[0:a1]
        if type(angkad) != int:
            try:
                angkad = int(angkad)
            except:
                print("[!] time is not defined")
        return angkad * 3600
    elif opsi == "d":
        angkah = t[0:a1]
        if type(angkah) != int:
            try:
                angkad = int(angkah)
            except:
                print("[!] time is not defined")
        return angkah * 216000
    else:
        print("[!] format time is not defined")

def play():
    cls()
    waktu = input("how many time will you set your alarm ??: ")
    while not waktu or waktu == "":
        cls()
        print("Please input the time !!\n")
        waktu = input("how many time will you set your alarm ??: ")

    reason = input("give the reason of your alarm !! [ press ENTER if you don't have reason ]: ")
    if not reason or reason == "":
        reason = "No reason"

    timernya = int(ms(waktu))
    print(f"You have been set time of alarm: {waktu} and the reason is: {reason}")
    time.sleep(timernya)
    engine = pyttsx3.init()
    engine.setProperty('rate',120)
    engine.say(f"Hello dude your alarm is over for the reason: {reason}")
    print(f"\n[!] Hello dude your alarm is over for the reason: {reason}\n")
    engine.runAndWait()

awal = input("[ Simple python alarm with voice ]\n\n[ ALARM ] -> set your alarm\n[ GUIDE ] -> show usage of simple python alarm\n[ EXIT ] -> stop the process\n\nSelect your options: ")

def balek():
    global awal
    while not awal or awal == "":
        cls()
        print("Please select the options\n")
        awal = input("[ Simple python alarm with voice ]\n\n[ ALARM ] -> set your alarm\n[ GUIDE ] -> show usage of simple python alarm\n[ EXIT ] -> stop the process\n\nchoose your selection: ")
    while awal.lower() != "alarm" and awal.lower() != "guide" and awal.lower() != "guides" and awal.lower() != "exit":
        os.system('cls')
        print("Options not found\n")
        awal = input("[ Simple python alarm with voice ]\n\n[ ALARM ] -> set your alarm\n[ GUIDE ] -> show usage of simple python alarm\n[ EXIT ] -> stop the process\n\nchoose your selection: ")

    if awal.lower() == "alarm":
        play()
    elif awal.lower() == "guide" or awal.lower() == "guides":
        cls()
        tutor = "1. first type ALARM in options for set your alarm\n2. then type how long time will you set your alarm, then press ENTER if you done\nNote: format of time must be [s|m|h|d], Example: -> 2s,2m,5m\n3. give the reason of your alarm, press ENTER if you don't have reason\n4. and you can waiting your alarm over, and if your alarm is over, some voice will warns you that your alarm is over\n"
        print(tutor)
        balik = input("type BACK for back to main menu: ")
        if balik.lower() == "back":
            cls()
            awal = input("[ Simple python alarm with voice ]\n\n[ ALARM ] -> set your alarm\n[ GUIDE ] -> show usage of simple python alarm\n[ EXIT ] -> stop the process\n\nchoose your selection: ")
            balek()
        else:
            balek()
    elif awal.lower() == "exit":
        quit()

balek()
        
