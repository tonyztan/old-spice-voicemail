#!/usr/bin/env python3

"""
Handles file operations, part of the Old Spice Voicemail Generator.

Contains functions for downloading and concatenating mp3 files,
and for getting individual file names and generating a list of file names.
"""

import sys
import os
import urllib.request
import urllib.error
import shutil

__author__ = 'Tony Zhaocheng Tan'
__copyright__ = "Copyright 2015, Tony Zhaocheng Tan"
__license__ = "MIT"
__version__ = "1.0"
__email__ = "tony@tonytan.io"

def download(name):
    """
    Downloads the file with the requested name from the server.

    Uses a secure HTTPS connection to https://tonyztan.github.io/.
    If a secure connection cannot be established, a warning is displayed to the user and the program is terminated.

    :param name: The name of the file to be downloaded. Must exist on the server.
    :return: Nothing is returned. The downloaded files are stored in the program's directory.
    """
    url = "https://tonyztan.github.io/static/old-spice-voicemail/" + name
    print("Downloading:", name)
    try:
        with urllib.request.urlopen(url, cafile="DigiCert_EV_Root.cer") as response, open(name, 'wb') as file:
            # Requests the file and verifies the server certificate using the expected DigiCert Root CA used by GitHub.
            # Copies all of the response from server to a local file of the same name.
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
    """
    Gets the name of the file corresponding to the category, gender, and option requested.
    :param category: Type of file. Can be "number", "reason", or "ending".
    :param gender: 'm' or 'f'.
    :param choice: Specifies the file being requested for.
    If the category is "number", then the choice can be any number from 0 to 9. ('8')
    If the category is "reason", then the choice can be any letter choice that is valid for the specified gender. ('b')
    If the category is "ending", then the choice can be any letter choice that is valid for the specified gender. ('a')
    :return: Returns the name of the file requested as a string.
    """
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
            sys.exit()
    else:
        print("Get Name Error! (Invalid category)")
        sys.exit()

def get_file_list(gender, phone, reasons, endings):
    """
    Creates a list of names of the files needed to produce the final mp3 based on user's preferences.
    :param gender: 'm' or 'f'.
    :param phone: a string that represents the phone number, consisting of exactly 10 digits. ('9876543210')
    :param reasons: a list of all the reasons a user selected, with each reason represented by a letter. (['a', 'c'])
    :param endings: a list of all the endings a user selected, with each ending represented by a letter. (['a', 'b'])
    :return: Returns a list of all the file names needed to create the final mp3 file.
    """
    filenames = []  # A list that contains the names of every file to be used.

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
    """
    Takes a list of spliced mp3 files and combines them together into one mp3 file,
    and then deletes the mp3 files used.

    Also outputs mp3list.txt listing the names of every file used to create the final file.

    :param filenames: a list of file names to be combined. (["m-b1-hello.mp3", "9.mp3", "7.mp3"])
    :param out_filename: a string that is the desired file name chosen by the user. ("JohnDoeVoicemail")
    :return: Nothing is returned. The combined mp3 file is stored in the program's directory.
    """
    while os.path.isfile(out_filename + ".mp3"):  # Checks for an existing file with the same name
        out_filename += ".output"
        print("The output file has been renamed to", out_filename + ".mp3 because a naming conflict has been detected.")
    destination = open(out_filename + ".mp3", 'wb')
    file_list = open("mp3list.txt", 'w')
    for filename in filenames:  # For each file in the list of files
        shutil.copyfileobj(open(filename, 'rb'), destination)  # Copy all contents of the file to the final output
        file_list.write(filename + "\n")  # Write the file name to mp3list.txt
    destination.close()
    file_list.close()
    print("Cleaning up temporary files...")
    for filename in set(filenames):  # Deduplicates the file list and then removes each file in it
        os.remove(filename)
    return
