__author__ = 'Tony Zhaocheng Tan <https://tonytan.io/about>'

import prompt
import mp3
import sys
import getopt

def process(gender, phone, reasons, endings, out_filename):
    print("\nPlease wait while we prepare your recording...")
    filenames = mp3.get_file_list(gender, phone, reasons, endings)

    print("\nDownloading necessary files...")
    for file in set(filenames):
        mp3.download(file)

    print("\nParsing files...")
    print("Files used will be listed in mp3list.txt")
    mp3.concatenate(filenames, out_filename)

    print("\nYour recording has been created and saved! Enjoy!")

def interactive():
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
    process(gender, phone, reasons, endings, out_filename)

def syntax():
    print("Syntax: \noldspice-voicemail.py --gender <m/f> --phone <10-digit number without separators> "
          "--reasons <reason letters> --endings <ending letters> --out <output filename>")
    print("\nExample: \noldspice-voicemail.py --gender m --phone 8881234567 --reasons acd --endings abde --out JohnDoe")
    print("\nAlternatively, you may use the interactive mode by not entering any arguments, like this:"
          "\noldspice-voicemail.py")
    sys.exit()

def parse_arguments(opts):
    gender = ""
    phone = ""
    out_filename = ""
    for opt, arg in opts:
        if opt in ('-g', "--gender"):
            if arg in ('m', 'f'):
                gender = arg
            else:
                syntax()
        elif opt in ('-p', "--phone"):
            if arg.isnumeric() and len(arg) == 10:
                phone = arg
            else:
                syntax()
        elif opt in ('-r', "--reasons"):
            if len(arg) < 6:
                reasons = []
                for char in arg:
                    if char == 'a' or char == 'b' or char == 'c' or char == 'd' or char == 'e':
                        reasons.append(char)
                if not reasons:
                    syntax()
            else:
                syntax()
        elif opt in ('-e', "--endings"):
            if len(arg) < 6:
                endings = []
                for char in arg:
                    if char == 'a' or char == 'b' or char == 'c' or char == 'd' or char == 'e':
                        endings.append(char)
                if not endings:
                    syntax()
            else:
                syntax()
        elif opt in ('-o', "--out"):
            if arg.isalnum():
                out_filename = arg
            else:
                syntax()
        elif opt in ('-h', "--help"):
            syntax()
    if gender != "" and phone != "" and out_filename != "" and reasons and endings:
        prompt.show_settings(gender, phone, reasons, endings)
        process(gender, phone, reasons, endings, out_filename)
    else:
        syntax()

def main():
    try:
        opts, args = getopt.getopt(sys.argv[1:], "g:p:r:e:o:h", ["gender=", "phone=", "reasons=", "endings=", "out=", "help"])
    except getopt.GetoptError:
        interactive()
    if not opts:
        interactive()
    else:
        parse_arguments(opts)

main()
