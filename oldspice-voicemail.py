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
    print("Thanks! Please wait while we prepare your recording...")

    filenames = []

    if gender == "m":
        filenames.append("m-b1-hello.mp3")
        filenames.append("m-b2-have_dialed.mp3")
    elif gender == "f":
        filenames.append("f-b1-hello_caller.mp3")
        filenames.append("f-b2-lady_at.mp3")

    for number in phone:
        name = mp3.get_name("number", gender, number)
        filenames.append(name)

    if gender == "m":
        filenames.append("m-r0-cannot_come_to_phone.mp3")
    elif gender == "f":
        filenames.append("f-r0.1-unable_to_take_call.mp3")
        filenames.append("f-r0.2-she_is_busy.mp3")

    for reason in reasons:
        name = mp3.get_name("reason", gender, reason)
        filenames.append(name)

    if gender == "m":
        filenames.append("m-leave_a_message.mp3")

    for ending in endings:
        name = mp3.get_name("ending", gender, ending)
        filenames.append(name)

    print("Downloading necessary files...")
    for file in filenames:
        mp3.download(file)
    mp3.concatenate(filenames, out_filename)
    print("Your recording has been created and saved! Enjoy!")

main()
