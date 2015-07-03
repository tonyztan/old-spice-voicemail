__author__ = 'Tony Zhaocheng Tan <https://tonytan.io/about>'

import urllib.request
import shutil

def download(name):
    url = "https://tonyztan.github.io/static/old-spice-voicemail/" + name
    with urllib.request.urlopen(url, cafile="DigiCert_EV_Root.cer") as response, open(name, 'wb') as file:
        shutil.copyfileobj(response, file)
    return

def get_name(category, gender, choice):
    if category == "number":
        if choice == "0" or choice == "1" or choice == "2" or choice == "3" or choice == "4"\
                or choice == "5" or choice == "6" or choice == "7" or choice == "8" or choice == "9":
            return choice + ".mp3"
        else:
            print("Get Name Error! (Invalid reason)")
            return

    elif category == "reason":
        if gender == "m":
            names = {'a': "m-r1-building.mp3", 'b': "m-r2-cracking_walnuts.mp3",
                     'c': "m-r3-polishing_monocole.mp3", 'd': "m-r4-ripping_weights.mp3"}
            return names[choice]
        elif gender == "f":
            names = {'a': "f-r1-ingesting_old_spice.mp3", 'b': "f-r2-listening_to_reading.mp3",
                     'c': "f-r3-lobster_dinner.mp3", 'd': "f-r4-moon_kiss.mp3", 'e': "f-r5-riding_a_horse.mp3"}
            return names[choice]
        else:
            print("Get Name Error! (Invalid reason)")
            return

    elif category == "ending":
        if gender == "m":
            names = {'a': "m-e1-horse.mp3", 'b': "m-e2-jingle.mp3", 'c': "m-e3-on_phone.mp3",
                     'd': "m-e4-swan_dive.mp3", 'e': "m-e5-voicemail.mp3"}
            return names[choice]
        elif gender == "f":
            names = {'a': "f-e1-she_will_get_back_to_you.mp3", 'b': "f-e2-thanks_for_calling.mp3"}
            return names[choice]
        else:
            print("Get Name Error! (Invalid ending)")
            return
    else:
        print("Get Name Error! (No category provided)")
        return

def concatenate(filenames, out_filename):
    destination = open(out_filename + ".mp3", 'wb')
    for filename in filenames:
        shutil.copyfileobj(open(filename, 'rb'), destination)
    destination.close()
