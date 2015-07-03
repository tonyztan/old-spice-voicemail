__author__ = 'Tony Zhaocheng Tan'

import prompt
import mp3

def main():
    print("Welcome to the Old Spice Voicemail generator!")
    gender = prompt.gender()
    phone = prompt.phone()
    reasons = prompt.reason(gender)
    endings = prompt.ending(gender)
    print(gender)
    print(phone)
    print(reasons)
    print(endings)
    for number in phone:
        name = mp3.get_name("number", gender, number)
        mp3.download(name)
    for reason in reasons:
        name = mp3.get_name("reason", gender, reason)
        mp3.download(name)
    for ending in endings:
        name = mp3.get_name("ending", gender, ending)
        mp3.download(name)

main()
