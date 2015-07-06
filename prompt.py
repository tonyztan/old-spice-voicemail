#!/usr/bin/env python3

"""
Handles interactive prompts, part of the Old Spice Voicemail Generator.

Each function prompts the user for a different piece of information.

Functions: gender, phone, reason, ending, filename, show_settings, confirm
"""

import sys

__author__ = 'Tony Zhaocheng Tan'
__copyright__ = "Copyright 2015, Tony Zhaocheng Tan"
__license__ = "MIT"
__version__ = "1.0"
__email__ = "tony@tonytan.io"

male_reasons = {'a': "Building an orphanage for children with their bare hands"
                " while playing a sweet, sweet lullaby for those children"
                " with two mallets against their abs xylophone.",
                'b': "Cracking walnuts with their man mind.",
                'c': "Polishing their monocle smile.",
                'd': "Ripping out mass loads of weights."}

female_reasons = {'a': "Ingesting my delicious Old Spice man smell.",
                  'b': "Listening to me read romantic poetry"
                  " while I make a bouquet of paper flowers from each read page.",
                  'c': "Enjoying a lobster dinner I prepared just for her while carrying her"
                  " on my back safely through piranha infested waters.",
                  'd': "Being serenaded on the moon with the view of the earth"
                  " while surviving off the oxygen in my lungs via a passionate kiss.",
                  'e': "Riding a horse backwards with me."}

male_endings = {'a': "I'm on a horse.",
                'b': "Do do do doot doo do do dooot.",
                'c': "I'm on a phone.",
                'd': "SWAN DIVE.",
                'e': "This voicemail is now diamonds."}

female_endings = {'a': "But she'll get back to you as soon as she can.",
                  'b': "Thanks for calling."}

def gender():
    """
    Prompts the user to choose "male" or "female".
    :return: Returns "m" or "f"
    """
    while True:
        gender = input("Would you like the: \n [1] Male version \n [2] Female version \n>")
        if gender in ("1", "m", "M", "male", "Male"):
            return "m"
        elif gender in ("2", "f", "F", "female", "Female"):
            return "f"
        else:
            print("Invalid input. \nPlease make sure you are entering the number of your choice.")

def phone():
    """
    Prompts the user to enter a 10-digit phone number.

    Ignoring all input that is not a number, the function makes sure that the number does not start with "0" or "1",
    and then checks to see if the number is exactly 10 digits long.
    :return: Returns the number as a string.
    """
    while True:
        number_raw = str(input("Please enter your 10-digit phone number: \n>"))
        number = ""
        have_number = False
        for char in number_raw:  # Iterates through the user input, and appends all numerical values to "number"
            if char in ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9"):
                number += char
                if char in ("2", "3", "4", "5", "6", "7", "8", "9"):
                    # Checks if inputs includes a number that is not 0 or 1
                    have_number = True

        if have_number:
            # U.S. Area codes do not start with "0" or "1"; therefore they are removed from the beginning
            while number[0] in ("0", "1"):
                number = number[1:]
            if len(number) == 10:
                return number

        print("Invalid input. \nPlease make sure you are entering a valid 10-digit phone number"
              "starting with your area code.")

def reason(gender):
    """
    Prompts the user to select reasons to be included in the voicemail message.
    :param gender: 'm' or 'f'.
    :return: Returns the selected reasons as letters in a list.
    """
    reasons = []
    reason_num = 1  # How many reasons are being selected.
    while True:
        done = False  # Represents whether the reason is done being selected.
        while not done:
            print("Please select reason number " + str(reason_num) + ":")
            if gender == "m":
                print("[a]", male_reasons['a'],
                      "\n[b]", male_reasons['b'],
                      "\n[c]", male_reasons['c'],
                      "\n[d]", male_reasons['d'])
            elif gender == "f":
                print("[a]", female_reasons['a'],
                      "\n[b]", female_reasons['b'],
                      "\n[c]", female_reasons['c'],
                      "\n[d]", female_reasons['d'],
                      "\n[e]", female_reasons['e'])
            reason = input(">")
            if reason not in ("a", "b", "c", "d") \
                    and (reason != "e" or gender != "f") and reason not in ("A", "B", "C", "D")\
                    and (reason != "E" or gender != "f"):  # Checks if the selected reason is valid for the gender.
                print("Invalid input. \nPlease make sure you are entering the letter of your choice.")
            else:
                reason = reason.lower()
                reasons.append(reason)
                done = True  # The reason is done being selected.
        done = False  # Represents if the question is done being answered.
        while not done:
            print("You have selected", str(reason_num), "reason(s).")
            more = input("Would you like to select more reasons? [yes/no] \n>")
            if more in ("yes", "y", "YES", "Y", "Yes"):
                reason_num += 1
                done = True  # Question answered, now loop will return to top to ask for next reason.
            elif more in ("no", "n", "NO", "N", "No"):
                return reasons  # Reason selection over, return list of reasons.
            else:
                print("Invalid input. \nPlease make sure you are entering 'yes' or 'no'.")

def ending(gender):
    """
    Prompts the user to select endings to be included in the voicemail message.
    :param gender: 'm' or 'f'.
    :return: Returns the selected endings as letters in a list.
    """
    if gender == "m":
        ending1 = "I'm on a horse."
        ending2 = "Do do do doot doo do do dooot."
        ending3 = "I'm on a phone."
        ending4 = "SWAN DIVE."
        ending5 = "This voicemail is now diamonds."
    elif gender == "f":
        ending1 = "But she'll get back to you as soon as she can."
        ending2 = "Thanks for calling."

    endings = []
    ending_num = 1  # How many endings are being selected.
    while True:
        done = False  # Represents whether the ending is done being selected.
        while not done:
            print("Please select ending number " + str(ending_num) + ":")
            if gender == "m":
                print("[a]", male_endings['a'],
                      "\n[b]", male_endings['b'],
                      "\n[c]", male_endings['c'],
                      "\n[d]", male_endings['d'],
                      "\n[e]", male_endings['e'])
            elif gender == "f":
                print("[a]", female_endings['a'],
                      "\n[b]", female_endings['b'])
            end = input(">")
            if end not in ("a", "b") \
                    and (end not in ("c", "d", "e") or gender != "m")\
                    and end not in ("A", "B") \
                    and (end not in ("C", "D", "E") or gender != "m"):
                # Checks if the selected ending is valid for the gender.
                print("Invalid input. \nPlease make sure you are entering the letter of your choice.")
            else:
                end = end.lower()
                endings.append(end)
                done = True  # The ending is done being selected.
        done = False  # Represents if the question is done being answered.
        while not done:
            print("You have selected " + str(ending_num) + " ending(s).")
            more = input("Would you like to select more endings? [yes/no] \n>")
            if more in ("yes", "y", "YES", "Y", "Yes"):
                ending_num += 1
                done = True  # Question answered, now loop will return to top to ask for next reason.
            elif more in ("no", "n", "NO", "N", "No"):
                return endings  # Ending selection over, return list of reasons.
            else:
                print("Invalid input. \nPlease make sure you are entering 'yes' or 'no'.")

def filename():
    """
    Prompts the user for the desired file name of the output mp3 file.

    Checks to make sure the name is alphanumeric.
    :return: Returns the name as a string.
    """
    while True:
        name = str(input("What would you like the audio file to be named? "
                         "(You do not need to include the extension.)\n>"))
        if name.isalnum():
            return name
        else:
            print("Invalid input. Please check to make sure that you have only entered letters and/or numbers.")

def show_settings(gender, phone, reasons, endings):
    """
    Prints out all the settings that the user has selected.
    :param gender: 'm' or 'f'.
    :param phone: a string that represents the phone number, consisting of exactly 10 digits. ('9876543210')
    :param reasons: a list of all the reasons a user selected, with each reason represented by a letter. (['a', 'c'])
    :param endings: a list of all the endings a user selected, with each ending represented by a letter. (['a', 'b'])
    :return: Nothing is returned.
    """
    print("\nHere are the options you have selected:")

    if str(gender) == 'm':
        gender = "Male"
    elif str(gender) == 'f':
        gender = "Female"
    print("Gender:", gender)
    print("Phone number:", phone)
    print("\nYou have selected the following reasons:")
    if gender == "Male":
        for choice in reasons:
            if choice in male_reasons:
                print(male_reasons[choice])
            else:
                print("Get Name Error! (Invalid reason)")
                sys.exit()
        print("\nYou have selected the following endings:")
        for choice in endings:
            if choice in male_endings:
                print(male_endings[choice])
            else:
                print("Get Name Error! (Invalid ending)")
                sys.exit()
    elif gender == "Female":
        for choice in reasons:
            if choice in female_reasons:
                print(female_reasons[choice])
            else:
                print("Get Name Error! (Invalid reason)")
                sys.exit()
        print("\nYou have selected the following endings:")
        print(endings)
        for choice in endings:
            if choice in female_endings:
                print(female_endings[choice])
            else:
                print("Get Name Error! (Invalid ending)")
                sys.exit()
    return

def confirm(gender, phone, reasons, endings):
    """
    Asks the user to confirm the settings that have been selected.
    :param gender: 'm' or 'f'.
    :param phone: a string that represents the phone number, consisting of exactly 10 digits. ('9876543210')
    :param reasons: a list of all the reasons a user selected, with each reason represented by a letter. (['a', 'c'])
    :param endings: a list of all the endings a user selected, with each ending represented by a letter. (['a', 'b'])
    :return: Returns True if the user has confirmed the settings. Returns False if the user wishes to start over.
    """
    show_settings(gender, phone, reasons, endings)
    while True:
        done = input("\nIs the above information correct?[yes/no] \n>")
        if done in ("yes", "y", "YES", "Y", "Yes"):
            return True
        elif done in ("no", "n", "NO", "N", "No"):
            return False
        else:
            print("Invalid input. \nPlease make sure you are entering 'yes' or 'no'.")
