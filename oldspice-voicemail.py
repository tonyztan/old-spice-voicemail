__author__ = 'Tony Zhaocheng Tan'

import prompt

def main():
    print("Welcome to the Old Spice Voicemail generator!")
    gender = prompt.gender()
    phone = prompt.phone()
    reasons = prompt.reasons(gender)
    endings = prompt.endings(gender)
    print(gender)
    print(phone)
    print(reasons)
    print(endings)

main()