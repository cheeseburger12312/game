import sys
from functions import *
from dialogue import *
from animations import computer_opening, loading_anim

print("\033[?25l", end="", flush=True)   # removes terminal cursor
clear_terminal()
saved_name, saved_password = checks_for_saved_account()

def ask_name_system():
    global saved_name

    opening_dialogue = opening[0].get("idk name")
    type_writter(saved_name, opening_dialogue)
    computer_opening()
    log_in()
    loading_anim()
    computer_scene()

def computer_scene():
    global saved_name
    spacer = "     "
    first_time = True
    timer_end = None

    print("Welcome")
    time.sleep(0.5)
    clear_terminal()

    while True:
        choice = arrow_selector(
            choice1="Check Email",
            choice2="Play a Game"
        )
        print()

        if timer_end is not None and timer_end.is_set():

            if choice == "Check Email":
                loading_anim()

                while True:
                    selected_mail = emails(
                        "Mia",
                        "email3",
                        "Alexa",
                        "email4"
                    )

                    if selected_mail == "Back":
                        clear_terminal()
                        break

                    if selected_mail == "Mia":
                        loading_anim()
                        clear_terminal()
                        print(mias_mail)

                        choice = back()

                        if choice == "Back":
                            break

                    elif selected_mail == "Alexa":
                        loading_anim()
                        clear_terminal()
                        print(alexa_mail)

                        choice = back()

                        if choice == "Back":
                            clear_terminal()
                            break

            else:
                type_writter("idk also")

        else:

            if choice == "Check Email":

                if first_time:
                    first_time = False

                    timer_end = timer(150)

                    while True:
                        loading_anim()

                        selected_mail = emails(
                            "Alexa",
                            "email2",
                            "email3",
                            "Back"
                        )

                        # GO BACK TO MAIN MENU
                        if selected_mail == "Back":
                            clear_terminal()
                            break

                        if selected_mail == "Alexa":
                            loading_anim()
                            clear_terminal()
                            print(alexa_mail)
                            time.sleep(0.5)

                            type_writter(
                                saved_name,
                                "Kinda feel bad for rejecting someone, "
                                "but <pause> I'm not into guys",
                                ask_question=True
                            )

                            print()
                            
                            choice = back()

                            # GO BACK TO MAIN MENU
                            if choice == "Back":
                                clear_terminal()
                                continue

                        else:
                            loading_anim()
                            clear_terminal()
                            print("No new Mail")
                            print()
                            type_writter(saved_name, "Still no mail...")

                            # Stay inside email menu
                            continue

                else:
                    loading_anim()
                    print("No new Mail")
                    print()
                    type_writter(saved_name, "Still no mail...")

            else:   
                type_writter(saved_name, "I just woke up")



