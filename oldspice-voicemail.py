__author__ = 'Tony Zhaocheng Tan'

def main():
    print("Welcome to the Old Spice Voicemail generator!")
    gender = gender_input()
    phone = phone_input()
    reasons = reasons_input(gender)
    endings = endings_input(gender)
    print(gender)
    print(phone)
    print(reasons)
    print(endings)

def gender_input():
    while True:
        gender = input("Would you like the: \n [1] Male version \n [2] Female version \n>")
        if gender == "1" or gender == "m" or gender == "M" or gender == "male" or gender == "Male":
            return "m"
        elif gender == "2" or gender == "f" or gender == "F" or gender == "female" or gender == "Female":
            return "f"
        else:
            print("Invalid input. \nPlease make sure you are entering the number of your choice.")

def phone_input():
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
                  "starting with your area code.")

def reasons_input(gender):
    if gender == "m":
        reason1 = "Building an orphanage for children with their bare hands" \
                  " while playing a sweet, sweet lullaby for those children" \
                  " with two mallets against their abs xylophone."
        reason2 = "Cracking walnuts with their man mind."
        reason3 = "Polishing their monocle smile."
        reason4 = "Ripping out mass loads of weights."
    elif gender == "f":
        reason1 = "Ingesting my delicious Old Spice man smell."
        reason2 = "Listening to me read romantic poetry" \
                  " while I make a bouquet of paper flowers from each read page."
        reason3 = "Enjoying a lobster dinner I prepared just for her while carrying her" \
                  " on my back safely through piranha infested waters."
        reason4 = "Being serenaded on the moon with the view of the earth" \
                  " while surviving off the oxygen in my lungs via a passionate kiss."
        reason5 = "Riding a horse backwards with me."
    reasons = []
    reason_num = 0
    while True:
        reason_num += 1
        done = False
        while not done:
            print("Please select reason number " + str(reason_num) + ":",
                  "\n[a]", reason1,
                  "\n[b]", reason2,
                  "\n[c]", reason3,
                  "\n[d]", reason4)
            if gender == "f":
                print("[e]", reason5)
            reason = input(">")
            if reason != "a" and reason != "b" and reason != "c" and reason != "d" \
                    and (reason != "e" or gender != "f") and reason != "A" and reason != "B"\
                    and reason != "C" and reason != "D" and (reason != "E" or gender != "f"):
                print("Invalid input. \nPlease make sure you are entering the letter of your choice.")
            else:
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

def endings_input(gender):
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
                print("Please select ending number " + str(ending_num) + ":",
                      "\n[a]", ending1,
                      "\n[b]", ending2)
                if gender == "m":
                    print("[c]", ending3,
                          "\n[d]", ending4,
                          "\n[e]", ending5)
                ending = input(">")
                if ending != "a" and ending != "b" \
                        and (ending != "c" and ending != "d" and ending != "e" or gender != "m")\
                        and ending != "A" and ending != "B" \
                        and (ending != "C" and ending != "D" and ending != "E" or gender != "m"):
                    print("Invalid input. \nPlease make sure you are entering the letter of your choice.")
                else:
                    endings.append(ending)
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


main()