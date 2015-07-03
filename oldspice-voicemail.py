__author__ = 'Tony Zhaocheng Tan <https://tonytan.io/about>'

import prompt
import mp3

def main():
    done = False
    while not done:
        print("Welcome to the Old Spice Voicemail generator!")
        gender = prompt.gender()
        phone = prompt.phone()
        reasons = prompt.reason(gender)
        endings = prompt.ending(gender)
        done = prompt.confirm(gender, phone, reasons, endings)
        if not done:
            print("Let's start over again.")
    out_filename = prompt.filename()
    print("Thanks! Please wait while we make your recording...")

    filenames = []
    for number in phone:
        name = mp3.get_name("number", gender, number)
        mp3.download(name)
        filenames.append(name)
    for reason in reasons:
        name = mp3.get_name("reason", gender, reason)
        mp3.download(name)
        filenames.append(name)
    for ending in endings:
        name = mp3.get_name("ending", gender, ending)
        mp3.download(name)
        filenames.append(name)
    mp3.concatenate(filenames, out_filename)
    print("Your file has been created and saved! Enjoy!")

main()
