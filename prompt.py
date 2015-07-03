__author__ = 'tonyz_000'

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
    while True:
        gender = input("Would you like the: \n [1] Male version \n [2] Female version \n>")
        if gender == "1" or gender == "m" or gender == "M" or gender == "male" or gender == "Male":
            return "m"
        elif gender == "2" or gender == "f" or gender == "F" or gender == "female" or gender == "Female":
            return "f"
        else:
            print("Invalid input. \nPlease make sure you are entering the number of your choice.")

def phone():
    while True:
        number_raw = str(input("Please enter your 10-digit phone number: \n>"))
        number = ""
        for char in number_raw:
            if char == "0" or char == "1" or char == "2" or char == "3" or char == "4"\
                    or char == "5" or char == "6" or char == "7" or char == "8" or char == "9":
                number += char
        # Area codes do not start with "0" or "1"; therefore may be user error
        while number[0] == "0" or number[0] == "1":
            number = number[1:]
        if len(number) == 10:
            return number
        else:
            print("Invalid input. \nPlease make sure you are entering a valid 10-digit phone number"
                  " starting with your area code.")

def reason(gender):
    reasons = []
    reason_num = 0
    while True:
        reason_num += 1
        done = False
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
            if reason != "a" and reason != "b" and reason != "c" and reason != "d" \
                    and (reason != "e" or gender != "f") and reason != "A" and reason != "B"\
                    and reason != "C" and reason != "D" and (reason != "E" or gender != "f"):
                print("Invalid input. \nPlease make sure you are entering the letter of your choice.")
            else:
                reason = reason.lower()
                reasons.append(reason)
                done = True
        done = False
        while not done:
            print("You have selected", str(reason_num), "reason(s).")
            more = input("Would you like to select more reasons? [yes/no] \n>")
            if more == "yes" or more == "y":
                done = True
            elif more == "no" or more == "n":
                return reasons
            else:
                print("Invalid input. \nPlease make sure you are entering 'yes' or 'no'.")

def ending(gender):
    if gender == "m":
        ending1 = "I'm on a horse."
        ending2 = "Do do do doot doo do do dooot."
        ending3 = "I'm on a phone."
        ending4 = "SWAN DIVE."
        ending5 = "This voicemail is now diamonds."
    elif gender == "f":
        ending1 = "But she'll get back to you as soon as she can."
        ending2 = "Thanks for calling."
    while True:
        complete = False
        endings = []
        ending_num = 0
        while not complete:
            ending_num += 1
            done = False
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
                if end != "a" and end != "b" \
                        and (end != "c" and end != "d" and end != "e" or gender != "m")\
                        and end != "A" and end != "B" \
                        and (end != "C" and end != "D" and end != "E" or gender != "m"):
                    print("Invalid input. \nPlease make sure you are entering the letter of your choice.")
                else:
                    end = end.lower()
                    endings.append(end)
                    done = True
            done = False
            while not done:
                print("You have selected " + str(ending_num) + " ending(s).")
                more = input("Would you like to select more endings? [yes/no] \n>")
                if more == "yes" or more == "y":
                    done = True
                elif more == "no" or more == "n":
                    return endings
                else:
                    print("Invalid input. \nPlease make sure you are entering 'yes' or 'no'.")

def filename():
    name = str(input("What would you like the audio file to be named? (You do not need to include the extension.)\n>"))
    return name

def confirm(gender, phone, reasons, endings):
    print("Here are the options you have selected:")
    print("Gender:", gender)
    print("Phone number:", phone)
    print("You have selected the following reasons:")
    if gender == "m":
        for choice in reasons:
            print(male_reasons[choice])
        print("You have selected the following endings:")
        for choice in endings:
            print(male_endings[choice])
    if gender == "f":
        for choice in reasons:
            print(female_reasons[choice])
        print("You have selected the following endings:")
        for choice in endings:
            print(female_endings[choice])
    while True:
        done = input("Is the above information correct?[yes/no] \n>")
        if done == "yes" or done == "y":
            return True
        elif done == "no" or done == "n":
            return False
        else:
            print("Invalid input. \nPlease make sure you are entering 'yes' or 'no'.")
