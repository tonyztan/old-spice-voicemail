#!/usr/bin/env python

"""
Old Spice Voicemail Generator.

Generates a voicemail message using spliced sounds of the Old Spice Guy,
based on a phone number, reasons, and endings selected by the user.

Outputs a mp3 file based on a name of the user's choosing and mp3list.txt listing the files used.

Provides an interactive user interface, but also supports command-line arguments.
"""

import sys
import getopt
import prompt
import mp3

__author__ = 'Tony Zhaocheng Tan'
__copyright__ = "Copyright 2015, Tony Zhaocheng Tan"
__license__ = "MIT"
__version__ = "1.0"
__email__ = "tony@tonytan.io"

def process(gender, phone, reasons, endings, out_filename):
    """
    Takes all the information and calls other functions to create the final mp3 file.
    :param gender: 'm' or 'f'.
    :param phone: a string that represents the phone number, consisting of exactly 10 digits. ('9876543210')
    :param reasons: a list of all the reasons a user selected, with each reason represented by a letter. (['a', 'c'])
    :param endings: a list of all the endings a user selected, with each ending represented by a letter. (['a', 'b'])
    :param out_filename: a string that is the desired file name chosen by the user. ("JohnDoeVoicemail")
    """
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
    """
    Provides an interactive user interface.

    Prompts the user for gender, phone, reason choice, and ending choice, and passes this on to process().
    """
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
    """
    Prints out the correct syntax for command-line arguments, and then terminates the program.
    """
    print("Syntax: \noldspice-voicemail.py --gender <m/f> --phone <10-digit number without separators> "
          "--reasons <reason letters> --endings <ending letters> --out <output filename>")
    print("\nExample: \noldspice-voicemail.py --gender m --phone 8881234567 --reasons acd --endings abde --out JohnDoe")
    print("\nAlternatively, you may use the interactive mode by not entering any arguments, like this:"
          "\noldspice-voicemail.py")
    sys.exit()

def parse_arguments(opts):
    """
    Parses all command-line arguments that the program is given.

    If all the necessary arguments have been provided correctly, the parameters are passed to process().

    Otherwise, syntax() is called and the program ends.
    :param opts: A list of all the arguments used when the program is run.
    """
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
                    if char in ('a', 'b', 'c', 'd', 'e'):
                        reasons.append(char)
                if not reasons:
                    syntax()
            else:
                syntax()
        elif opt in ('-e', "--endings"):
            if len(arg) < 6:
                endings = []
                for char in arg:
                    if char in ('a', 'b', 'c', 'd', 'e'):
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
    """
    Calls either interactive() or parse_arguments().

    If no arguments are given, interactive mode is started using interactive().

    If there are arguments to be parsed, parse_arguments() is called.
    """
    try:
        opts, args = getopt.getopt(sys.argv[1:], "g:p:r:e:o:h", ["gender=", "phone=", "reasons=", "endings=", "out=", "help"])
    except getopt.GetoptError:
        interactive()
    if not opts:
        interactive()
    else:
        parse_arguments(opts)

main()
