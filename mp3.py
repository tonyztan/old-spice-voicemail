__author__ = 'Tony Zhaocheng Tan <https://tonytan.io/about>'

import urllib.request
import urllib.error
import shutil
import os
import sys

def download(name):
    url = "https://tonyztan.github.io/static/old-spice-voicemail/" + name
    print("Downloading:", name)
    try:
        with urllib.request.urlopen(url, cafile="DigiCert_EV_Root.cer") as response, open(name, 'wb') as file:
            shutil.copyfileobj(response, file)
    except urllib.error.URLError:
        print("Your Internet connection is not private. A secure connection to the server cannot be established."
              "\n\nEither you are not properly connected to the Internet, "
              "or attackers may be trying to compromise your computer and steal your information."
              "\nYou cannot proceed right now because it is dangerous to do so."
              "\nNetwork errors and attacks are usually temporary, so this program will probably work later."
              "\n\nYou may wish to check your Internet connectivity or switch to a different network and try again.")
        sys.exit()
    return

def get_name(category, gender, choice):
    if category == "number":
        if choice in ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9"):
            return choice + ".mp3"
        else:
            print("Get Name Error! (Invalid number)")
            sys.exit()

    elif category == "reason":
        if gender == "m":
            names = {'a': "m-r1-building.mp3", 'b': "m-r2-cracking_walnuts.mp3",
                     'c': "m-r3-polishing_monocole.mp3", 'd': "m-r4-ripping_weights.mp3"}
            if choice in names:
                return names[choice]
            else:
                print("Get Name Error! (Invalid reason)")
                sys.exit()
        elif gender == "f":
            names = {'a': "f-r1-ingesting_old_spice.mp3", 'b': "f-r2-listening_to_reading.mp3",
                     'c': "f-r3-lobster_dinner.mp3", 'd': "f-r4-moon_kiss.mp3", 'e': "f-r5-riding_a_horse.mp3"}
            if choice in names:
                return names[choice]
            else:
                print("Get Name Error! (Invalid reason)")
                sys.exit()
        else:
            print("Get Name Error! (Invalid gender)")
            sys.exit()

    elif category == "ending":
        if gender == "m":
            names = {'a': "m-e1-horse.mp3", 'b': "m-e2-jingle.mp3", 'c': "m-e3-on_phone.mp3",
                     'd': "m-e4-swan_dive.mp3", 'e': "m-e5-voicemail.mp3"}
            if choice in names:
                return names[choice]
            else:
                print("Get Name Error! (Invalid ending)")
                sys.exit()
        elif gender == "f":
            names = {'a': "f-e1-she_will_get_back_to_you.mp3", 'b': "f-e2-thanks_for_calling.mp3"}
            if choice in names:
                return names[choice]
            else:
                print("Get Name Error! (Invalid ending)")
                sys.exit()
        else:
            print("Get Name Error! (Invalid gender)")
            return
    else:
        print("Get Name Error! (Invalid category)")
        sys.exit()

def get_file_list(gender, phone, reasons, endings):
    filenames = []

    if gender == "m":
        filenames.append("m-b1-hello.mp3")
        filenames.append("m-b2-have_dialed.mp3")
    elif gender == "f":
        filenames.append("f-b1-hello_caller.mp3")
        filenames.append("f-b2-lady_at.mp3")

    for number in phone:
        name = get_name("number", gender, number)
        filenames.append(name)

    if gender == "m":
        filenames.append("m-r0-cannot_come_to_phone.mp3")
    elif gender == "f":
        filenames.append("f-r0.1-unable_to_take_call.mp3")
        filenames.append("f-r0.2-she_is_busy.mp3")

    for reason in reasons:
        name = get_name("reason", gender, reason)
        filenames.append(name)

    if gender == "m":
        filenames.append("m-leave_a_message.mp3")

    for ending in endings:
        name = get_name("ending", gender, ending)
        filenames.append(name)

    return filenames

def concatenate(filenames, out_filename):
    destination = open(out_filename + ".mp3", 'wb')
    file_list = open("mp3list.txt", 'w')
    for filename in filenames:
        shutil.copyfileobj(open(filename, 'rb'), destination)
        file_list.write(filename + "\n")
    destination.close()
    file_list.close
    print("Cleaning up temporary files...")
    for filename in set(filenames):
        os.remove(filename)
    return
