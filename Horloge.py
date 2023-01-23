import time
import keyboard
# for this exercise you need to install keyboard

temps = True
prog = True

def horloge(hour,minute,second):
    global temps
    global prog
# permit to choose between the clock anglosaxon and européene
    print("chose you horloge: EU or UK ")
    swap = input()

    Sun = None
# Use to choose your alarm
    print("alarm hour")
    alhour = int(input())
    print("alarm min")
    almin = int(input())
    print("alarm second")
    alsec = int(input())

    print("use the keyboard key 'q' to pause the cloack and 's' to resume it")
# Clock européene
    if swap == "EU" or swap == "eu":
        while prog == True:
            while temps == True:
                time.sleep(1)
                second +=1
                if second == 60 :
                    minute+=1
                    second = 0
                if minute == 60 :
                    hour += 1
                    minute = 0
                if hour == 24 :
                    hour = 0
                    minute = 0
                    second = 0
                print('\r',hour,":",minute,":",second,end='')
                if alhour == hour and almin == minute and alsec == second:
                    print("ALERTE!!!!!!")
                if keyboard.is_pressed('q'):
                    print("  the cloack is in pause state press s")
                    temps = False
            if keyboard.is_pressed('s'):
                print("  the cloack start")
                temps = True
# Clock Anglosaxon
    if swap == "UK" or swap == "uk":
        while prog == True:
            while temps == True:
                time.sleep(1)
                second += 1
                if second == 60:
                    minute += 1
                    second = 0
                if minute == 60:
                    hour += 1
                    minute = 0
                if hour == 24:
                    hour = 0
                    minute = 0
                    second = 0
                if hour < 12 :
                    Sun = "AM"
                    print('\r',hour, ":", minute, ":", second,Sun,end='')
                else :
                    Sun = "PM"
                    print('\r',hour - 12, ":", minute, ":", second,Sun,end='')
                if alhour == hour and almin == minute and alsec == second:
                    print("ALERTE!!!!!!")
                if keyboard.is_pressed('q'):
                    print("  the cloack is in pause state press s")
                    temps = False
            if keyboard.is_pressed('s'):
                print("  the cloack start")
                temps = True


horloge(16,15,45)
